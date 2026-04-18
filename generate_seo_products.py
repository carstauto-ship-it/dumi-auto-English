#!/usr/bin/env python3
"""DUMI AUTO - Generate 8 new SEO-optimized product pages"""
import os

BASE_DIR = "/Users/carstauto/.openclaw/workspace/dumi-auto-website/products"
CSS_LINK = "../css/style.css"

PRODUCTS = [
    {
        "filename": "gloss-black-ppf.html",
        "name": "GLOSS BLACK",
        "subtitle": "高光黑漆面保护膜 | 亮面质感 | 极致光泽",
        "tag": "🔥 高光",
        "title": "GLOSS BLACK - DUMI AUTO | XPEL高光黑漆面保护膜",
        "description": "XPEL GLOSS BLACK高光黑漆面保护膜，为您的车辆提供深邃亮面的黑色光泽，同时具备PPF顶级防护性能。抵抗碎石、虫子、酸雨，全方位保护原厂车漆。",
        "keywords": "XPEL GLOSS BLACK PPF, 高光黑漆面保护膜, 汽车PPF, 亮面保护膜, 黑色车漆保护, XPEL授权经销商",
        "alt_visual": "XPEL GLOSS BLACK高光黑PPF贴膜效果展示",
        "gradient": "linear-gradient(135deg,#0a0a0a,#1a1a1a,#2d2d2d)",
        "placeholder": "🖤 GLOSS",
        "tag_color": "#1a1a1a",
        "features": [
            ("深邃亮面光泽", "高光黑表面处理，光泽度极高，呈现豪华质感"),
            ("自修复涂层", "轻微划痕可自动修复，保持持久亮丽外观"),
            ("抗碎石冲击", "10mil厚度基材，有效抵御高速碎石冲击"),
            ("防化学腐蚀", "抵抗酸雨、虫子尸体、鸟粪等腐蚀性物质"),
        ],
        "applications": ["豪华轿车", "性能跑车", "黑色系车辆", "商务用车"],
        "related": ["ultimate-plus.html", "stealth-ppf.html", "armor-ppf.html"],
    },
    {
        "filename": "metallic-ppf.html",
        "name": "METALLIC PPF",
        "subtitle": "金属质感漆面保护膜 | 闪亮金属光泽 | 科技感十足",
        "tag": "✨ 金属",
        "title": "METALLIC PPF - DUMI AUTO | XPEL金属质感漆面保护膜",
        "description": "XPEL METALLIC金属质感漆面保护膜，融合PPF专业防护与时尚金属光泽，为您的爱车打造独特的科技感和运动气息。适合追求个性的车主。",
        "keywords": "XPEL METALLIC PPF, 金属质感保护膜, 汽车PPF, 闪亮车衣, 金属光泽车膜, XPEL改色膜",
        "alt_visual": "XPEL METALLIC金属质感PPF贴膜效果展示",
        "gradient": "linear-gradient(135deg,#4a4a4a,#7a7a7a,#c0c0c0,#7a7a7a,#4a4a4a)",
        "placeholder": "⚡ METALLIC",
        "tag_color": "#4a4a4a",
        "features": [
            ("金属闪亮光泽", "特殊金属质感处理，阳光下闪烁耀眼"),
            ("PPF专业防护", "不变黄、不开裂，10年持久如新"),
            ("自修复功能", "轻微划痕热修复，保持完美表面"),
            ("高透明度", "不影响原厂车漆颜色，裸妆感透明保护"),
        ],
        "applications": ["性能跑车", "改装车主", "SUV车型", "年轻化车型"],
        "related": ["ultimate-plus.html", "color-ppf.html", "gloss-black-ppf.html"],
    },
    {
        "filename": "security-film.html",
        "name": "SECURITY FILM",
        "subtitle": "安全防护窗膜 | 防爆防盗 | 3MIL-14MIL多规格",
        "tag": "🔒 安全",
        "title": "SECURITY FILM - DUMI AUTO | 汽车安全防爆窗膜",
        "description": "DUMI AUTO安全防护窗膜，高厚度防爆设计，有效防止玻璃破碎飞溅，保障车内人员安全。同时具备防盗功能，是商务用车和家庭用车的理想选择。",
        "keywords": "汽车安全窗膜, 防爆窗膜, 防盗窗膜, 安全膜, 窗膜防碎, 澳大利亚窗膜",
        "alt_visual": "DUMI AUTO安全防爆窗膜效果展示",
        "gradient": "linear-gradient(135deg,#1a2a3a,#2d4a5a,#1a3a4a)",
        "placeholder": "🔒 SECURITY",
        "tag_color": "#1a3a4a",
        "features": [
            ("防爆保护", "高厚度设计，玻璃破碎不飞溅，保护车内人员"),
            ("防盗功能", "增加破窗难度，有效延缓盗窃行为"),
            ("多规格选择", "3MIL至14MIL厚度，满足不同安全需求"),
            ("高透光率", "保持清晰视野，不影响行车安全"),
        ],
        "applications": ["商务用车", "家用轿车", "SUV", "特种车辆"],
        "related": ["prime-window-film.html", "ceramic-tint.html", "carbon-tint.html"],
    },
    {
        "filename": "carbon-tint.html",
        "name": "CARBON TINT",
        "subtitle": "碳纤维窗膜 | 运动风格 | 出色隔热 | 信号无干扰",
        "tag": "🏁 碳纤维",
        "title": "CARBON TINT - DUMI AUTO | XPEL碳纤维窗膜",
        "description": "XPEL CARBON碳纤维窗膜，采用先进碳粒子技术，提供极致运动风格外观与优秀隔热性能。不含金属成分，对手机信号、GPS完全无干扰。",
        "keywords": "XPEL CARBON窗膜, 碳纤维窗膜, 汽车窗膜, 隔热窗膜, 信号无干扰窗膜, 运动风格窗膜",
        "alt_visual": "XPEL CARBON碳纤维窗膜贴膜效果展示",
        "gradient": "linear-gradient(135deg,#1a1a1a,#2d2d2d,#3a3a3a,#1a1a1a)",
        "placeholder": "🏁 CARBON",
        "tag_color": "#2d2d2d",
        "features": [
            ("碳粒子技术", "先进碳粒子分散，非金属，不干扰电子信号"),
            ("运动外观", "深邃碳纤维质感，提升车辆运动气息"),
            ("优秀隔热", "阻隔红外线热量，降低车内温度"),
            ("防紫外线", "阻隔99%以上紫外线，保护皮肤和内饰"),
        ],
        "applications": ["性能跑车", "运动轿车", "改装车主", "年轻用户"],
        "related": ["ceramic-tint.html", "prime-window-film.html", "security-film.html"],
    },
    {
        "filename": "satin-matte-ppf.html",
        "name": "SATIN MATTE",
        "subtitle": "绸缎哑光漆面保护膜 | 丝滑触感 | 低调奢华",
        "tag": "🪶 绸缎",
        "title": "SATIN MATTE - DUMI AUTO | XPEL绸缎哑光漆面保护膜",
        "description": "XPEL SATIN MATTE绸缎哑光漆面保护膜，介于亮面与完全哑光之间独特的绸缎质感，低调奢华又不失个性。适合追求独特品味的车主。",
        "keywords": "XPEL SATIN MATTE, 绸缎哑光PPF, 哑光车衣, 汽车保护膜, 奢华哑光, 悉尼PPF",
        "alt_visual": "XPEL SATIN MATTE绸缎哑光PPF效果展示",
        "gradient": "linear-gradient(135deg,#8a8a8a,#b0b0b0,#d0d0d0,#b0b0b0,#8a8a8a)",
        "placeholder": "🪶 SATIN",
        "tag_color": "#6a6a6a",
        "features": [
            ("绸缎哑光质感", "独特丝滑触感，非亮面非哑光，品味独特"),
            ("自修复涂层", "轻微划痕可热修复，表面持久如新"),
            ("抗污易清洁", "表面光滑，污渍不易附着，清洁简便"),
            ("十年质保", "不变黄、不开裂，官方10年质保"),
        ],
        "applications": ["豪华轿车", "行政用车", "个性车主", "收藏级车辆"],
        "related": ["stealth-ppf.html", "gloss-black-ppf.html", "ultimate-plus.html"],
    },
    {
        "filename": "graphene-coating.html",
        "name": "GRAPHENE COATING",
        "subtitle": "石墨烯镀晶 | 顶级疏水 | 极致硬度 | 耐高温",
        "tag": "⚡ 科技",
        "title": "GRAPHENE COATING - DUMI AUTO | 石墨烯汽车镀晶",
        "description": "DUMI AUTO石墨烯镀晶，采用革命性石墨烯技术，为车漆提供顶级疏水性、极高硬度和优异耐高温性能。单次施工，长效保护，是PPF之外的另一高端选择。",
        "keywords": "石墨烯镀晶, 汽车镀晶, 疏水镀晶, 车漆保护, 高硬度车衣, 洛杉矶镀晶",
        "alt_visual": "DUMI AUTO石墨烯镀晶效果展示",
        "gradient": "linear-gradient(135deg,#0f2027,#203a43,#2c5364)",
        "placeholder": "⚡ GRAPHENE",
        "tag_color": "#203a43",
        "features": [
            ("石墨烯技术", "新型碳材料，超高导热性，散热均匀迅速"),
            ("顶级疏水性", "水珠滚落效果显著，减少水渍水痕"),
            ("高硬度保护", "9H硬度，有效抵抗细微划痕"),
            ("耐高温抗老化", "石墨烯耐高温特性，长期使用不分解"),
        ],
        "applications": ["超级跑车", "日常代步车", "户外停放车辆", "高温地区车辆"],
        "related": ["ultimate-plus.html", "armor-ppf.html", "ceramic-tint.html"],
    },
    {
        "filename": "uv-protection-film.html",
        "name": "UV PROTECTION FILM",
        "subtitle": "防紫外线窗膜 | 阻隔99%紫外线 | 护肤级防护",
        "tag": "☀️ 防晒",
        "title": "UV PROTECTION FILM - DUMI AUTO | 汽车防紫外线窗膜",
        "description": "DUMI AUTO防紫外线窗膜，特殊UV涂层阻隔99%以上有害紫外线，有效保护车内人员皮肤健康，减缓内饰老化褪色。适合长期驾驶和注重健康的车主。",
        "keywords": "防紫外线窗膜, UV防护窗膜, 汽车防晒膜, 护肤窗膜, 阻隔紫外线窗膜, 洛杉矶窗膜",
        "alt_visual": "DUMI AUTO防紫外线窗膜效果展示",
        "gradient": "linear-gradient(135deg,#ff8c00,#ff4500,#ff6b35,#ffd700)",
        "placeholder": "☀️ UV FILTER",
        "tag_color": "#ff6b35",
        "features": [
            ("99%紫外线阻隔", "医疗级UV防护，保护皮肤，预防晒伤"),
            ("减缓内饰老化", "防止仪表台、座椅褪色，延长内饰寿命"),
            ("清晰透明", "高透光率，不影响视野和夜间行车"),
            ("健康驾驶", "降低车内紫外线暴露，适合长途驾驶"),
        ],
        "applications": ["女性车主", "儿童乘坐车辆", "长途驾驶", "敞篷车"],
        "related": ["ceramic-tint.html", "prime-window-film.html", "carbon-tint.html"],
    },
    {
        "filename": "crystalline-ppf.html",
        "name": "CRYSTALLINE PPF",
        "subtitle": "冰晶系列漆面保护膜 | 剔透如冰 | 极高透明度",
        "tag": "💎 冰晶",
        "title": "CRYSTALLINE - DUMI AUTO | XPEL冰晶系列漆面保护膜",
        "description": "XPEL CRYSTALLINE冰晶系列漆面保护膜，极高透明度设计，贴附后几乎与原厂车漆无异，为车漆提供隐形盔甲般的顶级保护。适合注重原厂状态的车主。",
        "keywords": "XPEL CRYSTALLINE, 冰晶PPF, 透明保护膜, 隐形车衣, 高透明PPF, 悉尼XPEL",
        "alt_visual": "XPEL CRYSTALLINE冰晶PPF效果展示",
        "gradient": "linear-gradient(135deg,#e0f7fa,#b2ebf2,#80deea,#e0f7fa)",
        "placeholder": "💎 CRYSTAL",
        "tag_color": "#00838f",
        "features": [
            ("极高透明度", "光学级透明度，贴附后与原厂车漆无异"),
            ("隐形保护", "如同隐形盔甲，看不见却时刻保护"),
            ("自修复功能", "轻微划痕自动修复，表面持久完美"),
            ("抗污自洁", "表面光滑，灰尘污渍不易附着"),
        ],
        "applications": ["豪华轿车", "超跑车主", "原厂车漆保护", "收藏级车辆"],
        "related": ["ultimate-plus.html", "gloss-black-ppf.html", "satin-matte-ppf.html"],
    },
]

