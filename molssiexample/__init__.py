"""
MolSSIExample
An example of MolSSI CookieCutter.
"""

# Add imports here
from .molssiexample import *
from . import math

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
