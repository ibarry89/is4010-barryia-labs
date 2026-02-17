"""
pytest configuration for week03

This conftest.py ensures lab03 module can be imported from the current directory.
"""

import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))
