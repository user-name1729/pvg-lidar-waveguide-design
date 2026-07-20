# Complete Optical Path: From 905 nm Laser to ±60° Output Beam

## System Architecture Overview

Your LC-PVG LiDAR system has a specific architecture combining:
- **360° mechanical scanning** (primary beam steering)
- **±60° LC-PVG beam shaping** (secondary optics)
- **Single-channel collection** (return signal path)

Here's the complete light path:

---

## TRANSMIT PATH: Laser → PVG → Scanner → Free Space

```
┌─────────────────────────────────────────────────────────────────┐
│                    TRANSMIT OPTICAL PATH                         │
└─────────────────────────────────────────────────────────────────┘

[1] 905 nm Pulsed Laser Diode (LD)
    |
    | ~5 mW average, ~10-100 ns pulses
    | Wavelength: 904-906 nm (narrow linewidth)
    | Beam: ~0.5 mm diameter, ~5-10° divergence
    |
    ↓
[2] Lens L1: Collimation (f = 5 mm)
    |
    | Converts divergent LD output → Collimated beam
    | Output: 5 mm diameter, <0.1° divergence
    | Power after optics: ~4.5 mW (90% transmission)
    |
    ↓
[3] Optional: Dichroic Beamsplitter (PBS)
    |
    | Separates transmit (TX) from receive (RX) paths
    | TX: 905 nm → toward PVG
    | RX: From free space → toward receiver
    |
    ↓
╔═════════════════════════════════════════════════════════════════╗
║  [4] **LC-PVG OPTICAL ELEMENT** (YOUR FABRICATED COMPONENT)   ║
║                                                                  ║
║  INPUT:  Collimated 905 nm beam (5 mm diameter, <0.1°)        ║
║                                                                  ║
║  FUNCTION: Transform narrow beam into ±60° divergent cone      ║
║                                                                  ║
║  MECHANISM:                                                      ║
║  • Spatially varying LC molecular tilt (8°/mm gradient)        ║
║  • Bragg diffraction at different angles across aperture       ║
║  • Encodes tilt pattern: θ(r) = 35° + 8°/mm × r              ║
║  • Near center: θ = 35° → small diffraction angle             ║
║  • At edge (r=4mm): θ = 67° → large diffraction angle (±60°)  ║
║                                                                  ║
║  OUTPUT: Divergent cone (±60° full angle, 120° total)         ║
║  • Uniform intensity distribution across cone                  ║
║  • Efficiency: 50% (meets target)                              ║
║  • Power after PVG: ~2.25 mW (90% of input × 50% coupling)   ║
║                                                                  ║
║  PHYSICAL PARAMETERS:                                           ║
║  • Material: E7 Nematic LC (Δn = 0.191 @ 905 nm)              ║
║  • Thickness: 25 μm                                             ║
║  • Grating period: 380 nm (varying ±15%)                       ║
║  • Duty cycle: 45% ridge, 55% gap                              ║
║  • Aperture: 8 mm diameter                                      ║
║  • Bragg wavelength: 905 nm (exact match)                       ║
║                                                                  ║
╚═════════════════════════════════════════════════════════════════╝
    |
    | ±60° divergent cone beam
    |
    ↓
[5] Mechanical Scanner (Rotating Mirror or Polygon)
    |
    | Type: Galvanometer mirror or MEMS polygon
    | Scan range: 360° (full rotation)
    | Scan rate: 10-20 Hz
    |
    | FUNCTION: Rotate the ±60° cone across full 360° azimuth
    |
    | INPUT: ±60° divergent cone from PVG
    | OUTPUT: Scanned beam sweeping through full hemisphere
    |
    ↓
[6] Collimating Lens L2 (Optional, for near-field)
    |
    | NOT NEEDED if using PVG cone directly
    | Only needed if you want to recollimate for specific range
    |
    ↓
[7] Optical Window/Dome (LIDAR Housing)
    |
    | Protects optics from environmental contamination
    | Minimal optical distortion (low power loss)
    |
    ↓
[8] FREE SPACE
    |
    | Output beam:
    | • Horizontal coverage: 360° (via scanner rotation)
    | • Vertical coverage: ±60° (via PVG cone)
    | • Total FOV: 360° × ±60° (hemisphere)
    | • Power: ~2 mW average
    | • Range: 0.1-200 m (depending on receiver sensitivity)
    |
    ↓
[Target/Scene]
    |
    Laser light reflects from objects in scene
    |
    ↓
```

