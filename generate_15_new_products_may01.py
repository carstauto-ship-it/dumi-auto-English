#!/usr/bin/env python3
"""Generate 15 new SEO-optimized product pages for dumi-auto.com - 2026-05-01"""
import os

BASE_DIR = "/Users/carstauto/.openclaw/workspace/dumi-auto-website/products"

NEW_PRODUCTS = [
    {
        "filename": "holographic-chrome-ppf.html",
        "name": "HOLOGRAPHIC CHROME PPF",
        "subtitle": "全息幻彩PPF | 随光变色 | 渐变金属质感 | 炫酷改装",
        "tag": "🌈 全息幻彩",
        "title": "HOLOGRAPHIC CHROME PPF - DUMI AUTO | Color-Shifting Holographic Paint Protection Film",
        "description": "DUMI HOLOGRAPHIC CHROME PPF delivers a stunning color-shifting holographic effect that changes appearance under different lighting angles. Transform your vehicle with a mesmerizing rainbow sheen while enjoying full paint protection. A true head-turner for car enthusiasts.",
        "keywords": "holographic ppf, holographic car wrap, color shifting ppf, chrome holographic film, car paint protection holographic, rainbow ppf, dumi holographic ppf, car wrapping film",
        "alt_visual": "DUMI HOLOGRAPHIC CHROME PPF applied on sports car showing rainbow color-shifting holographic effect",
        "gradient": "linear-gradient(135deg,#1a0a2a,#4a1a6a,#2a0a4a,#6a2a8a)",
        "placeholder": "🌈 HOLOGRAPHIC",
        "tag_color": "#4a1a6a",
        "features": [
            ("Dynamic Color-Shifting Effect", "Holographic micro-particles create rainbow shimmer that changes with light angle"),
            ("Full Paint Protection", "Unlike vinyl wrap, TPU base protects original paint from chips and scratches"),
            ("Glossy Chrome Base", "High-gloss foundation under the holographic layer for maximum visual impact"),
            ("Removable & Reversible", "Change your look anytime without damaging original paint"),
        ],
        "applications": ["Sports Cars", "Show Cars", "Car Enthusiasts", "Custom Builds"],
        "related": ["metallic-ppf.html", "electric-blue-ppf.html", "spectrum-chrome-film.html"],
        "h1": "HOLOGRAPHIC CHROME PPF™",
        "h2_intro": "Turn Heads with Dynamic Color-Shifting Holographic Protection",
    },
    {
        "filename": "storm-shield-ppf.html",
        "name": "STORM SHIELD PPF",
        "subtitle": "暴风雨防护PPF | 极端天气专用 | 越野/恶劣路况 | 强化装甲",
        "tag": "🛡️ 极端防护",
        "title": "STORM SHIELD PPF - DUMI AUTO | Extreme Weather Paint Protection Film for Off-Road",
        "description": "DUMI STORM SHIELD PPF is engineered for vehicles that face extreme conditions — rock crawling, desert trails, coastal roads, and winter salt. Extra-thick TPU construction with armored topcoat provides unmatched defense against everything nature throws at your vehicle.",
        "keywords": "storm shield ppf, extreme weather ppf, off-road ppf, rock crawler ppf, all-terrain ppf, heavy duty paint protection, dumi storm shield, off-road protection film",
        "alt_visual": "DUMI STORM SHIELD PPF installed on off-road vehicle traversing rocky terrain showing extreme protection",
        "gradient": "linear-gradient(135deg,#1a2a1a,#2d4a2d,#1a3a1a)",
        "placeholder": "🛡️ STORM SHIELD",
        "tag_color": "#1a3a1a",
        "features": [
            ("Armored 11MIL Thickness", "Thickest PPF in our lineup for maximum impact and abrasion resistance"),
            ("Salt & Chemical Resistant", "Specially formulated to withstand road salt, mud, and harsh chemicals"),
            ("Extreme Temperature Rated", "Performs in temperatures from -40°C to +60°C without degradation"),
            ("Full Underbody Capable", "Flexible enough to wrap contoured underbody panels and frame rails"),
        ],
        "applications": ["Off-Road Vehicles", "4x4s & Jeeps", "Winter Climate Vehicles", "Desert Runners"],
        "related": ["armor-ppf.html", "commercial-vehicle-ppf.html", "exterior-protective-film.html"],
        "h1": "STORM SHIELD PPF™",
        "h2_intro": "Built for Extremes — When Standard PPF Isn't Tough Enough",
    },
    {
        "filename": "diamond-glass-tint.html",
        "name": "DIAMOND GLASS TINT",
        "subtitle": "钻石玻璃窗膜 | 钻石级切割工艺 | 极致清晰 | 奢华定制",
        "tag": "💎 钻石玻璃",
        "title": "DIAMOND GLASS Window Tint - DUMI AUTO | Premium Diamond-Cut Window Film",
        "description": "DUMI DIAMOND GLASS TINT uses precision diamond-cut technology for unmatched optical clarity and heat rejection. The ultimate window film for luxury vehicles where no compromise is acceptable. Blocks 97% of infrared heat while maintaining perfect visibility.",
        "keywords": "diamond glass tint, premium window film, luxury window tint, crystal clear tint, high clarity window film, dumi diamond glass, luxury car tint",
        "alt_visual": "DUMI DIAMOND GLASS TINT showing crystal clear visibility through luxury car window",
        "gradient": "linear-gradient(135deg,#1a3a4a,#2a5a7a,#1a4a6a)",
        "placeholder": "💎 DIAMOND GLASS",
        "tag_color": "#2a5a7a",
        "features": [
            ("Diamond-Cut Precision", "Micron-precise manufacturing for flawless optical clarity"),
            ("97% IR Heat Rejection", "Maximum infrared heat blocking without dark tint or metal"),
            ("Zero Distortion", "Optically perfect film with zero distortion for safest driving visibility"),
            ("Ceramic Nano-Particle", "Latest-generation ceramic nanoparticles for consistent performance"),
        ],
        "applications": ["Luxury Sedans", "Executive SUVs", "High-End Coupes", "Prestige Vehicles"],
        "related": ["ceramic-matrix-tint.html", "crystalline-ppf.html", "pristine-ceramic-tint.html"],
        "h1": "DIAMOND GLASS TINT™",
        "h2_intro": "Precision-Engineered for Those Who Accept Only the Best",
    },
    {
        "filename": "electric-vehicle-ppf.html",
        "name": "ELECTRIC VEHICLE PPF",
        "subtitle": "电动车专用PPF | 信号零干扰 | 充电接口保护 | 智能出行",
        "tag": "⚡ 电动车专用",
        "title": "ELECTRIC VEHICLE PPF - DUMI AUTO | Signal-Friendly PPF for EVs & Hybrids",
        "description": "DUMI EV PPF is specifically engineered for electric and hybrid vehicles. 100% metal-free construction ensures zero interference with vehicle sensors, radar, GPS, and autopilot systems. Protect your EV's pristine paint without compromising its advanced technology.",
        "keywords": "electric vehicle ppf, EV ppf, Tesla ppf, signal friendly ppf, EV paint protection, autopilot ppf, dumi ev ppf, hybrid car protection film",
        "alt_visual": "DUMI ELECTRIC VEHICLE PPF installed on Tesla Model 3 showing invisible paint protection",
        "gradient": "linear-gradient(135deg,#0a2a3a,#1a4a6a,#0a3a5a)",
        "placeholder": "⚡ EV PPF",
        "tag_color": "#0a3a5a",
        "features": [
            ("100% Metal-Free Formula", "Zero signal interference with radar, sensors, GPS, or autopilot systems"),
            ("EV Charging Port Compatible", "Special formulation won't degrade near high-voltage charging equipment"),
            ("Aerodynamic Surface Smooth", "Ultra-smooth topcoat reduces drag coefficient for minor efficiency gains"),
            ("High-Gloss Retention", "Maintains that fresh-from-the-factory showroom gloss for years"),
        ],
        "applications": ["Tesla Vehicles", "Rivian Trucks", "All-Electric Vehicles", "Plug-in Hybrids"],
        "related": ["ultimate-plus.html", "nano-ceramic-tint.html", "crystal-glass-topcoat.html"],
        "h1": "ELECTRIC VEHICLE PPF™",
        "h2_intro": "Protection Built for the Next Generation of Vehicles",
    },
    {
        "filename": "satin-slate-grey-ppf.html",
        "name": "SATIN SLATE GREY PPF",
        "subtitle": "缎面板岩灰PPF | 低饱和灰 | 质感出众 | 改装首选",
        "tag": "🪨 缎面灰",
        "title": "SATIN SLATE GREY PPF - DUMI AUTO | Premium Satin Slate Grey Paint Protection Film",
        "description": "DUMI SATIN SLATE GREY PPF delivers a sophisticated low-saturation grey with a premium satin texture. The most popular color in the automotive market, now available with full PPF protection. Transform your vehicle with the timeless slate grey aesthetic.",
        "keywords": "satin slate grey ppf, slate grey ppf, grey ppf car, satin grey paint protection, automotive grey ppf, dumi slate grey ppf, car wrap grey",
        "alt_visual": "DUMI SATIN SLATE GREY PPF applied on luxury sedan showing sophisticated satin grey finish",
        "gradient": "linear-gradient(135deg,#2a2a2a,#4a4a4a,#3a3a3a)",
        "placeholder": "🪨 SLATE GREY",
        "tag_color": "#3a3a3a",
        "features": [
            ("Popular Slate Grey Color", "Low-saturation grey that's become the benchmark for modern luxury vehicles"),
            ("Premium Satin Texture", "Subtle texture between gloss and matte for a sophisticated look"),
            ("Full Paint Protection", "All the benefits of PPF in the most sought-after automotive color"),
            ("Self-Healing Topcoat", "Minor scratches disappear with heat, keeping the satin texture perfect"),
        ],
        "applications": ["Luxury Sedans", "Performance Vehicles", "SUVs & Crossovers", "Show Car Builds"],
        "related": ["stealth-matte-black-ppf.html", "matte-satin-ppf.html", "satin-matte-ppf.html"],
        "h1": "SATIN SLATE GREY PPF™",
        "h2_intro": "The Most Wanted Grey — Now With Full PPF Protection",
    },
    {
        "filename": "brake-caliper-ppf.html",
        "name": "BRAKE CALIPER PPF",
        "subtitle": "刹车卡钳PPF保护膜 | 专用贴合 | 高温耐受 | 炫彩卡钳",
        "tag": "🔧 卡钳专用",
        "title": "BRAKE CALIPER PPF - DUMI AUTO | Heat-Resistant Paint Protection Film for Brake Calipers",
        "description": "DUMI BRAKE CALIPER PPF is a specialized high-heat-resistant film designed specifically for brake caliper protection. Protects your expensive calipers from brake dust oxidation, road salt, and stone chips while maintaining the stunning factory finish. Heat-rated to 300°C.",
        "keywords": "brake caliper ppf, caliper protection film, brake dust protection, high heat ppf, caliper wrap film, automotive caliper protection, dumi caliper ppf",
        "alt_visual": "DUMI BRAKE CALIPER PPF applied on red painted brake caliper showing heat-resistant protection",
        "gradient": "linear-gradient(135deg,#3a1a1a,#6a2a2a,#4a1a1a)",
        "placeholder": "🔧 CALIPER PPF",
        "tag_color": "#6a2a2a",
        "features": [
            ("300°C Heat Rated", "Engineered to withstand extreme brake temperatures without degradation"),
            ("Brake Dust Protection", "Shields caliper finish from corrosive brake dust and acid residue"),
            ("Precision Cut Patterns", "Computer-cut templates for popular vehicle makes and models"),
            ("Multi-Color Options", "Available in black, red, yellow, and custom colors to match your style"),
        ],
        "applications": ["Sports Cars", "Track Cars", "Modified Vehicles", "Show Cars"],
        "related": ["exterior-matte-film.html", "headlight-protection.html", "anti-graffiti-film.html"],
        "h1": "BRAKE CALIPER PPF™",
        "h2_intro": "Protect Your Performance Investment — Brake Caliper PPF",
    },
    {
        "filename": "underbody-protective-film.html",
        "name": "UNDERBODY SHIELD",
        "subtitle": "底盘装甲防护膜 | 防石击 | 防腐蚀 | 越野必备",
        "tag": "🛡️ 底盘防护",
        "title": "UNDERBODY SHIELD - DUMI AUTO | Heavy-Duty Underbody Protection Film for Cars",
        "description": "DUMI UNDERBODY SHIELD provides heavy-duty protection for your vehicle's underbody — the most vulnerable area to rock chips, road debris, and corrosion. Essential for off-road vehicles, winter climates, and anyone who wants to protect their car's structural integrity.",
        "keywords": "underbody protection film, undercarriage shield, chassis protection, rock chip underbody, anti-corrosion film, car underbody ppf, dumi underbody shield",
        "alt_visual": "DUMI UNDERBODY SHIELD applied on vehicle undercarriage showing complete chassis protection coverage",
        "gradient": "linear-gradient(135deg,#1a1a1a,#2d2d2d,#1a1a1a)",
        "placeholder": "🛡️ UNDERBODY",
        "tag_color": "#1a1a1a",
        "features": [
            ("Heavy-Duty 14MIL Construction", "Thickest film in our lineup — designed for real-world road abuse"),
            ("Corrosion & Salt Resistant", "Protects against road salt, mud, and moisture that cause rust"),
            ("Stone Chip Defense", "Absorbs impacts from gravel, rocks, and road debris"),
            ("Acoustic Dampening", "Reduces road noise transmitted through the underbody"),
        ],
        "applications": ["Off-Road Vehicles", "Winter Climate Cars", "Daily Commuters", "Performance Vehicles"],
        "related": ["storm-shield-ppf.html", "exterior-protective-film.html", "armor-ppf.html"],
        "h1": "UNDERBODY SHIELD™",
        "h2_intro": "The Armor Your Vehicle's Underbelly Desperately Needs",
    },
    {
        "filename": "carbon-fiber-window-tint.html",
        "name": "CARBON FIBER TINT",
        "subtitle": "碳纤维纹理窗膜 | 运动风格 | 高端改装 | 独特质感",
        "tag": "🏎️ 碳纤维纹",
        "title": "CARBON FIBER Window Tint - DUMI AUTO | Carbon Fiber Pattern Window Film for Sporty Look",
        "description": "DUMI CARBON FIBER TINT features an authentic carbon fiber weave pattern visible from both inside and outside your vehicle. Unlike solid dark tints, this unique film gives your windows a high-tech motorsport aesthetic while providing excellent heat rejection.",
        "keywords": "carbon fiber tint, carbon window film, sporty window tint, carbon weave tint, motorsport window film, dumi carbon fiber tint, car styling film",
        "alt_visual": "DUMI CARBON FIBER TINT applied on sports car window showing carbon weave pattern visible from outside",
        "gradient": "linear-gradient(135deg,#1a1a1a,#2d2d2d,#1a1a1a)",
        "placeholder": "🏎️ CARBON TINT",
        "tag_color": "#1a1a1a",
        "features": [
            ("Authentic Carbon Fiber Weave", "Real carbon fiber pattern — not a printed fake"),
            ("Distinctive Motorsport Look", "Visible carbon pattern gives your car a unique high-tech aesthetic"),
            ("Good Heat Rejection", "Carbon particle technology provides solid IR heat blocking"),
            ("Privacy Without Blackout", "Stylish tinted look without losing all visibility"),
        ],
        "applications": ["Sports Cars", "Track Cars", "Modified Vehicles", "Car Enthusiasts"],
        "related": ["carbon-tint.html", "carbon-ceramic-tint.html", "gradient-smoke-film.html"],
        "h1": "CARBON FIBER TINT™",
        "h2_intro": "Motorsport Aesthetics — Carbon Fiber Style Meets Window Film",
    },
    {
        "filename": "fabric-protection-coating.html",
        "name": "FABRIC PROTECTION COATING",
        "subtitle": "内饰织物保护镀晶 | 绒面/织物专用 | 防污防水 | 内饰翻新",
        "tag": "🧵 织物保护",
        "title": "FABRIC PROTECTION Coating - DUMI AUTO | Ceramic Coating for Car Interior Fabrics & Carpets",
        "description": "DUMI FABRIC PROTECTION COATING uses advanced ceramic nanotechnology to create an invisible protective barrier on car interior fabrics, carpets, and upholstery. Repels water, oil, and stains while maintaining the natural feel of your car's interior fabrics.",
        "keywords": "fabric protection coating, carpet ceramic coating, interior fabric protection, car upholstery coating, stain repellent coating, dumi fabric protection, car interior coating",
        "alt_visual": "DUMI FABRIC PROTECTION COATING applied on car carpet showing water beading and stain resistance",
        "gradient": "linear-gradient(135deg,#2a2a3a,#4a4a6a,#3a3a5a)",
        "placeholder": "🧵 FABRIC COATING",
        "tag_color": "#4a4a6a",
        "features": [
            ("Invisible Ceramic Barrier", "Nano-coating wraps individual fibers without changing fabric feel"),
            ("Oil & Water Repellent", "Spills bead up and can be blotted away before staining"),
            ("Breathable Protection", "Fabric remains soft and natural while being protected"),
            ("Long-Lasting Formula", "Durable ceramic bond lasts 1-2 years per application"),
        ],
        "applications": ["Car Interiors", "Floor Mats", "Convertible Tops", "Upholstery"],
        "related": ["ceramic-pro-coating.html", "hydrophobic-topcoat.html", "glass-ceramic-topcoat.html"],
        "h1": "FABRIC PROTECTION COATING™",
        "h2_intro": "Keep Your Interior Fabrics Pristine — Ceramic Repellent Protection",
    },
    {
        "filename": "uv-block-ceramic-spray.html",
        "name": "UV BLOCK CERAMIC SPRAY",
        "subtitle": "紫外线阻隔陶瓷喷雾 | 即喷即用 | 内饰防晒 | 快速护理",
        "tag": "☀️ 紫外线防护",
        "title": "UV BLOCK Ceramic Spray - DUMI AUTO | Instant UV Protection Spray for Car Interior & Exterior",
        "description": "DUMI UV BLOCK CERAMIC SPRAY provides instant UV protection for any surface — interior trim, dashboards, soft tops, and exterior paint. Spray on and wipe off for fast, effective UV blocking that prevents fading, cracking, and aging of car surfaces.",
        "keywords": "UV block spray, car UV protection spray, dashboard UV coating, interior UV spray, sun protection spray, dumi UV block, car care UV protection",
        "alt_visual": "DUMI UV BLOCK CERAMIC SPRAY being applied on car dashboard showing instant UV protection",
        "gradient": "linear-gradient(135deg,#3a2a1a,#6a4a2a,#4a3a1a)",
        "placeholder": "☀️ UV BLOCK SPRAY",
        "tag_color": "#6a4a2a",
        "features": [
            ("Instant Spray-On Application", "Simply spray and wipe — no professional skills required"),
            ("UVA & UVB Blocking", "Comprehensive UV spectrum protection prevents all types of sun damage"),
            ("Multi-Surface Compatible", "Works on plastic, vinyl, leather, rubber, and painted surfaces"),
            ("Quick-Dry Formula", "Cures in minutes, providing immediate protection"),
        ],
        "applications": ["Dashboard Protection", "Soft Top Protection", "Interior Trim", "Rubber Seals"],
        "related": ["hydrophobic-topcoat.html", "auto-ceramic-coating-spray.html", "anti-oxidation-coating.html"],
        "h1": "UV BLOCK CERAMIC SPRAY™",
        "h2_intro": "One Spray Blocks UV Damage — Fast Protection for Any Surface",
    },
    {
        "filename": "matte-surface-sealer.html",
        "name": "MATTE SURFACE SEALER",
        "subtitle": "哑光表面密封剂 | 哑光专用 | 保持哑光质感 | 防护+护理",
        "tag": "🎨 哑光护理",
        "title": "MATTE SURFACE SEALER - DUMI AUTO | Protective Sealant Designed for Matte PPF & Paint",
        "description": "DUMI MATTE SURFACE SEALER is specifically formulated for matte and satin finishes. Unlike glossy sealants that add shine, this product maintains the authentic matte look while providing water repellency, UV protection, and makes the surface easier to clean.",
        "keywords": "matte surface sealer, matte ppf sealant, satin paint sealant, matte car care, matte protection, dumi matte sealer, matte finish maintenance",
        "alt_visual": "DUMI MATTE SURFACE SEALER applied on matte PPF surface showing water beading without adding shine",
        "gradient": "linear-gradient(135deg,#2a2a2a,#4a4a4a,#3a3a3a)",
        "placeholder": "🎨 MATTE SEALER",
        "tag_color": "#3a3a3a",
        "features": [
            ("Matte-Specific Formula", "Engineered to protect matte surfaces WITHOUT adding gloss"),
            ("Maintains Original Look", "No shine, no wet-look — just authentic matte finish preservation"),
            ("Makes Cleaning Easier", "Hydrophobic properties help dirt and contamination release more easily"),
            ("UV Fade Protection", "Shields matte surface from UV-induced fading and discoloration"),
        ],
        "applications": ["Matte PPF Vehicles", "Satin Paint Finishes", "Matte Wrapped Vehicles", "Stealth Finishes"],
        "related": ["stealth-pro-ppf.html", "matte-satin-ppf.html", "hydrophobic-topcoat.html"],
        "h1": "MATTE SURFACE SEALER™",
        "h2_intro": "The Only Sealant That Preserves Matte — Without Adding Shine",
    },
    {
        "filename": "brake-disc-ceramic-coating.html",
        "name": "BRAKE DISC CERAMIC COATING",
        "subtitle": "刹车盘陶瓷镀晶 | 高温耐受 | 防锈防腐 | 制动性能提升",
        "tag": "🛑 刹车盘镀晶",
        "title": "BRAKE DISC CERAMIC Coating - DUMI AUTO | High-Temp Ceramic Coating for Brake Discs & Drums",
        "description": "DUMI BRAKE DISC CERAMIC COATING provides extreme temperature-resistant ceramic protection for brake discs and drums. Prevents rust, reduces brake dust adhesion, and can improve braking performance by maintaining cleaner braking surfaces. Essential for track cars and vehicles in winter climates.",
        "keywords": "brake disc ceramic coating, brake rotor coating, high temp ceramic coating, rust prevention brake, brake dust reduction, dumi brake disc coating, automotive ceramic coating",
        "alt_visual": "DUMI BRAKE DISC CERAMIC COATING applied on brake disc showing rust prevention and clean braking surface",
        "gradient": "linear-gradient(135deg,#2a1a1a,#5a2a2a,#3a1a1a)",
        "placeholder": "🛑 BRAKE DISC",
        "tag_color": "#5a2a2a",
        "features": [
            ("600°C Temperature Rated", "Ceramic matrix formulated to withstand extreme braking heat"),
            ("Prevents Surface Rust", "Stops flash rust on bare metal brake disc surfaces"),
            ("Reduces Brake Dust", "Ceramic coating makes it harder for brake dust to bond to surfaces"),
            ("Track-Day Ready", "Designed for high-heat track use without degrading"),
        ],
        "applications": ["Track Cars", "Winter Climate Vehicles", "Performance Cars", "Collector Vehicles"],
        "related": ["brake-caliper-ppf.html", "ceramic-pro-coating.html", "headlight-ceramic-coating.html"],
        "h1": "BRAKE DISC CERAMIC COATING™",
        "h2_intro": "Protect Your Brakes — High-Temp Ceramic for Disc & Drum",
    },
    {
        "filename": "ultra-gloss-defender-ppf.html",
        "name": "ULTRA GLOSS DEFENDER",
        "subtitle": "极致光泽保护膜 | 增亮30% | 高光漆面专用 | 原厂光泽",
        "tag": "✨ 极致光泽",
        "title": "ULTRA GLOSS DEFENDER PPF - DUMI AUTO | Maximum Gloss Enhancement Paint Protection Film",
        "description": "DUMI ULTRA GLOSS DEFENDER is our most optically clear PPF ever made. Formulated to enhance the natural gloss of your paint rather than mute it. Adds approximately 30% more visual gloss while providing the same rock-solid protection. The choice for true gloss enthusiasts.",
        "keywords": "ultra gloss ppf, high gloss paint protection, gloss enhancement ppf, show car ppf, maximum shine ppf, dumi ultra gloss, car paint protection",
        "alt_visual": "DUMI ULTRA GLOSS DEFENDER applied on sports car showing enhanced mirror-like glossy finish",
        "gradient": "linear-gradient(135deg,#1a1a2a,#2d2d5a,#1a1a3a)",
        "placeholder": "✨ ULTRA GLOSS",
        "tag_color": "#2d2d5a",
        "features": [
            ("30% More Gloss", "Proprietary formula enhances paint gloss rather than reducing it"),
            ("Optically Perfect Clarity", "Our clearest film ever — virtually zero optical distortion"),
            ("Self-Healing Topcoat", "Advanced nano-coating repairs minor scratches with heat"),
            ("Hydrophobic Surface", "Water and dirt shed easily, keeping that fresh-gloss look longer"),
        ],
        "applications": ["Show Cars", "Sports Cars", "Classic Cars", "Gloss Enthusiasts"],
        "related": ["ultimate-plus.html", "crystalline-ppf.html", "diamond-guard-ppf.html"],
        "h1": "ULTRA GLOSS DEFENDER™",
        "h2_intro": "Maximum Gloss Enhancement — Because Shine Matters",
    },
    {
        "filename": "military-grade-urethane-ppf.html",
        "name": "MILITARY GRADE URETHANE",
        "subtitle": "军事级聚氨酯PPF | 军用标准 | 最高防护等级 | 超级耐久",
        "tag": "🎖️ 军事级",
        "title": "MILITARY GRADE URETHANE PPF - DUMI AUTO | Defense-Grade Paint Protection Film",
        "description": "DUMI MILITARY GRADE URETHANE PPF uses materials originally developed for military vehicle armor applications. This is the same material used to protect military vehicles in hostile environments. If you want the absolute maximum protection available, this is it. Exceeds 8MIL military impact standards.",
        "keywords": "military grade ppf, defense ppf, armored vehicle ppf, heavy duty military film, military standard ppf, dumi military ppf, extreme protection film",
        "alt_visual": "DUMI MILITARY GRADE URETHANE PPF material showing extreme durability under stress test",
        "gradient": "linear-gradient(135deg,#0d1a0d,#1a2d1a,#0d1a0d)",
        "placeholder": "🎖️ MILITARY GRADE",
        "tag_color": "#1a2d1a",
        "features": [
            ("Military-Spec Materials", "Originally developed for defense and military vehicle applications"),
            ("Exceeds 8MIL Impact Standard", "Tested to military impact resistance specifications"),
            ("Chemical Agent Resistant", "Resistant to military-grade chemical agents and fuels"),
            ("Ballistic Fragment Mitigation", "Designed to mitigate ballistic fragments and debris impact"),
        ],
        "applications": ["High-Security Vehicles", "Armored Cars", "Military-Area Vehicles", "High-Threat Environments"],
        "related": ["storm-shield-ppf.html", "armor-ppf.html", "underbody-protective-film.html"],
        "h1": "MILITARY GRADE URETHANE™",
        "h2_intro": "Defense Technology for Civilian Vehicles — Military-Grade Protection",
    },
    {
        "filename": "prestige-clear-ceramic-tint.html",
        "name": "PRESTIGE CLEAR CERAMIC",
        "subtitle": " prestige 透明陶瓷窗膜 | 0%遮光 | 100%信号 | 极致清晰",
        "tag": "🔷 prestige 透明",
        "title": "PRESTIGE CLEAR CERAMIC Tint - DUMI AUTO | 0% VLT Crystal Clear Signal-Friendly Window Film",
        "description": "DUMI PRESTIGE CLEAR CERAMIC is our clearest window film — virtually invisible with 0% visible light absorption.享受陶瓷技术的热量阻隔，同时保持完全清晰，无任何色调。100%金属免费，无信号干扰。完美的车窗膜，如果你是谁不爱深色色调，但仍然希望热量和紫外线保护。",
        "keywords": "prestige clear ceramic tint, clear window film, 0% tint, signal friendly window film, clear heat rejection film, dumi prestige clear, car window film clear",
        "alt_visual": "DUMI PRESTIGE CLEAR CERAMIC tint showing completely clear window with no visible tint",
        "gradient": "linear-gradient(135deg,#1a3a4a,#2a5a7a,#1a4a6a)",
        "placeholder": "🔷 CLEAR CERAMIC",
        "tag_color": "#1a4a6a",
        "features": [
            ("0% VLT — Completely Clear", "Zero visible light absorption — looks like no film at all"),
            ("Ceramic Heat Rejection", "Still blocks 85% of infrared heat despite being crystal clear"),
            ("100% Signal Friendly", "No metal means GPS, phone, and radar detectors work perfectly"),
            ("UVA & UVB Blocking", "Blocks 99%+ of harmful UV rays protecting skin and interior"),
        ],
        "applications": ["Professional Drivers", "Fleet Vehicles", "Luxury Clear Tint Seekers", "Electric Vehicles"],
        "related": ["nano-ceramic-tint.html", "ceramic-tint.html", "pristine-ceramic-tint.html"],
        "h1": "PRESTIGE CLEAR CERAMIC™",
        "h2_intro": "Crystal Clear Protection — When You Want Heat Block Without Any Tint",
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
