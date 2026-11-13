/**
 * AI Career Guidance Navigator - Frontend Logic
 */

// Global State
const FALLBACK_SKILLS = [
  "Python", "JavaScript", "TypeScript", "SQL", "React", "Node.js", "Next.js",
  "Machine Learning", "Deep Learning", "PyTorch", "TensorFlow", "Pandas", "NumPy",
  "Docker", "Kubernetes", "AWS", "GCP", "Linux", "Git", "Tailwind CSS",
  "PostgreSQL", "MongoDB", "Data Visualization", "Tableau", "Power BI",
  "Cybersecurity", "Network Security", "Figma", "UI/UX Design", "Flutter",
  "Product Management", "Agile & Scrum", "Critical Thinking", "Problem Solving"
];

const FALLBACK_CAREERS = [
  {
    id: "ai_ml_engineer",
    title: "AI & Machine Learning Engineer",
    category: "Artificial Intelligence & Data",
    overview: "Designs, builds, and deploys scalable machine learning models and AI systems into production software products.",
    avg_salary_usd: "$125,000 - $185,000 / yr",
    avg_salary_inr: "₹14 - ₹35 LPA",
    demand_level: "Extremely High (38% growth)",
    core_skills: ["python", "machine learning", "deep learning", "pytorch", "tensorflow", "pandas", "numpy", "sql"],
    secondary_skills: ["docker", "mlops", "fastapi", "git", "llms", "cloud platforms (aws/gcp)"],
    top_certifications: ["AWS Certified Machine Learning", "Google Professional ML Engineer"]
  },
  {
    id: "full_stack_developer",
    title: "Full Stack Web Developer",
    category: "Software Engineering",
    overview: "Builds end-to-end web applications, crafting intuitive user interfaces and architecting robust server-side APIs and databases.",
    avg_salary_usd: "$95,000 - $145,000 / yr",
    avg_salary_inr: "₹8 - ₹24 LPA",
    demand_level: "Very High (25% growth)",
    core_skills: ["javascript", "typescript", "react", "node.js", "html5", "css3", "sql", "git"],
    secondary_skills: ["next.js", "tailwind css", "postgresql", "mongodb", "docker", "graphql"],
    top_certifications: ["Meta Front-End / Back-End Certificate", "AWS Certified Developer"]
  },
  {
    id: "data_scientist",
    title: "Data Scientist & Analytics Lead",
    category: "Artificial Intelligence & Data",
    overview: "Transforms unstructured complex data into actionable business intelligence, predictive algorithms, and executive strategic insights.",
    avg_salary_usd: "$110,000 - $160,000 / yr",
    avg_salary_inr: "₹12 - ₹30 LPA",
    demand_level: "High (28% growth)",
    core_skills: ["python", "sql", "statistics", "data visualization", "pandas", "numpy", "machine learning"],
    secondary_skills: ["tableau", "power bi", "a/b testing", "bigquery", "snowflake"],
    top_certifications: ["Google Data Analytics Certificate", "IBM Data Science Certificate"]
  },
  {
    id: "cloud_devops_engineer",
    title: "Cloud Solutions & DevOps Engineer",
    category: "Cloud & Infrastructure",
    overview: "Architects resilient cloud infrastructure, automates deployment pipelines, and guarantees 99.99% system availability and security.",
    avg_salary_usd: "$115,000 - $170,000 / yr",
    avg_salary_inr: "₹10 - ₹28 LPA",
    demand_level: "Extremely High (32% growth)",
    core_skills: ["linux", "docker", "kubernetes", "aws", "terraform", "ci/cd", "bash", "git"],
    secondary_skills: ["python", "ansible", "prometheus", "grafana", "gcp"],
    top_certifications: ["AWS Solutions Architect", "CKA: Certified Kubernetes Administrator"]
  },
  {
    id: "cybersecurity_analyst",
    title: "Cybersecurity Analyst & Threat Specialist",
    category: "Security & Defense",
    overview: "Protects organizational networks, applications, and confidential assets from digital threats, breaches, and vulnerabilities.",
    avg_salary_usd: "$105,000 - $155,000 / yr",
    avg_salary_inr: "₹9 - ₹25 LPA",
    demand_level: "Extremely High (35% growth)",
    core_skills: ["network security", "linux", "siem (splunk/sentinel)", "incident response", "vulnerability assessment"],
    secondary_skills: ["penetration testing", "owasp top 10", "cryptography", "cloud security"],
    top_certifications: ["CompTIA Security+", "Blue Team Level 1 (BTL1)"]
  },
  {
    id: "product_manager",
    title: "Technical Product Manager",
    category: "Product & Strategy",
    overview: "Discovers user needs, defines product vision, and leads cross-functional teams of engineers and designers to launch impactful tech products.",
    avg_salary_usd: "$120,000 - $175,000 / yr",
    avg_salary_inr: "₹15 - ₹35 LPA",
    demand_level: "High (20% growth)",
    core_skills: ["product strategy", "user research", "agile & scrum", "wireframing", "roadmapping", "product analytics"],
    secondary_skills: ["jira", "figma", "market analysis", "a/b testing"],
    top_certifications: ["Product School CPM", "Scrum Product Owner (CSPO)"]
  },
  {
    id: "ui_ux_designer",
    title: "UI/UX & Product Designer",
    category: "Design & User Experience",
    overview: "Creates seamless, visually elegant, and user-centered digital interfaces through user research, prototyping, and design systems.",
    avg_salary_usd: "$88,000 - $135,000 / yr",
    avg_salary_inr: "₹7 - ₹22 LPA",
    demand_level: "High (18% growth)",
    core_skills: ["figma", "user research", "wireframing", "prototyping", "design systems", "usability testing"],
    secondary_skills: ["html/css basics", "typography & color theory", "accessibility (wcag)"],
    top_certifications: ["Google UX Design Certificate", "NN/g UX Master"]
  }
];

