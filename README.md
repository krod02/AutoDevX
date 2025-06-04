# 🤖 AutoDevX – Autonomous AI Developer Agent

AutoDevX is an intelligent, multi-agent AI system that automates the software development lifecycle. Given a user story, it plans tasks, writes code, tests it, reviews/refactors the output, and generates commit-ready results — all autonomously.

---

## 🚀 Core Features

- 🔍 **PlannerAgent** – Breaks down user stories into dev tasks
- 💻 **CoderAgent** – Writes code for each task using a custom-trained LLM
- 🧪 **TesterAgent** – Auto-generates test cases
- 👨‍⚖️ **ReviewerAgent** – Reviews, refactors, and rates code quality
- ✅ **CommitAgent** *(optional)* – Suggests commits & PR summaries

---

## 🛠 Tech Stack

- Python · PyTorch · FastAPI · Hugging Face Transformers  
- LangGraph / LangChain · GitHub API · Docker  
- Custom-trained Code LLMs + RLHF pipelines

---

## 📁 Project Structure

```bash
autodevx/
├── agents/         # Autonomous code agents (planner, coder, etc.)
├── data/           # Training datasets (GitHub issues, PRs, etc.)
├── models/         # Fine-tuned model code & weights
├── backend/        # FastAPI orchestration service
├── frontend/       # Optional UI (Streamlit or VSCode extension)
├── notebooks/      # EDA & training evaluation
├── prompts/        # Prompt templates for each task
├── utils/          # Helper functions (tokenizer, AST parsers)
