# PVG LiDAR Waveguide Design Log

Research progress, design decisions, and findings documented chronologically.

## 2026-07-19: Project Initialization

### Objectives Established
- Design PVG optical waveguide for automotive LiDAR
- Single-channel configuration at 905 nm
- Mechanical beam steering with ±60° horizontal FOV
- Production-oriented framework
- Ray-tracing simulation capability

### Initial Design Specifications
- **Horizontal FOV**: ±60° (wide coverage)
- **Vertical FOV**: ±15° (road monitoring)
- **Wavelength**: 905 nm (LiDAR standard)
- **Coupling Efficiency Target**: >50%
- **Scan Rate**: 10-20 Hz
- **Range**: 0.1-200 m

### Key Technical Challenges Identified
1. Wide FOV requires grating design optimization
2. Single-mode operation for beam quality
3. Coupling efficiency across full FOV
4. Aberration management
5. Thermal stability and compensation

### Framework Design
- Ray-Tracing Engine: Custom vectorized NumPy implementation
- Design Modules: Waveguide, grating coupler, mechanical scanner
- Analysis Tools: Performance metrics, optimization

---

**Last Updated**: 2026-07-19
