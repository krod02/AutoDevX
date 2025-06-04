# 🤖 AutoDevX — Autonomous AI Developer Agent

AutoDevX is a cutting-edge multi-agent AI system that automates the software development lifecycle. Given a user story, AutoDevX plans tasks, writes production-ready code, generates test cases, performs code review and refactoring, and outputs commit-ready suggestions — without human intervention.

This project demonstrates real-world applications of LLMs, multi-agent orchestration, and autonomous workflows. It’s built to showcase what modern AI agents can do when trained and deployed properly — and to push the boundary of developer productivity.

---

## 🚀 Core Capabilities

- 🧠 **PlannerAgent** — Breaks user stories into actionable technical tasks
- 💻 **CoderAgent** — Writes code using a fine-tuned LLM on GitHub commits
- 🧪 **TesterAgent** — Auto-generates test cases using coverage-aware prompts
- 👨‍⚖️ **ReviewerAgent** — Reviews and refactors generated code
- ✅ **CommitAgent** *(optional)* — Outputs Git-style commit messages

---

## 🛠 Tech Stack

| Area           | Tools/Tech                          |
|----------------|-------------------------------------|
| Language       | Python                              |
| Core Models    | Fine-tuned LLMs (CodeGen, StarCoder, Mistral) |
| ML Frameworks  | PyTorch, Transformers, HuggingFace  |
| Orchestration  | FastAPI, LangGraph (multi-agent)    |
| UI Layer       | Streamlit or VSCode Extension (TBD) |
| DevOps         | Docker, GitHub Actions              |
| Dataset Sources| GitHub Issues, Commits, PRs         |

---

## 📁 Project Structure

```bash
autodevx/
├── agents/         # Planner, Coder, Reviewer, Tester logic
├── backend/        # FastAPI agent orchestrator
├── data/           # GitHub issues, commits, and PR datasets
├── docs/           # Architecture, training details, and prompt guides
├── frontend/       # Optional UI (Streamlit app or VSCode extension)
├── models/         # Fine-tuning scripts and checkpoints
├── notebooks/      # Model training + evaluation experiments
├── prompts/        # Prompt templates and formatting logic
├── utils/          # Helper functions (e.g., tokenization, AST)
├── docker/         # Containerization setup
├── README.md       # This file
├── requirements.txt
└── .gitignore