RELATED_PRODUCTS_MAP = {
    "ultimate-plus.html": ("🔥 热销", "ULTIMATE PLUS", "旗舰级漆面保护膜"),
    "stealth-ppf.html": ("🪶 哑光", "STEALTH", "原厂哑光质感"),
    "gloss-black-ppf.html": ("🖤 高光", "GLOSS BLACK", "高光黑漆面保护膜"),
    "armor-ppf.html": ("🛡️ 重度", "ARMOR", "重度防护漆面保护膜"),
    "color-ppf.html": ("🎨 改色", "COLOR PPF", "彩色漆面保护膜"),
    "ceramic-tint.html": ("🪟 陶瓷", "CERAMIC窗膜", "高端陶瓷窗膜"),
    "prime-window-film.html": ("🪟 窗膜", "PRIME窗膜", "陶瓷纳米窗膜"),
    "security-film.html": ("🔒 安全", "SECURITY窗膜", "防爆安全窗膜"),
    "carbon-tint.html": ("🏁 碳纤维", "CARBON窗膜", "运动风格窗膜"),
    "satin-matte-ppf.html": ("🪶 绸缎", "SATIN MATTE", "绸缎哑光PPF"),
    "graphene-coating.html": ("⚡ 科技", "GRAPHENE镀晶", "石墨烯镀晶"),
    "uv-protection-film.html": ("☀️ 防晒", "UV窗膜", "防紫外线窗膜"),
    "crystalline-ppf.html": ("💎 冰晶", "CRYSTALLINE", "冰晶系列PPF"),
}

