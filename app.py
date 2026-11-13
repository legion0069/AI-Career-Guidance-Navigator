import os
import sys
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Header
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from pydantic import BaseModel, Field

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from career_data import (
    CAREER_DATABASE,
    ALL_SKILLS_LIST,
    match_user_to_careers,
    analyze_resume_text
)

app = FastAPI(
    title="AI Career Guidance Navigator",
    description="Intelligent career roadmap, skill gap analysis, and transition advisory platform.",
    version="1.0.0",
    redirect_slashes=False
)

# Custom Vercel Path Rewriter Middleware to handle Vercel serverless query-based rewrites
class VercelPathRewriterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path_param = request.query_params.get("path")
        if path_param is not None:
            clean_path = path_param.strip()
            if not clean_path or clean_path == "/" or clean_path == "index" or clean_path == "index.py":
                request.scope["path"] = "/"
            else:
                if not clean_path.startswith("/"):
                    clean_path = "/" + clean_path
                # Ensure /api prefix is normalized
                if not clean_path.startswith("/api"):
                    clean_path = "/api" + clean_path
                request.scope["path"] = clean_path

        # If running behind Vercel edge rewrite without query param
        matched_path = request.headers.get("x-matched-path")
        if not path_param and matched_path and matched_path not in ("/api/index.py", "/api/index"):
            request.scope["path"] = matched_path

        return await call_next(request)

app.add_middleware(VercelPathRewriterMiddleware)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = os.path.join(BASE_DIR, "static")
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

# Mount static files if directory exists
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
elif os.path.exists(os.path.join(PUBLIC_DIR, "static")):
    app.mount("/static", StaticFiles(directory=os.path.join(PUBLIC_DIR, "static")), name="static")

# Request Models
class AssessmentRequest(BaseModel):
    education: str = "Computer Science / STEM"
    experience_level: str = "Beginner / Transitioning"
    skills: List[str] = Field(default_factory=list)
    interests: List[str] = Field(default_factory=list)
    work_style: List[str] = Field(default_factory=list)
    target_category: Optional[str] = "All"


class ResumeRequest(BaseModel):
    resume_text: str
    target_career_id: str


class ChatMessage(BaseModel):
    message: str
    target_career_id: Optional[str] = None
    chat_history: Optional[List[dict]] = Field(default_factory=list)
    api_key: Optional[str] = None


def get_index_html():
    candidates = [
        os.path.join(PUBLIC_DIR, "index.html"),
        os.path.join(STATIC_DIR, "index.html"),
        os.path.join(BASE_DIR, "index.html")
    ]
    for c in candidates:
        if os.path.exists(c):
            with open(c, "r", encoding="utf-8") as f:
                return f.read()
    return "<h1>AI Career Guidance Navigator</h1><p>Index file not found.</p>"


@app.get("/", response_class=HTMLResponse)
@app.get("/api", response_class=HTMLResponse)
@app.get("/api/", response_class=HTMLResponse)
@app.get("/api/index", response_class=HTMLResponse)
@app.get("/api/index.py", response_class=HTMLResponse)
def serve_index():
    return HTMLResponse(content=get_index_html())


@app.get("/skills")
@app.get("/api/skills")
def get_skills():
    categories = {
        "Programming & Frameworks": [
            "Python", "JavaScript", "TypeScript", "React", "Node.js", "Next.js", "HTML5", "CSS3", "Tailwind CSS", "Flutter", "Swift", "Kotlin"
        ],
        "AI, Data & Analytics": [
            "Machine Learning", "Deep Learning", "PyTorch", "TensorFlow", "Pandas", "NumPy", "SQL", "Tableau", "Power BI", "Statistics", "A/B Testing", "Spark", "Airflow", "Snowflake", "BigQuery"
        ],
        "Cloud, DevOps & Security": [
            "Docker", "Kubernetes", "AWS", "GCP", "Azure", "Linux", "Terraform", "CI/CD", "Git", "Cybersecurity", "Network Security", "SIEM (Splunk)", "Wireshark", "Penetration Testing"
        ],
        "Product, Design & Soft Skills": [
            "Figma", "UI/UX Design", "Wireframing", "Product Management", "Agile & Scrum", "Roadmapping", "Critical Thinking", "Problem Solving", "Communication", "Leadership"
        ]
    }
    return {
        "all_skills": ALL_SKILLS_LIST,
        "categories": categories
    }