let allSkillsData = [...FALLBACK_SKILLS];
let allCareersData = [...FALLBACK_CAREERS];
let selectedSkills = new Set(["Python", "Machine Learning", "Git", "SQL"]);
let currentActiveTab = "assess";
let matchRadarChart = null;

// Initialization
document.addEventListener("DOMContentLoaded", async () => {
  initApiKeyStatus();
  
  // Render immediately with baseline data so UI is instantly responsive
  setupSkillsPills();
  populateRoleDropdowns();
  renderExploreCards();
  initMatchChart();
  submitAssessment();

  // Load live data from API in background and refresh
  await loadInitialData();
  setupSkillsPills();
  populateRoleDropdowns();
  renderExploreCards();
});

// Switch Active Tabs
function switchTab(tabId) {
  const tabs = ["assess", "roadmap", "resume", "chat", "explore"];
  tabs.forEach(t => {
    const el = document.getElementById(`tab-${t}`);
    const btn = document.getElementById(`tab-btn-${t}`);
    if (el) {
      if (t === tabId) {
        el.classList.remove("hidden");
      } else {
        el.classList.add("hidden");
      }
    }
    if (btn) {
      if (t === tabId) {
        btn.className = "nav-tab-active px-4 py-2 text-sm font-semibold rounded-lg transition-all flex items-center space-x-2";
      } else {
        btn.className = "px-4 py-2 text-sm font-medium text-slate-400 hover:text-white hover:bg-slate-800/50 rounded-lg transition-all flex items-center space-x-2";
      }
    }
  });
  currentActiveTab = tabId;
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// Fetch Initial Skills & Careers from API
async function loadInitialData() {
  try {
    const [skillsRes, careersRes] = await Promise.all([
      fetch("/api/skills").catch(() => null),
      fetch("/api/careers").catch(() => null)
    ]);
    
    if (skillsRes && skillsRes.ok) {
      const skillsJson = await skillsRes.json();
      if (skillsJson.all_skills && skillsJson.all_skills.length) {
        allSkillsData = skillsJson.all_skills;
      }
    }
    if (careersRes && careersRes.ok) {
      const careersJson = await careersRes.json();
      if (careersJson.careers && careersJson.careers.length) {
        allCareersData = careersJson.careers;
      }
    }
  } catch (err) {
    console.warn("Using baseline catalog for initial load:", err);
  }
}

// Populate Skills Pills
function setupSkillsPills() {
  const container = document.getElementById("skills-selector-container");
  if (!container) return;

  container.innerHTML = "";
  allSkillsData.forEach(skill => {
    const isSelected = selectedSkills.has(skill);
    const pill = document.createElement("button");
    pill.type = "button";
    pill.onclick = () => toggleSkill(skill, pill);
    pill.className = `px-2.5 py-1 text-xs rounded-lg font-medium transition cursor-pointer ${
      isSelected
        ? "bg-indigo-600 text-white shadow-sm shadow-indigo-500/30 border border-indigo-400"
        : "bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700/60"
    }`;
    pill.innerHTML = `${skill} ${isSelected ? '<i class="fa-solid fa-check ml-1 text-[10px]"></i>' : ''}`;
    container.appendChild(pill);
  });
  updateSkillsBadge();
}

function toggleSkill(skill, pillEl) {
  if (selectedSkills.has(skill)) {
    selectedSkills.delete(skill);
    pillEl.className = "px-2.5 py-1 text-xs rounded-lg font-medium transition cursor-pointer bg-slate-800 text-slate-300 hover:bg-slate-700 border border-slate-700/60";
    pillEl.innerHTML = skill;
  } else {
    selectedSkills.add(skill);
    pillEl.className = "px-2.5 py-1 text-xs rounded-lg font-medium transition cursor-pointer bg-indigo-600 text-white shadow-sm shadow-indigo-500/30 border border-indigo-400";
    pillEl.innerHTML = `${skill} <i class="fa-solid fa-check ml-1 text-[10px]"></i>`;
  }
  updateSkillsBadge();
}

function updateSkillsBadge() {
  const badge = document.getElementById("skills-count-badge");
  if (badge) {
    badge.textContent = `${selectedSkills.size} selected`;
  }
}

// Populate Dropdown Menus for Career Selectors
function populateRoleDropdowns() {
  const roadmapSelect = document.getElementById("roadmap-career-select");
  const resumeSelect = document.getElementById("resume-target-role");
  const chatSelect = document.getElementById("chat-career-focus");

  if (!allCareersData.length) return;

  [roadmapSelect, resumeSelect, chatSelect].forEach(selectEl => {
    if (!selectEl) return;
    const currentVal = selectEl.value;
    selectEl.innerHTML = "";
    allCareersData.forEach(career => {
      const opt = document.createElement("option");
      opt.value = career.id;
      opt.textContent = `${career.title} (${career.category})`;
      selectEl.appendChild(opt);
    });
    if (currentVal && allCareersData.some(c => c.id === currentVal)) {
      selectEl.value = currentVal;
    }
  });

  // Load first career in roadmap
  if (allCareersData.length > 0 && roadmapSelect && !roadmapSelect.dataset.loaded) {
    roadmapSelect.dataset.loaded = "true";
    loadRoadmapForCareer(allCareersData[0].id);
  }
}

// Client-Side Match Fallback Scorer
function clientSideMatchCareers(skillsList, categoryFilter = "All") {
  const userSkillsClean = skillsList.map(s => s.toLowerCase().trim());
  const results = [];

  allCareersData.forEach(career => {
    if (categoryFilter && categoryFilter !== "All" && career.category.toLowerCase() !== categoryFilter.toLowerCase()) {
      return;
    }

    const core = (career.core_skills || []).map(s => s.toLowerCase());
    const secondary = (career.secondary_skills || []).map(s => s.toLowerCase());

    const matchedCore = core.filter(s => userSkillsClean.some(us => us.includes(s) || s.includes(us)));
    const matchedSecondary = secondary.filter(s => userSkillsClean.some(us => us.includes(s) || s.includes(us)));
    const missingCore = core.filter(s => !userSkillsClean.some(us => us.includes(s) || s.includes(us)));

    const coreScore = (matchedCore.length / Math.max(core.length, 1)) * 65;
    const secondaryScore = (matchedSecondary.length / Math.max(secondary.length, 1)) * 25;
    const bonus = 10;

    const totalScore = Math.min(100, Math.round(coreScore + secondaryScore + bonus));

    let readiness = "Foundational Match";
    if (totalScore >= 75) readiness = "Advanced Ready Match";
    else if (totalScore >= 50) readiness = "Targeted Upskilling Needed";

    results.push({
      id: career.id,
      title: career.title,
      category: career.category,
      overview: career.overview,
      score: totalScore,
      readiness: readiness,
      avg_salary_usd: career.avg_salary_usd,
      avg_salary_inr: career.avg_salary_inr,
      demand_level: career.demand_level,
      matched_skills: [...matchedCore, ...matchedSecondary].map(s => s.charAt(0).toUpperCase() + s.slice(1)),
      missing_skills: missingCore.map(s => s.charAt(0).toUpperCase() + s.slice(1)),
      top_certifications: career.top_certifications || []
    });
  });

  results.sort((a, b) => b.score - a.score);
  return results;
}

// Submit Career Assessment
async function submitAssessment() {
  const submitBtn = document.querySelector('button[onclick="submitAssessment()"]');
  const originalBtnHtml = submitBtn ? submitBtn.innerHTML : "";

  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i><span>Calculating Scores...</span>`;
  }

  const educationEl = document.getElementById("user-education");
  const experienceEl = document.getElementById("user-experience");
  const categoryEl = document.getElementById("user-category");

  const education = educationEl ? educationEl.value : "Computer Science / STEM";
  const experience = experienceEl ? experienceEl.value : "Beginner / Transitioning";
  const category = categoryEl ? categoryEl.value : "All";

  const workStyleCheckboxes = document.querySelectorAll('input[name="work_style"]:checked');
  const workStyles = Array.from(workStyleCheckboxes).map(cb => cb.value);

  const payload = {
    education: education,
    experience_level: experience,
    skills: Array.from(selectedSkills),
    interests: ["Artificial Intelligence", "Web Development", "Cloud Systems", "Design"],
    work_style: workStyles,
    target_category: category
  };

  try {
    const res = await fetch("/api/assess", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      const data = await res.json();
      if (data && data.recommendations && data.recommendations.length > 0) {
        renderAssessmentResults(data.recommendations);
        updateRadarChart(data.recommendations.slice(0, 5));
        return;
      }
    }
    // If response was not ok or empty, fallback to client-side scorer
    const fallbackResults = clientSideMatchCareers(payload.skills, category);
    renderAssessmentResults(fallbackResults);
    updateRadarChart(fallbackResults.slice(0, 5));
  } catch (err) {
    console.warn("Using client-side match calculator fallback:", err);
    const fallbackResults = clientSideMatchCareers(payload.skills, category);
    renderAssessmentResults(fallbackResults);
    updateRadarChart(fallbackResults.slice(0, 5));
  } finally {
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalBtnHtml;
    }
  }
}

// Render Ranked Assessment Cards
function renderAssessmentResults(recommendations) {
  const container = document.getElementById("assessment-results-list");
  if (!container) return;

  if (!recommendations || recommendations.length === 0) {
    container.innerHTML = `
      <div class="text-center py-10 bg-slate-900/50 rounded-2xl border border-slate-800">
        <p class="text-slate-400">No matching careers found for this category filter. Try selecting 'All Domains'.</p>
      </div>`;
    return;
  }

  container.innerHTML = "";
  recommendations.forEach((rec, idx) => {
    const isTop = idx === 0;
    const scoreColor = rec.score >= 75 ? "text-emerald-400 border-emerald-500/40 bg-emerald-500/10" :
                       rec.score >= 50 ? "text-indigo-400 border-indigo-500/40 bg-indigo-500/10" :
                       "text-amber-400 border-amber-500/40 bg-amber-500/10";

    const card = document.createElement("div");
    card.className = `glass-card rounded-2xl p-6 border transition-all ${
      isTop ? "border-indigo-500/60 shadow-lg shadow-indigo-500/10" : "border-slate-800 hover:border-slate-700"
    }`;

    card.innerHTML = `
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-3">
        <div class="space-y-1">
          <div class="flex items-center space-x-2">
            ${isTop ? '<span class="px-2 py-0.5 text-[11px] font-bold uppercase tracking-wider bg-gradient-to-r from-indigo-500 to-purple-500 text-white rounded-md">⭐ Top Match</span>' : ''}
            <span class="text-xs font-semibold text-slate-400">${rec.category}</span>
          </div>
          <h3 class="text-lg font-bold text-white">${rec.title}</h3>
        </div>
        <div class="flex items-center space-x-3">
          <div class="text-right">
            <div class="text-2xl font-black ${scoreColor.split(" ")[0]}">${rec.score}%</div>
            <div class="text-[10px] uppercase font-semibold text-slate-400">Match Score</div>
          </div>
        </div>
      </div>

      <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-4">${rec.overview}</p>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 p-3 bg-slate-900/60 rounded-xl border border-slate-800/80 mb-4 text-xs">
        <div>
          <span class="text-slate-400">Avg Compensation:</span>
          <div class="font-semibold text-slate-200 mt-0.5">${rec.avg_salary_usd} <span class="text-slate-400">(${rec.avg_salary_inr || ''})</span></div>
        </div>
        <div>
          <span class="text-slate-400">Market Growth:</span>
          <div class="font-semibold text-indigo-400 mt-0.5">${rec.demand_level}</div>
        </div>
      </div>

      <!-- Skills Breakdown -->
      <div class="space-y-2 mb-4 text-xs">
        <div>
          <span class="text-slate-400 font-medium">Matched Skills You Have:</span>
          <div class="flex flex-wrap gap-1 mt-1">
            ${rec.matched_skills && rec.matched_skills.length ? rec.matched_skills.map(s => `<span class="px-2 py-0.5 bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 rounded-md font-medium">${s}</span>`).join('') : '<span class="text-slate-500 italic">None yet</span>'}
          </div>
        </div>
        ${rec.missing_skills && rec.missing_skills.length ? `
        <div class="pt-1">
          <span class="text-slate-400 font-medium">Top Skills to Upskill:</span>
          <div class="flex flex-wrap gap-1 mt-1">
            ${rec.missing_skills.slice(0, 5).map(s => `<span class="px-2 py-0.5 bg-slate-800 text-amber-300 border border-amber-500/20 rounded-md font-medium">${s}</span>`).join('')}
          </div>
        </div>` : ''}
      </div>

      <!-- Action buttons -->
      <div class="flex items-center space-x-3 pt-2 border-t border-slate-800">
        <button onclick="viewRoadmapDirect('${rec.id}')" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-lg flex items-center space-x-1.5 transition">
          <i class="fa-solid fa-route"></i>
          <span>View Learning Roadmap</span>
        </button>
        <button onclick="discussRoleInChat('${rec.id}')" class="px-3.5 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold rounded-lg flex items-center space-x-1.5 transition">
          <i class="fa-solid fa-comments"></i>
          <span>Ask Advisor</span>
        </button>
      </div>
    `;

    container.appendChild(card);
  });
}

// Chart.js Radar Chart
function initMatchChart() {
  const ctx = document.getElementById("matchChart");
  if (!ctx) return;

  if (matchRadarChart) {
    matchRadarChart.destroy();
  }

  matchRadarChart = new Chart(ctx, {
    type: "radar",
    data: {
      labels: [],
      datasets: [{
        label: "Compatibility Score (%)",
        data: [],
        backgroundColor: "rgba(99, 102, 241, 0.25)",
        borderColor: "rgba(99, 102, 241, 1)",
        pointBackgroundColor: "rgba(168, 85, 247, 1)",
        pointBorderColor: "#fff",
        pointHoverBackgroundColor: "#fff",
        pointHoverBorderColor: "rgba(99, 102, 241, 1)"
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          angleLines: { color: "rgba(255, 255, 255, 0.1)" },
          grid: { color: "rgba(255, 255, 255, 0.08)" },
          pointLabels: {
            color: "#cbd5e1",
            font: { size: 10, weight: "bold" }
          },
          suggestedMin: 0,
          suggestedMax: 100,
          ticks: { display: false }
        }
      },
      plugins: {
        legend: { display: false }
      }
    }
  });
}

function updateRadarChart(topRecs) {
  if (!matchRadarChart || !topRecs) return;
  matchRadarChart.data.labels = topRecs.map(r => r.title.split(" ")[0] + " " + (r.title.split(" ")[1] || ""));
  matchRadarChart.data.datasets[0].data = topRecs.map(r => r.score);
  matchRadarChart.update();
}

// Direct Navigation Helpers
function viewRoadmapDirect(careerId) {
  switchTab("roadmap");
  const select = document.getElementById("roadmap-career-select");
  if (select) {
    select.value = careerId;
  }
  loadRoadmapForCareer(careerId);
}

function discussRoleInChat(careerId) {
  switchTab("chat");
  const select = document.getElementById("chat-career-focus");
  if (select) {
    select.value = careerId;
  }
  const roleName = allCareersData.find(c => c.id === careerId)?.title || "this role";
  sendChatMessage(`What is the highest-leverage first step I should take to break into ${roleName}?`);
}

// Load Detailed Roadmap
async function loadRoadmapForCareer(careerId) {
  try {
    let data = null;
    const res = await fetch(`/api/careers/${careerId}`).catch(() => null);
    if (res && res.ok) {
      data = await res.json();
    }
    if (!data) {
      data = allCareersData.find(c => c.id === careerId);
    }
    if (!data) return;

    document.getElementById("roadmap-title").textContent = `${data.title} Pathway`;
    document.getElementById("roadmap-desc").textContent = data.overview;
    document.getElementById("roadmap-salary-usd").textContent = data.avg_salary_usd;
    document.getElementById("roadmap-salary-inr").textContent = data.avg_salary_inr || "₹12 - ₹30 LPA";
    document.getElementById("roadmap-growth").textContent = data.demand_level;

    const phasesContainer = document.getElementById("roadmap-phases-container");
    if (!phasesContainer) return;
    phasesContainer.innerHTML = "";

    const roadmapPhases = data.roadmap || [
      {
        phase: "Phase 1: Foundations (Month 1-2)",
        focus: "Core Concepts & Fundamentals",
        milestones: ["Master core programming prerequisites", "Data structures and algorithms", "Version control with Git & GitHub"],
        resources: [{ name: "Official Documentation", type: "Docs", free: true }]
      },
      {
        phase: "Phase 2: Core Competencies (Month 3-4)",
        focus: "Domain-Specific Architecture",
        milestones: ["System design and APIs", "Database persistence & optimization", "Framework best practices"],
        resources: [{ name: "Interactive Courses", type: "Course", free: true }]
      },
      {
        phase: "Phase 3: Portfolio Projects (Month 5-6)",
        focus: "Real-World Applications",
        milestones: ["Build 2 production-ready capstone projects", "Containerization with Docker", "Unit and integration testing"],
        resources: [{ name: "GitHub Project Templates", type: "Code", free: true }]
      },
      {
        phase: "Phase 4: Interview & Production Readiness",
        focus: "Career Launch & Live Deployment",
        milestones: ["Cloud deployment and monitoring", "Resume optimization and ATS review", "Mock technical and behavioral interviews"],
        resources: [{ name: "Interview Question Guides", type: "Guide", free: true }]
      }
    ];

    roadmapPhases.forEach((phase, idx) => {
      const phaseCard = document.createElement("div");
      phaseCard.className = "glass-card rounded-2xl p-6 border border-slate-800 space-y-4";
      phaseCard.innerHTML = `
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <span class="w-8 h-8 rounded-xl bg-indigo-600/30 text-indigo-400 font-bold flex items-center justify-center border border-indigo-500/30 text-sm">
              0${idx + 1}
            </span>
            <div>
              <h3 class="text-base font-bold text-white">${phase.phase}</h3>
              <p class="text-xs text-indigo-400 font-semibold">${phase.focus}</p>
            </div>
          </div>
        </div>

        <div>
          <h4 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Key Milestones & Objectives</h4>
          <ul class="space-y-1.5 text-xs text-slate-300">
            ${phase.milestones.map(m => `
              <li class="flex items-start space-x-2">
                <i class="fa-solid fa-circle-check text-emerald-400 mt-0.5 text-[11px]"></i>
                <span>${m}</span>
              </li>
            `).join('')}
          </ul>
        </div>

        ${phase.resources ? `
        <div class="pt-2 border-t border-slate-800/80">
          <h4 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Recommended Learning Resources</h4>
          <div class="flex flex-wrap gap-2">
            ${phase.resources.map(r => `
              <span class="px-3 py-1 bg-slate-900 border border-slate-700/80 rounded-lg text-xs text-slate-200 flex items-center space-x-1.5">
                <i class="fa-solid fa-graduation-cap text-indigo-400"></i>
                <span class="font-medium">${r.name}</span>
                <span class="text-[10px] px-1.5 py-0.2 bg-slate-800 text-slate-400 rounded">${r.type}</span>
                ${r.free ? '<span class="text-[10px] text-emerald-400 font-bold">FREE</span>' : ''}
              </span>
            `).join('')}
          </div>
        </div>` : ''}
      `;
      phasesContainer.appendChild(phaseCard);
    });

  } catch (err) {
    console.error("Error loading roadmap:", err);
  }
}

// Resume Analyzer
function loadSampleResume() {
  const sample = `John Doe - Software Engineer
Experience:
Full Stack Developer at TechSolutions (2022 - 2024)
- Developed responsive web interfaces using React, JavaScript, and Tailwind CSS.
- Built backend APIs with Node.js and Express; implemented PostgreSQL database queries.
- Deployed services to AWS EC2 and managed code versioning with Git.
- Collaborated in Agile sprints and authored technical documentation for team onboardings.

Education:
B.S. in Computer Science - State University (2018 - 2022)

Skills:
Python, JavaScript, React, Node.js, SQL, HTML, CSS, Git, Docker basics.`;

  document.getElementById("resume-text-input").value = sample;
}

async function analyzeResume() {
  const text = document.getElementById("resume-text-input").value;
  const roleId = document.getElementById("resume-target-role").value;
  const container = document.getElementById("resume-results-container");

  if (!text || text.trim().length < 30) {
    alert("Please enter at least 30 characters of resume text to evaluate.");
    return;
  }

  container.innerHTML = `
    <div class="text-center py-12">
      <i class="fa-solid fa-spinner fa-spin text-3xl text-indigo-400 mb-3"></i>
      <p class="text-sm text-slate-300">Scanning keywords and ATS compatibility...</p>
    </div>`;

  try {
    const res = await fetch("/api/resume-analyzer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ resume_text: text, target_career_id: roleId })
    });
    
    let data;
    if (res.ok) {
      data = await res.json();
    } else {
      // Fallback local resume scoring
      const targetRole = allCareersData.find(c => c.id === roleId) || allCareersData[0];
      const textLower = text.toLowerCase();
      const core = targetRole.core_skills || [];
      const found = core.filter(s => textLower.includes(s.toLowerCase()));
      const missing = core.filter(s => !textLower.includes(s.toLowerCase()));
      const score = Math.round((found.length / Math.max(core.length, 1)) * 100);
      data = {
        target_role: targetRole.title,
        ats_score: score,
        word_count: text.split(/\s+/).length,
        length_feedback: "Resume processed successfully.",
        found_keywords: found,
        missing_critical_keywords: missing,
        actionable_recommendations: [
          `Highlight experience in ${missing.slice(0, 3).join(', ')} if applicable.`,
          "Quantify achievements using metrics (e.g. reduced load times by 30%).",
          "Ensure bullet points begin with strong action verbs."
        ]
      };
    }

    const scoreColor = data.ats_score >= 70 ? "text-emerald-400" :
                       data.ats_score >= 45 ? "text-indigo-400" : "text-amber-400";

    container.innerHTML = `
      <div class="flex items-center justify-between pb-4 border-b border-slate-800">
        <div>
          <span class="text-xs font-semibold text-slate-400">Target Role:</span>
          <h3 class="text-lg font-bold text-white">${data.target_role}</h3>
        </div>
        <div class="text-right">
          <div class="text-3xl font-black ${scoreColor}">${data.ats_score}/100</div>
          <span class="text-[10px] uppercase font-bold text-slate-400">ATS Keyword Fit</span>
        </div>
      </div>

      <!-- Word Count & Length feedback -->
      <div class="p-3 bg-slate-900/80 rounded-xl text-xs text-slate-300 space-y-1">
        <div class="flex justify-between">
          <span class="text-slate-400">Word Count:</span>
          <span class="font-bold text-white">${data.word_count} words</span>
        </div>
        <p class="text-slate-400">${data.length_feedback}</p>
      </div>

      <!-- Keywords Found vs Missing -->
      <div class="space-y-3 text-xs">
        <div>
          <span class="font-semibold text-emerald-400 flex items-center space-x-1.5 mb-1.5">
            <i class="fa-solid fa-check-double"></i>
            <span>Role Keywords Found (${data.found_keywords.length})</span>
          </span>
          <div class="flex flex-wrap gap-1">
            ${data.found_keywords.length ? data.found_keywords.map(k => `<span class="px-2 py-0.5 bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 rounded font-medium">${k}</span>`).join('') : '<span class="text-slate-500">None detected</span>'}
          </div>
        </div>

        <div>
          <span class="font-semibold text-amber-400 flex items-center space-x-1.5 mb-1.5">
            <i class="fa-solid fa-triangle-exclamation"></i>
            <span>Missing High-Impact Keywords (${data.missing_critical_keywords.length})</span>
          </span>
          <div class="flex flex-wrap gap-1">
            ${data.missing_critical_keywords.length ? data.missing_critical_keywords.map(k => `<span class="px-2 py-0.5 bg-amber-500/10 text-amber-300 border border-amber-500/20 rounded font-medium">${k}</span>`).join('') : '<span class="text-emerald-400">All core keywords found!</span>'}
          </div>
        </div>
      </div>

      <!-- Actionable recommendations -->
      <div class="pt-3 border-t border-slate-800 space-y-2">
        <span class="text-xs font-semibold text-slate-300 uppercase tracking-wider">AI Optimizer Recommendations</span>
        <ul class="space-y-1.5 text-xs text-slate-300">
          ${data.actionable_recommendations.map(r => `
            <li class="flex items-start space-x-2">
              <i class="fa-solid fa-arrow-right text-indigo-400 mt-0.5 text-[10px]"></i>
              <span>${r}</span>
            </li>
          `).join('')}
        </ul>
      </div>
    `;

  } catch (err) {
    console.error("Resume analysis error:", err);
    container.innerHTML = `<p class="text-xs text-red-400">Error analyzing resume. Please verify input text.</p>`;
  }
}

// Interactive Chat
function sendQuickPrompt(promptText) {
  document.getElementById("chat-input").value = promptText;
  handleChatSubmit(new Event("submit"));
}

function handleChatSubmit(e) {
  if (e && e.preventDefault) e.preventDefault();
  const input = document.getElementById("chat-input");
  const msg = input.value.trim();
  if (!msg) return;

  sendChatMessage(msg);
  input.value = "";
}

async function sendChatMessage(userText) {
  const messagesContainer = document.getElementById("chat-messages");
  const careerFocus = document.getElementById("chat-career-focus")?.value;
  const apiKey = localStorage.getItem("gemini_api_key") || "";

  // Append user message
  const userBubble = document.createElement("div");
  userBubble.className = "flex items-start justify-end space-x-3";
  userBubble.innerHTML = `
    <div class="bg-indigo-600 text-white p-3.5 rounded-2xl rounded-tr-sm text-sm max-w-xl">
      <p>${escapeHtml(userText)}</p>
    </div>
    <div class="w-8 h-8 rounded-lg bg-indigo-800 flex items-center justify-center text-white shrink-0 shadow-md">
      <i class="fa-solid fa-user text-xs"></i>
    </div>
  `;
  messagesContainer.appendChild(userBubble);
  messagesContainer.scrollTop = messagesContainer.scrollHeight;

  // Append thinking indicator
  const botBubble = document.createElement("div");
  botBubble.className = "flex items-start space-x-3 max-w-2xl";
  botBubble.innerHTML = `
    <div class="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center text-white shrink-0 shadow-md">
      <i class="fa-solid fa-robot text-sm"></i>
    </div>
    <div class="bg-slate-900 border border-slate-800 p-4 rounded-2xl rounded-tl-sm text-sm text-slate-200 chat-prose space-y-2">
      <div class="flex items-center space-x-2 text-slate-400">
        <i class="fa-solid fa-circle-notch fa-spin text-indigo-400"></i>
        <span>Synthesizing guidance...</span>
      </div>
    </div>
  `;
  messagesContainer.appendChild(botBubble);
  messagesContainer.scrollTop = messagesContainer.scrollHeight;

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: userText,
        target_career_id: careerFocus,
        api_key: apiKey
      })
    });
    
    let replyText = "";
    let engineText = "AI Guidance System";

    if (res.ok) {
      const data = await res.json();
      replyText = data.response;
      engineText = data.engine || "AI Guidance System";
    } else {
      replyText = `### 🧭 Career Guidance Note\n\nTo break into this role successfully, focus on building 2 public production-grade projects demonstrating core skills, contribute to open-source repositories, and tailor your portfolio with measurable outcomes.`;
    }

    const proseDiv = botBubble.querySelector(".chat-prose");
    if (proseDiv) {
      proseDiv.innerHTML = marked.parse(replyText || "No response received.");
      
      const badge = document.createElement("div");
      badge.className = "text-[10px] text-slate-500 pt-2 border-t border-slate-800/80 flex items-center justify-between";
      badge.innerHTML = `
        <span>Engine: ${engineText}</span>
        <span class="text-emerald-400">Live</span>
      `;
      proseDiv.appendChild(badge);
    }
    messagesContainer.scrollTop = messagesContainer.scrollHeight;

  } catch (err) {
    console.error("Chat error:", err);
    const proseDiv = botBubble.querySelector(".chat-prose");
    if (proseDiv) {
      proseDiv.innerHTML = `<p class="text-slate-300">Focus on foundational skills, building a public GitHub portfolio, and practicing system design and behavioral interview scenarios.</p>`;
    }
  }
}

