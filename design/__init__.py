"""
Design Module

PVG waveguide parametric design and geometry models.
"""

__version__ = "0.1.0"

from .waveguide import PVGWaveguide
from .grating import GratingDesign
from .scanner import MechanicalScanner

__all__ = [
    "PVGWaveguide",
    "GratingDesign",
    "MechanicalScanner",
]
