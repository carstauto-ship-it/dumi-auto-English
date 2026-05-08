#!/usr/bin/env python3
"""Generate 15 new SEO-optimized product pages for dumi-auto.com - 2026-05-08"""
import os

BASE_DIR = "/Users/carstauto/.openclaw/workspace/dumi-auto-website/products"

NEW_PRODUCTS = [
    {
        "filename": "nano-ceramic-glass-coating.html",
        "name": "NANO CERAMIC GLASS COATING",
        "subtitle": "纳米陶瓷玻璃镀晶 | 前挡风玻璃专用 | 疏水防污 | 提升视野",
        "tag": "🪟 玻璃镀晶",
        "title": "NANO CERAMIC Glass Coating - DUMI AUTO | Hydrophobic Windshield Ceramic Coating",
        "description": "DUMI NANO CERAMIC GLASS COATING is a professional-grade 9H hardness coating specifically formulated for automotive glass surfaces. Creates an extremely hydrophobic layer that causes rain to bead and sheet off at speeds as low as 30mph, dramatically improving visibility and safety during wet weather driving.",
        "keywords": "nano ceramic glass coating, windshield ceramic coating, hydrophobic glass coating, car glass coating, rain repellent coating, 9H glass coating, dumi glass coating, automotive glass protection",
        "alt_visual": "DUMI NANO CERAMIC GLASS COATING applied on car windshield showing water beading and sheet-off effect in rain",
        "gradient": "linear-gradient(135deg,#0a2a4a,#1a5a8a,#0a3a6a)",
        "placeholder": "🪟 GLASS COATING",
        "tag_color": "#1a5a8a",
        "features": [
            ("9H Hardness on Glass", "Professional-grade ceramic hardness bonds permanently to glass surface"),
            ("Extreme Hydrophobic Effect", "Water beads and sheets off at low speeds — no need for wipers in light rain"),
            ("Ice & Frost Resistance", "Ice and frost adhere poorly to the ceramic surface, easy removal"),
            ("Bug & Bird Dropping Repellent", "Organic matter slides off easily without etching the glass"),
        ],
        "applications": ["Windshield Protection", "Side Windows", "Mirrors", "Glass Headlights"],
        "related": ["automotive-glass-coating.html", "ceramic-pro-coating.html", "headlight-ceramic-coating.html"],
        "h1": "NANO CERAMIC GLASS COATING™",
        "h2_intro": "Professional Hydrophobic Glass Protection — See Clearly in Any Weather",
    },
    {
        "filename": "premium-edge-guard-ppf.html",
        "name": "PREMIUM EDGE GUARD PPF",
        "subtitle": "PPF边缘防护条 | 抗剥离 | 保护膜边缘 | 专业安装",
        "tag": "🛡️ 边缘防护",
        "title": "PREMIUM EDGE GUARD PPF - DUMI AUTO | Professional Edge Protection Strip for PPF Installation",
        "description": "DUMI PREMIUM EDGE GUARD is a specialized edge-sealing tape designed to prevent PPF edge lifting and peeling. Used by professional installers worldwide to ensure long-term PPF adhesion at edges — the most common failure point. Essential for hoods, bumpers, and fender edges.",
        "keywords": "ppf edge guard, edge sealing tape, ppf edge protection, paint protection film edge, edge lifting prevention, ppf installation supplies, dumi edge guard, automotive edge tape",
        "alt_visual": "DUMI PREMIUM EDGE GUARD PPF tape being applied to hood edge showing professional edge sealing technique",
        "gradient": "linear-gradient(135deg,#1a2a1a,#2d4a2d,#1a3a1a)",
        "placeholder": "🛡️ EDGE GUARD",
        "tag_color": "#1a3a1a",
        "features": [
            ("Prevents Edge Lifting", "Specially formulated adhesive bonds permanently at PPF edges"),
            ("Virtually Invisible", "Crystal-clear tape blends seamlessly with any PPF color"),
            ("Professional Grade", "Used by certified PPF installers worldwide"),
            ("Works on All PPF Types", "Compatible with matte, gloss, and satin PPF finishes"),
        ],
        "applications": ["Hood Edges", "Bumper Edges", "Fender Flares", "Door Handle Cavities"],
        "related": ["ultimate-plus.html", "stealth-pro-ppf.html", "armor-ppf.html"],
        "h1": "PREMIUM EDGE GUARD™",
        "h2_intro": "Stop PPF Edge Lifting Before It Starts — Professional Edge Sealing",
    },
    {
        "filename": "solar-heat-reject-ceramic-tint.html",
        "name": "SOLAR HEAT REJECT CERAMIC",
        "subtitle": "太阳热量阻隔陶瓷窗膜 | 降温15°C | 节能空调 | 红外阻隔",
        "tag": "☀️ 太阳隔热",
        "title": "SOLAR HEAT REJECT CERAMIC Tint - DUMI AUTO | Maximum Solar Heat Blocking Window Film",
        "description": "DUMI SOLAR HEAT REJECT CERAMIC is engineered for maximum solar heat rejection — blocking up to 97% of infrared radiation and reducing interior cabin temperatures by up to 15°C. The ultimate comfort window film for vehicles parked in direct sunlight or driven in hot climates.",
        "keywords": "solar heat reject tint, heat blocking window film, ceramic heat rejection, car window film hot climate, sun heat protection, infrared blocking film, dumi solar heat reject, automotive thermal barrier",
        "alt_visual": "DUMI SOLAR HEAT REJECT CERAMIC window film installed on car showing dramatic heat reduction in hot climate",
        "gradient": "linear-gradient(135deg,#4a2a1a,#7a4a2a,#5a3a1a)",
        "placeholder": "☀️ SOLAR HEAT REJECT",
        "tag_color": "#7a4a2a",
        "features": [
            ("97% IR Heat Rejection", "Blocks nearly all infrared radiation that heats car interiors"),
            ("15°C Interior Temperature Reduction", "Measured difference in cabin temperature vs unprotected glass"),
            ("Reduces AC Load", "Less heat means your air conditioning works less, improving fuel economy"),
            ("Non-Metal Formula", "100% ceramic particles — no corrosion risk and full signal compatibility"),
        ],
        "applications": ["Hot Climate Vehicles", "Parked in Sun", "Convertibles", "Electric Vehicles"],
        "related": ["ceramic-matrix-tint.html", "nano-ceramic-tint.html", "diamond-glass-tint.html"],
        "h1": "SOLAR HEAT REJECT CERAMIC™",
        "h2_intro": "Block the Heat, Not the View — Maximum Solar Heat Rejection Technology",
    },
    {
        "filename": "stealth-chrome-delete-ppf.html",
        "name": "STEALTH CHROME DELETE",
        "subtitle": "哑光黑化改装膜 | 亮黑/哑光黑 | 镀铬件黑化 | 改装必备",
        "tag": "🎨 黑化改装",
        "title": "STEALTH CHROME DELETE PPF - DUMI AUTO | Matte Black Chrome Delete Film for Automotive Trim",
        "description": "DUMI STEALTH CHROME DELETE is a specialized wrap film designed to transform chrome vehicle trim into a sleek black finish. Available in both high-gloss black and true satin matte black. The easiest and most reversible way to achieve the popular chrome-delete look without permanent modification.",
        "keywords": "chrome delete film, chrome delete ppf, black out chrome trim, matte black trim film, gloss black chrome delete, automotive blackening film, dumi chrome delete, car trim black wrap",
        "alt_visual": "DUMI STEALTH CHROME DELETE film applied on chrome door handles and window trim showing sleek black finish",
        "gradient": "linear-gradient(135deg,#0d0d0d,#1a1a1a,#0d0d0d)",
        "placeholder": "🎨 CHROME DELETE",
        "tag_color": "#1a1a1a",
        "features": [
            ("Gloss & Matte Options", "Choose high-gloss black or true satin matte to match your style"),
            ("Removable & Repositionable", "Air-release adhesive allows repositioning during installation"),
            ("Protects Chrome Underneath", "Unlike paint, this film protects the original chrome finish"),
            ("Stretch-Friendly", "Conforms to curved trim pieces without lifting or wrinkling"),
        ],
        "applications": ["Door Handles", "Window Trim", "Mirror Caps", "Badge Surrounds", "Bumper Trim"],
        "related": ["stealth-pro-ppf.html", "vinyl-wrap-premium-roll.html", "exterior-matte-film.html"],
        "h1": "STEALTH CHROME DELETE™",
        "h2_intro": "Transform Chrome to Black in Hours — The Chrome Delete Solution",
    },
    {
        "filename": "self-healing-paint-restoration-film.html",
        "name": "SELF-HEALING PAINT RESTORATION",
        "subtitle": "自修复车漆修复膜 | 遮盖划痕 | 即时修复 | 亮面如新",
        "tag": "🔧 自修复",
        "title": "SELF-HEALING Paint Restoration Film - DUMI AUTO | Scratch-Concealing Self-Healing PPF",
        "description": "DUMI SELF-HEALING PAINT RESTORATION film uses advanced thermo-polyurethane technology that actually heals minor scratches on its own. Apply over existing light scratches and swirl marks — the film visually conceals damage while providing ongoing protection that maintains a flawless finish indefinitely.",
        "keywords": "self healing ppf, paint restoration film, scratch concealing film, self repairing ppf, ppf for scratches, automotive paint protection, dumi self healing, scratch hiding film",
        "alt_visual": "DUMI SELF-HEALING PAINT RESTORATION film applied over scratched paint showing visual scratch concealment",
        "gradient": "linear-gradient(135deg,#1a1a2a,#2d2d5a,#1a1a3a)",
        "placeholder": "🔧 SELF-HEALING",
        "tag_color": "#2d2d5a",
        "features": [
            ("Visual Scratch Concealment", "Applied over existing light damage for instant cosmetic improvement"),
            ("Continuous Self-Healing", "Heat-activated healing keeps surface flawless indefinitely"),
            ("Optical Clarity", "Crystal-clear film doesn't alter paint color or appearance"),
            ("Thin & Conformable", "Ultra-thin construction for invisible protection on curves"),
        ],
        "applications": ["Show Cars", "Daily Drivers", "Collector Vehicles", "Lease Returns"],
        "related": ["paint-restoration-coating.html", "ultra-gloss-defender-ppf.html", "crystalline-ppf.html"],
        "h1": "SELF-HEALING PAINT RESTORATION™",
        "h2_intro": "Hide Scratches, Prevent Future Damage — Self-Healing Technology",
    },
    {
        "filename": "color-stable-charcoal-tint.html",
        "name": "COLOR STABLE CHARCOAL TINT",
        "subtitle": "色彩稳定炭灰窗膜 | 不褪色 | 经典炭灰 | 隐私保护",
        "tag": "🖤 炭灰经典",
        "title": "COLOR STABLE CHARCOAL Window Tint - DUMI AUTO | Non-Fading Charcoal Window Film",
        "description": "DUMI COLOR STABLE CHARCOAL uses proprietary dye technology that resists fade and color shift far longer than conventional window film. The classic charcoal color provides excellent privacy and heat rejection while maintaining its original appearance for years without turning purple or changing hue.",
        "keywords": "color stable tint, charcoal window film, non-fading tint, purple free tint, classic charcoal tint, car window tint, dumi color stable, automotive tint charcoal",
        "alt_visual": "DUMI COLOR STABLE CHARCOAL window tint showing classic dark charcoal appearance with no purple color shift",
        "gradient": "linear-gradient(135deg,#1a1a1a,#2d2d2d,#1a1a1a)",
        "placeholder": "🖤 CHARCOAL TINT",
        "tag_color": "#2d2d2d",
        "features": [
            ("Non-Fade Formula", "Proprietary dye technology prevents purple color shift"),
            ("Classic Charcoal Appearance", "Timeless dark charcoal look that never goes out of style"),
            ("Excellent Heat Rejection", "Blocks 50%+ of total solar energy despite non-ceramic construction"),
            ("Lifetime Color Guarantee", "DUMI warranty covers any color change or fading"),
        ],
        "applications": ["Sedans", "SUVs", "Trucks", "Any Vehicle Type"],
        "related": ["carbon-tint.html", "ceramic-tint.html", "gradient-smoke-film.html"],
        "h1": "COLOR STABLE CHARCOAL™",
        "h2_intro": "Timeless Style That Lasts — Color Stable Charcoal That Never Fades",
    },
    {
        "filename": "polarized-ice-blue-tint.html",
        "name": "POLARIZED ICE BLUE TINT",
        "subtitle": "极地冰蓝窗膜 | 独特冰蓝色 | 时尚改装 | 视线清晰",
        "tag": "❄️ 极地冰蓝",
        "title": "POLARIZED ICE BLUE Window Tint - DUMI AUTO | Stylish Ice Blue Automotive Window Film",
        "description": "DUMI POLARIZED ICE BLUE combines a stunning ice-blue tinted appearance with functional heat rejection. The unique color gives your vehicle a distinctive look that stands out from conventional tints while providing the comfort benefits of solar heat reduction. Polarized construction reduces glare without darkening visibility.",
        "keywords": "ice blue tint, blue window film, polarized automotive tint, blue car tint, ice blue window, dumi ice blue, cool blue tint, automotive tint blue",
        "alt_visual": "DUMI POLARIZED ICE BLUE tint showing distinctive ice blue appearance through car window",
        "gradient": "linear-gradient(135deg,#1a2a3a,#2a5a7a,#1a3a5a)",
        "placeholder": "❄️ ICE BLUE TINT",
        "tag_color": "#2a5a7a",
        "features": [
            ("Distinctive Ice Blue Color", "Unlike any conventional tint — truly unique automotive style"),
            ("Polarized Construction", "Reduces glare from oncoming headlights and bright sunlight"),
            ("Heat Rejection", "Functional solar control with stunning visual appeal"),
            ("Quality Dye System", "Premium dye maintains color stability without fading"),
        ],
        "applications": ["Sports Cars", "Luxury Vehicles", "Custom Builds", "Car Enthusiasts"],
        "related": ["aurora-silver-ppf.html", "gradient-smoke-film.html", "carbon-ceramic-tint.html"],
        "h1": "POLARIZED ICE BLUE™",
        "h2_intro": "Stand Out From the Crowd — Ice Blue That Turns Heads",
    },
    {
        "filename": "ceramic-paint-sealant-spray.html",
        "name": "CERAMIC PAINT SEALANT SPRAY",
        "subtitle": "陶瓷车漆密封喷雾 | 即喷即用 | DIY便捷 | 快速镀晶",
        "tag": "✨ DIY镀晶",
        "title": "CERAMIC Paint Sealant Spray - DUMI AUTO | Quick & Easy DIY Ceramic Coating Spray",
        "description": "DUMI CERAMIC PAINT SEALANT SPRAY brings professional ceramic coating technology to any car owner. Simply spray on and wipe off to add a durable ceramic layer to your paint. Provides 6+ months of protection with water beading, UV blocking, and that incredible ceramic slickness — no professional skills required.",
        "keywords": "ceramic paint sealant spray, diy ceramic coating, spray ceramic coating, quick ceramic coating, car paint sealant spray, dumi ceramic sealant, automotive spray ceramic, easy ceramic coating",
        "alt_visual": "DUMI CERAMIC PAINT SEALANT SPRAY being applied showing easy spray-on wipe-off ceramic protection",
        "gradient": "linear-gradient(135deg,#1a2a3a,#2a5a7a,#1a3a5a)",
        "placeholder": "✨ CERAMIC SEALANT",
        "tag_color": "#2a5a7a",
        "features": [
            ("Spray-On Ease", "Simply spray and wipe — no special equipment or skills needed"),
            ("6+ Month Protection", "Durable ceramic bond lasts 6+ months per application"),
            ("Hydrophobic & Slick", "That incredible ceramic water-beading and silky-smooth feel"),
            ("UV Fade Protection", "Shields paint from sun-induced oxidation and fading"),
        ],
        "applications": ["DIY Car Care", "Car Enthusiasts", "Fleet Vehicles", "Quick Detail Protection"],
        "related": ["ceramic-pro-coating.html", "hydrophobic-topcoat.html", "auto-ceramic-coating-spray.html"],
        "h1": "CERAMIC PAINT SEALANT SPRAY™",
        "h2_intro": "Professional Ceramic Protection — Spray On, Wipe Off, Done",
    },
    {
        "filename": "paint-protection-tape-roll.html",
        "name": "PAINT PROTECTION TAPE ROLL",
        "subtitle": "DIY漆面保护胶带 | 随手贴 | 高粘耐用 | 局部防护",
        "tag": "📦 DIY必备",
        "title": "PAINT PROTECTION Tape Roll - DUMI AUTO | Pre-Cut DIY Paint Protection Tape for Any Vehicle",
        "description": "DUMI PAINT PROTECTION TAPE ROLL is a self-adhesive TPU tape designed for DIY paint protection on high-impact areas. Apply to door sills, hood edges, trunk lips, and anywhere rocks and debris cause chips. Clear construction makes it nearly invisible while providing the same PPF protection as our full-coverage products.",
        "keywords": "paint protection tape, ppf tape roll, door sill protection tape, hood protection tape, diy ppf tape, automotive protection tape, dumi ppf tape, clear protection tape",
        "alt_visual": "DUMI PAINT PROTECTION TAPE ROLL applied on door sills showing invisible scratch and chip protection",
        "gradient": "linear-gradient(135deg,#1a1a2a,#2d2d5a,#1a1a3a)",
        "placeholder": "📦 PPF TAPE",
        "tag_color": "#2d2d5a",
        "features": [
            ("Self-Adhesive TPU", "Same material as premium PPF with pressure-sensitive adhesive"),
            ("Crystal Clear", "Virtually invisible on any paint color"),
            ("Cut to Any Size", "Roll format lets you cut exact lengths for your needs"),
            ("8MIL Thickness", "Thick enough for real protection, thin enough to conform easily"),
        ],
        "applications": ["Door Sills", "Hood Edges", "Trunk Lips", "Mirror Backs", "Anywhere Rocks Hit"],
        "related": ["premium-edge-guard-ppf.html", "ultimate-plus.html", "anti-graffiti-film.html"],
        "h1": "PAINT PROTECTION TAPE ROLL™",
        "h2_intro": "Protect Specific Areas — DIY Paint Protection Tape for High-Impact Zones",
    },
    {
        "filename": "ceramic-wheel-guard-film.html",
        "name": "CERAMIC WHEEL GUARD FILM",
        "subtitle": "轮毂防护陶瓷膜 | 防刹车粉 | 耐高温 | 保持清洁",
        "tag": "🛞 轮毂防护",
        "title": "CERAMIC Wheel Guard Film - DUMI AUTO | Brake Dust Resistant Ceramic Wheel Protection",
        "description": "DUMI CERAMIC WHEEL GUARD is a high-heat-resistant ceramic coating film designed specifically for wheel surfaces. Protects expensive alloy wheels from corrosive brake dust, road salt, and brake fluid while maintaining the factory finish. Heat-resistant to 400°C, making it suitable for any vehicle from daily drivers to track cars.",
        "keywords": "wheel guard film, brake dust protection, ceramic wheel coating, alloy wheel protection, wheel ppf film, dumi wheel guard, automotive wheel protection, brake dust resistant coating",
        "alt_visual": "DUMI CERAMIC WHEEL GUARD applied on alloy wheel showing brake dust resistance and heat protection",
        "gradient": "linear-gradient(135deg,#2a2a2a,#4a4a4a,#3a3a3a)",
        "placeholder": "🛞 WHEEL GUARD",
        "tag_color": "#3a3a3a",
        "features": [
            ("400°C Heat Resistance", "Withstands extreme brake heat without degrading"),
            ("Brake Dust Barrier", "Prevents corrosive brake dust from etching wheel finish"),
            ("Chemical Resistance", "Protects against road salt, brake fluid, and cleaning chemicals"),
            ("Easy Clean Surface", "Hydrophobic ceramic surface makes wheel cleaning effortless"),
        ],
        "applications": ["Performance Wheels", "Luxury Alloy Wheels", "Track Car Wheels", "Winter Climate Vehicles"],
        "related": ["ceramic-wheel-coating.html", "brake-caliper-ppf.html", "brake-disc-ceramic-coating.html"],
        "h1": "CERAMIC WHEEL GUARD™",
        "h2_intro": "Keep Your Wheels Pristine — Ceramic Protection Against Brake Dust",
    },
    {
        "filename": "infrared-infrared-blocking-tint.html",
        "name": "INFRARED BLOCKING CERAMIC TINT",
        "subtitle": "红外阻隔陶瓷窗膜 | 顶级隔热 | 信号自由 | 舒适驾乘",
        "tag": "🌡️ 红外阻隔",
        "title": "INFRARED BLOCKING CERAMIC Tint - DUMI AUTO | Top-Tier IR Heat Blocking Window Film",
        "description": "DUMI INFRARED BLOCKING CERAMIC represents our most advanced window film technology. Multi-layer ceramic particles block up to 99% of infrared heat radiation while maintaining optical clarity. The premium choice for customers who demand maximum comfort without any compromises on visibility or signal transmission.",
        "keywords": "infrared blocking tint, IR heat blocking film, ceramic infrared tint, maximum heat rejection tint, premium window film, dumi IR blocking, automotive infrared protection, signal friendly heat blocking",
        "alt_visual": "DUMI INFRARED BLOCKING CERAMIC window tint showing maximum heat rejection with crystal clear visibility",
        "gradient": "linear-gradient(135deg,#1a3a4a,#2a6a8a,#1a4a7a)",
        "placeholder": "🌡️ IR BLOCKING",
        "tag_color": "#2a6a8a",
        "features": [
            ("99% IR Heat Blocking", "Multi-layer ceramic technology blocks nearly all infrared radiation"),
            ("Maximum Solar Rejection", "Blocks up to 85% of total solar energy"),
            ("Zero Signal Interference", "100% ceramic construction — no metal means full GPS and radio compatibility"),
            ("Crystal Clear Options", "Available in multiple VLT levels from near-clear to dark"),
        ],
        "applications": ["Luxury Vehicles", "Electric Vehicles", "Hot Climate Cars", "Premium Builds"],
        "related": ["ceramic-matrix-tint.html", "solar-heat-reject-ceramic-tint.html", "pristine-ceramic-tint.html"],
        "h1": "INFRARED BLOCKING CERAMIC™",
        "h2_intro": "Block the Heat, Not the Signal — Ultimate IR Blocking Technology",
    },
    {
        "filename": "anti-scratch-matte-finish-film.html",
        "name": "ANTI-SCRATCH MATTE FINISH",
        "subtitle": "抗划痕哑光膜 | 哑光质感 | 防护+美观 | 自修复可选",
        "tag": "🖤 哑光抗划",
        "title": "ANTI-SCRATCH MATTE FINISH Film - DUMI AUTO | Scratch-Resistant Matte Protection Film",
        "description": "DUMI ANTI-SCRATCH MATTE FINISH combines the sophisticated look of matte paint with enhanced scratch resistance. Proprietary topcoat technology resists swirl marks and fine scratches that commonly affect matte finishes. Enjoy the stealth aesthetic without the usual matte-care anxiety.",
        "keywords": "anti-scratch matte film, scratch resistant matte ppf, matte protection film, stealth ppf scratch resistant, matte car wrap protection, dumi anti-scratch matte, automotive matte protection, scratch guard matte",
        "alt_visual": "DUMI ANTI-SCRATCH MATTE FINISH film showing enhanced scratch resistance on matte black car surface",
        "gradient": "linear-gradient(135deg,#0d0d0d,#1a1a1a,#0d0d0d)",
        "placeholder": "🖤 MATTE ANTI-SCRATCH",
        "tag_color": "#1a1a1a",
        "features": [
            ("Enhanced Scratch Resistance", "Proprietary topcoat resists swirl marks and fine scratches"),
            ("True Matte Texture", "Authentic satin-matte finish — not a compromise"),
            ("Protects Original Matte", "Shield factory matte paint from damage and contamination"),
            ("Self-Healing Option", "Available in self-healing variant for ultimate surface perfection"),
        ],
        "applications": ["Matte Paint Vehicles", "Stealth Builds", "Luxury Sedans", "Show Cars"],
        "related": ["stealth-pro-ppf.html", "matte-satin-ppf.html", "premium-edge-guard-ppf.html"],
        "h1": "ANTI-SCRATCH MATTE FINISH™",
        "h2_intro": "Matte Looks Without Matte Anxiety — Enhanced Scratch Resistance",
    },
    {
        "filename": "marine-grade-boat-ppf.html",
        "name": "MARINE GRADE BOAT PPF",
        "subtitle": "船舶级游艇PPF | 盐雾防腐 | 海洋环境 | 极端防护",
        "tag": "🚤 船舶专用",
        "title": "MARINE GRADE BOAT PPF - DUMI AUTO | Saltwater-Resistant Paint Protection for Marine Vessels",
        "description": "DUMI MARINE GRADE BOAT PPF is specifically engineered for the harsh marine environment. Salt-resistant, UV-stabilized, and designed to withstand constant exposure to saltwater, sun, and marine growth. Protect your boat's hull, console, and upholstery from the devastating effects of saltwater corrosion.",
        "keywords": "marine ppf, boat paint protection film, saltwater resistant ppf, marine grade film, boat hull protection, yacht ppf film, dumi marine ppf, boat protection film",
        "alt_visual": "DUMI MARINE GRADE BOAT PPF applied on boat hull showing saltwater and UV resistance in marine environment",
        "gradient": "linear-gradient(135deg,#0a2a3a,#1a5a7a,#0a3a6a)",
        "placeholder": "🚤 MARINE PPF",
        "tag_color": "#1a5a7a",
        "features": [
            ("Saltwater Resistant", "Formulated to resist salt crystallization and salt-induced corrosion"),
            ("UV Stabilized", "Marine-grade UV inhibitors prevent degradation from constant sun exposure"),
            ("Flexible for Hulls", "Conforms to curved hull surfaces without lifting"),
            ("Chemical Resistant", "Resists saltwater, sunscreen, fuel, and marine cleaning chemicals"),
        ],
        "applications": ["Boat Hulls", "Marine Consoles", "Tender Boats", "Personal Watercraft"],
        "related": ["marine-acoustic-panels.html", "storm-shield-ppf.html", "uv-protection-film.html"],
        "h1": "MARINE GRADE BOAT PPF™",
        "h2_intro": "Built for the Sea — Marine-Grade Protection Against Salt & Sun",
    },
    {
        "filename": "premium-carbon-ceramic-tint.html",
        "name": "PREMIUM CARBON CERAMIC TINT",
        "subtitle": "高端碳纤维陶瓷窗膜 | 碳+陶瓷双技术 | 双重隔热 | 经典耐用",
        "tag": "🔥 碳陶瓷双技术",
        "title": "PREMIUM CARBON CERAMIC Tint - DUMI AUTO | Carbon + Ceramic Hybrid Window Film",
        "description": "DUMI PREMIUM CARBON CERAMIC combines carbon particle technology with ceramic nanoparticles for dual-mechanism heat rejection. Carbon particles provide excellent IR blocking while ceramic particles add durability and UV protection. The result is a premium window film with outstanding performance across all solar spectrums.",
        "keywords": "carbon ceramic tint, hybrid window film, carbon ceramic hybrid, premium car tint, dual technology tint, dumi carbon ceramic, automotive tint hybrid, carbon plus ceramic",
        "alt_visual": "DUMI PREMIUM CARBON CERAMIC tint showing dual carbon and ceramic technology heat rejection performance",
        "gradient": "linear-gradient(135deg,#1a2a1a,#2d5a2d,#1a3a1a)",
        "placeholder": "🔥 CARBON CERAMIC",
        "tag_color": "#2d5a2d",
        "features": [
            ("Dual-Mechanism Heat Rejection", "Carbon + ceramic provides comprehensive IR and UV blocking"),
            ("Premium Dark Charcoal", "Deep charcoal color provides excellent privacy and aesthetics"),
            ("Long-Term Stability", "Ceramic component prevents dye degradation common in carbon-only films"),
            ("Full Signal Compatibility", "No metal means GPS, radar, and phone signals work perfectly"),
        ],
        "applications": ["Luxury Sedans", "Performance Vehicles", "Family SUVs", "Premium Builds"],
        "related": ["carbon-tint.html", "ceramic-matrix-tint.html", "infrared-infrared-blocking-tint.html"],
        "h1": "PREMIUM CARBON CERAMIC™",
        "h2_intro": "Two Technologies, One Premium Film — Carbon + Ceramic Combined",
    },
    {
        "filename": "scratch-resist-ultimate-plus-ppf.html",
        "name": "SCRATCH RESIST ULTIMATE PLUS",
        "subtitle": "耐划痕终极加强PPF | 10MIL加厚 | 军规级防护 | 全方位保障",
        "tag": "🛡️ 终极防护",
        "title": "SCRATCH RESIST ULTIMATE PLUS PPF - DUMI AUTO | 10MIL Heavy-Duty Scratch Resistant Paint Protection",
        "description": "DUMI SCRATCH RESIST ULTIMATE PLUS is our thickest and most protective PPF in the Ultimate line. At 10MIL total thickness with a 5MIL topcoat, it provides exceptional resistance to rock chips, scratches, and road debris. The ultimate choice for heavy daily commutes, delivery vehicles, and vehicles in high-debris environments.",
        "keywords": "scratch resist ppf, ultimate plus ppf, heavy duty ppf, thick ppf film, rock chip protection, commercial ppf, dumi ultimate plus, fleet vehicle ppf",
        "alt_visual": "DUMI SCRATCH RESIST ULTIMATE PLUS PPF applied on daily commuter vehicle showing maximum rock chip protection",
        "gradient": "linear-gradient(135deg,#1a1a2a,#2d2d5a,#1a1a3a)",
        "placeholder": "🛡️ ULTIMATE PLUS",
        "tag_color": "#2d2d5a",
        "features": [
            ("10MIL Total Thickness", "Our thickest Ultimate-series film for maximum protection"),
            ("5MIL Topcoat for Scratch Resistance", "Thickest topcoat in our lineup resists scratches and chips"),
            ("Self-Healing Topcoat", "Heat-activated self-repair keeps the surface pristine"),
            ("Warranty Covered", "Backed by DUMI 10-year warranty against yellowing and peeling"),
        ],
        "applications": ["Delivery Vehicles", "Fleet Cars", "Heavy Commute Vehicles", "Family SUVs"],
        "related": ["ultimate-plus.html", "armor-ppf.html", "military-grade-urethane-ppf.html"],
        "h1": "SCRATCH RESIST ULTIMATE PLUS™",
        "h2_intro": "Our Thickest Ultimate Film — When Maximum Protection Is the Only Option",
    },
]