def get_related_html(related_files):
    html = '<div class="products-grid">\n'
    for fname in related_files:
        if fname in RELATED_PRODUCTS_MAP:
            tag, name, desc = RELATED_PRODUCTS_MAP[fname]
            fname_escaped = fname.replace("-", " ").replace(".html", "").upper()
            gradient = "#1a1a2e" if "PPF" in fname or fname in ["ultimate-plus.html", "stealth-ppf.html"] else "#0f3460"
            if "COLOR" in name.upper() or "改色" in desc:
                gradient = "#8B0000"
            if "STEALTH" in name.upper():
                gradient = "#2c2c2c"
            if "ARMOR" in name.upper():
                gradient = "#1a3a3a"
            if "CERAMIC" in name.upper():
                gradient = "#1a3a5c"
            if "SATIN" in name.upper():
                gradient = "#6a6a6a"
            if "GRAPHENE" in name.upper():
                gradient = "#0f2027"
            if "UV" in name.upper():
                gradient = "#ff6b35"
            if "CRYSTAL" in name.upper():
                gradient = "#00838f"
            if "SECURITY" in name.upper():
                gradient = "#1a3a4a"
            if "CARBON" in name.upper():
                gradient = "#2d2d2d"
            html += f'''                <a href="{fname}" class="product-card">
                    <div class="product-img" style="background: linear-gradient(135deg,{gradient},#{gradient[1:]}ee);">
                        <div class="product-placeholder">{tag.split()[1] if len(tag.split()) > 1 else tag}</div>
                    </div>
                    <div class="product-info">
                        <span class="product-tag">{tag.split()[0]}</span>
                        <h3>{name}</h3>
                        <p>{desc}</p>
                        <span class="product-price">了解详情 →</span>
                    </div>
                </a>\n'''
    html += '            </div>'
    return html

