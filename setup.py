"""
setup.py
Maintains application dependencies
Usage:
- python setup.py develop
- python setup.py install (for final production app)
"""
from os import path
from setuptools import setup, find_packages

COMMENT = '#'

def parse_requirements(file_path="requirements.txt"):
    """
    Generate a list of package strings to install from
    a requirements.txt

    path: path to requirements.txt
    """
    requirements = []
    if path.isfile(file_path):
        with open(file_path, 'r') as f:
            lines = f.read().splitlines()
            requirements = [
                line.split(COMMENT)[0].strip() 
                for line in lines if not line.startswith(COMMENT)]
    else:
        print(f"Requirements not found at provided path {path}")
    return requirements

setup(
    name = "lango-tune",
    version = "0.0.1",
    packages = find_packages(where='src'),
    python_requires = ">3.0, <3.8",
    install_requires = parse_requirements(),
    )