def generate_product_html(p):
    features_html = ""
    for title, desc in p["features"]:
        features_html += f'''  <div class="product-feature-item">
    <span class="feature-icon">✓</span>
    <div>
      <strong>{title}</strong>
      <p>{desc}</p>
    </div>
  </div>
'''

    apps_html = ""
    for app in p["applications"]:
        apps_html += f'<span>{app}</span>'

    related_html = ""
    for rel in p["related"]:
        rel_name = rel.replace(".html", "").replace("-", " ").title()
        related_html += f'''  <a href="{rel}" class="product-card">
    <div class="product-img" style="background: {p["gradient"]};">
      <img src="../images/products/dumi_shield-4.webp" alt="{rel_name} - DUMI PPF Product" style="width:100%;height:100%;object-fit:cover;">
    </div>
    <div class="product-info">
      <h3>{rel_name.upper()}</h3>
      <p>DUMI Product</p>
      <span class="product-price">Learn More →</span>
    </div>
  </a>
'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p["title"]}</title>
  <meta name="description" content="{p["description"]}">
  <meta name="keywords" content="{p["keywords"]}">
  <link rel="stylesheet" href="../css/style.css">
  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{p["name"]}",
  "description": "{p["description"]}",
  "brand": {{
    "@type": "Brand",
    "name": "DUMI AUTO"
  }},
  "offers": {{
    "@type": "Offer",
    "priceCurrency": "USD",
    "price": "0",
    "availability": "https://schema.org/InStock",
    "seller": {{
      "@type": "Organization",
      "name": "DUMI AUTO"
    }}
  }}
}}
</script>
</head>
<body>
  <header class="header">
    <div class="container">
      <div class="logo"><h1>DUMI<span>AUTO</span></h1><p>Professional Auto Protection Film Expert</p></div>
      <nav class="nav">
        <a href="../index.html">Home</a>
        <a href="../index.html#products">Products</a>
        <a href="../index.html#services">Services</a>
        <a href="../index.html#about">About</a>
        <a href="../index.html#contact">Contact</a>
      </nav>
      <div class="header-cta"><a href="../index.html#contact" class="btn-primary">Book Now</a></div>
    </div>
  </header>

  <section class="product-detail">
    <div class="container">
      <div class="breadcrumb">
        <a href="../index.html">Home</a> / <a href="../index.html#products">Products</a> / {p["name"]}
      </div>
      <div class="product-detail-grid">
        <div class="product-detail-img">
          <div class="product-detail-visual" style="background: {p["gradient"]};">
            <img src="../images/products/dumi_shield-4.webp" alt="{p["alt_visual"]}" style="width:100%;height:100%;object-fit:cover;border-radius:12px;">
          </div>
        </div>
        <div class="product-detail-info">
          <div class="product-detail-tag">{p["tag"]}</div>
          <h1>{p["h1"]}</h1>
          <p class="product-subtitle">{p["subtitle"]}</p>
          <div class="product-detail-desc">
            <h2>{p["h2_intro"]}</h2>
            <p>{p["description"]}</p>
          </div>
          <div class="product-features">
{features_html}
          </div>
          <div class="product-applications">
            <h3>Suitable Scenarios</h3>
            <div class="application-tags">
              {apps_html}
            </div>
          </div>
          <div class="product-cta">
            <a href="../index.html#contact" class="btn-primary">Get a Quote →</a>
            <a href="ultimate-plus.html" class="btn-outline">View Standard PPF</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="related-products">
    <div class="container">
      <div class="section-header">
        <h2>Related Products</h2>
      </div>
      <div class="products-grid">
{related_html}
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand"><h2>DUMI<span>AUTO</span></h2><p>Professional Auto Protection Film Expert · Professional PPF Manufacturer / Factory Direct</p></div>
        <div class="footer-links"><h4>Product Categories</h4><a href="ultimate-plus.html">Paint Protection Film (PPF)</a><a href="prime-window-film.html">Window Tint Series</a><a href="stealth-ppf.html">STEALTH Matte Film</a><a href="color-ppf.html">COLOR Change Film</a></div>
        <div class="footer-links"><h4>Quick Links</h4><a href="../index.html">Home</a><a href="../index.html#contact">Contact Us</a></div>
        <div class="footer-contact"><h4>Contact</h4><p>📧 carstauto2017@gmail.com</p><p>📱 +86-13001727017</p><p>📱 +61-493342108</p></div>
      </div>
      <div class="footer-bottom"><p>© 2026 DUMI AUTO. All rights reserved. | Professional PPF Manufacturer / Factory Direct</p></div>
    </div>
  </footer>

  <style>
    .breadcrumb {{ padding: 20px 0; font-size: 13px; color: #999; }}
    .product-detail {{ padding: 20px 0 60px; }}
    .product-detail-grid {{ display: grid; grid-template-columns: 1fr 1.2fr; gap: 50px; align-items: start; }}
    .product-detail-visual {{ height: 450px; border-radius: 12px; display: flex; align-items: center; justify-content: center; }}
    .product-detail-placeholder {{ font-size: 48px; color: rgba(255,255,255,0.15); }}
    .product-detail-tag {{ display: inline-block; background: {p["tag_color"]}; color: white; padding: 4px 12px; border-radius: 4px; font-size: 12px; font-weight: 600; margin-bottom: 15px; }}
    .product-detail-info h1 {{ font-size: 42px; font-weight: 800; color: #1a1a2e; margin-bottom: 10px; letter-spacing: 2px; }}
    .product-subtitle {{ font-size: 16px; color: #888; margin-bottom: 25px; }}
    .product-detail-desc {{ background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 25px; border-left: 4px solid {p["tag_color"]}; }}
    .product-detail-desc h2 {{ font-size: 16px; font-weight: 700; color: #1a1a2e; margin-bottom: 10px; }}
    .product-detail-desc p {{ color: #555; line-height: 1.8; }}
    .product-features {{ margin-bottom: 25px; }}
    .product-feature-item {{ display: flex; align-items: flex-start; gap: 12px; margin-bottom: 14px; }}
    .feature-icon {{ background: {p["tag_color"]}; color: white; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; flex-shrink: 0; margin-top: 2px; }}
    .product-feature-item strong {{ display: block; font-size: 14px; color: #1a1a2e; }}
    .product-feature-item p {{ font-size: 12px; color: #888; }}
    .product-applications h3 {{ font-size: 16px; font-weight: 700; color: #1a1a2e; margin-bottom: 12px; }}
    .application-tags {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .application-tags span {{ background: #1a1a2e; color: white; padding: 6px 14px; border-radius: 4px; font-size: 13px; }}
    .product-cta {{ display: flex; gap: 15px; margin-top: 30px; }}
    .related-products {{ padding: 60px 0; }}
    @media (max-width: 768px) {{ .product-detail-grid {{ grid-template-columns: 1fr; }} }}
  </style>
</body>
</html>'''
    return html


def main():
    created = []
    for p in NEW_PRODUCTS:
        filepath = os.path.join(BASE_DIR, p["filename"])
        html = generate_product_html(p)
        with open(filepath, "w") as f:
            f.write(html)
        created.append(p["filename"])
        print(f"✅ Created: {p['filename']}")

    print(f"\nTotal created: {len(created)}")
    return created


if __name__ == "__main__":
    main()
