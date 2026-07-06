# Python Web Application Series: Module 01

An actively developed Python web application establishing a foundational framework for modular template-driven layouts, core routing, and modern package management. This project serves as Phase 1 of an ongoing full-stack software development sequence.

## 🚀 Key Features (In Active Development)
* **Template Architecture**: Modular HTML architecture featuring clean template inheritance (`base.html`).
* **Identity Flows**: Pre-configured frontend portals for dedicated `Login` and `Signup` user states.
* **Modern Package Management**: Explicit environment builds utilizing `uv` and standard declarative metadata (`pyproject.toml`).

## 🛠️ Tech Stack & Architecture
* **Backend Runtime**: Python 3.14+
* **Environment Tooling**: `uv` (Fast Python package installer and resolver)
* **Frontend Interface**: Semantic HTML5, Custom CSS3 variables

## 🗺️ Project Roadmap
- [x] Configure repository baseline and strict production `.gitignore`
- [x] Design layout wireframes (`Home`, `About`, `Contact`, `Login`, `Signup`)
- [ ] Connect core app execution handlers inside `app.py`
- [ ] Implement local or database user storage models
- [ ] Deploy initial prototype live to production hosting (e.g., Render/Railway)

## 📦 Local Workspace Replication

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd python-webapp-01
   ```

2. **Initialize workspace & sync lockfile dependencies:**
   ```bash
   uv sync
   ```

3. **Execute local development server:**
   ```bash
   uv run app.py
   ```