---

## RETURN PATH: Reflected Light → Receiver

```
┌─────────────────────────────────────────────────────────────────┐
│                     RETURN (RX) OPTICAL PATH                    │
└─────────────────────────────────────────────────────────────────┘

[Scene/Target]
    |
    Reflected light from scene
    | Return signal: ~nW to μW (extremely weak!)
    | Spread over wider solid angle
    |
    ↓
[7] Optical Window/Dome
    |
    Return light enters LIDAR housing
    |
    ↓
[6] Collection Optics (Telescope/Lens)
    |
    TYPE: Often the same scanner optics in reverse
    (or dedicated receiver optics)
    |
    FUNCTION: Collect return light and focus onto detector
    |
    Typical f/# : f/1.5 to f/4 (for good collection)
    |
    ↓
[5] Mechanical Scanner (Same mirror in reverse)
    |
    For single-channel systems, the SAME scanner that
    transmitted the beam also helps collect returns
    |
    This is called "monostatic" configuration
    |
    ↓
[3] Dichroic Beamsplitter (RX path)
    |
    Separates 905 nm return signal from 905 nm TX
    (This is tricky! Same wavelength!)
    |
    SOLUTIONS:
    A) Time-gated detection: Only measure after pulse ends
    B) Spatial separation: TX and RX paths slightly offset
    C) Polarization separation: TX/RX at different polarizations
    |
    ↓
[9] Bandpass Filter (905 nm ± few nm)
    |
    Rejects background light, thermal noise
    Passes only 905 nm return signal
    |
    ↓
[10] Avalanche Photodiode (APD) or PIN Photodiode
    |
    Detects individual photons (in geiger mode) or
    Measures return power (linear mode)
    |
    Output: Electrical signal (current pulse)
    |
    ↓
[11] Signal Processing Electronics
    |
    • Time-to-digital converter (TDC)
    • Measures round-trip time: Δt = 2 × Range / c
    • Computes distance: Range = c × Δt / 2
    |
    ↓
[12] Point Cloud Data
    |
    (x, y, z, intensity) for each scanned point
    Complete 3D map of scene

```

---

## THE PVG'S SPECIFIC ROLE IN THE SYSTEM

### **What the PVG Does**

```
INPUT BEAM              PVG TRANSFORMATION           OUTPUT BEAM

Collimated              Spatially varying LC         Divergent cone
5 mm diameter           tilt angle                   ±60° FOV
<0.1° divergence        (8°/mm gradient)             Uniform intensity
~4.5 mW                                              ~2.25 mW (50% efficient)

        Single narrow ray                Multiple rays at different angles
              |                                  /  /  /  |  \  \  \
              |                                /  /  /   |   \  \  \
              |        [LC-PVG]            -60° -40° -20° 0° +20° +40° +60°
        ────────────────────────────────────────────────
              ↓              ↓                   ↓
        Collimated       Diffracting         Diverging
        input            element             output
```

### **How PVG Creates ±60° Divergence**

The LC-PVG is fundamentally a **spatially varying optical element**:

**Near the center of the 8 mm aperture:**
- Molecular tilt angle: θ = 35°
- Bragg diffraction angle: ~0° (small angle)
- Light travels mostly straight through

**Moving radially outward:**
- Molecular tilt angle gradually increases
- θ(r) = 35° + 8°/mm × r
- Diffraction angle increases correspondingly

