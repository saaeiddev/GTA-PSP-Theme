# Compatibility and test report

Target devices: PSP-1000, 2000, 3000, N1000 (Go), E1000 (Street), where firmware supports native PTF themes. This is a target list, not a list of verified devices. Header firmware metadata is 6.20. Device-specific menu items can fall back to system icons. No physical device and no genuine XMB environment were available: installation, visual appearance, PSP Go storage and all firmware versions remain unverified. No simulated image is represented as a screenshot.

Structural checks: PTF Studio encoder and parser built 475048 bytes and decoded 73 images; an independent Python parser validated 74 records (including the reserved record), GIM headers, expected dimensions and indexed palettes, and 480×272 24-bit wallpaper BMP. PNG dimensions, alpha presence and focus transparency were validated separately. SHA-256 db8eeaed4253151959f8553b7ff8fc7261edef447613ed253d73120d9170a238. These checks cannot establish hardware compatibility.