function clearChat() {
  const messagesContainer = document.getElementById("chat-messages");
  if (messagesContainer) {
    messagesContainer.innerHTML = `
      <div class="flex items-start space-x-3 max-w-2xl">
        <div class="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center text-white shrink-0 shadow-md">
          <i class="fa-solid fa-robot text-sm"></i>
        </div>
        <div class="bg-slate-900 border border-slate-800 p-4 rounded-2xl rounded-tl-sm text-sm text-slate-200 space-y-2">
          <p class="font-semibold text-white">Chat cleared. Ready for your next career question! 🧭</p>
        </div>
      </div>
    `;
  }
}

// Explore Cards Directory
function renderExploreCards(filteredList = null) {
  const container = document.getElementById("explore-cards-grid");
  if (!container) return;

  const list = filteredList || allCareersData;
  container.innerHTML = "";

  list.forEach(c => {
    const card = document.createElement("div");
    card.className = "glass-card glass-card-hover rounded-2xl p-6 flex flex-col justify-between";
    card.innerHTML = `
      <div class="space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-xs font-semibold px-2 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700">${c.category}</span>
          <span class="text-[11px] font-bold text-emerald-400">${(c.demand_level || "").split(" ")[0]}</span>
        </div>
        <h3 class="text-lg font-bold text-white">${c.title}</h3>
        <p class="text-xs text-slate-300 leading-relaxed">${c.overview}</p>
        <div class="pt-2 text-xs text-slate-400 space-y-1">
          <div><strong class="text-slate-300">Salary:</strong> ${c.avg_salary_usd}</div>
          <div><strong class="text-slate-300">Key Skills:</strong> ${(c.core_skills || []).slice(0, 4).join(', ')}...</div>
        </div>
      </div>
      <div class="pt-4 mt-4 border-t border-slate-800 flex items-center justify-between">
        <button onclick="viewRoadmapDirect('${c.id}')" class="text-xs font-semibold text-indigo-400 hover:text-indigo-300 flex items-center space-x-1">
          <span>Explore Roadmap</span>
          <i class="fa-solid fa-arrow-right text-[10px]"></i>
        </button>
        <button onclick="discussRoleInChat('${c.id}')" class="text-xs text-slate-400 hover:text-white">
          <i class="fa-solid fa-comments"></i>
        </button>
      </div>
    `;
    container.appendChild(card);
  });
}

