"""
AI Career Guidance Navigator - Career Knowledge Base & Data Models
Contains rich taxonomies for career roles, skill requirements, roadmap phases,
and intelligent matching algorithms.
"""

from typing import List, Dict, Any

CAREER_DATABASE: Dict[str, Dict[str, Any]] = {
    "ai_ml_engineer": {
        "id": "ai_ml_engineer",
        "title": "AI & Machine Learning Engineer",
        "category": "Artificial Intelligence & Data",
        "overview": "Designs, builds, and deploys scalable machine learning models and AI systems into production software products.",
        "avg_salary_usd": "$125,000 - $185,000 / yr",
        "avg_salary_inr": "₹14 - ₹35 LPA",
        "demand_level": "Extremely High (38% growth)",
        "work_style": ["Analytical", "Problem Solving", "Continuous Learning", "Autonomous"],
        "core_skills": [
            "python", "machine learning", "deep learning", "pytorch", "tensorflow",
            "mathematics & linear algebra", "pandas", "numpy", "sql", "data preprocessing"
        ],
        "secondary_skills": [
            "docker", "mlops", "fastapi", "git", "scikit-learn", "llms", "hugging face", "langchain", "cloud platforms (aws/gcp)"
        ],
        "soft_skills": [
            "Critical Thinking", "Research Aptitude", "Cross-functional Collaboration", "Scientific Curiosity"
        ],
        "suitable_education": ["Computer Science", "Data Science", "Mathematics", "Statistics", "Engineering", "Self-Taught / STEM"],
        "roadmap": [
            {
                "phase": "Phase 1: Foundations (Month 1-2)",
                "focus": "Programming & Mathematical Groundwork",
                "milestones": [
                    "Master Python: OOP, list comprehensions, generators, and debugging",
                    "Calculus & Linear Algebra: vectors, matrices, eigenvalues, gradients",
                    "Probability & Statistics: Bayes' theorem, distributions, hypothesis testing",
                    "Data Wrangling with NumPy, Pandas, and Matplotlib/Seaborn"
                ],
                "resources": [
                    {"name": "3Blue1Brown - Essence of Linear Algebra", "type": "Video Series", "free": True},
                    {"name": "Kaggle Learn: Python & Pandas", "type": "Interactive Course", "free": True}
                ]
            },
            {
                "phase": "Phase 2: Core Machine Learning (Month 3-4)",
                "focus": "Classical ML & Feature Engineering",
                "milestones": [
                    "Supervised Learning: Linear/Logistic Regression, Decision Trees, Random Forests, XGBoost",
                    "Unsupervised Learning: K-Means, PCA, Hierarchical Clustering",
                    "Model Evaluation: Cross-validation, ROC-AUC, precision/recall, loss functions",
                    "Complete 3 Kaggle tabular competitions"
                ],
                "resources": [
                    {"name": "Andrew Ng - Machine Learning Specialization (Coursera/DeepLearning.AI)", "type": "Course", "free": True},
                    {"name": "Scikit-Learn Official Guides", "type": "Documentation", "free": True}
                ]
            },
            {
                "phase": "Phase 3: Deep Learning & Generative AI (Month 5-6)",
                "focus": "Neural Networks, Transformers & LLMs",
                "milestones": [
                    "Deep Learning with PyTorch: CNNs for Computer Vision, RNNs/Transformers for NLP",
                    "Fine-tuning Open-Source LLMs (Llama, Mistral) with Hugging Face & PEFT/LoRA",
                    "Vector Databases (Chroma/FAISS) and RAG applications with LangChain / LlamaIndex",
                    "Build an end-to-end multi-modal or RAG production assistant"
                ],
                "resources": [
                    {"name": "Fast.ai - Practical Deep Learning for Coders", "type": "Course", "free": True},
                    {"name": "Hugging Face NLP Course", "type": "Interactive Course", "free": True}
                ]
            },
            {
                "phase": "Phase 4: MLOps & Production Readiness (Month 7-8)",
                "focus": "Model Deployment, Monitoring & Career Launch",
                "milestones": [
                    "Package models as REST APIs using FastAPI & Docker",
                    "CI/CD and Model Tracking with MLflow and GitHub Actions",
                    "Cloud deployment on AWS SageMaker / GCP Vertex AI / Render",
                    "Publish 2 polished portfolio projects on GitHub with live demos"
                ],
                "resources": [
                    {"name": "Made With ML (MLOps Guide)", "type": "Website", "free": True},
                    {"name": "Full Stack Deep Learning Course", "type": "Course", "free": True}
                ]
            }
        ],
        "top_certifications": ["AWS Certified Machine Learning - Specialty", "Google Professional Machine Learning Engineer", "TensorFlow Developer Certificate"],
        "interview_topics": ["Bias-Variance Tradeoff", "Backpropagation Math", "Attention Mechanism & Transformers", "RAG Pipeline Architecture", "Model Latency Optimization"]
    },

    "full_stack_developer": {
        "id": "full_stack_developer",
        "title": "Full Stack Web Developer",
        "category": "Software Engineering",
        "overview": "Builds end-to-end web applications, crafting intuitive user interfaces and architecting robust server-side APIs and databases.",
        "avg_salary_usd": "$95,000 - $145,000 / yr",
        "avg_salary_inr": "₹8 - ₹24 LPA",
        "demand_level": "Very High (25% growth)",
        "work_style": ["Creative & Visual", "Logical Problem Solving", "Fast Iteration", "Product Minded"],
        "core_skills": [
            "javascript", "typescript", "react", "node.js", "html5", "css3", "sql", "git", "rest apis"
        ],
        "secondary_skills": [
            "next.js", "tailwind css", "postgresql", "mongodb", "docker", "graphql", "redis", "cloud hosting (vercel/aws)"
        ],
        "soft_skills": [
            "Communication", "Attention to Detail", "Team Collaboration", "Agile Adaptability"
        ],
        "suitable_education": ["Computer Science", "Information Technology", "Bootcamp Graduate", "Self-Taught Any Discipline"],
        "roadmap": [
            {
                "phase": "Phase 1: Web Fundamentals (Month 1)",
                "focus": "Semantic HTML, Modern CSS, Responsive Design",
                "milestones": [
                    "HTML5 semantics, accessibility (a11y), forms, DOM tree",
                    "CSS3 Flexbox, Grid, animations, and Tailwind CSS",
                    "JavaScript ES6+: promises, async/await, closures, fetch API",
                    "Build responsive portfolio and interactive landing page"
                ],
                "resources": [
                    {"name": "The Odin Project - Foundations", "type": "Curriculum", "free": True},
                    {"name": "MDN Web Docs", "type": "Reference", "free": True}
                ]
            },
            {
                "phase": "Phase 2: Modern Frontend (Month 2-3)",
                "focus": "React & Modern UI Ecosystem",
                "milestones": [
                    "React hooks, custom hooks, component lifecycles, and state management (Zustand/Redux)",
                    "TypeScript integration with React for strict type safety",
                    "Client-side routing, Next.js App Router, SSR & SSG",
                    "Build an interactive dashboard consuming third-party REST APIs"
                ],
                "resources": [
                    {"name": "React Official Docs (react.dev)", "type": "Interactive Docs", "free": True},
                    {"name": "Next.js Learn Course", "type": "Tutorial", "free": True}
                ]
            },
            {
                "phase": "Phase 3: Backend & Database Architecture (Month 4-5)",
                "focus": "Server APIs, Authentication, Databases",
                "milestones": [
                    "Node.js & Express / NestJS / FastAPI server architecture",
                    "Relational DBs (PostgreSQL) with Prisma ORM / SQLAlchemy",
                    "NoSQL (MongoDB / Redis) for caching and sessions",
                    "JWT authentication, OAuth2, role-based access control (RBAC)",
                    "Build a complete SaaS prototype with payments & auth"
                ],
                "resources": [
                    {"name": "Full Stack Open (University of Helsinki)", "type": "Course", "free": True},
                    {"name": "Prisma & PostgreSQL Tutorials", "type": "Guides", "free": True}
                ]
            },
            {
                "phase": "Phase 4: DevOps, Testing & Launch (Month 6)",
                "focus": "Deployment, Automated Testing & System Design",
                "milestones": [
                    "Unit & integration tests with Jest, Playwright, or Cypress",
                    "Docker containerization & multi-stage builds",
                    "CI/CD workflows with GitHub Actions & cloud deployment",
                    "System design: microservices vs monolith, load balancing, caching"
                ],
                "resources": [
                    {"name": "Docker for Beginners", "type": "Video", "free": True},
                    {"name": "System Design Primer by Donne Martin", "type": "GitHub Repo", "free": True}
                ]
            }
        ],
        "top_certifications": ["Meta Front-End / Back-End Professional Certificate", "AWS Certified Developer - Associate"],
        "interview_topics": ["Event Loop & Async JS", "React Reconciliation & Virtual DOM", "Database Indexing & Normalization", "Security (CORS, XSS, CSRF)", "System Design of Web Apps"]
    },

    "data_scientist": {
        "id": "data_scientist",
        "title": "Data Scientist & Analytics Lead",
        "category": "Artificial Intelligence & Data",
        "overview": "Transforms unstructured complex data into actionable business intelligence, predictive algorithms, and executive strategic insights.",
        "avg_salary_usd": "$110,000 - $160,000 / yr",
        "avg_salary_inr": "₹12 - ₹30 LPA",
        "demand_level": "High (28% growth)",
        "work_style": ["Investigative", "Statistical Reasoning", "Business Strategy", "Data Storytelling"],
        "core_skills": [
            "python", "sql", "statistics", "data visualization", "pandas", "numpy", "machine learning", "exploratory data analysis"
        ],
        "secondary_skills": [
            "tableau", "power bi", "a/b testing", "r", "bigquery", "snowflake", "spark", "scikit-learn"
        ],
        "soft_skills": [
            "Business Acumen", "Storytelling with Data", "Stakeholder Communication", "Hypothesis Formulation"
        ],
        "suitable_education": ["Statistics", "Economics", "Mathematics", "Computer Science", "Business Analytics"],
        "roadmap": [
            {
                "phase": "Phase 1: Statistical Foundations & Advanced SQL (Month 1-2)",
                "focus": "Quantitative Logic & Database Querying",
                "milestones": [
                    "Descriptive & inferential statistics, confidence intervals, p-values",
                    "Advanced SQL: Window functions, CTEs, self-joins, query optimization",
                    "Python for scientific computing: Pandas vectorization & NumPy indexing",
                    "Design & evaluate rigorous A/B experiments"
                ],
                "resources": [
                    {"name": "Mode Analytics SQL Tutorial", "type": "Tutorial", "free": True},
                    {"name": "Khan Academy Statistics & Probability", "type": "Course", "free": True}
                ]
            },
            {
                "phase": "Phase 2: Exploratory Data Analysis & Visualization (Month 3)",
                "focus": "Visual Data Storytelling",
                "milestones": [
                    "Interactive dashboards using Tableau, Power BI, or Streamlit",
                    "Seaborn & Plotly for multivariate visualizations",
                    "Handling missing data, outliers, skewness, and normalization",
                    "Write executive-level data insights memo"
                ],
                "resources": [
                    {"name": "Storytelling with Data by Cole Nussbaumer Knaflic", "type": "Book/Blog", "free": False},
                    {"name": "Streamlit Documentation & Gallery", "type": "Interactive", "free": True}
                ]
            },
            {
                "phase": "Phase 3: Predictive Modeling & ML (Month 4-5)",
                "focus": "Supervised & Unsupervised Analytics",
                "milestones": [
                    "Classification, Regression, and Time Series Forecasting (Prophet, ARIMA)",
                    "Customer segmentation with K-means, churn prediction, recommendation engines",
                    "Feature engineering and dimensionality reduction (t-SNE, UMAP)",
                    "Publish 2 domain-specific analytics case studies (e.g., E-commerce, FinTech)"
                ],
                "resources": [
                    {"name": "Applied Data Science with Python (University of Michigan)", "type": "Course", "free": True},
                    {"name": "Hands-On Machine Learning with Scikit-Learn", "type": "Book", "free": False}
                ]
            },
            {
                "phase": "Phase 4: Big Data & Enterprise Scale (Month 6)",
                "focus": "Cloud Warehouses & Scaling",
                "milestones": [
                    "Cloud Data Warehouses: BigQuery or Snowflake",
                    "Distributed computing with Apache Spark / PySpark",
                    "Automated data pipelines with dbt and Airflow",
                    "Mock technical interviews and presentation coaching"
                ],
                "resources": [
                    {"name": "dbt Learn Documentation", "type": "Docs", "free": True},
                    {"name": "Datacamp Data Science Career Track", "type": "Platform", "free": False}
                ]
            }
        ],
        "top_certifications": ["Google Data Analytics Professional Certificate", "IBM Data Science Professional Certificate", "Databricks Certified Data Scientist"],
        "interview_topics": ["A/B Testing Metric Selection", "Overfitting vs Underfitting", "SQL Window Functions Live Coding", "Business Problem Framing", "Central Limit Theorem"]
    },

    "cloud_devops_engineer": {
        "id": "cloud_devops_engineer",
        "title": "Cloud Solutions & DevOps Engineer",
        "category": "Cloud & Infrastructure",
        "overview": "Architects resilient cloud infrastructure, automates deployment pipelines, and guarantees 99.99% system availability and security.",
        "avg_salary_usd": "$115,000 - $170,000 / yr",
        "avg_salary_inr": "₹10 - ₹28 LPA",
        "demand_level": "Extremely High (32% growth)",
        "work_style": ["Systematic", "Automation-Driven", "High Reliability", "Incident Responder"],
        "core_skills": [
            "linux", "docker", "kubernetes", "aws", "terraform", "ci/cd", "bash", "git", "networking"
        ],
        "secondary_skills": [
            "python", "ansible", "prometheus", "grafana", "gcp", "azure", "helm", "security (devsecops)"
        ],
        "soft_skills": [
            "Calm Under Pressure", "Root Cause Analysis", "Clear Technical Documentation", "Proactive Mindset"
        ],
        "suitable_education": ["Computer Science", "Information Systems", "System Administration", "Engineering"],
        "roadmap": [
            {
                "phase": "Phase 1: Linux & Networking Fundamentals (Month 1)",
                "focus": "OS Internals, Shell Scripting, TCP/IP",
                "milestones": [
                    "Linux administration: file systems, permissions, systemd, process management",
                    "Bash scripting for automated tasks and system audits",
                    "Networking: TCP/IP, DNS, SSL/TLS, reverse proxies (Nginx), HTTP protocols",
                    "Version control with Git branching strategies (GitFlow, Trunk-based)"
                ],
                "resources": [
                    {"name": "Linux Journey (linuxjourney.com)", "type": "Interactive Guide", "free": True},
                    {"name": "OverTheWire: Bandit Wargame", "type": "Practice Game", "free": True}
                ]
            },
            {
                "phase": "Phase 2: Cloud Core & Containerization (Month 2-3)",
                "focus": "AWS/GCP & Docker",
                "milestones": [
                    "AWS Core Services: EC2, VPC, S3, IAM, Route53, RDS, CloudFront",
                    "Docker: Dockerfile optimization, multi-stage builds, docker-compose",
                    "Security best practices: IAM least-privilege policies, secret management",
                    "Deploy containerized microservices to cloud"
                ],
                "resources": [
                    {"name": "AWS Skill Builder / Free Tier Lab Guides", "type": "Hands-on", "free": True},
                    {"name": "Docker Mastery on Udemy / YouTube FreeCodeCamp", "type": "Video", "free": True}
                ]
            },
            {
                "phase": "Phase 3: Infrastructure as Code & CI/CD (Month 4-5)",
                "focus": "Terraform & GitHub Actions",
                "milestones": [
                    "Terraform: declarative syntax, modules, state management, drift detection",
                    "Automated CI/CD pipelines with GitHub Actions, GitLab CI, or Jenkins",
                    "Automated testing, linting, and zero-downtime deployment strategies",
                    "Provision entire cloud infrastructure via code repository"
                ],
                "resources": [
                    {"name": "HashiCorp Terraform Associate Tutorials", "type": "Official Docs", "free": True},
                    {"name": "GitHub Actions Documentation", "type": "Docs", "free": True}
                ]
            },
            {
                "phase": "Phase 4: Kubernetes & Observability (Month 6)",
                "focus": "Container Orchestration & Monitoring",
                "milestones": [
                    "Kubernetes architecture: Pods, Deployments, Services, Ingress, ConfigMaps",
                    "Deploy production K8s clusters (EKS/GKE) with Helm charts",
                    "Observability: metrics collection with Prometheus, dashboards with Grafana, log aggregation with Loki/ELK",
                    "Simulate failure scenarios and write incident post-mortems"
                ],
                "resources": [
                    {"name": "Kubernetes the Hard Way by Kelsey Hightower", "type": "GitHub Repo", "free": True},
                    {"name": "Mumshad Mannambeth CKA prep course", "type": "Course", "free": False}
                ]
            }
        ],
        "top_certifications": ["AWS Certified Solutions Architect - Associate", "CKA: Certified Kubernetes Administrator", "HashiCorp Certified: Terraform Associate"],
        "interview_topics": ["Zero Downtime Deployment Strategies", "Kubernetes Pod Lifecycle & Troubleshooting", "VPC Peering & Routing Tables", "Terraform State Locking", "Observability vs Monitoring"]
    },

    "cybersecurity_analyst": {
        "id": "cybersecurity_analyst",
        "title": "Cybersecurity Analyst & Threat Specialist",
        "category": "Security & Defense",
        "overview": "Protects organizational networks, applications, and confidential assets from digital threats, breaches, and vulnerabilities.",
        "avg_salary_usd": "$105,000 - $155,000 / yr",
        "avg_salary_inr": "₹9 - ₹25 LPA",
        "demand_level": "Extremely High (35% growth)",
        "work_style": ["Detail Oriented", "Ethical Mindset", "Investigative", "Vigilant"],
        "core_skills": [
            "network security", "linux", "siem (splunk/sentinel)", "incident response", "vulnerability assessment", "wireshark", "python/bash"
        ],
        "secondary_skills": [
            "penetration testing", "owasp top 10", "cryptography", "cloud security", "threat hunting", "firewalls", "forensics"
        ],
        "soft_skills": [
            "Integrity", "Stress Tolerance", "Analytical Rigor", "Clear Incident Reporting"
        ],
        "suitable_education": ["Cybersecurity", "Computer Science", "Information Assurance", "Criminology / Law"],
        "roadmap": [
            {
                "phase": "Phase 1: IT & Network Architecture (Month 1-2)",
                "focus": "OS Security & Packet Analysis",
                "milestones": [
                    "OSI Model, TCP/IP headers, routing, subnetting, DNS, ARP",
                    "Deep packet inspection using Wireshark and tcpdump",
                    "Linux and Windows endpoint administration and hardening",
                    "Understand common attacks: MITM, DoS, Spoofing, Phishing"
                ],
                "resources": [
                    {"name": "Professor Messer's CompTIA Network+ & Security+", "type": "Video Series", "free": True},
                    {"name": "Wireshark Sample Captures Lab", "type": "Hands-on", "free": True}
                ]
            },
            {
                "phase": "Phase 2: Defensive Security & SOC Operations (Month 3-4)",
                "focus": "SIEM, Monitoring, Log Analysis",
                "milestones": [
                    "SIEM platforms: Splunk, Elastic SIEM, Microsoft Sentinel",
                    "Log analysis: syslog, Windows Event Viewer, firewall and proxy logs",
                    "Incident response lifecycle (NIST / SANS frameworks)",
                    "Threat intelligence gathering with MITRE ATT&CK matrix"
                ],
                "resources": [
                    {"name": "TryHackMe - SOC Level 1 Pathway", "type": "Interactive Labs", "free": False},
                    {"name": "MITRE ATT&CK Framework Documentation", "type": "Reference", "free": True}
                ]
            },
            {
                "phase": "Phase 3: Vulnerability Assessment & Web Security (Month 5)",
                "focus": "OWASP Top 10 & Scanning Tools",
                "milestones": [
                    "Web application security: SQL Injection, XSS, CSRF, IDOR, SSRF",
                    "Vulnerability scanning with Nessus, Nmap, and OpenVAS",
                    "Burp Suite basics for manual vulnerability testing",
                    "Draft comprehensive vulnerability assessment reports with remediation steps"
                ],
                "resources": [
                    {"name": "PortSwigger Web Security Academy", "type": "Interactive Labs", "free": True},
                    {"name": "Hack The Box Academy", "type": "Labs", "free": False}
                ]
            },
            {
                "phase": "Phase 4: Cloud Security & Certifications (Month 6-7)",
                "focus": "Enterprise Readiness & Incident Drills",
                "milestones": [
                    "Cloud Security: AWS GuardDuty, Security Hub, IAM policies",
                    "Basic Python automation for threat intelligence feeds and parsing logs",
                    "Conduct table-top ransomware response drill",
                    "CompTIA Security+ or BTL1 certification"
                ],
                "resources": [
                    {"name": "Blue Team Labs Online (BTLO)", "type": "Practice", "free": True},
                    {"name": "CIS Controls and Benchmarks", "type": "Standards", "free": True}
                ]
            }
        ],
        "top_certifications": ["CompTIA Security+", "Blue Team Level 1 (BTL1)", "Certified Information Systems Security Professional (CISSP)", "CEH (Certified Ethical Hacker)"],
        "interview_topics": ["Three-way Handshake & SYN Floods", "OWASP Top 10 Explanations & Fixes", "Incident Response Steps under NIST", "Symmetric vs Asymmetric Encryption", "Investigating a Suspicious Email Header"]
    },

    "product_manager": {
        "id": "product_manager",
        "title": "Technical Product Manager",
        "category": "Product & Strategy",
        "overview": "Discovers user needs, defines product vision, and leads cross-functional teams of engineers and designers to launch impactful tech products.",
        "avg_salary_usd": "$120,000 - $175,000 / yr",
        "avg_salary_inr": "₹15 - ₹35 LPA",
        "demand_level": "High (20% growth)",
        "work_style": ["Strategic", "Empathetic", "Leadership without Authority", "Metrics-Driven"],
        "core_skills": [
            "product strategy", "user research", "agile & scrum", "wireframing", "roadmapping", "product analytics", "a/b testing", "sql basics"
        ],
        "secondary_skills": [
            "jira", "figma", "mixpanel / amplitude", "market analysis", "technical architecture awareness", "go-to-market strategy"
        ],
        "soft_skills": [
            "High Emotional Intelligence", "Executive Presentation", "Conflict Resolution", "Decisiveness"
        ],
        "suitable_education": ["Engineering", "Business / MBA", "Human-Computer Interaction", "Any background with product curiosity"],
        "roadmap": [
            {
                "phase": "Phase 1: Product Mindset & Discovery (Month 1)",
                "focus": "Customer Empathy & Problem Validation",
                "milestones": [
                    "Product discovery frameworks (Design Thinking, Jobs-to-be-Done)",
                    "Conducting effective user interviews and synthesis into personas",
                    "Competitive landscape mapping and market sizing (TAM/SAM/SOM)",
                    "Write a comprehensive Problem Statement document"
                ],
                "resources": [
                    {"name": "Inspired by Marty Cagan", "type": "Book", "free": False},
                    {"name": "Lenny's Newsletter & Podcast", "type": "Blog", "free": True}
                ]
            },
            {
                "phase": "Phase 2: Product Requirements & Execution (Month 2-3)",
                "focus": "PRD Writing & Agile Delivery",
                "milestones": [
                    "Drafting comprehensive Product Requirement Documents (PRDs)",
                    "User stories, acceptance criteria, and edge-case mapping",
                    "Agile workflows: Sprint planning, backlog grooming, retrospective in Jira",
                    "Low-fidelity wireframing with Figma / Balsamiq"
                ],
                "resources": [
                    {"name": "Atlassian Agile Coach Guides", "type": "Guides", "free": True},
                    {"name": "Product School Resources & Templates", "type": "Templates", "free": True}
                ]
            },
            {
                "phase": "Phase 3: Data-Driven Decisions & Growth (Month 4)",
                "focus": "Metrics, Telemetry & Experimentation",
                "milestones": [
                    "Product metrics: North Star Metric, OKRs, CAC, LTV, Churn, Retention cohorts",
                    "Telemetry tracking with Mixpanel / Amplitude / Google Analytics",
                    "Designing hypothesis-driven A/B tests and statistical validation",
                    "Basic SQL for self-serve querying of user funnels"
                ],
                "resources": [
                    {"name": "Reforge Product Strategy Series", "type": "Articles", "free": True},
                    {"name": "Amplitude Product Analytics Certification", "type": "Course", "free": True}
                ]
            },
            {
                "phase": "Phase 4: Capstone Teardown & PM Interview Prep (Month 5-6)",
                "focus": "Portfolio Teardowns & Case Interviews",
                "milestones": [
                    "Publish 2 detailed product teardowns with redesigned feature proposals",
                    "Product design interviews: 'Design an ATM for elderly users'",
                    "Product sense & analytical estimation: Fermi problems",
                    "Behavioral leadership questions (STAR method)"
                ],
                "resources": [
                    {"name": "Decode and Conquer by Lewis C. Lin", "type": "Book", "free": False},
                    {"name": "Exponent Product Management Interview Prep", "type": "Practice", "free": True}
                ]
            }
        ],
        "top_certifications": ["Product School Certified Product Manager (CPM)", "Scrum Product Owner (CSPO)", "Pragmatic Institute Certified"],
        "interview_topics": ["Favorite Product and How to Improve It", "Prioritization Frameworks (RICE, MoSCoW)", "Root-cause Analysis of Metric Drop", "Managing Engineering Disagreements", "Defining North Star Metrics"]
    },

    "ui_ux_designer": {
        "id": "ui_ux_designer",
        "title": "UI/UX & Product Designer",
        "category": "Design & User Experience",
        "overview": "Creates seamless, visually elegant, and user-centered digital interfaces through user research, prototyping, and design systems.",
        "avg_salary_usd": "$88,000 - $135,000 / yr",
        "avg_salary_inr": "₹7 - ₹22 LPA",
        "demand_level": "High (18% growth)",
        "work_style": ["Creative", "Human-Centric", "Visual Polish", "Collaborative"],
        "core_skills": [
            "figma", "user research", "wireframing", "prototyping", "design systems", "information architecture", "usability testing"
        ],
        "secondary_skills": [
            "html/css basics", "micro-interactions", "typography & color theory", "accessibility (wcag)", "framer / lottie", "design tokens"
        ],
        "soft_skills": [
            "Empathy", "Constructive Critique", "Storytelling", "Client Presentation"
        ],
        "suitable_education": ["Design", "HCI", "Psychology", "Fine Arts", "Any Creative Discipline"],
        "roadmap": [
            {
                "phase": "Phase 1: Design Principles & Figma Mastery (Month 1-2)",
                "focus": "Visual Design & Tooling",
                "milestones": [
                    "Design fundamentals: hierarchy, typography, grids, whitespace, color contrast",
                    "Master Figma: auto-layout, components, variants, variables, interactive components",
                    "Study WCAG 2.1 accessibility guidelines",
                    "Recreate 5 iconic mobile apps with pixel precision"
                ],
                "resources": [
                    {"name": "Figma Official YouTube Tutorial Series", "type": "Video", "free": True},
                    {"name": "Refactoring UI by Adam Wathan & Steve Schoger", "type": "Book", "free": False}
                ]
            },
            {
                "phase": "Phase 2: UX Research & Information Architecture (Month 3)",
                "focus": "User Insights & Flow Design",
                "milestones": [
                    "User interviews, surveys, affinity mapping, and user personas",
                    "User journeys, empathy maps, and service blueprints",
                    "Information architecture and card sorting exercises",
                    "Usability testing sessions and heuristic evaluations"
                ],
                "resources": [
                    {"name": "Nielsen Norman Group Articles & Videos", "type": "Reference", "free": True},
                    {"name": "Interaction Design Foundation (IxDF)", "type": "Courses", "free": False}
                ]
            },
            {
                "phase": "Phase 3: Design Systems & Advanced Prototyping (Month 4)",
                "focus": "Scalability & Micro-interactions",
                "milestones": [
                    "Building multi-platform design systems with atomic design principles",
                    "Figma variables, design tokens, responsive breakpoints",
                    "High-fidelity micro-interactions and smart animations",
                    "Developer handoff documentation in Figma / Zeplin"
                ],
                "resources": [
                    {"name": "Design Systems Handbook by InVision", "type": "E-book", "free": True},
                    {"name": "Google Material Design 3 Documentation", "type": "Reference", "free": True}
                ]
            },
            {
                "phase": "Phase 4: Case Studies & Portfolio Website (Month 5-6)",
                "focus": "Portfolio & Critique Readiness",
                "milestones": [
                    "Craft 2-3 in-depth end-to-end case studies showing problem-solving process",
                    "Publish a responsive portfolio site (using Framer, Webflow, or custom code)",
                    "Practice live app critique and whiteboard design challenges",
                    "Network with design communities on ADPList and Dribbble"
                ],
                "resources": [
                    {"name": "Cofolios (Design Intern & New Grad Portfolios)", "type": "Inspiration", "free": True},
                    {"name": "ADPList Mentorship Platform", "type": "Mentorship", "free": True}
                ]
            }
        ],
        "top_certifications": ["Google UX Design Professional Certificate", "Nielsen Norman Group UX Master Certified"],
        "interview_topics": ["Walkthrough of a Past Portfolio Case Study", "Live Whiteboard Challenge", "Handling Conflicting Engineering Constraints", "Design System Governance", "Heuristic Evaluation of an Interface"]
    },

    "mobile_app_developer": {
        "id": "mobile_app_developer",
        "title": "Mobile App Developer (iOS / Flutter / React Native)",
        "category": "Software Engineering",
        "overview": "Builds high-performance native and cross-platform smartphone applications for millions of active mobile users worldwide.",
        "avg_salary_usd": "$98,000 - $150,000 / yr",
        "avg_salary_inr": "₹8 - ₹24 LPA",
        "demand_level": "High (22% growth)",
        "work_style": ["Fast-Paced", "User-Focused", "Device-Specific Optimization"],
        "core_skills": [
            "flutter / dart" , "react native / typescript", "swift / kotlin", "mobile ui design", "rest apis", "offline storage (sqlite/realm)", "git"
        ],
        "secondary_skills": [
            "firebase", "app store deployment", "google play console", "push notifications", "state management (bloc/redux)", "graphql"
        ],
        "soft_skills": [
            "Detail Orientation", "User Empathy", "Resource Optimization", "Collaboration"
        ],
        "suitable_education": ["Computer Science", "Software Engineering", "Self-Taught"],
        "roadmap": [
            {
                "phase": "Phase 1: Language & Core Paradigm (Month 1-2)",
                "focus": "Dart/Swift & Mobile Architecture",
                "milestones": [
                    "Master Dart (for Flutter) or Swift/Kotlin (for Native)",
                    "Understanding reactive declarative UI architectures",
                    "Component lifecycles, navigation stacks, and gesture detectors",
                    "Build an offline notes and todo app with local persistence"
                ],
                "resources": [
                    {"name": "Flutter Official Documentation & Codelabs", "type": "Interactive", "free": True},
                    {"name": "100 Days of SwiftUI by Paul Hudson", "type": "Course", "free": True}
                ]
            },
            {
                "phase": "Phase 2: State Management & Networking (Month 3-4)",
                "focus": "Complex State & API Integration",
                "milestones": [
                    "State management: Riverpod / BLoC / Redux",
                    "Asynchronous networking, caching, and error states",
                    "Integrating device hardware: Camera, Geolocation, Biometrics",
                    "Build a live weather & map tracking application"
                ],
                "resources": [
                    {"name": "Reso Coder Flutter Clean Architecture Tutorials", "type": "Tutorials", "free": True}
                ]
            },
            {
                "phase": "Phase 3: Backend Integration & Performance (Month 5)",
                "focus": "Firebase, Auth & Profiling",
                "milestones": [
                    "Firebase Authentication, Firestore, and Cloud Functions",
                    "Push Notifications (FCM) and deep-linking schemas",
                    "Memory profiling, frame-rate (60/120fps) optimization, battery drain reduction"
                ],
                "resources": [
                    {"name": "Firebase Guides for Mobile", "type": "Docs", "free": True}
                ]
            },
            {
                "phase": "Phase 4: Store Publishing & Production (Month 6)",
                "focus": "App Store & Play Store Release",
                "milestones": [
                    "Signing keys, certificates, provisioning profiles",
                    "Publishing an app to Google Play Store & Apple TestFlight",
                    "In-app purchases and analytics instrumentation",
                    "Automating builds with Fastlane"
                ],
                "resources": [
                    {"name": "Fastlane Documentation", "type": "Docs", "free": True}
                ]
            }
        ],
        "top_certifications": ["Meta Android/iOS Developer Certificate", "Google Associate Android Developer"],
        "interview_topics": ["State Management Tradeoffs", "App Lifecycle States", "Memory Leaks in Mobile", "Handling Offline Mode & Sync", "App Store Guidelines Compliance"]
    },

    "data_engineer": {
        "id": "data_engineer",
        "title": "Data Engineer & Pipeline Architect",
        "category": "Artificial Intelligence & Data",
        "overview": "Builds high-throughput ETL data pipelines, orchestrates data lakes, and ensures clean reliable data streams for AI and business analysts.",
        "avg_salary_usd": "$115,000 - $165,000 / yr",
        "avg_salary_inr": "₹11 - ₹28 LPA",
        "demand_level": "Extremely High (33% growth)",
        "work_style": ["Engineering-First", "High Volume", "Reliability-Minded"],
        "core_skills": [
            "python", "sql", "apache spark", "airflow", "data warehousing (snowflake/bigquery)", "etl/elt", "kafka", "docker"
        ],
        "secondary_skills": [
            "dbt", "aws (s3, glue, redshift)", "scala", "data modeling (star/snowflake)", "delta lake", "presto/trino"
        ],
        "soft_skills": [
            "System Thinking", "Collaborative", "Reliability Discipline", "Documentation"
        ],
        "suitable_education": ["Computer Science", "Data Engineering", "Information Systems", "STEM"],
        "roadmap": [
            {
                "phase": "Phase 1: Advanced SQL & Data Modeling (Month 1)",
                "focus": "Relational Theory & Dimensional Modeling",
                "milestones": [
                    "Complex SQL queries, window functions, indexing, and EXPLAIN plans",
                    "Dimensional modeling: Kimball methodology, facts, dimensions, slowly changing dimensions (SCD)",
                    "Data ingestion scripts in Python with robust error handling"
                ],
                "resources": [
                    {"name": "The Data Warehouse Toolkit by Ralph Kimball", "type": "Book", "free": False}
                ]
            },
            {
                "phase": "Phase 2: Orchestration & Modern Data Stack (Month 2-3)",
                "focus": "Airflow & dbt",
                "milestones": [
                    "Data pipeline orchestration using Apache Airflow DAGs",
                    "Data transformations with dbt (data build tool) and automated testing",
                    "Setting up and querying cloud data warehouses (Snowflake, BigQuery)",
                    "Build an automated ETL pipeline transforming raw API data into business analytics views"
                ],
                "resources": [
                    {"name": "Astronomer Airflow Tutorials", "type": "Guides", "free": True},
                    {"name": "dbt Fundamentals Course", "type": "Interactive Course", "free": True}
                ]
            },
            {
                "phase": "Phase 3: Big Data & Distributed Systems (Month 4-5)",
                "focus": "Apache Spark & Streaming",
                "milestones": [
                    "PySpark / Spark SQL for petabyte-scale distributed dataframes",
                    "Streaming architecture with Apache Kafka and Spark Streaming",
                    "Parquet file format, partitioning strategies, and Delta Lake ACID transactions"
                ],
                "resources": [
                    {"name": "Spark: The Definitive Guide", "type": "Book", "free": False}
                ]
            },
            {
                "phase": "Phase 4: Cloud Infrastructure & Production (Month 6)",
                "focus": "Infrastructure as Code & CI/CD for Data",
                "milestones": [
                    "Deploying pipelines on AWS / GCP using Docker and Terraform",
                    "Data observability, pipeline alerting, and data contracts",
                    "Publish 2 scalable data engineering projects on GitHub with architecture diagrams"
                ],
                "resources": [
                    {"name": "Data Engineering Zoomcamp (DataTalks.Club)", "type": "Free Bootcamp", "free": True}
                ]
            }
        ],
        "top_certifications": ["Databricks Certified Data Engineer Associate", "Google Professional Data Engineer", "AWS Certified Data Engineer"],
        "interview_topics": ["Star Schema vs 3NF", "Spark Shuffle & Partitioning Optimization", "Batch vs Real-Time Streaming Tradeoffs", "Handling Late-Arriving Data in Kafka", "Idempotency in Data Pipelines"]
    }
}


