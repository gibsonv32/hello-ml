# Reproducible AI Workflow — Generic Project Template

This README is a **starter playbook** for any new AI/ML project on macOS using **Conda, VS Code, Git/GitHub, Jupyter**, and optional **Kaggle/Colab**. Copy this whole file into new repos and replace placeholders like `MYPROJECT`, `proj311`, and `your_file.csv`.

---

## 0) Goal
Create a clean, repeatable workflow you can reuse:
- Consistent Python environment (Conda)
- Standard project layout (code / tests / notebooks / data)
- Quick health checks (pytest)
- Version control (Git + GitHub)
- EDA notebook tied to local data
- Optional: Kaggle dataset pull, Colab GPU

---

## 1) One-time machine prep (skip if already done)
**Where:** macOS Terminal
```bash
# Make Conda available in every shell
source /opt/anaconda3/etc/profile.d/conda.sh
conda init zsh
exec zsh
```
VS Code extensions (recommended): Python, Pylance, Jupyter, GitHub PRs & Issues.

---

## 2) New project: environment
**Where:** Terminal
```bash
# name it for this project (edit both names)
conda create -n proj311 -y python=3.11
conda activate proj311

# core libs
conda install -y numpy pandas scikit-learn matplotlib pytest jupyter
# optional
# conda install -y seaborn ipywidgets
```

**Why:** each project gets its own sandbox so versions dont clash.

---

## 3) New project: scaffold folders
**Where:** Terminal
```bash
export PROJ=MYPROJECT
mkdir -p ~/ai-projects/$PROJ/{src,tests,notebooks,data/raw,data/interim}
cd ~/ai-projects/$PROJ

# README quickstart
cat > README.md <<'EOF'
# MYPROJECT
Short description here.

## Quick start
source /opt/anaconda3/etc/profile.d/conda.sh
conda activate proj311
python -m pytest -q
