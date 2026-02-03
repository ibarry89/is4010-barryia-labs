"""
pytest configuration file

This file configures pytest to properly discover and import modules from
week folders. It adds each week directory to sys.path so that imports like
'from lab03 import ...' work correctly when running pytest from the repo root.
"""

import sys
from pathlib import Path

# Get the repository root directory
repo_root = Path(__file__).parent

# Add all week directories to Python path
for i in range(0, 15):  # weeks 0-14
    week_dir = repo_root / f"week{i:02d}"
    if week_dir.exists():
        sys.path.insert(0, str(week_dir))