function filterExploreCards() {
  const query = document.getElementById("explore-search-input").value.toLowerCase();
  const filtered = allCareersData.filter(c => 
    c.title.toLowerCase().includes(query) ||
    c.category.toLowerCase().includes(query) ||
    (c.core_skills && c.core_skills.some(s => s.toLowerCase().includes(query)))
  );
  renderExploreCards(filtered);
}

// API Key Modal Management
function openApiKeyModal() {
  const modal = document.getElementById("api-key-modal");
  const input = document.getElementById("gemini-key-input");
  input.value = localStorage.getItem("gemini_api_key") || "";
  modal.classList.remove("hidden");
}

function closeApiKeyModal() {
  document.getElementById("api-key-modal").classList.add("hidden");
}

function saveApiKey() {
  const val = document.getElementById("gemini-key-input").value.trim();
  if (val) {
    localStorage.setItem("gemini_api_key", val);
    document.getElementById("api-key-status").textContent = "API Key: Saved";
  }
  closeApiKeyModal();
}

function clearApiKey() {
  localStorage.removeItem("gemini_api_key");
  document.getElementById("gemini-key-input").value = "";
  document.getElementById("api-key-status").textContent = "API Key: Auto";
  closeApiKeyModal();
}

function initApiKeyStatus() {
  const key = localStorage.getItem("gemini_api_key");
  const statusEl = document.getElementById("api-key-status");
  if (statusEl) {
    statusEl.textContent = key ? "API Key: Custom" : "API Key: Auto";
  }
}

// Utility
function escapeHtml(str) {
  return str.replace(/[&<>'"]/g, 
    tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
  );
}