**At the edge (r = 4 mm):**
- Molecular tilt angle: θ = 67°
- Bragg diffraction angle: ~60°
- Light is deflected at maximum angle

**Result:** Continuous gradient of deflection angles
- Creates smooth divergent cone
- Uniform intensity (with proper design optimization)
- Total cone angle: ±60° (120° full angle)

---

## OPTICAL SYSTEM SCHEMATIC

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                   TRANSMIT CHAIN                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

   905 nm LD
    (5mW)
      │
      └─→ [Collimator L1] ─→ [PBS Dichroic] ─→ [LC-PVG]
                                                    │
                                    (±60° divergent cone, 2.25 mW)
                                                    │
         ┌──────────────────────────────────────────┘
         │
         ↓
    [Rotating Mirror Scanner]
      (360° rotation)
         │
    (Scanned ±60° cone, covers full hemisphere)
         │
         ↓
    [Optical Window/Dome]
         │
         ↓
    FREE SPACE (0.1-200 m range)
         │
         └─→ [Scene/Targets]
             (Reflects light)
             │
             ↓

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                   RECEIVE CHAIN                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

    FREE SPACE (return signal nW-μW)
         │
         ↓
    [Optical Window/Dome]
         │
         ↓
    [Collection Optics]
    (telescope or same scanner optics)
         │
         ↓
    [Rotating Mirror Scanner] ←─ (synchronized with TX)
         │
         ↓
    [PBS Dichroic] ←─ (separates TX/RX same wavelength)
         │
         ↓
    [905 nm Bandpass Filter]
    (rejects background, noise)
         │
         ↓
    [APD/PIN Photodiode]
    (detects single photons or return power)
         │
         ↓
    [Signal Processing]
    (time-to-digital converter)
         │
         ↓
    [3D Point Cloud Output]