def get_app_tags(applications):
    return "".join(f'<span>{app}</span>' for app in applications)

def generate_product_page(p):
    features_html = ""
    for title, desc in p["features"]:
        features_html += f'''
                        <div class="product-feature-item">
                            <span class="feature-icon">✓</span>
                            <div><strong>{title}</strong><p>{desc}</p></div>
                        </div>
        '''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p["title"]}</title>
    <meta name="description" content="{p["description"]}">
    <meta name="keywords" content="{p["keywords"]}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{p["title"]}">
    <meta property="og:description" content="{p["description"]}">
    <meta property="og:type" content="product">
    <link rel="canonical" href="https://dumi-panel.com/products/{p["filename"]}">
    <link rel="stylesheet" href="{CSS_LINK}">
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="logo"><h1>DUMI<span>AUTO</span></h1><p>专业汽车保护膜专家</p></div>
            <nav class="nav"><a href="../index.html">首页</a><a href="../index.html#products">产品中心</a><a href="../index.html#services">服务项目</a><a href="../index.html#about">关于我们</a><a href="../index.html#contact">联系我们</a></nav>
            <div class="header-cta"><a href="../index.html#contact" class="btn-primary">立即预约</a></div>
        </div>
    </header>
    <section class="product-detail">
        <div class="container">
            <div class="breadcrumb"><a href="../index.html">首页</a> / <a href="../index.html#products">产品中心</a> / {p["name"]}</div>
            <div class="product-detail-grid">
                <div class="product-detail-img">
                    <div class="product-detail-visual" style="background: {p["gradient"]};">
                        <img src="../images/{p["filename"].replace(".html","")}.jpg" alt="{p["alt_visual"]}" style="width:100%;height:100%;object-fit:cover;border-radius:12px;" onerror="this.style.display='none';this.parentElement.innerHTML='<div style=\\'display:flex;align-items:center;justify-content:center;height:100%;font-size:48px;color:rgba(255,255,255,0.15);\\'>{p["placeholder"]}</div>'">
                    </div>
                </div>
                <div class="product-detail-info">
                    <div class="product-detail-tag" style="background:{p["tag_color"]};">{p["tag"]}</div>
                    <h1>{p["name"]}™</h1>
                    <p class="product-subtitle">{p["subtitle"]}</p>
                    <div class="product-detail-desc">
                        <p>{p["description"]}</p>
                    </div>
                    <div class="product-features">
                        <h3 style="font-size:16px;font-weight:700;color:#1a1a2e;margin-bottom:15px;">产品特点</h3>
                        {features_html}
                    </div>
                    <div class="product-applications">
                        <h3>适用场景</h3>
                        <div class="application-tags">{get_app_tags(p["applications"])}</div>
                    </div>
                    <div class="product-cta">
                        <a href="../index.html#contact" class="btn-primary">获取报价 →</a>
                        <a href="../index.html#products" class="btn-outline">查看更多产品</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="related-products">
        <div class="container">
            <div class="section-header"><h2>相关产品</h2></div>
            {get_related_html(p["related"])}
        </div>
    </section>
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand"><h2>DUMI<span>AUTO</span></h2><p>专业汽车保护膜专家 · XPEL授权经销商</p></div>
                <div class="footer-links"><h4>产品分类</h4><a href="ultimate-plus.html">漆面保护膜 PPF</a><a href="prime-window-film.html">窗膜系列</a><a href="stealth-ppf.html">STEALTH哑光膜</a><a href="color-ppf.html">COLOR改色膜</a></div>
                <div class="footer-links"><h4>快速链接</h4><a href="../index.html">首页</a><a href="../index.html#contact">联系我们</a></div>
                <div class="footer-contact"><h4>联系方式</h4><p>📧 carstauto2010@gmail.com</p><p>📱 +86-13001727017</p><p>📱 +61-493342108</p></div>
            </div>
            <div class="footer-bottom"><p>© 2024 DUMI AUTO. All rights reserved. | XPEL Authorized Dealer</p></div>
        </div>
    </footer>
    <style>
        .breadcrumb {{ padding: 20px 0; font-size: 13px; color: #999; }}
        .product-detail {{ padding: 20px 0 60px; }}
        .product-detail-grid {{ display: grid; grid-template-columns: 1fr 1.2fr; gap: 50px; align-items: start; }}
        .product-detail-visual {{ height: 450px; border-radius: 12px; display: flex; align-items: center; justify-content: center; overflow: hidden; }}
        .product-detail-tag {{ display: inline-block; color: white; padding: 4px 12px; border-radius: 4px; font-size: 12px; font-weight: 600; margin-bottom: 15px; }}
        .product-detail-info h1 {{ font-size: 42px; font-weight: 800; color: #1a1a2e; margin-bottom: 10px; letter-spacing: 2px; }}
        .product-subtitle {{ font-size: 16px; color: #888; margin-bottom: 25px; }}
        .product-detail-desc {{ background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 25px; border-left: 4px solid {p["tag_color"]}; }}
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
</html>
'''
    return html

for p in PRODUCTS:
    filepath = os.path.join(BASE_DIR, p["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(generate_product_page(p))
    print(f"✅ Created: {p['filename']}")

print(f"\n🎉 Total {len(PRODUCTS)} product pages generated!")
