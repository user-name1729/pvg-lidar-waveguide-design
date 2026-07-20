"""
PVG Waveguide Design

Parametric photonic volume grating (PVG) model for 905 nm LiDAR.
Specialized for uniform conical beam output with ±60° divergence.
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, Dict, Optional


@dataclass
class PVGWaveguide:
    """
    Parametric PVG design for ±60° divergent cone.
    
    This is a LIQUID CRYSTAL POLARIZATION VOLUME GRATING (LC-PVG),
    not a silicon waveguide.
    
    Key difference: Uses spatially varying LC molecular orientation
    to create a diffractive cone that outputs a uniform beam with
    ±60° divergence from a collimated input.
    """
    
    # ========== LC Material Properties ==========
    wavelength: float = 905e-9  # 905 nm LiDAR
    lc_material: str = "E7"  # Nematic LC (Δn ≈ 0.19-0.20)
    
    # Refractive indices at 905 nm for E7 LC
    n_ordinary: float = 1.465  # n_o (perpendicular to director)
    n_extraordinary: float = 1.656  # n_e (parallel to director)
    
    # Derived birefringence
    @property
    def birefringence(self) -> float:
        """Birefringence Δn = n_e - n_o"""
        return self.n_extraordinary - self.n_ordinary
    
    @property
    def n_avg(self) -> float:
        """Average refractive index"""
        return (self.n_ordinary + self.n_extraordinary) / 2
    
    # ========== Grating Period Design ==========
    grating_period_base: float = 380e-9  # 380 nm base period
    
    # For ±60° divergence, need spatially varying period
    # Period variation: Λ(r) = Λ_base * (1 + α*r)
    period_modulation_factor: float = 0.15  # ±15% variation (tunable)
    
    @property
    def grating_period_min(self) -> float:
        """Minimum grating period at edge of aperture"""
        return self.grating_period_base * (1 - self.period_modulation_factor)
    
    @property
    def grating_period_max(self) -> float:
        """Maximum grating period at center"""
        return self.grating_period_base * (1 + self.period_modulation_factor)
    
    # ========== Layer Thickness ==========
    # Critical for achieving high efficiency
    thickness_um: float = 25.0  # 25 μm thick LC layer
    
    @property
    def thickness(self) -> float:
        """Layer thickness in meters"""
        return self.thickness_um * 1e-6
    
    # ========== Molecular Orientation Pattern ==========
    # Controls the diffraction efficiency and beam shaping
    
    base_tilt_angle_deg: float = 35.0  # Base molecular tilt (degrees from normal)
    
    @property
    def base_tilt_angle_rad(self) -> float:
        """Base tilt angle in radians"""
        return np.radians(self.base_tilt_angle_deg)
    
    # Spatial variation of tilt angle
    # For ±60° cone output, need gradient in tilt
    tilt_gradient_deg_per_mm: float = 8.0  # Tilt changes 8°/mm radially
    
    @property
    def tilt_gradient_rad_per_m(self) -> float:
        """Tilt gradient in rad/m"""
        return np.radians(self.tilt_gradient_deg_per_mm) / 1e-3
    
    # ========== Aperture Size ==========
    # Determines practical output divergence angle
    aperture_diameter_mm: float = 8.0  # 8 mm diameter aperture
    
    @property
    def aperture_diameter(self) -> float:
        """Aperture diameter in meters"""
        return self.aperture_diameter_mm * 1e-3
    
    @property
    def aperture_radius(self) -> float:
        """Aperture radius in meters"""
        return self.aperture_diameter / 2
    
    # ========== Duty Cycle ==========
    # Ridge-to-gap ratio in the grating
    duty_cycle: float = 0.45  # 45% ridge, 55% gap
    
    # ========== Input Beam ==========
    input_beam_diameter_mm: float = 5.0  # 5 mm collimated beam
    input_beam_divergence_deg: float = 0.05  # Very collimated (<0.1°)
    
    # ========== Expected Performance ==========
    @property
    def expected_efficiency(self) -> float:
        """Estimate diffraction efficiency"""
        # For uniform cone with spatial modulation:
        # η ≈ sin²(π·Δn·d/λ) × coupling_factor
        
        # Efficiency factor from coupled-wave theory
        phase_modulation = (np.pi * self.birefringence * self.thickness 
                          / self.wavelength)
        max_efficiency = np.sin(phase_modulation)**2
        
        # Reduce for spatial modulation losses (~80%)
        # and uniform cone distribution (~70%)
        coupling_efficiency = max_efficiency * 0.80 * 0.70
        
        return np.clip(coupling_efficiency, 0, 1)
    
    @property
    def expected_fov_degrees(self) -> float:
        """Expected output field of view (full cone angle)"""
        # Approximate FOV from aperture size and grating gradient
        # FOV ≈ 2 * arctan(radius / focal_length_equiv)
        
        # Effective focal length from grating gradient
        focal_length_equiv = self.aperture_radius / np.tan(
            self.tilt_gradient_rad_per_m * self.aperture_radius / 2
        )
        
        fov_rad = 2 * np.arctan(self.aperture_radius / focal_length_equiv)
        fov_deg = np.degrees(fov_rad)
        
        return np.clip(fov_deg, 0, 180)
    
    # ========== Design Validation ==========
    
    def bragg_wavelength_at_tilt(self, tilt_angle_rad: float) -> float:
        """Calculate Bragg wavelength for given molecular tilt angle"""
        # For volume grating: λ_B = 2·Λ·n_eff·sin(θ_tilt)
        lambda_b = (2 * self.grating_period_base * self.n_avg 
                   * np.sin(tilt_angle_rad))
        return lambda_b
    
    def angular_acceptance_bandwidth(self) -> float:
        """
        Calculate angular acceptance bandwidth (FWHM) in degrees.
        Narrower bandwidth = more selective, wider = more forgiving.
        """
        # For volume grating: Δθ ≈ λ / (2π·n_eff·d)
        delta_theta_rad = self.wavelength / (2 * np.pi * self.n_avg * self.thickness)
        delta_theta_deg = np.degrees(delta_theta_rad)
        
        return delta_theta_deg
    
    def phase_matching_condition(self) -> float:
        """
        Check phase matching efficiency.
        Returns phase modulation magnitude (should be ~π/2 for max efficiency).
        """
        phase_mod = (np.pi * self.birefringence * self.thickness 
                    / self.wavelength)
        return phase_mod
    
    def thermal_drift_per_degree(self) -> float:
        """
        Estimate thermal drift in output angle per °C change.
        LC birefringence changes with temperature: dn/dT ≈ -4×10⁻⁴/°C
        """
        # Temperature coefficient of LC
        dn_dT = -4e-4  # 1/°C
        
        # Bragg angle dependence on birefringence
        # sin(θ_B) ∝ Δn, so dθ_B/dΔn ≈ cos(θ_B) / (n_eff·Λ·2)
        
        sin_theta = self.birefringence / (2 * self.n_avg)
        sin_theta = np.clip(sin_theta, -1, 1)
        cos_theta = np.sqrt(1 - sin_theta**2)
        
        dtheta_dn = cos_theta / (self.n_avg * self.grating_period_base * 2)
        dtheta_dT = dtheta_dn * dn_dT
        
        return np.degrees(dtheta_dT)
    
    # ========== Parameter Summary ==========
    
    def get_parameters(self) -> Dict:
        """Return all design parameters as dictionary"""
        return {
            # LC Material
            'lc_material': self.lc_material,
            'n_ordinary': self.n_ordinary,
            'n_extraordinary': self.n_extraordinary,
            'birefringence': self.birefringence,
            'n_avg': self.n_avg,
            
            # Grating
            'wavelength_nm': self.wavelength * 1e9,
            'grating_period_base_nm': self.grating_period_base * 1e9,
            'grating_period_min_nm': self.grating_period_min * 1e9,
            'grating_period_max_nm': self.grating_period_max * 1e9,
            'period_modulation_factor': self.period_modulation_factor,
            'duty_cycle': self.duty_cycle,
            
            # Thickness & Molecular Orientation
            'thickness_um': self.thickness_um,
            'base_tilt_angle_deg': self.base_tilt_angle_deg,
            'tilt_gradient_deg_per_mm': self.tilt_gradient_deg_per_mm,
            'phase_matching_magnitude': self.phase_matching_condition(),
            
            # Aperture & Beam
            'aperture_diameter_mm': self.aperture_diameter_mm,
            'input_beam_diameter_mm': self.input_beam_diameter_mm,
            'input_beam_divergence_deg': self.input_beam_divergence_deg,
            
            # Performance
            'expected_efficiency_pct': self.expected_efficiency * 100,
            'expected_fov_deg': self.expected_fov_degrees,
            'angular_acceptance_deg': self.angular_acceptance_bandwidth(),
            'thermal_drift_deg_per_C': self.thermal_drift_per_degree(),
            
            # Bragg wavelength (at base tilt angle)
            'bragg_wavelength_nm': self.bragg_wavelength_at_tilt(
                self.base_tilt_angle_rad) * 1e9,
        }
    
    def validate_design(self) -> Tuple[bool, str]:
        """
        Validate design against requirements.
        Returns (is_valid, message)
        """
        issues = []
        
        # Check 1: Bragg wavelength should match 905 nm
        bragg_wl = self.bragg_wavelength_at_tilt(self.base_tilt_angle_rad)
        if abs(bragg_wl - self.wavelength) > 50e-9:  # >50 nm drift
            issues.append(
                f"Bragg wavelength {bragg_wl*1e9:.1f} nm deviates from "
                f"target 905 nm (diff: {(bragg_wl-self.wavelength)*1e9:.1f} nm)"
            )
        
        # Check 2: Phase matching for efficiency
        phase_mod = self.phase_matching_condition()
        if phase_mod < np.pi/3 or phase_mod > 2*np.pi:
            issues.append(
                f"Phase modulation {phase_mod:.2f} rad outside optimal range "
                f"[π/3, 2π]. Expected efficiency may be lower."
            )
        
        # Check 3: Expected efficiency >50%
        if self.expected_efficiency < 0.5:
            issues.append(
                f"Expected efficiency {self.expected_efficiency*100:.1f}% "
                f"below 50% target"
            )
        
        # Check 4: Expected FOV covers ±60°
        if self.expected_fov_degrees < 110:  # Full cone < 120° (~±60°)
            issues.append(
                f"Expected FOV {self.expected_fov_degrees:.1f}° below ±60° target"
            )
        
        # Check 5: Thermal stability
        thermal_drift = abs(self.thermal_drift_per_degree())
        if thermal_drift > 0.1:  # >0.1°/°C
            issues.append(
                f"Thermal drift {thermal_drift:.3f}°/°C may require active "
                f"compensation for automotive range (-40 to +80°C)"
            )
        
        if issues:
            return False, "\n".join(["Design issues found:"] + issues)
        else:
            return True, "Design validated successfully ✓"
    
    def __repr__(self) -> str:
        params = self.get_parameters()
        return (
            f"LC-PVG Waveguide Design:\n"
            f"  Material: {params['lc_material']}, Δn={params['birefringence']:.4f}\n"
            f"  Wavelength: {params['wavelength_nm']:.0f} nm\n"
            f"  Grating period: {params['grating_period_base_nm']:.0f} nm "
            f"(range: {params['grating_period_min_nm']:.0f}-{params['grating_period_max_nm']:.0f} nm)\n"
            f"  Thickness: {params['thickness_um']:.1f} μm\n"
            f"  Aperture: {params['aperture_diameter_mm']:.1f} mm\n"
            f"  Efficiency: {params['expected_efficiency_pct']:.1f}%\n"
            f"  FOV: ±{params['expected_fov_deg']/2:.1f}°\n"
            f"  Thermal drift: {params['thermal_drift_deg_per_C']:.4f}°/°C"
        )