ALL_SKILLS_LIST = [
    # Technical / Programming
    "Python", "JavaScript", "TypeScript", "SQL", "HTML5", "CSS3", "React", "Node.js", "Next.js",
    "Machine Learning", "Deep Learning", "PyTorch", "TensorFlow", "Pandas", "NumPy",
    "Docker", "Kubernetes", "AWS", "GCP", "Azure", "Linux", "Terraform", "CI/CD", "Git",
    "Tailwind CSS", "PostgreSQL", "MongoDB", "Redis", "GraphQL", "REST APIs",
    "Data Visualization", "Tableau", "Power BI", "Statistics", "A/B Testing", "Spark", "Airflow", "Snowflake", "BigQuery", "Kafka",
    "Cybersecurity", "Network Security", "SIEM (Splunk)", "Wireshark", "Penetration Testing", "OWASP Top 10",
    "Figma", "UI/UX Design", "Wireframing", "Prototyping", "Design Systems", "Usability Testing",
    "Flutter", "Dart", "Swift", "Kotlin", "React Native", "Firebase",
    "Product Management", "Agile & Scrum", "Roadmapping", "Product Analytics", "Market Research",
    # Soft skills
    "Critical Thinking", "Problem Solving", "Communication", "Leadership", "Team Collaboration",
    "Creativity", "Time Management", "Adaptability", "Attention to Detail", "Public Speaking"
]


