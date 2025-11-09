# FileTypeConverter

A Python-based tool for converting PDF files to DOCX format.

## Virtual Environment Setup

This project uses a Python virtual environment to manage dependencies. Here's why this is important:

1. **Project Isolation**
   - Each project has its own dependencies without conflicts
   - Different versions of packages can be used for different projects
   - Prevents "dependency hell" where packages conflict

2. **Reproducibility**
   - The `requirements.txt` file lists exact versions of packages
   - Other developers can recreate the exact same environment
   - Makes deployment more reliable

3. **Clean Development**
   - Keeps your global Python installation clean
   - Complete isolation from system packages
   - Prevents accidental use of globally installed packages

## Setup Instructions

1. Clone the repository
```bash
git clone [your-repo-url]
cd FileTypeConverter
```

2. Create virtual environment
```bash
python -m venv .venv
```

3. Activate virtual environment

Windows:
```powershell
.\.venv\Scripts\activate
```

Unix/MacOS:
```bash
source .venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

## Project Structure

- `.venv/`: Virtual environment folder (not included in git)
- `requirements.txt`: List of Python dependencies
- `pdftodocx.py`: Main conversion script

## Development Notes

- Python version: 3.11.5
- Virtual environment configuration is in `.venv/pyvenv.cfg`
- Dependencies are isolated from system Python packages