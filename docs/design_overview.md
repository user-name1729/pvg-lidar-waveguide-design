# PVG LiDAR Waveguide Design Overview

## Executive Summary

This project develops a comprehensive framework for designing photonic waveguide grating (PVG) optical systems for automotive LiDAR applications. The focus is on a single-channel waveguide with mechanical beam steering at 905 nm wavelength, supporting a wide ±60° horizontal field of view.

## Design Specifications

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Operating Wavelength | 905 nm | Standard automotive LiDAR wavelength |
| Horizontal FOV | ±60° | Wide coverage for autonomous vehicles |
| Vertical FOV | ±15° | Sufficient for road monitoring |
| Beam Steering | Mechanical | Proven, scalable approach |
| Channels | Single | Simplified design, cost-effective |
| Range | 0.1 - 200 m | Typical automotive requirement |
| Coupling Efficiency Target | >50% | Realistic with optimized design |
| Scan Rate | 10-20 Hz | Real-time perception requirement |

## PVG Technology Fundamentals

### What is a Photonic Waveguide Grating?

A PVG is a waveguide with periodic refractive index modulation that:
- Guides light along a narrow channel (confines photons)
- Uses grating structures for mode coupling (in/out of waveguide)
- Provides single-mode propagation with low loss
- Enables precise beam steering through grating design

### Advantages for Automotive LiDAR

1. **Compact**: Submicron feature sizes enable miniaturized systems
2. **Efficient**: High coupling efficiency reduces power consumption
3. **Integrated**: Compatible with silicon photonics manufacturing
4. **Precise**: Wavelength selectivity and beam shaping
5. **Scalable**: Mass production potential with standard CMOS processes

## Design Approach

### Phase 1: Optical Design
- Waveguide geometry optimization (width, thickness, length)
- Grating coupler design (period, duty cycle, profile)
- Mode analysis and effective index calculations
- Coupling efficiency prediction

### Phase 2: Ray-Tracing Validation
- Geometric optics simulation of light propagation
- Beam quality analysis across FOV
- Aberration identification
- Performance verification

### Phase 3: System Integration
- Mechanical scanner coupling
- Thermal effects and compensation
- Manufacturing tolerance analysis
- Cost and scalability assessment

## Key Technical Challenges

1. **Wide FOV Challenge**: ±60° horizontal FOV requires careful grating design to maintain efficiency across wide angle range

2. **Mode Control**: Single-mode operation ensures consistent beam quality and polarization

3. **Coupling Efficiency**: Maximizing grating coupler efficiency while maintaining spectral bandwidth

4. **Aberration Correction**: Managing field curvature, distortion, and coma across wide FOV

5. **Thermal Stability**: Waveguide effective index varies with temperature (~10^-4/K), affecting beam steering

## References

1. Chrostowski & Hochberg (2015) - Silicon Photonics Design
2. Bogaerts et al. (2012) - Silicon Microring Resonators
3. Automotive LiDAR standards (ISO 26262, etc.)

---

**Next Steps**: See implementation notebooks in `notebooks/` directory.