def match_user_to_careers(
    education: str,
    experience_level: str,
    user_skills: List[str],
    user_interests: List[str],
    preferred_work_style: List[str],
    target_category: str = None
) -> List[Dict[str, Any]]:
    """
    Ranks careers based on user profile compatibility.
    Computes skills match %, missing skills, and holistic compatibility score.
    """
    user_skills_clean = [s.strip().lower() for s in user_skills if s.strip()]
    results = []

    for cid, career in CAREER_DATABASE.items():
        if target_category and target_category.lower() != "all" and career["category"].lower() != target_category.lower():
            continue

        core = [s.lower() for s in career["core_skills"]]
        secondary = [s.lower() for s in career["secondary_skills"]]
        all_required = core + secondary

        # Matching core skills
        matched_core = [s for s in core if any(us in s or s in us for us in user_skills_clean)]
        matched_secondary = [s for s in secondary if any(us in s or s in us for us in user_skills_clean)]
        missing_core = [s for s in core if not any(us in s or s in us for us in user_skills_clean)]

        core_score = (len(matched_core) / max(len(core), 1)) * 60
        secondary_score = (len(matched_secondary) / max(len(secondary), 1)) * 20

        # Interests / work style alignment
        career_styles = [ws.lower() for ws in career.get("work_style", [])]
        user_styles = [ws.lower() for ws in preferred_work_style]
        user_ints = [i.lower() for i in user_interests]

        style_overlap = sum(1 for us in user_styles if any(cs in us or us in cs for cs in career_styles))
        interest_overlap = sum(1 for ui in user_ints if any(kw in career["overview"].lower() or kw in career["category"].lower() for kw in ui.split()))

        alignment_score = min(20, (style_overlap * 5) + (interest_overlap * 5))

        total_score = min(100, int(core_score + secondary_score + alignment_score))

        # Readiness level
        if total_score >= 75:
            readiness = "Ready to Transition / Advanced Match"
        elif total_score >= 50:
            readiness = "Moderate Match (Targeted upskilling needed)"
        elif total_score >= 30:
            readiness = "Foundational Stage (Good prospective path)"
        else:
            readiness = "Exploratory (Requires foundational learning)"

        results.append({
            "id": career["id"],
            "title": career["title"],
            "category": career["category"],
            "overview": career["overview"],
            "score": total_score,
            "readiness": readiness,
            "avg_salary_usd": career["avg_salary_usd"],
            "avg_salary_inr": career["avg_salary_inr"],
            "demand_level": career["demand_level"],
            "matched_skills": [s.title() for s in matched_core + matched_secondary],
            "missing_skills": [s.title() for s in missing_core],
            "top_certifications": career["top_certifications"][:2],
            "roadmap_preview": career["roadmap"][0]["phase"] + " - " + career["roadmap"][0]["focus"]
        })

    # Sort descending by compatibility score
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def analyze_resume_text(resume_text: str, target_career_id: str) -> Dict[str, Any]:
    """
    Evaluates resume content against standard industry keywords for the chosen role.
    """
    career = CAREER_DATABASE.get(target_career_id)
    if not career:
        return {"error": "Career path not found"}

    text_lower = resume_text.lower()
    core = [s.lower() for s in career["core_skills"]]
    secondary = [s.lower() for s in career["secondary_skills"]]

    found_core = [s for s in core if s in text_lower]
    missing_core = [s for s in core if s not in text_lower]
    found_secondary = [s for s in secondary if s in text_lower]
    missing_secondary = [s for s in secondary if s not in text_lower]

    ats_score = int(
        (len(found_core) / max(len(core), 1)) * 70 +
        (len(found_secondary) / max(len(secondary), 1)) * 30
    )

    # Word count and quality checks
    words = resume_text.split()
    length_feedback = "Good length."
    if len(words) < 150:
        length_feedback = "Your resume is brief (under 150 words). Expand on technical projects, quantitative metrics, and toolstacks."
    elif len(words) > 1200:
        length_feedback = "Your resume is somewhat lengthy. Consider condensing to 1-2 focused pages with punchy bullet points."

    # Action verbs check
    action_verbs = ["architected", "developed", "deployed", "implemented", "optimized", "spearheaded", "engineered", "reduced", "increased", "automated"]
    found_verbs = [v for v in action_verbs if v in text_lower]

    recommendations = []
    if missing_core:
        recommendations.append(f"Add key technical skills you might have: {', '.join([s.title() for s in missing_core[:4]])}.")
    if len(found_verbs) < 3:
        recommendations.append("Strengthen bullet points using strong action verbs (e.g., 'Architected', 'Deployed', 'Automated', 'Optimized').")
    if not any(char.isdigit() for char in resume_text):
        recommendations.append("Include measurable impact and metrics (e.g., 'Improved latency by 35%', 'Reduced cloud spend by $12k/mo').")
    recommendations.append("Tailor your summary statement to explicitly mention targeting " + career["title"] + " roles.")

    return {
        "target_role": career["title"],
        "ats_score": ats_score,
        "length_feedback": length_feedback,
        "word_count": len(words),
        "found_keywords": [s.title() for s in (found_core + found_secondary)],
        "missing_critical_keywords": [s.title() for s in missing_core],
        "strong_action_verbs_found": [v.title() for v in found_verbs],
        "actionable_recommendations": recommendations
    }

