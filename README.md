# AI-Career-Guidance-Navigator

> An intelligent, full-stack AI career navigation and skill-gap assessment platform designed to help students, developers, and transitioning professionals discover high-impact career pathways, analyze competency gaps, visualize step-by-step learning roadmaps, optimize resumes, and consult with an AI career mentor.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-v3-38B2AC.svg)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🌟 Key Features

### 1. 🧭 Intelligent Career Assessment & Match Scoring
- Dynamic multi-dimensional evaluation covering educational background, existing technical skills, work style, and industry interests.
- Computes granular **Skill Compatibility %**, identifying exact matched competencies and priority skills to learn.
- Interactive **Radar Chart** visualizer comparing candidate capability profiles against top roles.

### 2. 🗺️ Structured 4-Phase Learning Roadmaps
- Milestone-driven pathways for in-demand roles including:
  - **AI & Machine Learning Engineer**
  - **Full Stack Web Developer**
  - **Data Scientist & Analytics Lead**
  - **Cloud Solutions & DevOps Engineer**
  - **Cybersecurity Analyst & Threat Specialist**
  - **Technical Product Manager**
  - **UI/UX & Product Designer**
  - **Mobile App Developer (iOS / Flutter / React Native)**
  - **Data Engineer & Pipeline Architect**
- Includes phase breakdown (Foundations ➔ Core Competencies ➔ Projects & Portfolio ➔ Production Readiness), curated learning resources (free/paid), industry certifications, and key interview rounds.

### 3. 📄 AI Resume & ATS Competency Analyzer
- Scans resume text against industry keywords and role expectations.
- Calculates an **ATS Compatibility Score (0 - 100)**.
- Pinpoints critical missing keywords, assesses action verb density, reviews length/formatting, and delivers tailored bullet-point revision advice.

### 4. 💬 AI Career Advisor Chat
- Interactive conversational assistant for guidance on career transitions, portfolio building, compensation negotiation, and interview preparation.
- **Dual-Engine Architecture**: Operates with an intelligent built-in expert knowledge base offline, or seamlessly connects to **Google Gemini 2.5 Flash** when an API key is provided.

### 5. 📚 Comprehensive Career Catalog
- Browse, search, and filter high-growth tech careers with global ($ USD) and Indian (₹ LPA) compensation benchmarks, market demand outlooks, and prerequisites.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/legion0069/AI-Career-Guidance-Navigator.git
cd AI-Career-Guidance-Navigator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
You can start the server directly using:
```bash
python app.py
```
*Or on Windows, simply double-click `run.bat`.*

### 4. Open in Browser
Visit **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your web browser.

---

## ☁️ Deploy to Vercel

The application is pre-configured for **1-click Vercel deployment** using Serverless Functions and `vercel.json`.

### Option A: Via GitHub & Vercel Dashboard (Recommended)
1. Go to [Vercel Dashboard](https://vercel.com/new).
2. Click **"Import Project"** and select `legion0069/AI-Career-Guidance-Navigator`.
3. In **Environment Variables** (optional):
   - Add `GEMINI_API_KEY` (if you wish to use live Gemini AI inference).
4. Click **Deploy**. Vercel will build and assign you a live production URL (e.g., `https://ai-career-guidance-navigator.vercel.app`).

### Option B: Via Vercel CLI
```bash
# Log in to your Vercel account
vercel login

# Deploy to preview
vercel

# Deploy directly to production
vercel --prod
```

---

## ⚙️ Configuration (Optional)

The application works completely out-of-the-box using the built-in offline intelligence engine.

If you wish to enable live Gemini AI inference:
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Add your Google AI Studio API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
*(Alternatively, enter your API key directly in the web UI under the **"API Key"** settings button in the top right.)*

---

## 📂 Project Architecture

```
AI-Career-Guidance-Navigator/
├── app.py                     # FastAPI application & REST API routes
├── career_data.py             # Career taxonomies, roadmap phases & scoring algorithms
├── requirements.txt           # Python package dependencies
├── run.bat                    # One-click Windows launch script
├── .gitignore                 # Version control exclusions
├── .env.example               # Environment configuration template
├── README.md                  # Comprehensive project documentation
└── static/
    ├── index.html             # Single-page UI with Tailwind & Chart.js
    ├── css/
    │   └── custom.css         # Custom animations & glassmorphism theme
    └── js/
        └── app.js             # Client-side reactivity, chart rendering & API calls
```

---

## 📡 REST API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the Single Page Application |
| `GET` | `/api/skills` | Returns list of categorized technical & soft skills |
| `GET` | `/api/careers` | Lists all career profiles with summaries & salaries |
| `GET` | `/api/careers/{career_id}` | Retrieves full career profile and 4-phase roadmap |
| `POST` | `/api/assess` | Computes user match score and career ranking |
| `POST` | `/api/resume-analyzer` | Evaluates resume text against target role keywords |
| `POST` | `/api/chat` | AI Career Advisor chat endpoint (Gemini or Offline engine) |

---

## 🛡️ License

This project is licensed under the MIT License - feel free to use, modify, and distribute.

