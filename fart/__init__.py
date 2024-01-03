"""fart - Figlet ART for documentation"""
import os
import sys

__version__ = '0.2.0'
__author__ = 'Evan Cushing <evdcush@protonmail.com>'

#=== Pathing hack
project_path = os.path.abspath(os.path.dirname(__file__))
if project_path not in sys.path:
    sys.path.append(project_path)
