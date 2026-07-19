"""
Optical Engine Module

Core ray-tracing simulation engine for photonic waveguide grating (PVG) optical systems.
"""

__version__ = "0.1.0"
__author__ = "PVG LiDAR Research Team"

from .ray import Ray, RayBundle
from .tracer import RayTracer
from .optics import OpticalElement, Lens, Mirror, GratingCoupler
from .materials import Material, MATERIALS_905NM

__all__ = [
    "Ray",
    "RayBundle",
    "RayTracer",
    "OpticalElement",
    "Lens",
    "Mirror",
    "GratingCoupler",
    "Material",
    "MATERIALS_905NM",
]