```

---

## THE PVG IN CONTEXT: System Beam Path

### **Key Performance Metrics**

| Stage | Beam Property | Value |
|-------|---|---|
| **Input (905 nm LD)** | Power | 5 mW avg |
| | Diameter | 0.5 mm |
| | Divergence | 5-10° |
| **After Collimator L1** | Power | 4.5 mW (90% efficiency) |
| | Diameter | 5 mm |
| | Divergence | <0.1° |
| **After LC-PVG** | Power | 2.25 mW (50% efficiency) |
| | Beam type | Divergent cone |
| | FOV | ±60° (120° total) |
| | Uniformity | ±5% intensity variation |
| **After Scanner (rotated)** | Power | ~2 mW (10% loss in optics) |
| | Scan coverage | 360° × ±60° |
| | Scan rate | 10-20 Hz |
| | Beam quality | Limited by PVG aberrations |
| **At target (100 m range)** | Spot size | ~10-20 m diameter (rough) |
| | Irradiance | ~1-10 W/m² (depends on range) |
| **Return signal (100 m)** | Signal strength | ~nW to 10 μW |
| | Collection efficiency | ~5-20% (depends on aperture) |

---

## WAVEGUIDE vs FREE-SPACE CONFUSION

**Important clarification:**

Your system is NOT a "waveguide" in the traditional fiber-optic sense. Rather, it's:

1. **Fiber input** → Collimator (converts diverging fiber mode to collimated beam)
2. **LC-PVG element** → Diffractive optics (converts collimated → divergent)
3. **Free-space propagation** → Mechanical scanner rotates the cone
4. **Return collection** → Reverse path (optional telescope collects returns)

**The LC-PVG is NOT a "waveguide" that contains light.** Instead:
- It's a **diffractive optical element** that *transforms* a beam
- The light is free-space propagating after the PVG
- It acts as a spatial light modulator (SLM)

---

## CRITICAL SYSTEM DESIGN CONSIDERATIONS

### **1. Spatial Overlap of TX and RX**

Since you're using the same scanner for both transmission and reception:
- The ±60° TX beam sweeps across the scene
- The returned light enters the dome
- Must align receiver aperture with TX beam footprint
- Typical overlap: 90-95%

### **2. TX/RX Isolation at 905 nm**

Challenge: Both TX and RX use exactly 905 nm wavelength

Solutions:
- **Time-gated detection**: Only measure after TX pulse ends
- **Polarization filtering**: TX = linear H, RX = linear V (need isolation optics)
- **Wavelength filtering**: Use narrowband filter ±1-2 nm around 905 nm
- **Spatial separation**: Slight offset between TX exit and RX aperture

Most common: **Time-gated approach**
- TX pulse: 10-100 ns
- Wait 100 ns for light to travel forward
- RX window: 400 ns (for 100 m range, 2-way trip = 667 ns)
- Works well because return is spread over larger solid angle

### **3. Beam Divergence Impact on Range**

Your ±60° cone diverges **rapidly**:
- At 1 m: Spot size ~2 m diameter (very large!)
- At 10 m: Spot size ~20 m diameter
- At 100 m: Spot size ~200 m diameter

**This is actually GOOD for automotive LiDAR** because:
- ✓ Covers large area per scan
- ✓ Multiple targets illuminated simultaneously
- ✓ Robust to vibration/jitter (large beam tolerates small pointing errors)

**Trade-off:**
- Power density drops rapidly: ~1/r² law
- Longer range requires higher TX power OR higher receiver sensitivity

### **4. Thermal Compensation**

Your LC-PVG has thermal drift: ~-0.004°/°C

Over automotive range (-40 to +80°C = 120°C):
- Total drift: ~-0.48°
- Effect on ±60° cone: Negligible (<1% of cone size)
- But affects fine-pointing accuracy

**Solution options:**
- Active thermal control (hold substrate at constant temp, ±1°C)
- Wavelength tuning (shift laser wavelength slightly to compensate)
- Accept drift as system tolerance (if <1° acceptable)

---

## COMPLETE OPTICAL PATH SUMMARY

**Transmit:**
```
905 nm LD → Collimator → PBS → LC-PVG → Scanner → Free Space
5 mW       90% eff     —     50% eff   95% eff   2 mW output
```

**Return:**
```
Free Space → Collection Optics → Scanner → PBS → Filter → APD
Return signal   50-80% eff     —      —     95%   ~1% eff
                                                  (single photon detect)
```

**Total System Efficiency:**
- TX path: 5 mW → 2 mW free space (40%)
- RX path: ~nW incident → ~pW detected (depends on range/target)
- Dominant loss: TX power (90% → 50% in PVG)

**To increase efficiency:**
- Improve PVG design (target 60%+ instead of 50%)
- Use higher power laser (10-20 mW)
- Optimize collection optics (larger aperture)

---

## WHAT THIS MEANS FOR YOUR DESIGN

### **PVG is the KEY optical element that:**

1. ✓ **Transforms input beam**: Collimated → Divergent cone
2. ✓ **Defines output FOV**: ±60° coverage (your specification)
3. ✓ **Controls beam uniformity**: Should be ±5% across cone
4. ✓ **Sets efficiency target**: 50% is primary loss mechanism
5. ✓ **Enables passive beam shaping**: No moving parts in PVG itself

### **Everything else (scanner, collimator, etc.) is standard optics**

The **LC-PVG is your research contribution** — it's the novel element that enables this unique optical architecture.

---

**Does this clarify the complete system architecture and the PVG's role?**

Would you like me to elaborate on:
1. **RX path optimization** (collecting return signals efficiently)?
2. **Mechanical scanner integration** with the PVG output?
3. **Signal processing** (how to convert time-of-flight to 3D coordinates)?
4. **Performance simulations** across the complete optical path?
5. **Trade-off analysis** (efficiency vs FOV vs range)?
