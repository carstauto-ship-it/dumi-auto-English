#!/usr/bin/env python3
"""DUMI AUTO - Generate 20 new SEO-optimized product pages (Batch 2026-04-24)"""
import os
import json

BASE_DIR = "/Users/carstauto/.openclaw/workspace/dumi-auto-website/products"
CSS_LINK = "../css/style.css"

PRODUCTS = [
    # ========== PPF 1-8 ==========
    {
        "filename": "hydro-ceramic-ppf.html",
        "name": "HYDRO CERAMIC PPF",
        "subtitle": "水凝陶瓷漆面保护膜 | 极致自修复 | 亲水疏水双效",
        "tag": "🧪 水凝",
        "title": "HYDRO CERAMIC PPF - DUMI AUTO | XPEL水凝陶瓷漆面保护膜",
        "description": "XPEL HYDRO CERAMIC水凝陶瓷漆面保护膜，融合先进水凝技术与纳米陶瓷涂层，提供顶级自修复与疏水双重功效。抵抗碎石、虫子、酸雨，同时让水珠轻松滚落，保持车身持久洁净。适合追求完美体验的车主。",
        "keywords": "XPEL HYDRO CERAMIC PPF, 水凝陶瓷车衣, 自修复PPF, 疏水车衣, 汽车保护膜, 悉尼PPF",
        "alt_visual": "XPEL HYDRO CERAMIC水凝陶瓷PPF效果展示",
        "gradient": "linear-gradient(135deg,#00bcd4,#00838f,#006064,#00bcd4)",
        "placeholder": "💧 HYDRO",
        "tag_color": "#00838f",
        "features": [
            ("水凝自修复技术", "先进水凝胶涂层，轻微划痕遇水快速自修复"),
            ("双效疏水", "亲水与疏水双重特性，雨水冲刷即洁净"),
            ("10mil军工级基材", "顶级TPU基材，高强度抗冲击"),
            ("防化学腐蚀", "抵抗酸雨、虫子、鸟粪，持久如新"),
        ],
        "applications": ["豪华轿车", "超跑车主", "户外停车", "城市通勤"],
        "related": ["ultimate-plus.html", "ceramic-tint.html", "nano-ceramic-ppf.html"],
    },
    {
        "filename": "ultra-gloss-warm-ppf.html",
        "name": "ULTRA GLOSS WARM",
        "subtitle": "温润光泽漆面保护膜 | 暖调光泽 | 自然质感",
        "tag": "🌟 温润",
        "title": "ULTRA GLOSS WARM - DUMI AUTO | 温润光泽漆面保护膜",
        "description": "DUMI AUTO ULTRA GLOSS WARM温润光泽漆面保护膜，专为亚洲车漆颜色调校的光泽处理，呈现温润自然的暖调光泽。不是冷白刺眼，而是恰到好处的温润质感，深受华人车主喜爱。",
        "keywords": "温润光泽PPF, 暖色车衣, 高光保护膜, 亚洲车漆专用, 汽车PPF, 洛杉矶PPF",
        "alt_visual": "ULTRA GLOSS WARM温润光泽PPF贴膜效果",
        "gradient": "linear-gradient(135deg,#b87333,#d4a017,#f0c040,#d4a017,#b87333)",
        "placeholder": "🌟 WARM",
        "tag_color": "#b87333",
        "features": [
            ("温润暖调光泽", "专为亚洲车漆设计，不是冷白而是自然温润"),
            ("高透光自修复", "透明度高，不改变原厂色泽同时保护车漆"),
            ("抗污自洁", "表面光滑，污渍不易附着，清洗简便"),
            ("5年安心质保", "官方5年质保，放心使用"),
        ],
        "applications": ["豪华轿车", "家用SUV", "华人车主", "户外停放车辆"],
        "related": ["ultimate-plus.html", "gloss-black-ppf.html", "crystalline-ppf.html"],
    },
    {
        "filename": "silk-ceramic-ppf.html",
        "name": "SILK CERAMIC PPF",
        "subtitle": "丝绸陶瓷漆面保护膜 | 丝滑触感 | 陶瓷硬度",
        "tag": "🧵 丝绸",
        "title": "SILK CERAMIC PPF - DUMI AUTO | 丝绸陶瓷漆面保护膜",
        "description": "DUMI AUTO SILK CERAMIC丝绸陶瓷漆面保护膜，结合丝绸般柔滑触感与陶瓷超高硬度，为车漆提供如丝绸掠过般的极致手感与金刚石级的硬度保护。自修复与高硬度完美融合。",
        "keywords": "丝绸陶瓷PPF, 丝滑车衣, 陶瓷硬度PPF, 汽车保护膜, 高硬度车衣, 悉尼PPF",
        "alt_visual": "SILK CERAMIC丝绸陶瓷PPF效果展示",
        "gradient": "linear-gradient(135deg,#f5f5f5,#e8e8e8,#dcdcdc,#e8e8e8,#f5f5f5)",
        "placeholder": "🧵 SILK",
        "tag_color": "#9e9e9e",
        "features": [
            ("丝绸般柔滑触感", "表面处理如丝绸般细腻，触感无与伦比"),
            ("9H陶瓷硬度", "表面硬度达9H，有效抵抗划痕与砂石"),
            ("自修复涂层", "轻微划痕热修复，保持表面完美"),
            ("十年质保不变黄", "顶级TPU+陶瓷，十年不发黄"),
        ],
        "applications": ["豪华轿车", "超跑", "收藏级车辆", "高端车主"],
        "related": ["satin-matte-ppf.html", "crystalline-ppf.html", "ultimate-plus.html"],
    },
    {
        "filename": "matte-protective-ppf.html",
        "name": "MATTE PROTECTIVE PPF",
        "subtitle": "哑光防护漆面保护膜 | 哑光质感 | 全方位防护",
        "tag": "🔘 哑光",
        "title": "MATTE PROTECTIVE PPF - DUMI AUTO | 哑光防护漆面保护膜",
        "description": "DUMI AUTO MATTE PROTECTIVE哑光防护漆面保护膜，为哑光车漆提供专业级保护。保持哑光质感的同时，有效防止碎石、划痕、紫外线对原厂车漆的伤害。适合哑光改装车主与原厂哑光车型。",
        "keywords": "哑光保护膜, 哑光PPF, 消光保护, 汽车哑光车衣, 悉尼PPF, XPEL哑光",
        "alt_visual": "MATTE PROTECTIVE哑光PPF效果展示",
        "gradient": "linear-gradient(135deg,#4a4a4a,#6a6a6a,#8a8a8a,#6a6a6a,#4a4a4a)",
        "placeholder": "🔘 MATTE",
        "tag_color": "#5a5a5a",
        "features": [
            ("原厂哑光质感", "贴附后保持完美哑光效果，不改变原厂质感"),
            ("抗碎石冲击", "8mil厚度，优异抗冲击性能"),
            ("防化学腐蚀", "抵抗酸雨、虫子、鸟粪等腐蚀性物质"),
            ("自修复功能", "轻微划痕热修复，哑光表面持久如新"),
        ],
        "applications": ["哑光改装车", "原厂哑光车型", "商务哑光轿车", "越野车型"],
        "related": ["stealth-ppf.html", "matte-satin-ppf.html", "armor-ppf.html"],
    },
    {
        "filename": "pearl-white-ppf.html",
        "name": "PEARL WHITE PPF",
        "subtitle": "珍珠白漆面保护膜 | 珠光质感 | 典雅尊贵",
        "tag": "🌈 珍珠",
        "title": "PEARL WHITE PPF - DUMI AUTO | 珍珠白漆面保护膜",
        "description": "DUMI AUTO PEARL WHITE珍珠白漆面保护膜，为白色车辆提供温润的珍珠光泽效果。不是单调的纯白，而是带有微妙珍珠闪光的典雅白。保护车漆的同时提升整车的质感与品位。",
        "keywords": "珍珠白PPF, 白色车衣, 珠光保护膜, 汽车PPF, 悉尼PPF, 白色车漆保护",
        "alt_visual": "PEARL WHITE珍珠白PPF效果展示",
        "gradient": "linear-gradient(135deg,#ffffff,#f8f8ff,#e6e6fa,#f0f8ff,#ffffff)",
        "placeholder": "🌈 PEARL",
        "tag_color": "#b0c4de",
        "features": [
            ("珍珠光泽效果", "添加珠光因子，白色车漆呈现温润光泽"),
            ("有效防护", "防止浅划痕、太阳纹、氧化等常见问题"),
            ("抗污易清洁", "表面光滑，污渍不易附着，清水冲洗即可"),
            ("提升 resale 价值", "保护原厂车漆，二手车价值更高"),
        ],
        "applications": ["白色轿车", "白色SUV", "豪华白色车型", "家用代步车"],
        "related": ["ultimate-plus.html", "crystalline-ppf.html", "gloss-black-ppf.html"],
    },
    {
        "filename": "midnight-blue-ppf.html",
        "name": "MIDNIGHT BLUE PPF",
        "subtitle": "午夜蓝漆面保护膜 | 深邃神秘 | 蓝色光泽",
        "tag": "🌌 午夜",
        "title": "MIDNIGHT BLUE PPF - DUMI AUTO | 午夜蓝漆面保护膜",
        "description": "DUMI AUTO MIDNIGHT BLUE午夜蓝漆面保护膜，为深蓝色系车辆提供深邃神秘的视觉体验。在光源下呈现蓝色金属光泽，在暗处则保持神秘深邃的视觉效果。是蓝色车主的首选保护方案。",
        "keywords": "午夜蓝PPF, 深蓝车衣, 蓝色保护膜, 汽车PPF, 悉尼PPF, 蓝色车漆保护",
        "alt_visual": "MIDNIGHT BLUE午夜蓝PPF效果展示",
        "gradient": "linear-gradient(135deg,#000080,#0000cd,#191970,#0000cd,#000080)",
        "placeholder": "🌌 MIDNIGHT",
        "tag_color": "#000080",
        "features": [
            ("深邃蓝色光泽", "特殊调色，深夜中透着蓝色金属光"),
            ("TPU顶级防护", "10mil厚度，顶级TPU基材"),
            ("自修复涂层", "轻微划痕自动修复，保持完美外观"),
            ("抗紫外线", "阻隔紫外线，防止车漆褪色老化"),
        ],
        "applications": ["深蓝色车辆", "性能轿车", "改装车主", "个性化车型"],
        "related": ["ultimate-plus.html", "metallic-ppf.html", "color-ppf.html"],
    },
    {
        "filename": "urban-shield-ppf.html",
        "name": "URBAN SHIELD PPF",
        "subtitle": "都市护盾漆面保护膜 | 城市通勤首选 | 日常防护",
        "tag": "🏙️ 都市",
        "title": "URBAN SHIELD PPF - DUMI AUTO | 都市护盾漆面保护膜",
        "description": "DUMI AUTO URBAN SHIELD都市护盾漆面保护膜，专为城市日常通勤设计的高性价比PPF产品。有效抵御城市环境中的树枝刮擦、垃圾堆积、轻微碰撞，是城市车主的经济实惠之选。",
        "keywords": "都市护盾PPF, 城市车衣, 通勤PPF, 经济实惠PPF, 汽车保护膜, 悉尼PPF",
        "alt_visual": "URBAN SHIELD都市护盾PPF效果展示",
        "gradient": "linear-gradient(135deg,#2c3e50,#34495e,#2c3e50)",
        "placeholder": "🏙️ URBAN",
        "tag_color": "#34495e",
        "features": [
            ("城市日常防护", "针对城市环境优化，树枝、垃圾、小刮蹭统统防护"),
            ("高性价比", "合理价格，优质防护，城市通勤首选"),
            ("自修复功能", "轻微划痕热修复，保持表面如新"),
            ("简易维护", "普通清洁即可，无需特殊护理"),
        ],
        "applications": ["城市通勤车", "家用轿车", "新手车主", "租车公司"],
        "related": ["armor-ppf.html", "ultimate-plus.html", "clear-protective-tint.html"],
    },
    {
        "filename": "exotic-cherry-red-ppf.html",
        "name": "EXOTIC CHERRY RED PPF",
        "subtitle": "烈焰樱桃红漆面保护膜 | 激情红色 | 超高饱和",
        "tag": "🔥 烈焰",
        "title": "EXOTIC CHERRY RED PPF - DUMI AUTO | 烈焰樱桃红漆面保护膜",
        "description": "DUMI AUTO EXOTIC CHERRY RED烈焰樱桃红漆面保护膜，专为红色系车辆设计的超高饱和度色彩保护膜。提升原厂红色的艳丽度，同时提供专业级PPF防护，让您的红色座驾成为街头焦点。",
        "keywords": "烈焰樱桃红PPF, 红色车衣, 超红保护膜, 汽车PPF, 悉尼PPF, 红色车漆保护",
        "alt_visual": "EXOTIC CHERRY RED烈焰红PPF效果展示",
        "gradient": "linear-gradient(135deg,#8b0000,#dc143c,#ff4500,#dc143c,#8b0000)",
        "placeholder": "🔥 CHERRY",
        "tag_color": "#dc143c",
        "features": [
            ("超高饱和红色", "增强原厂红色，呈现烈焰般的艳丽效果"),
            ("色彩保护技术", "防止红色车漆氧化褪色，长久保持鲜艳"),
            ("顶级防护", "10mil TPU基材，抵御碎石与划痕"),
            ("自修复功能", "轻微划痕热修复，色彩表面持久如新"),
        ],
        "applications": ["红色轿跑", "红色超跑", "个性改装车", "红色SUV"],
        "related": ["color-ppf.html", "ultimate-plus.html", "gloss-black-ppf.html"],
    },
    # ========== WINDOW TINT 9-15 ==========
    {
        "filename": "gradient-smoke-film.html",
        "name": "GRADIENT SMOKE FILM",
        "subtitle": "渐变烟灰窗膜 | 上深下浅 | 时尚美观",
        "tag": "🌫️ 渐变",
        "title": "GRADIENT SMOKE FILM - DUMI AUTO | 渐变烟灰窗膜",
        "description": "DUMI AUTO GRADIENT SMOKE渐变烟灰窗膜，上部深色逐渐过渡到底部浅色，兼顾隐私保护与行车安全。独特渐变设计增添车辆时尚感，是改装车主的热门选择。",
        "keywords": "渐变窗膜, 烟灰窗膜, 改装窗膜, 汽车窗膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "GRADIENT SMOKE渐变烟灰窗膜效果展示",
        "gradient": "linear-gradient(135deg,#1a1a1a,#4a4a4a,#8a8a8a,#4a4a4a,#1a1a1a)",
        "placeholder": "🌫️ GRADIENT",
        "tag_color": "#4a4a4a",
        "features": [
            ("渐变时尚设计", "上深下浅渐变，兼顾美观与实用性"),
            ("隐私保护", "上方深色有效保护车内隐私"),
            ("行车安全", "底部浅色不妨碍后视镜视线"),
            ("隔热节能", "阻隔红外线，降低车内温度"),
        ],
        "applications": ["改装车主", "年轻用户", "轿车", "SUV"],
        "related": ["limo-black-film.html", "privacy-smoke-film.html", "ceramic-tint.html"],
    },
    {
        "filename": "infrared-rejection-tint.html",
        "name": "INFRARED REJECTION TINT",
        "subtitle": "红外线阻隔窗膜 | 顶级隔热 | 舒适驾乘",
        "tag": "🌡️ 隔热",
        "title": "INFRARED REJECTION TINT - DUMI AUTO | 顶级红外线阻隔窗膜",
        "description": "DUMI AUTO红外线阻隔窗膜，采用先进纳米陶瓷粒子技术，阻隔95%以上红外线热量。显著降低车内温度，减少空调能耗，同时保护车内人员免受有害紫外线伤害。",
        "keywords": "红外线阻隔窗膜, 纳米隔热窗膜, 汽车窗膜, 防晒窗膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "红外线阻隔窗膜效果展示",
        "gradient": "linear-gradient(135deg,#ff6b35,#ff4500,#ff8c00,#ffd700)",
        "placeholder": "🌡️ IR BLOCK",
        "tag_color": "#ff6b35",
        "features": [
            ("95%红外线阻隔", "先进纳米技术，顶级隔热性能"),
            ("降低车内温度", "显著减少阳光直射带来的热量积聚"),
            ("保护皮肤", "阻隔99%以上有害紫外线"),
            ("信号无干扰", "非金属陶瓷技术，不干扰手机和GPS信号"),
        ],
        "applications": ["高温地区车辆", "长途驾驶", "家庭用车", "商务用车"],
        "related": ["ceramic-tint.html", "ceramic-pro-window-film.html", "prime-window-film.html"],
    },
    {
        "filename": "deep-black-tint.html",
        "name": "DEEP BLACK TINT",
        "subtitle": "深邃黑窗膜 | 极致隐私 | 经典永恒",
        "tag": "🖤 深邃",
        "title": "DEEP BLACK TINT - DUMI AUTO | 深邃黑窗膜",
        "description": "DUMI AUTO DEEP BLACK深邃黑窗膜，提供最极致的隐私保护与经典黑色外观。透光率极低，有效阻挡外界视线，同时为车辆增添神秘运动的视觉效果。",
        "keywords": "深邃黑窗膜, 隐私窗膜, 汽车窗膜, 黑膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "DEEP BLACK深邃黑窗膜效果展示",
        "gradient": "linear-gradient(135deg,#000000,#0a0a0a,#1a1a1a,#0a0a0a,#000000)",
        "placeholder": "🖤 DEEP BLACK",
        "tag_color": "#1a1a1a",
        "features": [
            ("极致隐私", "极低透光率，外界无法窥视车内"),
            ("经典黑色外观", "为车辆增添神秘运动气息"),
            ("优秀隔热", "阻隔太阳热量，降低车内温度"),
            ("防碎爆裂", "玻璃破碎时不飞溅，保护车内人员"),
        ],
        "applications": ["商务用车", "SUV", "豪华轿车", "改装车主"],
        "related": ["limo-black-film.html", "privacy-smoke-film.html", "security-film.html"],
    },
    {
        "filename": "solar-defense-film.html",
        "name": "SOLAR DEFENSE FILM",
        "subtitle": "太阳防御窗膜 | 全方位防晒 | 健康驾驶",
        "tag": "☀️ 防晒",
        "title": "SOLAR DEFENSE FILM - DUMI AUTO | 太阳防御窗膜",
        "description": "DUMI AUTO SOLAR DEFENSE太阳防御窗膜，全方位阻隔太阳光中的有害射线。保护皮肤免受晒伤，防止内饰老化褪色，特别适合有儿童和皮肤敏感乘客的家庭用车。",
        "keywords": "太阳防御窗膜, 全防晒窗膜, 健康窗膜, 汽车窗膜, 家庭用车窗膜, 悉尼窗膜",
        "alt_visual": "SOLAR DEFENSE太阳防御窗膜效果展示",
        "gradient": "linear-gradient(135deg,#ff8c00,#ffd700,#ff6b35,#ff4500)",
        "placeholder": "☀️ SOLAR",
        "tag_color": "#ff8c00",
        "features": [
            ("全方位UV防护", "阻隔99%以上UVA/UVB，全天候保护"),
            ("防止内饰老化", "减缓仪表台、座椅、皮革褪色老化"),
            ("保护皮肤健康", "降低皮肤癌风险，适合儿童和敏感肌肤"),
            ("清晰透明", "高透光率，不影响行车视线"),
        ],
        "applications": ["家庭用车", "儿童乘坐车辆", "长途驾驶", "户外停车"],
        "related": ["uv-protection-film.html", "ceramic-tint.html", "infrared-rejection-tint.html"],
    },
    {
        "filename": "reflection-proof-tint.html",
        "name": "REFLECTION PROOF TINT",
        "subtitle": "防反光窗膜 | 安全驾驶 | 消除眩光",
        "tag": "🛡️ 防眩",
        "title": "REFLECTION PROOF TINT - DUMI AUTO | 汽车防反光窗膜",
        "description": "DUMI AUTO REFLECTION PROOF防反光窗膜，有效减少夜间行车时对面车辆大灯造成的眩光，提升行车安全。同时具备优异隔热性能，是注重安全的车主的理想选择。",
        "keywords": "防反光窗膜, 防眩光窗膜, 安全窗膜, 汽车窗膜, 夜间驾驶窗膜, 悉尼窗膜",
        "alt_visual": "REFLECTION PROOF防反光窗膜效果展示",
        "gradient": "linear-gradient(135deg,#1a2a4a,#2d4a7a,#1a3a5a,#1a2a4a)",
        "placeholder": "🛡️ NO GLARE",
        "tag_color": "#1a3a5a",
        "features": [
            ("防眩光技术", "减少夜间对面大灯造成的眩光影响"),
            ("提升夜间安全", "改善夜间行车视野，降低眼睛疲劳"),
            ("优异隔热", "阻隔太阳热量，保持车内凉爽"),
            ("高清晰度", "不降低可视性，保持清晰视野"),
        ],
        "applications": ["经常夜间驾驶", "长途驾驶者", "年长驾驶员", "家庭用车"],
        "related": ["ceramic-tint.html", "prime-window-film.html", "security-film.html"],
    },
    {
        "filename": "color-stable-film.html",
        "name": "COLOR STABLE FILM",
        "subtitle": "色彩稳定窗膜 | 永不褪色 | 持久如新",
        "tag": "🎨 保色",
        "title": "COLOR STABLE FILM - DUMI AUTO | 色彩稳定窗膜",
        "description": "DUMI AUTO COLOR STABLE色彩稳定窗膜，采用染色技术确保窗膜颜色永不褪色。长期使用仍保持原有色泽，同时提供良好的隔热和隐私保护效果。",
        "keywords": "色彩稳定窗膜, 不褪色窗膜, 染色窗膜, 汽车窗膜, 悉尼窗膜, 经济型窗膜",
        "alt_visual": "COLOR STABLE色彩稳定窗膜效果展示",
        "gradient": "linear-gradient(135deg,#2d2d2d,#3a3a3a,#4a4a4a,#3a3a3a,#2d2d2d)",
        "placeholder": "🎨 COLOR",
        "tag_color": "#3a3a3a",
        "features": [
            ("色彩永不褪色", "先进染色技术，颜色稳定不分解"),
            ("经济实惠", "高性价比，优质隔热与隐私保护"),
            ("减少眩光", "降低阳光和夜间灯光造成的眩光"),
            ("多种透光率", "从深色到浅色，多种规格可选"),
        ],
        "applications": ["经济型车主", "家用轿车", "SUV", "租赁车辆"],
        "related": ["dyed-window-film.html", "privacy-smoke-film.html", "hybrid-window-film.html"],
    },
    {
        "filename": "ice-blue-tint.html",
        "name": "ICE BLUE TINT",
        "subtitle": "冰蓝窗膜 | 清新视觉 | 时尚之选",
        "tag": "❄️ 冰蓝",
        "title": "ICE BLUE TINT - DUMI AUTO | 冰蓝时尚窗膜",
        "description": "DUMI AUTO ICE BLUE冰蓝窗膜，清新的冰蓝色调为您的车窗增添独特时尚感。在提供隐私保护和隔热性能的同时，让您的车辆在众多车辆中脱颖而出。",
        "keywords": "冰蓝窗膜, 蓝色窗膜, 时尚窗膜, 汽车窗膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "ICE BLUE冰蓝窗膜效果展示",
        "gradient": "linear-gradient(135deg,#00bcd4,#00acc1,#00838f,#00acc1,#00bcd4)",
        "placeholder": "❄️ ICE BLUE",
        "tag_color": "#00acc1",
        "features": [
            ("清新冰蓝色彩", "独特冰蓝色调，时尚个性的选择"),
            ("良好隔热", "有效阻隔太阳热量，降低车内温度"),
            ("隐私保护", "减少外界窥视，保护车内财物"),
            ("信号无干扰", "陶瓷技术，不影响电子设备信号"),
        ],
        "applications": ["年轻车主", "改装车主", "轿车", "个性车主"],
        "related": ["ceramic-tint.html", "prime-window-film.html", "carbon-tint.html"],
    },
    # ========== SPECIALTY & COATING 16-20 ==========
    {
        "filename": "stealth-matte-tint.html",
        "name": "STEALTH MATTE TINT",
        "subtitle": "哑光窗膜 | 磨砂质感 | 低调神秘",
        "tag": "🔇 哑光",
        "title": "STEALTH MATTE TINT - DUMI AUTO | 哑光窗膜",
        "description": "DUMI AUTO STEALTH MATTE哑光窗膜，采用磨砂质感处理，为车窗提供独特的哑光外观与隐私保护。低调神秘，深受改装车主的喜爱，是打造个性化车辆的重要组成部分。",
        "keywords": "哑光窗膜, 磨砂窗膜, 改装窗膜, 汽车窗膜, 悉尼窗膜, 低调窗膜",
        "alt_visual": "STEALTH MATTE哑光窗膜效果展示",
        "gradient": "linear-gradient(135deg,#3a3a3a,#5a5a5a,#7a7a7a,#5a5a5a,#3a3a3a)",
        "placeholder": "🔇 MATTE",
        "tag_color": "#5a5a5a",
        "features": [
            ("磨砂哑光质感", "独特磨砂处理，呈现低调神秘外观"),
            ("隐私保护", "磨砂效果有效阻挡外界视线"),
            ("隔热性能", "阻隔太阳热量，保持车内凉爽"),
            ("防刮耐磨", "表面处理，耐刮擦耐磨损"),
        ],
        "applications": ["改装车主", "个性车主", "轿车", "SUV"],
        "related": ["carbon-tint.html", "stealth-ppf.html", "matte-satin-ppf.html"],
    },
    {
        "filename": "diamond-ceramic-coating.html",
        "name": "DIAMOND CERAMIC COATING",
        "subtitle": "钻石陶瓷镀晶 | 钻石级硬度 | 极致光泽",
        "tag": "💎 钻石",
        "title": "DIAMOND CERAMIC COATING - DUMI AUTO | 钻石陶瓷镀晶",
        "description": "DUMI AUTO DIAMOND CERAMIC钻石陶瓷镀晶，采用含有钻石微粒的顶级陶瓷配方，提供钻石级硬度和极致光泽。单次施工可维持2-3年，是车漆保护的最高级别选择之一。",
        "keywords": "钻石陶瓷镀晶, 钻石镀晶, 汽车镀晶, 顶级车漆保护, 悉尼镀晶, 洛杉矶镀晶",
        "alt_visual": "DIAMOND CERAMIC钻石陶瓷镀晶效果展示",
        "gradient": "linear-gradient(135deg,#e0f7fa,#b2ebf2,#80deea,#e0f7fa)",
        "placeholder": "💎 DIAMOND",
        "tag_color": "#00838f",
        "features": [
            ("钻石级硬度", "添加钻石微粒，硬度高达9H"),
            ("极致镜面光泽", "施工后呈现如钻石切割般的锐利光泽"),
            ("长效保护", "单次施工，维持2-3年"),
            ("疏水自洁", "水珠滚落，灰尘不易附着"),
        ],
        "applications": ["豪华超跑", "收藏级车辆", "顶级车主", "完美主义者"],
        "related": ["graphene-coating.html", "nano-self-healing-coating.html", "hydrophobic-topcoat.html"],
    },
    {
        "filename": "anti-oxidation-coating.html",
        "name": "ANTI-OXIDATION COATING",
        "subtitle": "抗氧化镀晶 | 防老化 | 车漆长青",
        "tag": "🌿 抗氧化",
        "title": "ANTI-OXIDATION COATING - DUMI AUTO | 汽车抗氧化镀晶",
        "description": "DUMI AUTO抗氧化镀晶，专为防止车漆氧化老化设计。形成致密保护层，阻隔空气中的氧气与车漆接触，从根本上防止氧化反应，是延长车漆寿命的理想选择。",
        "keywords": "抗氧化镀晶, 防老化镀晶, 车漆保护, 汽车镀晶, 悉尼镀晶, 洛杉矶镀晶",
        "alt_visual": "ANTI-OXIDATION抗氧化镀晶效果展示",
        "gradient": "linear-gradient(135deg,#2e7d32,#388e3c,#4caf50,#388e3c,#2e7d32)",
        "placeholder": "🌿 ANTI-OX",
        "tag_color": "#388e3c",
        "features": [
            ("抗氧化技术", "阻隔氧气与车漆接触，防止氧化反应"),
            ("延缓老化", "防止车漆褪色、失光、老化"),
            ("提升光泽", "增加车漆深层光泽，恢复新车质感"),
            ("长效保护", "单次施工，保护时间长达1-2年"),
        ],
        "applications": ["老旧车辆", "白色车漆", "户外停放车辆", "沿海地区车辆"],
        "related": ["graphene-coating.html", "diamond-ceramic-coating.html", "hydrophobic-topcoat.html"],
    },
    {
        "filename": "self-leveling-coating.html",
        "name": "SELF-LEVELING COATING",
        "subtitle": "自流平镀晶 | 自动填补 | 镜面效果",
        "tag": "🪞 自流平",
        "title": "SELF-LEVELING COATING - DUMI AUTO | 自流平镀晶",
        "description": "DUMI AUTO自流平镀晶，采用先进自流平技术，能够自动填补车漆表面的细微划痕和旋纹。施工后呈现完美镜面效果，特别适合想要恢复车漆完美状态的车主。",
        "keywords": "自流平镀晶, 自动修复镀晶, 车漆翻新, 汽车镀晶, 悉尼镀晶, 洛杉矶镀晶",
        "alt_visual": "SELF-LEVELING自流平镀晶效果展示",
        "gradient": "linear-gradient(135deg,#cfd8dc,#b0bec5,#90a4ae,#b0bec5,#cfd8dc)",
        "placeholder": "🪞 LEVELING",
        "tag_color": "#607d8b",
        "features": [
            ("自流平技术", "自动填补细微划痕和旋纹"),
            ("完美镜面", "施工后呈现极致光滑的镜面效果"),
            ("简易施工", "自流平特性，施工更加均匀"),
            ("长效保护", "保护膜层坚固，维持1-2年"),
        ],
        "applications": ["二手车", "有轻微划痕的车辆", "车漆翻新", "完美主义者"],
        "related": ["diamond-ceramic-coating.html", "anti-oxidation-coating.html", "hydrophobic-topcoat.html"],
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
    "nano-ceramic-ppf.html": ("🧪 纳米", "NANO CERAMIC", "纳米陶瓷PPF"),
    "matte-satin-ppf.html": ("🔘 哑光绸缎", "MATTE SATIN", "哑光绸缎PPF"),
    "limo-black-film.html": ("🖤 limo", "LIMO BLACK", "深色limo窗膜"),
    "privacy-smoke-film.html": ("🌫️ 烟灰", "PRIVACY SMOKE", "隐私烟灰窗膜"),
    "ceramic-pro-window-film.html": ("🪟 Pro", "CERAMIC PRO", "专业级陶瓷窗膜"),
    "dyed-window-film.html": ("🎨 染色", "DYED窗膜", "经济型染色窗膜"),
    "hybrid-window-film.html": ("🔗 混合", "HYBRID窗膜", "混合技术窗膜"),
    "metalized-window-film.html": ("⚙️ 金属化", "METALIZED窗膜", "金属化隔热窗膜"),
    "clear-protective-tint.html": ("🔵 透明", "CLEAR TINT", "透明防护窗膜"),
    "anti-graffiti-film.html": ("🔫 防涂鸦", "ANTI-GRAFFITI", "防涂鸦保护膜"),
    "hydrophobic-topcoat.html": ("💧 疏水", "HYDROPHOBIC", "疏水顶涂层"),
    "nano-self-healing-coating.html": ("🧪 自修复", "NANO SELF-HEALING", "纳米自修复镀晶"),
    "diamond-guard-ppf.html": ("💎 钻石", "DIAMOND GUARD", "钻石防护PPF"),
}

def get_related_html(related_files):
    html = '<div class="products-grid">\n'
    for fname in related_files:
        if fname in RELATED_PRODUCTS_MAP:
            tag, name, desc = RELATED_PRODUCTS_MAP[fname]
            gradient = "#1a1a2e"
            if "PPF" in fname or fname in ["ultimate-plus.html", "stealth-ppf.html", "armor-ppf.html", "matte-protective-ppf.html", "urban-shield-ppf.html"]:
                gradient = "#1a1a2e"
            if "COLOR" in name.upper() or "改色" in desc or "CHERRY" in name.upper():
                gradient = "#8B0000"
            if "STEALTH" in name.upper():
                gradient = "#2c2c2c"
            if "ARMOR" in name.upper():
                gradient = "#1a3a3a"
            if "CERAMIC" in name.upper() and "TINT" not in fname:
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
            if "DIAMOND" in name.upper():
                gradient = "#00838f"
            if "HYDRO" in name.upper():
                gradient = "#00838f"
            if "MATTE" in name.upper() and "TINT" in fname:
                gradient = "#5a5a5a"
            if "ICE BLUE" in name.upper():
                gradient = "#00acc1"
            if "HYDROPHOBIC" in name.upper():
                gradient = "#006064"
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
    <link rel="canonical" href="https://dumi-auto.com/products/{p["filename"]}">
    <link rel="stylesheet" href="{CSS_LINK}">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "{p["name"]}",
        "description": "{p["description"]}",
        "brand": {{"@type": "Brand", "name": "DUMI AUTO"}},
        "offers": {{
            "@type": "Offer",
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "seller": {{"@type": "Organization", "name": "DUMI AUTO"}}
        }}
    }}
    </script>
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

new_products = []
for p in PRODUCTS:
    filepath = os.path.join(BASE_DIR, p["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(generate_product_page(p))
    new_products.append(p["filename"])
    print(f"✅ Created: {p['filename']}")

print(f"\n🎉 Total {len(new_products)} product pages generated!")

# Also update sitemap.xml
sitemap_path = "/Users/carstauto/.openclaw/workspace/dumi-auto-website/sitemap.xml"
today = "2026-04-24"

with open(sitemap_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find closing </urlset> and insert new entries before it
new_entries = ""
for fname in new_products:
    new_entries += f'''  <url>
    <loc>https://dumi-auto.com/products/{fname}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''

content = content.replace("</urlset>", new_entries + "</urlset>")
content = content.replace('<lastmod>2026-04-20</lastmod>', f'<lastmod>{today}</lastmod>')

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ sitemap.xml updated with {len(new_products)} new entries")