@app.get("/careers")
@app.get("/api/careers")
def get_careers():
    summary_list = []
    for cid, c in CAREER_DATABASE.items():
        summary_list.append({
            "id": c["id"],
            "title": c["title"],
            "category": c["category"],
            "overview": c["overview"],
            "avg_salary_usd": c["avg_salary_usd"],
            "avg_salary_inr": c["avg_salary_inr"],
            "demand_level": c["demand_level"],
            "core_skills": c["core_skills"],
            "top_certifications": c["top_certifications"]
        })
    return {"careers": summary_list}


@app.get("/careers/{career_id}")
@app.get("/api/careers/{career_id}")
def get_career_detail(career_id: str):
    career = CAREER_DATABASE.get(career_id)
    if not career:
        raise HTTPException(status_code=404, detail="Career role not found")
    return career


@app.post("/assess")
@app.post("/api/assess")
def run_assessment(payload: AssessmentRequest):
    recommendations = match_user_to_careers(
        education=payload.education,
        experience_level=payload.experience_level,
        user_skills=payload.skills,
        user_interests=payload.interests,
        preferred_work_style=payload.work_style,
        target_category=payload.target_category
    )
    return {
        "total_analyzed": len(CAREER_DATABASE),
        "recommendations": recommendations,
        "top_match": recommendations[0] if recommendations else None
    }


@app.post("/resume-analyzer")
@app.post("/api/resume-analyzer")
def evaluate_resume(payload: ResumeRequest):
    if not payload.resume_text or len(payload.resume_text.strip()) < 30:
        raise HTTPException(status_code=400, detail="Please provide meaningful resume text (minimum 30 characters).")
    
    analysis = analyze_resume_text(payload.resume_text, payload.target_career_id)
    return analysis


