#!/usr/bin/env python3
"""Generate 15 new SEO-optimized product pages for dumi-auto.com"""
import os

BASE_DIR = "/Users/carstauto/.openclaw/workspace/dumi-auto-website/products"

NEW_PRODUCTS = [
    {
        "filename": "stealth-pro-ppf.html",
        "name": "STEALTH PRO",
        "subtitle": "专业级哑光漆面保护膜 | 顶级自修复 | 工厂直供",
        "tag": "🖤 旗舰哑光",
        "title": "STEALTH PRO PPF - DUMI AUTO | Professional Matte Paint Protection Film",
        "description": "STEALTH PRO is the flagship matte PPF from DUMI AUTO. 9MIL thickness with enhanced self-healing coating, ultimate protection for matte and satin finishes. Factory direct pricing, professional installation available in Los Angeles and Sydney.",
        "keywords": "stealth ppf, matte ppf, satin ppf, paint protection film, car protection film, invisible car armor, dumi ppf, professional ppf",
        "alt_visual": "DUMI STEALTH PRO matte PPF applied on luxury sports car showing satin finish",
        "gradient": "linear-gradient(135deg,#1a1a1a,#2d2d2d,#1a1a1a)",
        "placeholder": "🖤 STEALTH PRO",
        "tag_color": "#1a1a1a",
        "features": [
            ("Professional 9MIL Thickness", "Heavy-duty base for maximum impact and scratch resistance"),
            ("Enhanced Self-Healing", "Advanced nano-coating repairs minor scratches on demand"),
            ("Satin/Matte Finish", "Unique non-glossy surface for a subtle, premium look"),
            ("Yellowing Resistant", "Premium TPU material stays clear and colorless over time"),
        ],
        "applications": ["Luxury Sedans", "Sports Cars", " matte-finish Vehicles", "Show Cars"],
        "related": ["stealth-ppf.html", "stealth-matte-black-ppf.html", "ultimate-plus.html"],
        "h1": "STEALTH PRO™",
        "h2_intro": "The Professional Choice for Matte Paint Protection",
    },
    {
        "filename": "ceramic-pro-coating.html",
        "name": "CERAMIC PRO",
        "subtitle": "专业级陶瓷镀晶 | 9H硬度 | 超疏水 | 3年持久",
        "tag": "🔷 陶瓷镀晶",
        "title": "CERAMIC PRO Coating - DUMI AUTO | Professional 9H Ceramic Coating for Cars",
        "description": "DUMI CERAMIC PRO is a professional-grade ceramic coating offering 9H hardness, super hydrophobic effect, and 3+ years of protection. The ultimate ceramic coating for automotive paint, glass, wheels, and trim. Factory direct.",
        "keywords": "ceramic coating, 9H ceramic coating, car ceramic coating, hydrophobic coating, car protection, paint sealant, dumi ceramic, automotive ceramic coating",
        "alt_visual": "DUMI CERAMIC PRO 9H ceramic coating applied on car hood showing water beading effect",
        "gradient": "linear-gradient(135deg,#1a2a3a,#2d4a6a,#1a3a5a)",
        "placeholder": "🔷 CERAMIC PRO",
        "tag_color": "#1a3a5a",
        "features": [
            ("9H Hardness", "Industry-leading hardness protects against scratches and swirl marks"),
            ("Super Hydrophobic", "Water beads off instantly, keeps car cleaner longer"),
            ("3+ Year Durability", "Long-lasting protection vs. traditional wax or sealants"),
            ("Multi-Surface Formula", "Safe on paint, glass, wheels, headlights, and plastic trim"),
        ],
        "applications": ["New Cars", "Show Cars", "Daily Drivers", "Marine Vehicles"],
        "related": ["diamond-ceramic-coating.html", "fusion-ceramic-coating.html", "graphene-coating.html"],
        "h1": "CERAMIC PRO™",
        "h2_intro": "Professional-Grade Ceramic Protection for Every Vehicle",
    },
    {
        "filename": "tpu-color-wrap.html",
        "name": "TPU COLOR WRAP",
        "subtitle": "TPU改色膜 | 透明+颜色双层结构 | 保护+美观兼顾",
        "tag": "🎨 TPU改色",
        "title": "TPU COLOR WRAP Film - DUMI AUTO | Premium TPU Color Change Film",
        "description": "DUMI TPU COLOR WRAP combines transparent TPU protective layer with colored surface. Get the best of both worlds — change your car's color while adding PPF-level paint protection. Available in 20+ colors. Factory direct pricing.",
        "keywords": "TPU color wrap, color change film, car wrap, color ppf, paint protection film color, car color change, dumi wrap, automotive color film",
        "alt_visual": "DUMI TPU COLOR WRAP film in midnight blue applied on sports car showing vibrant color and protection",
        "gradient": "linear-gradient(135deg,#1a1a3a,#2d2d5a,#1a1a3a)",
        "placeholder": "🎨 TPU COLOR",
        "tag_color": "#1a1a3a",
        "features": [
            ("TPU + Color Technology", "Dual-layer: transparent TPU protection + vibrant color surface"),
            ("Paint Protection", "Unlike vinyl wrap, TPU base protects from scratches and chips"),
            ("20+ Color Options", "Matte, gloss, and satin finishes in popular colors"),
            ("Removable & Reversible", "Change your look anytime without permanent modification"),
        ],
        "applications": ["Style-Conscious Owners", "Lease Vehicles", "Car Enthusiasts", "Fleet Vehicles"],
        "related": ["color-ppf.html", "ultimate-plus.html", "metallic-ppf.html"],
        "h1": "TPU COLOR WRAP™",
        "h2_intro": "The Smart Way to Change Color — With PPF-Level Protection",
    },
    {
        "filename": "nano-ceramic-tint.html",
        "name": "NANO CERAMIC TINT",
        "subtitle": "纳米陶瓷窗膜 | 非金属 | 信号无阻 | 极致清晰",
        "tag": "🪟 纳米陶瓷",
        "title": "NANO CERAMIC Window Tint - DUMI AUTO | Signal-Friendly Ceramic Tint Film",
        "description": "DUMI NANO CERAMIC window tint uses advanced nano-ceramic particles for superior heat rejection without any metal. 100% signal-friendly for GPS, phones, and radar detectors. Superior optical clarity for a safe driving experience.",
        "keywords": "nano ceramic tint, ceramic window film, signal friendly tint, car window tint, heat rejection window film, non-metallic tint, dumi ceramic tint",
        "alt_visual": "DUMI NANO CERAMIC window tint installed on luxury SUV showing crystal clear visibility",
        "gradient": "linear-gradient(135deg,#1a2a2a,#2d4a4a,#1a3a3a)",
        "placeholder": "🪟 NANO CERAMIC",
        "tag_color": "#1a3a3a",
        "features": [
            ("Nano-Ceramic Technology", "Advanced ceramic particles for maximum IR heat rejection"),
            ("100% Metal-Free", "No signal interference with GPS, phones, or electronic devices"),
            ("Superior Optical Clarity", "Crystal-clear visibility for safer nighttime and rainy driving"),
            ("UV Rejection", "Blocks 99%+ harmful UV rays protecting skin and interior"),
        ],
        "applications": ["Modern Vehicles", "Electric Vehicles", "Connected Cars", "Luxury Vehicles"],
        "related": ["ceramic-tint.html", "ceramic-ir-window-film.html", "prime-window-film.html"],
        "h1": "NANO CERAMIC TINT™",
        "h2_intro": "Signal-Friendly Ceramic Tint — No Metal, No Compromise",
    },
    {
        "filename": "xpel-ultimate-plus-plus.html",
        "name": "ULTIMATE PLUS+",
        "subtitle": "终极加强版PPF | 10MIL厚度 | 增强自修复 | 极限防护",
        "tag": "🛡️ 终极加强",
        "title": "ULTIMATE PLUS+ PPF - DUMI AUTO | 10MIL Heavy-Duty Paint Protection Film",
        "description": "ULTIMATE PLUS+ is DUMI's thickest, most protective PPF ever made. 10MIL thickness with enhanced self-healing topcoat provides the ultimate defense against rock chips, scratches, and road debris. For those who demand maximum protection.",
        "keywords": "ultimate plus ppf, heavy duty ppf, 10mil ppf, paint protection film, car protection film, rock chip protection, heavy duty paint film, dumi ppf",
        "alt_visual": "DUMI ULTIMATE PLUS+ 10MIL PPF installed on off-road truck showing maximum protection",
        "gradient": "linear-gradient(135deg,#0d1a2a,#1a2a3a,#0d1a2a)",
        "placeholder": "🛡️ ULTIMATE PLUS+",
        "tag_color": "#0d1a2a",
        "features": [
            ("10MIL Ultimate Thickness", "Thickest PPF available for maximum rock chip and impact protection"),
            ("Enhanced Self-Healing", "Improved topcoat formula repairs deeper and faster"),
            ("Extreme Clarity", "DUMI's clearest PPF yet — virtually invisible protection"),
            ("10-Year Warranty", "Backed by DUMI's comprehensive manufacturer warranty"),
        ],
        "applications": ["Off-Road Vehicles", "Heavy-Duty Trucks", "Highway Commuters", "Construction Vehicles"],
        "related": ["ultimate-plus.html", "armor-ppf.html", "stealth-pro-ppf.html"],
        "h1": "ULTIMATE PLUS+™",
        "h2_intro": "Our Thickest, Strongest PPF — Built for Ultimate Protection",
    },
    {
        "filename": "auto-ceramic-coating-spray.html",
        "name": "CERAMIC COATING SPRAY",
        "subtitle": "陶瓷镀晶喷雾 | DIY友好 | 即喷即用 | 快速镀晶",
        "tag": "✨ DIY陶瓷",
        "title": "Ceramic Coating Spray - DUMI AUTO | DIY Instant Ceramic Coating Spray-On Protection",
        "description": "DUMI Ceramic Coating Spray delivers professional-grade ceramic protection in an easy-to-apply spray formula. No professional skills needed — spray on, wipe off, and get 6+ months of hydrophobic ceramic protection at home.",
        "keywords": "ceramic coating spray, diy ceramic coating, spray on ceramic, quick ceramic coating, car ceramic spray, hydrophobic spray, dumi ceramic spray",
        "alt_visual": "DUMI Ceramic Coating Spray being applied on car hood at home showing water beading",
        "gradient": "linear-gradient(135deg,#1a3a2a,#2d5a3a,#1a4a3a)",
        "placeholder": "✨ CERAMIC SPRAY",
        "tag_color": "#1a4a3a",
        "features": [
            ("Spray-On Application", "Easy DIY application — no professional skills or equipment needed"),
            ("Hydrophobic Effect", "Water and dirt bead off, keeping your car cleaner longer"),
            ("6+ Month Protection", "Lasts 6+ months per application, far longer than traditional wax"),
            ("Multiple Surfaces", "Works on paint, glass, wheels, and plastic trim"),
        ],
        "applications": ["DIY Car Owners", "Car Enthusiasts", "Fleet Maintenance", "Quick Detailing"],
        "related": ["ceramic-pro-coating.html", "hydrophobic-topcoat.html", "nano-ceramic-coating-spray.html"],
        "h1": "CERAMIC COATING SPRAY™",
        "h2_intro": "Professional Ceramic Protection — At Home, In Minutes",
    },
    {
        "filename": "privacy-ceramic-tint.html",
        "name": "PRIVACY CERAMIC TINT",
        "subtitle": "陶瓷隐私窗膜 | 5%透光率 | 超级隐私 | 信号友好",
        "tag": "🔇 隐私窗膜",
        "title": "PRIVACY CERAMIC Window Tint - DUMI AUTO | Ceramic Privacy Tint Film 5% VLT",
        "description": "DUMI PRIVACY CERAMIC tint combines deep 5% VLT darkness with advanced ceramic technology. Maximum privacy and heat rejection without any signal interference. Perfect for executives, families, and anyone who values privacy.",
        "keywords": "privacy window tint, ceramic privacy tint, limo tint, 5% tint, car privacy film, privacy ceramic tint, dumi privacy tint",
        "alt_visual": "DUMI PRIVACY CERAMIC tint installed on executive SUV showing deep privacy darkening effect",
        "gradient": "linear-gradient(135deg,#0a0a1a,#1a1a2a,#0a0a1a)",
        "placeholder": "🔇 PRIVACY TINT",
        "tag_color": "#0a0a1a",
        "features": [
            ("5% VLT — Maximum Privacy", "Deep darkness provides maximum privacy for passengers and cargo"),
            ("Ceramic Heat Rejection", "Advanced ceramic particles block infrared heat effectively"),
            ("Zero Signal Interference", "100% metal-free formula — all electronics work perfectly"),
            ("UV Protection", "Blocks 99%+ UV rays, protecting skin and preventing interior fading"),
        ],
        "applications": ["Executive Vehicles", "Family SUVs", "Luxury Sedans", "Limo & Transport"],
        "related": ["platinum-privacy-tint.html", "ceramic-tint.html", "limo-black-film.html"],
        "h1": "PRIVACY CERAMIC TINT™",
        "h2_intro": "Maximum Privacy + Ceramic Technology — The Best of Both Worlds",
    },
    {
        "filename": "clear-matte-hybrid-ppf.html",
        "name": "CLEAR MATTE HYBRID",
        "subtitle": "清透哑光混合PPF | 半透明哑光 | 独特质感 | 保护+风格",
        "tag": "🎨 混合质感",
        "title": "CLEAR MATTE HYBRID PPF - DUMI AUTO | Semi-Matte Transparent Paint Protection Film",
        "description": "DUMI CLEAR MATTE HYBRID PPF is a unique semi-matte, semi-gloss finish that sits between traditional glossy PPF and full satin matte. A subtle premium look with full paint protection. Ideal for owners who want something different.",
        "keywords": "clear matte ppf, hybrid ppf, semi-matte ppf, satin gloss ppf, paint protection film, car protection film, unique ppf finish, dumi hybrid ppf",
        "alt_visual": "DUMI CLEAR MATTE HYBRID PPF applied on sports car showing unique semi-gloss satin finish",
        "gradient": "linear-gradient(135deg,#2a2a2a,#4a4a4a,#2a2a2a)",
        "placeholder": "🎨 CLEAR MATTE",
        "tag_color": "#2a2a2a",
        "features": [
            ("Unique Semi-Matte Finish", "One-of-a-kind look — neither full gloss nor full matte"),
            ("Full PPF Protection", "All the protection of traditional PPF in a unique aesthetic"),
            ("Self-Healing Topcoat", "Minor scratches disappear with heat or sunlight"),
            ("Yellowing Resistant", "Premium TPU maintains clarity and color stability"),
        ],
        "applications": ["Car Enthusiasts", "Luxury Vehicles", "Unique Style Seekers", "Show Cars"],
        "related": ["stealth-pro-ppf.html", "satin-matte-ppf.html", "ultimate-plus.html"],
        "h1": "CLEAR MATTE HYBRID™",
        "h2_intro": "The Unique In-Between Finish for the Discerning Owner",
    },
    {
        "filename": "infrared-heat-blocking-tint.html",
        "name": "IR HEAT BLOCK TINT",
        "subtitle": "红外线阻隔窗膜 | 95%红外阻隔 | 极致隔热 | 凉爽车内",
        "tag": "🌡️ 极致隔热",
        "title": "IR HEAT BLOCK Window Tint - DUMI AUTO | 95% Infrared Heat Rejection Window Film",
        "description": "DUMI IR HEAT BLOCK tint blocks up to 95% of infrared heat radiation, keeping your car significantly cooler in summer. Advanced multi-layer ceramic technology provides maximum heat rejection without dark tint required.",
        "keywords": "IR heat block tint, infrared window tint, heat rejection tint, ceramic heat tint, car cooling film, hot climate tint, dumi heat block",
        "alt_visual": "DUMI IR HEAT BLOCK window tint showing infrared heat being blocked from car interior",
        "gradient": "linear-gradient(135deg,#3a1a1a,#6a2a2a,#3a1a1a)",
        "placeholder": "🌡️ IR HEAT BLOCK",
        "tag_color": "#3a1a1a",
        "features": [
            ("95% IR Heat Rejection", "Blocks up to 95% of infrared heat — stay cool even in summer"),
            ("Light Tint Option", "Stay legal with lighter VLT while still blocking maximum heat"),
            ("Ceramic Multi-Layer", "Premium multi-layer ceramic construction for consistent performance"),
            ("Reduces AC Load", "Less heat inside means less work for your air conditioning"),
        ],
        "applications": ["Hot Climate Regions", "Daily Commuters", "Family Vehicles", "EVs"],
        "related": ["ceramic-ir-window-film.html", "solar-defense-film.html", "ceramic-matrix-tint.html"],
        "h1": "IR HEAT BLOCK TINT™",
        "h2_intro": "Block 95% of Infrared Heat — Stay Cool Without Dark Tint",
    },
    {
        "filename": "automotive-glass-coating.html",
        "name": "GLASS CERAMIC COATING",
        "subtitle": "玻璃陶瓷镀晶 | 挡风玻璃镀晶 | 疏水防雨 | 安全驾驶",
        "tag": "🪟 玻璃镀晶",
        "title": "Glass Ceramic Coating - DUMI AUTO | Windshield Ceramic Coating for Hydrophobic Protection",
        "description": "DUMI Glass Ceramic Coating creates a durable hydrophobic layer on all glass surfaces — windshield, side windows, and mirrors. Rain beads up and rolls off at speed, dramatically improving visibility and safety in wet weather.",
        "keywords": "glass ceramic coating, windshield coating, rain repellent coating, car glass coating, hydrophobic glass, water repellent windshield, dumi glass coating",
        "alt_visual": "DUMI Glass Ceramic Coating on car windshield showing water beading and rolling off at speed",
        "gradient": "linear-gradient(135deg,#1a3a4a,#2a5a7a,#1a4a6a)",
        "placeholder": "🪟 GLASS CERAMIC",
        "tag_color": "#1a4a6a",
        "features": [
            ("Hydrophobic Glass Protection", "Water beads and flies off at speed — no wiper needed in light rain"),
            ("Improved Safety", "Better wet-weather visibility means safer, more confident driving"),
            ("Easy Ice Removal", "Ice and frost don't stick — de-icing is quick and easy"),
            ("Durable Bond", "Lasts 1+ year per application, far outlasting spray-on alternatives"),
        ],
        "applications": ["Daily Drivers", "RVs and Caravans", "All-Weather Climates", "Fleet Vehicles"],
        "related": ["glass-ceramic-topcoat.html", "ceramic-pro-coating.html", "hydrophobic-topcoat.html"],
        "h1": "GLASS CERAMIC COATING™",
        "h2_intro": "See Clearly in the Rain — Hydrophobic Glass Protection for All Glass Surfaces",
    },
    {
        "filename": "exterior-matte-film.html",
        "name": "EXTERIOR MATTE FILM",
        "subtitle": "外饰哑光膜 | 外饰件专用 | 镜面/镀铬哑光化 | 改装风格",
        "tag": "🎨 外饰专用",
        "title": "EXTERIOR MATTE Film - DUMI AUTO | Matte Finish Film for Exterior Trim & Chrome Delete",
        "description": "DUMI EXTERIOR MATTE FILM is a premium cast vinyl film designed for exterior trim, mirror caps, and chrome delete applications. Transforms shiny chrome or plastic parts into a sleek matte finish. Easy to apply and removable without damage.",
        "keywords": "exterior matte film, chrome delete film, trim wrap, matte vinyl film, car chrome delete, exterior film, dumi exterior film, car styling film",
        "alt_visual": "DUMI EXTERIOR MATTE film applied on car mirror caps and trim showing sleek matte black finish",
        "gradient": "linear-gradient(135deg,#1a1a1a,#3a3a3a,#1a1a1a)",
        "placeholder": "🎨 EXTERIOR MATTE",
        "tag_color": "#1a1a1a",
        "features": [
            ("Premium Cast Vinyl", "High-quality 3M cast film for durability and conformal fit"),
            ("Chrome Delete Ready", "Transform chrome trim to sleek matte black instantly"),
            ("Air-Release Adhesive", "Bubble-free application even on curved surfaces"),
            ("Removable", "Cleanly removable without damaging underlying paint"),
        ],
        "applications": ["Chrome Delete Projects", "Trim Customization", "Show Car Prep", "Rental Fleets"],
        "related": ["chrome-delete-kit.html", "stealth-matte-black-ppf.html", "vinyl-wrap-premium-roll.html"],
        "h1": "EXTERIOR MATTE FILM™",
        "h2_intro": "Transform Chrome to Matte — The Quick Chrome Delete Solution",
    },
    {
        "filename": "headlight-ceramic-coating.html",
        "name": "HEADLIGHT CERAMIC COATING",
        "subtitle": "大灯陶瓷镀晶 | 防止黄化 | 持久清澈 | 提升照明",
        "tag": "💡 大灯专用",
        "title": "HEADLIGHT CERAMIC Coating - DUMI AUTO | UV Protection & Clarity for Headlights & Taillights",
        "description": "DUMI HEADLIGHT CERAMIC COATING provides long-lasting UV protection for headlights, taillights, and fog lights. Prevents yellowing, clouding, and oxidation while maintaining maximum light output and road visibility.",
        "keywords": "headlight ceramic coating, headlight protection, prevent headlight yellowing, taillight coating, UV headlight protection, car light coating, dumi headlight coating",
        "alt_visual": "DUMI HEADLIGHT CERAMIC COATING applied on car headlight showing crystal clear UV protection",
        "gradient": "linear-gradient(135deg,#2a2a1a,#5a5a2a,#3a3a1a)",
        "placeholder": "💡 HEADLIGHT CERAMIC",
        "tag_color": "#3a3a1a",
        "features": [
            ("UV Yellowing Prevention", "Blocks UV rays that cause headlights to cloud and yellow over time"),
            ("Crystal Clear Clarity", "Maintains maximum light transmission for optimal visibility"),
            ("Chemical Resistance", "Resists road salt, bugs, and acid rain damage"),
            ("Long-Lasting", "Durable ceramic bond outlasts traditional clear bras or sprays"),
        ],
        "applications": ["Aging Vehicles", "New Car Protection", "Show Cars", "Daily Commuters"],
        "related": ["headlight-protection.html", "crystal-glass-topcoat.html", "ceramic-pro-coating.html"],
        "h1": "HEADLIGHT CERAMIC COATING™",
        "h2_intro": "Keep Headlights Crystal Clear — Prevent Yellowing & Maintain Visibility",
    },
    {
        "filename": "commercial-vehicle-ppf.html",
        "name": "COMMERCIAL PPF",
        "subtitle": "商用车PPF | 车队保护 | 货车/卡车专用 | 降本增效",
        "tag": "🚛 商用车",
        "title": "COMMERCIAL PPF - DUMI AUTO | Paint Protection Film for Fleet & Commercial Vehicles",
        "description": "DUMI COMMERCIAL PPF is designed for commercial fleets, work trucks, and high-mileage commercial vehicles. Protects your fleet from rock chips, scratches, and weather damage — reducing repair costs and maintaining vehicle value.",
        "keywords": "commercial ppf, fleet ppf, truck ppf, commercial vehicle protection, fleet paint protection, work truck ppf, dumi commercial ppf",
        "alt_visual": "DUMI COMMERCIAL PPF applied on commercial delivery truck showing full-front protection coverage",
        "gradient": "linear-gradient(135deg,#1a2a1a,#2d4a2a,#1a3a1a)",
        "placeholder": "🚛 COMMERCIAL PPF",
        "tag_color": "#1a3a1a",
        "features": [
            ("Fleet Volume Pricing", "Special commercial pricing for volume PPF installations"),
            ("High-Impact Zones Covered", "Full-front kit protects against gravel, debris, and road damage"),
            ("Reduces Maintenance Costs", "Minimizes paint repair and touch-up needs across your fleet"),
            ("Professional Installation", "Certified DUMI installers available nationwide"),
        ],
        "applications": ["Delivery Fleets", "Construction Vehicles", "Service Trucks", "Commercial Vans"],
        "related": ["armor-ppf.html", "ultimate-plus.html", "exterior-protective-film.html"],
        "h1": "COMMERCIAL PPF™",
        "h2_intro": "Protect Your Fleet, Reduce Your Costs — PPF Built for Commercial Use",
    },
    {
        "filename": "solar-control-tint.html",
        "name": "SOLAR CONTROL TINT",
        "subtitle": "太阳控制窗膜 | 节能窗膜 | 降低油耗 | 环保驾驶",
        "tag": "☀️ 节能窗膜",
        "title": "SOLAR CONTROL Window Tint - DUMI AUTO | Energy-Saving Window Film for Cars",
        "description": "DUMI SOLAR CONTROL window tint reduces solar heat gain inside your vehicle, lowering cabin temperature and reducing air conditioning load. Saves fuel, keeps passengers cooler, and protects your car's interior from UV damage.",
        "keywords": "solar control tint, energy saving window film, car window tint, heat reduction tint, fuel saving tint, car cooling film, dumi solar tint",
        "alt_visual": "DUMI SOLAR CONTROL window tint reducing solar heat inside car with infrared thermal comparison",
        "gradient": "linear-gradient(135deg,#3a2a1a,#6a4a2a,#4a3a1a)",
        "placeholder": "☀️ SOLAR CONTROL",
        "tag_color": "#4a3a1a",
        "features": [
            ("Reduces Cabin Heat", "Keeps car significantly cooler in summer heat"),
            ("Lowers AC Fuel Impact", "Less air conditioning use means better fuel economy"),
            ("Interior UV Protection", "Prevents dashboard, seats, and trim from fading and cracking"),
            ("Legal VLT Options", "Available in a range of VLTs to meet state regulations"),
        ],
        "applications": ["Hot Climate Vehicles", "EV Owners", "Daily Commuters", "Family Vehicles"],
        "related": ["solar-defense-film.html", "ceramic-matrix-tint.html", "nano-ceramic-tint.html"],
        "h1": "SOLAR CONTROL TINT™",
        "h2_intro": "Stay Cool, Save Fuel, Protect Interior — Smart Solar Control Technology",
    },
    {
        "filename": "paint-restoration-coating.html",
        "name": "PAINT RESTORATION COATING",
        "subtitle": "车漆修复镀晶 | 旧车翻新 | 填平划痕 | 焕新光泽",
        "tag": "✨ 修复焕新",
        "title": "PAINT RESTORATION Coating - DUMI AUTO | Scratch-Filling Ceramic Coating for Older Vehicles",
        "description": "DUMI PAINT RESTORATION COATING uses advanced ceramic particles to fill minor scratches, swirl marks, and oxidation while providing long-lasting ceramic protection. Brings older vehicles back to life with a showroom-quality finish.",
        "keywords": "paint restoration coating, ceramic paint repair, scratch filling coating, car paint renewal, swirl mark removal, ceramic polish, dumi restoration coating",
        "alt_visual": "DUMI PAINT RESTORATION COATING applied on older car hood showing swirl marks removed and glossy finish restored",
        "gradient": "linear-gradient(135deg,#2a3a4a,#4a6a8a,#3a5a7a)",
        "placeholder": "✨ PAINT RESTORATION",
        "tag_color": "#3a5a7a",
        "features": [
            ("Scratch-Filling Technology", "Fills and conceals minor scratches and swirl marks"),
            ("Oxidation Reversal", "Helps restore faded and oxidized paint to original color"),
            ("Showroom Gloss", "Delivers a deep, wet-look gloss previously only seen at the detailer"),
            ("Ceramic Protection", "After filling, seals the surface with durable ceramic coating"),
        ],
        "applications": ["Older Vehicles", "Daily Drivers", "Collector Cars", "Neglected Paint"],
        "related": ["ceramic-pro-coating.html", "fusion-ceramic-coating.html", "graphene-coating.html"],
        "h1": "PAINT RESTORATION COATING™",
        "h2_intro": "Restore Your Paint's Glory — Fill Scratches, Renew Shine, Add Protection",
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