@app.post("/chat")
@app.post("/api/chat")
def career_chat(payload: ChatMessage):
    user_query = payload.message.strip()
    if not user_query:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    selected_career = CAREER_DATABASE.get(payload.target_career_id) if payload.target_career_id else None
    api_key = payload.api_key or os.environ.get("GEMINI_API_KEY")

    # If Gemini API key is available, attempt calling Gemini
    if api_key:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            
            career_context = ""
            if selected_career:
                career_context = f"\nContext on user's target career:\nRole: {selected_career['title']}\nCategory: {selected_career['category']}\nCore Skills: {', '.join(selected_career['core_skills'])}\nSalary USD: {selected_career['avg_salary_usd']}\nDemand: {selected_career['demand_level']}"

            prompt = f"""You are an elite, encouraging, and highly practical AI Career Guidance Navigator & Mentor.
The user is asking: "{user_query}"
{career_context}

Provide a well-structured, actionable, and inspiring response with:
1. Direct answer with clear guidance
2. Actionable next steps or recommended portfolio projects
3. Key pitfalls or common mistakes to avoid
Format with clean bullet points and markdown bolding."""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            if response and response.text:
                return {
                    "response": response.text,
                    "engine": "Gemini 2.5 Flash",
                    "status": "success"
                }
        except Exception as e:
            pass

    # Built-in contextual AI advisor response
    query_lower = user_query.lower()
    role_title = selected_career["title"] if selected_career else "Technology & AI Careers"
    role_skills = ", ".join(selected_career["core_skills"][:5]) if selected_career else "Python, System Design, Problem Solving"

    if any(k in query_lower for k in ["roadmap", "learn", "start", "beginner", "path"]):
        reply = f"""### 🚀 Tailored Action Roadmap for **{role_title}**

To successfully master this pathway from scratch or transition:

1. **Foundations First (Weeks 1-4)**:
   - Focus intensely on fundamental prerequisites: **{role_skills}**.
   - Build daily coding habits: 45–60 minutes of active hands-on practice beats binge-watching video tutorials.

2. **Core Competency Projects (Weeks 5-10)**:
   - Move beyond generic tutorials. Build 2 unique, end-to-end practical projects that solve a real problem.
   - For example: an end-to-end automated pipeline or a deployed full-stack solution with clear README and live demo links.

3. **Production Polish & MLOps/DevOps (Weeks 11-14)**:
   - Containerize applications with Docker, deploy to cloud hosting (AWS / GCP / Vercel / Render), and configure basic CI/CD.

4. **Interview & Portfolio Acceleration**:
   - Write clear case studies explaining *why* architectural decisions were made, challenges faced, and measurable outcomes."""

    elif any(k in query_lower for k in ["salary", "pay", "compensation", "package", "earn"]):
        usd = selected_career["avg_salary_usd"] if selected_career else "$90,000 - $160,000 / yr"
        inr = selected_career["avg_salary_inr"] if selected_career else "₹8 - ₹25 LPA"
        reply = f"""### 💰 Compensation Benchmark for **{role_title}**

- **North America / Remote International**: `{usd}`
- **India / Emerging Tech Hubs**: `{inr}`

**Key Levers to Negotiate Top-Tier Compensation:**
- **System Architecture & Scale**: Demonstrating experience with high concurrency or distributed systems.
- **Production Ownership**: Having shipped user-facing products with telemetry and reliability.
- **Cross-functional Impact**: Framing your contributions in terms of revenue saved, latency reduced, or user adoption accelerated."""

    elif any(k in query_lower for k in ["interview", "questions", "prep", "hiring"]):
        topics = ", ".join(selected_career.get("interview_topics", ["System Design", "Core Algorithms", "Practical Debugging"])) if selected_career else "Data Structures, System Design, Behavioral"
        reply = f"""### 🎯 High-Probability Interview Topics for **{role_title}**

1. **Technical Deep Dives**:
   - Key areas asked in rounds: **{topics}**.
   - Expect deep dives into your GitHub projects: be ready to explain trade-offs and edge cases.

2. **System Design & Problem Solving**:
   - Practice whiteboard architecture: explain data flows, bottlenecks, caching, and database schemas.

3. **Behavioral & Cultural (STAR Method)**:
   - *Situation, Task, Action, Result*: Have 3 stories ready: a technical disagreement resolved, a production incident handled, and a difficult bug root-caused."""

    elif any(k in query_lower for k in ["resume", "cv", "ats"]):
        reply = f"""### 📄 Resume Optimization Strategy for **{role_title}**

1. **Top 20% Real Estate**: Ensure your headline and opening summary explicitly align with `{role_title}`.
2. **Quantified Bullet Points**: Use Google's XYZ formula: *"Accomplished [X], as measured by [Y], by doing [Z]"*.
3. **Core Tech Stack**: Explicitly list your proficiencies in: **{role_skills}**.
4. **Clickable Proof**: Provide hyperlinks directly to live project deployments and GitHub repositories."""

    else:
        reply = f"""### 🧭 Career Guidance on **{role_title}**

Thank you for asking: *"{user_query}"*

Here are key expert insights to guide your next decision:
- **Market Demand**: This field continues to experience rapid evolution. Professionals who bridge theoretical domain knowledge with practical deployment skills consistently stand out.
- **Immediate Next Step**: Strengthen your command of `{role_skills}` by developing a public case study.
- **Continuous Learning**: Leverage open-source communities, contribute to relevant repositories, and seek feedback from peers or mentors on platforms like LinkedIn and ADPList.

*Tip: You can also use our interactive Assessment or Resume Reviewer tab above to get personalized scores and step-by-step roadmaps!*"""

    return {
        "response": reply,
        "engine": "AI Career Knowledge Engine (Offline/Local)",
        "status": "success"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
