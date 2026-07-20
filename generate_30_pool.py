#!/usr/bin/env python3
"""DUMI AUTO - Generate 30+ new product pages (Pool for daily 15 rotation)
Categories: PPF variants, Ceramic Coating, Window Tint, Wrap Film
"""
import os, json, sys
from datetime import datetime

BASE_DIR = "/tmp/dumi-publish-dumi-auto/products"
CSS_LINK = "../css/style.css"
TODAY = datetime.now().strftime("%Y-%m-%d")

# ============ 30+ PRODUCT POOL (date-based rotation) ============
PRODUCT_POOL = [
    # ===== PPF Variants 1-12 =====
    {
        "filename": "ultimate-plus-2026.html", "name": "ULTIMATE PLUS 2026",
        "subtitle": "顶级2026款漆面保护膜 | 全新升级 | 至尊防护",
        "tag": "👑 至尊", "title": "ULTIMATE PLUS 2026 - DUMI AUTO | 顶级漆面保护膜",
        "description": "DUMI AUTO ULTIMATE PLUS 2026是XPEL最新升级的顶级漆面保护膜，采用革命性2026新配方，在自修复、抗污、抗黄变三大核心性能上全面提升。是豪华车主的不二之选。",
        "keywords": "ULTIMATE PLUS 2026, 顶级PPF, 2026新配方, 汽车保护膜, 悉尼PPF, 豪华车保护",
        "alt_visual": "ULTIMATE PLUS 2026至尊漆面保护膜", "gradient": "linear-gradient(135deg,#1a1a2e,#16213e,#0f3460,#16213e,#1a1a2e)",
        "placeholder": "👑 ULTRA", "tag_color": "#0f3460",
        "features": [("2026全新配方", "XPEL最新研发，分子结构升级"), ("抗黄变升级", "10年不变黄，比旧款提升50%"), ("顶级自修复", "热修复能力增强30%"), ("官方10年质保", "全球联保，售后无忧")],
        "applications": ["豪华轿车", "超跑", "收藏级车辆", "高端商务车"], "related": ["ultimate-plus-black.html", "stealth-ppf.html"],
    },
    {
        "filename": "stealth-armor-ppf.html", "name": "STEALTH ARMOR PPF",
        "subtitle": "隐形装甲漆面保护膜 | 哑光质感 | 极致防护",
        "tag": "🛡️ 装甲", "title": "STEALTH ARMOR PPF - DUMI AUTO | 隐形装甲漆面保护膜",
        "description": "DUMI AUTO STEALTH ARMOR隐形装甲漆面保护膜，专为军用级别防护设计。10mil顶级TPU基材，可抵御高速碎石冲击，是越野与硬派SUV的最佳搭档。",
        "keywords": "STEALTH ARMOR, 装甲PPF, 越野车衣, 硬派SUV, 汽车保护膜, 军用级",
        "alt_visual": "STEALTH ARMOR装甲级漆面保护膜", "gradient": "linear-gradient(135deg,#2c3e50,#34495e,#1c2833,#34495e,#2c3e50)",
        "placeholder": "🛡️ STEALTH", "tag_color": "#1c2833",
        "features": [("10mil加厚基材", "军用级厚度，抵御高速碎石"), ("哑光质感", "低调奢华，无反光"), ("越野专用", "恶劣路况下保护车漆"), ("10年质保", "长期可靠保护")],
        "applications": ["越野车", "硬派SUV", "皮卡", "军车"], "related": ["armor-ppf.html", "matte-protective-ppf.html"],
    },
    {
        "filename": "trinity-ppf.html", "name": "TRINITY PPF",
        "subtitle": "三重防护漆面保护膜 | 三层结构 | 终极防护",
        "tag": "🔱 三重", "title": "TRINITY PPF - DUMI AUTO | 三重防护漆面保护膜",
        "description": "DUMI AUTO TRINITY三重防护漆面保护膜，革命性三层复合结构，提供无与伦比的综合防护。基材+自修复层+抗污层三效合一，质保长达12年。",
        "keywords": "TRINITY PPF, 三重防护, 三层结构, 汽车保护膜, 高端PPF, 悉尼PPF",
        "alt_visual": "TRINITY三重防护漆面保护膜", "gradient": "linear-gradient(135deg,#4a148c,#6a1b9a,#7b1fa2,#6a1b9a,#4a148c)",
        "placeholder": "🔱 TRINITY", "tag_color": "#6a1b9a",
        "features": [("三层复合结构", "基材+自修复+抗污层叠加"), ("12年超长质保", "行业最长质保期"), ("极致防护", "综合防护性能提升200%"), ("奢华光泽", "保持原厂漆面极致光泽")],
        "applications": ["豪华轿车", "商务用车", "长期投资车", "收藏车"], "related": ["ultimate-plus-2026.html", "fusion-hybrid-ppf.html"],
    },
    {
        "filename": "fusion-hybrid-ppf.html", "name": "FUSION HYBRID PPF",
        "subtitle": "混合融合漆面保护膜 | PPF+陶瓷涂层 | 二合一",
        "tag": "💎 融合", "title": "FUSION HYBRID PPF - DUMI AUTO | 混合融合漆面保护膜",
        "description": "DUMI AUTO FUSION HYBRID革命性产品，将PPF与陶瓷涂层完美融合，一次施工获得双倍保护。节省时间，提升效果，是忙碌车主的首选。",
        "keywords": "FUSION HYBRID, PPF+陶瓷, 二合一, 混合保护膜, 汽车保护, 悉尼PPF",
        "alt_visual": "FUSION HYBRID融合保护膜", "gradient": "linear-gradient(135deg,#00897b,#00acc1,#0097a7,#00acc1,#00897b)",
        "placeholder": "💎 FUSION", "tag_color": "#00897b",
        "features": [("PPF+陶瓷二合一", "一次施工双倍保护"), ("节省50%时间", "比分开施工快一倍"), ("永久疏水", "陶瓷层带来永久疏水效果"), ("增强光泽", "比单一PPF亮3倍")],
        "applications": ["商务精英", "高端车主", "效率优先用户", "豪华SUV"], "related": ["trinity-ppf.html", "pro-9h-ceramic.html"],
    },
    {
        "filename": "apex-shield-ppf.html", "name": "APEX SHIELD PPF",
        "subtitle": "巅峰护盾漆面保护膜 | 顶级TPU | 极致光泽",
        "tag": "🏔️ 巅峰", "title": "APEX SHIELD PPF - DUMI AUTO | 巅峰护盾漆面保护膜",
        "description": "DUMI AUTO APEX SHIELD巅峰护盾漆面保护膜，使用业界最顶级的TPU基材，配合XPEL专利涂层技术。光泽度提升40%，防护等级达到行业最高标准。",
        "keywords": "APEX SHIELD, 巅峰护盾, 顶级TPU, 高光泽PPF, 汽车保护膜, 悉尼PPF",
        "alt_visual": "APEX SHIELD巅峰护盾PPF", "gradient": "linear-gradient(135deg,#1976d2,#1565c0,#0d47a1,#1565c0,#1976d2)",
        "placeholder": "🏔️ APEX", "tag_color": "#1565c0",
        "features": [("顶级TPU基材", "业界最顶级原材料"), ("光泽度+40%", "比普通PPF亮40%"), ("专利涂层技术", "XPEL独家涂层配方"), ("抗紫外线", "防止车漆老化褪色")],
        "applications": ["豪华轿车", "超跑车主", "高端商务车", "收藏车"], "related": ["ultimate-plus-2026.html", "trinity-ppf.html"],
    },
    {
        "filename": "zenith-matte-ppf.html", "name": "ZENITH MATTE PPF",
        "subtitle": "巅峰哑光漆面保护膜 | 极致哑光 | 顶级质感",
        "tag": "🌑 哑光", "title": "ZENITH MATTE PPF - DUMI AUTO | 巅峰哑光漆面保护膜",
        "description": "DUMI AUTO ZENITH MATTE巅峰哑光漆面保护膜，为追求极致哑光质感的车主设计。完美呈现原厂哑光效果，同时提供专业级PPF防护。",
        "keywords": "ZENITH MATTE, 哑光PPF, 哑光车衣, 顶级哑光, 汽车保护膜, 悉尼哑光PPF",
        "alt_visual": "ZENITH MATTE巅峰哑光保护膜", "gradient": "linear-gradient(135deg,#37474f,#455a64,#546e7a,#455a64,#37474f)",
        "placeholder": "🌑 ZENITH", "tag_color": "#37474f",
        "features": [("极致哑光质感", "完美呈现原厂哑光效果"), ("哑光专用配方", "专为哑光设计"), ("抗指纹", "表面不易留指纹"), ("清洁简便", "普通清洁即可")],
        "applications": ["哑光改装车", "原厂哑光车", "商务哑光车", "个性化车主"], "related": ["matte-protective-ppf.html", "satin-matte-ppf.html"],
    },
    {
        "filename": "nova-ceramic-ppf.html", "name": "NOVA CERAMIC PPF",
        "subtitle": "新星陶瓷漆面保护膜 | 陶瓷光泽 | 革新科技",
        "tag": "💫 新星", "title": "NOVA CERAMIC PPF - DUMI AUTO | 新星陶瓷漆面保护膜",
        "description": "DUMI AUTO NOVA CERAMIC新星陶瓷漆面保护膜，融合最新陶瓷科技，提供超越传统PPF的陶瓷光泽与疏水性能。革新性产品，重新定义车漆保护。",
        "keywords": "NOVA CERAMIC, 陶瓷PPF, 革新科技, 疏水车衣, 汽车保护膜, 悉尼PPF",
        "alt_visual": "NOVA CERAMIC新星陶瓷保护膜", "gradient": "linear-gradient(135deg,#7b1fa2,#8e24aa,#9c27b0,#8e24aa,#7b1fa2)",
        "placeholder": "💫 NOVA", "tag_color": "#7b1fa2",
        "features": [("陶瓷光泽", "超越传统PPF的陶瓷光泽"), ("永久疏水", "水珠自动滚落"), ("革新科技", "2026最新材料科技"), ("易清洁", "污渍不易附着")],
        "applications": ["豪华车主", "科技爱好者", "年轻精英", "超跑车主"], "related": ["fusion-hybrid-ppf.html", "pro-9h-ceramic.html"],
    },
    {
        "filename": "eclipse-tint-ppf.html", "name": "ECLIPSE TINT PPF",
        "subtitle": "暗夜日蚀漆面保护膜 | 极致深色 | 神秘质感",
        "tag": "🌚 暗夜", "title": "ECLIPSE TINT PPF - DUMI AUTO | 暗夜日蚀漆面保护膜",
        "description": "DUMI AUTO ECLIPSE TINT暗夜日蚀漆面保护膜，提供极致深色保护效果。在保护原厂车漆的同时，营造神秘深邃的视觉效果。",
        "keywords": "ECLIPSE TINT, 暗夜PPF, 深色车衣, 神秘质感, 汽车保护膜, 悉尼PPF",
        "alt_visual": "ECLIPSE TINT暗夜保护膜", "gradient": "linear-gradient(135deg,#0a0a0a,#1a1a1a,#2c2c2c,#1a1a1a,#0a0a0a)",
        "placeholder": "🌚 ECLIPSE", "tag_color": "#0a0a0a",
        "features": [("极致深色", "比普通PPF暗30%"), ("神秘质感", "营造深邃视觉效果"), ("保护原漆", "不影响车漆本身"), ("隐私保护", "有效保护车内隐私")],
        "applications": ["黑色车主", "商务车", "豪华轿车", "改装车"], "related": ["gloss-black-ppf.html", "privacy-tint-pro.html"],
    },
    {
        "filename": "orion-protect-ppf.html", "name": "ORION PROTECT PPF",
        "subtitle": "猎户护盾漆面保护膜 | 星空科技 | 多层防护",
        "tag": "✨ 星空", "title": "ORION PROTECT PPF - DUMI AUTO | 猎户护盾漆面保护膜",
        "description": "DUMI AUTO ORION PROTECT猎户护盾漆面保护膜，融合星空科技概念，多层防护结构。提供超越传统PPF的全方位保护，是车主的守护之星。",
        "keywords": "ORION PROTECT, 猎户PPF, 星空科技, 多层防护, 汽车保护膜, 悉尼PPF",
        "alt_visual": "ORION PROTECT猎户护盾保护膜", "gradient": "linear-gradient(135deg,#1a237e,#283593,#303f9f,#283593,#1a237e)",
        "placeholder": "✨ ORION", "tag_color": "#283593",
        "features": [("多层防护", "4层结构综合保护"), ("星空科技概念", "源自NASA航天技术"), ("全方位保护", "无死角覆盖"), ("永久自修复", "表面划痕自动消失")],
        "applications": ["科技爱好者", "豪华车主", "完美主义者", "商务车"], "related": ["trinity-ppf.html", "ultimate-plus-2026.html"],
    },
    {
        "filename": "phoenix-fire-ppf.html", "name": "PHOENIX FIRE PPF",
        "subtitle": "凤凰火焰漆面保护膜 | 自修复王者 | 重生科技",
        "tag": "🔥 凤凰", "title": "PHOENIX FIRE PPF - DUMI AUTO | 凤凰火焰漆面保护膜",
        "description": "DUMI AUTO PHOENIX FIRE凤凰火焰漆面保护膜，自修复能力达到业界顶级。划痕遇热自动修复，如同凤凰涅槃重生，让您的车漆永远焕然一新。",
        "keywords": "PHOENIX FIRE, 凤凰PPF, 顶级自修复, 重生科技, 汽车保护膜, 悉尼PPF",
        "alt_visual": "PHOENIX FIRE凤凰保护膜", "gradient": "linear-gradient(135deg,#d32f2f,#c62828,#b71c1c,#c62828,#d32f2f)",
        "placeholder": "🔥 PHOENIX", "tag_color": "#c62828",
        "features": [("顶级自修复", "遇热自动修复划痕"), ("重生科技", "永不磨损的车漆"), ("极致耐热", "耐高温性能提升"), ("长寿命", "15年超长使用寿命")],
        "applications": ["超跑", "豪华轿车", "收藏车", "高端车主"], "related": ["ultimate-plus-2026.html", "apex-shield-ppf.html"],
    },
    {
        "filename": "dragon-scale-ppf.html", "name": "DRAGON SCALE PPF",
        "subtitle": "龙鳞漆面保护膜 | 鳞片纹理 | 至刚至柔",
        "tag": "🐉 龙鳞", "title": "DRAGON SCALE PPF - DUMI AUTO | 龙鳞漆面保护膜",
        "description": "DUMI AUTO DRAGON SCALE龙鳞漆面保护膜，灵感来自东方神龙鳞片。独特的微观结构提供超强抗刮能力，刚柔并济，坚不可摧。",
        "keywords": "DRAGON SCALE, 龙鳞PPF, 鳞片纹理, 高抗刮, 汽车保护膜, 悉尼PPF",
        "alt_visual": "DRAGON SCALE龙鳞保护膜", "gradient": "linear-gradient(135deg,#1b5e20,#2e7d32,#388e3c,#2e7d32,#1b5e20)",
        "placeholder": "🐉 DRAGON", "tag_color": "#2e7d32",
        "features": [("龙鳞微观结构", "灵感来自东方神龙"), ("超强抗刮", "硬度提升50%"), ("刚柔并济", "柔软度与硬度兼得"), ("独特纹理", "微观视觉美感")],
        "applications": ["豪华SUV", "越野车", "商务车", "个性化车主"], "related": ["stealth-armor-ppf.html", "apex-shield-ppf.html"],
    },
    {
        "filename": "titanium-armor-ppf.html", "name": "TITANIUM ARMOR PPF",
        "subtitle": "钛金护甲漆面保护膜 | 军工级别 | 至刚硬度",
        "tag": "⚙️ 钛金", "title": "TITANIUM ARMOR PPF - DUMI AUTO | 钛金护甲漆面保护膜",
        "description": "DUMI AUTO TITANIUM ARMOR钛金护甲漆面保护膜，军工级别硬度，钛合金般坚固。可抵御高速行驶中的石击、树枝刮擦，是极限驾驶的最佳选择。",
        "keywords": "TITANIUM ARMOR, 钛金PPF, 军工级别, 高硬度, 汽车保护膜, 极限驾驶",
        "alt_visual": "TITANIUM ARMOR钛金护甲保护膜", "gradient": "linear-gradient(135deg,#37474f,#455a64,#37474f,#263238,#37474f)",
        "placeholder": "⚙️ TITANIUM", "tag_color": "#455a64",
        "features": [("军工级别硬度", "钛合金般坚固"), ("抵御高速石击", "200km/h石击无损伤"), ("极限驾驶适用", "赛车级保护"), ("抗变形", "高温不变形")],
        "applications": ["赛车", "越野车", "极限驾驶", "军车"], "related": ["stealth-armor-ppf.html", "dragon-scale-ppf.html"],
    },
    # ===== Ceramic Coating 13-20 =====
    {
        "filename": "pro-9h-ceramic.html", "name": "PRO 9H CERAMIC",
        "subtitle": "专业9H陶瓷涂层 | 9H硬度 | 钻石光泽",
        "tag": "💎 9H", "title": "PRO 9H CERAMIC - DUMI AUTO | 专业9H陶瓷涂层",
        "description": "DUMI AUTO PRO 9H专业9H陶瓷涂层，达到铅笔硬度9H等级，提供钻石般光泽与抗刮能力。一次施工，五年保护。",
        "keywords": "PRO 9H, 9H陶瓷涂层, 钻石光泽, 汽车陶瓷涂层, 悉尼陶瓷, 9H硬度",
        "alt_visual": "PRO 9H专业陶瓷涂层", "gradient": "linear-gradient(135deg,#0277bd,#01579b,#004d40,#01579b,#0277bd)",
        "placeholder": "💎 9H", "tag_color": "#01579b",
        "features": [("9H铅笔硬度", "钻石级别硬度"), ("5年长久保护", "一次施工5年无忧"), ("钻石光泽", "镜面级反光效果"), ("疏水疏油", "水珠油污自动滚落")],
        "applications": ["豪华车主", "新车保护", "二手车翻新", "高端车主"], "related": ["graphene-ceramic-pro.html", "diamond-coating-pro.html"],
    },
    {
        "filename": "graphene-ceramic-pro.html", "name": "GRAPHENE CERAMIC PRO",
        "subtitle": "石墨烯专业陶瓷涂层 | 石墨烯科技 | 至强防护",
        "tag": "⚛️ 石墨烯", "title": "GRAPHENE CERAMIC PRO - DUMI AUTO | 石墨烯专业陶瓷涂层",
        "description": "DUMI AUTO GRAPHENE CERAMIC PRO石墨烯专业陶瓷涂层，融合石墨烯尖端科技，比传统陶瓷涂层硬3倍、抗污5倍。2026最新科技。",
        "keywords": "GRAPHENE CERAMIC, 石墨烯涂层, 2026科技, 汽车陶瓷, 悉尼陶瓷, 高端涂层",
        "alt_visual": "GRAPHENE CERAMIC PRO石墨烯陶瓷涂层", "gradient": "linear-gradient(135deg,#263238,#37474f,#455a64,#37474f,#263238)",
        "placeholder": "⚛️ GRAPHENE", "tag_color": "#263238",
        "features": [("石墨烯科技", "21世纪尖端材料"), ("硬度3倍", "超越传统陶瓷"), ("抗污5倍", "几乎不沾污渍"), ("7年保护", "超长寿命")],
        "applications": ["科技爱好者", "豪华车主", "完美主义者", "展示车"], "related": ["pro-9h-ceramic.html", "titanium-ceramic-shield.html"],
    },
    {
        "filename": "titanium-ceramic-shield.html", "name": "TITANIUM CERAMIC SHIELD",
        "subtitle": "钛金陶瓷护盾 | 军工陶瓷 | 顶级防护",
        "tag": "🛡️ 钛盾", "title": "TITANIUM CERAMIC SHIELD - DUMI AUTO | 钛金陶瓷护盾",
        "description": "DUMI AUTO TITANIUM CERAMIC SHIELD钛金陶瓷护盾，融合军工陶瓷技术，提供顶级防护与光泽。豪华车主的不二之选。",
        "keywords": "TITANIUM CERAMIC, 钛金陶瓷, 军工涂层, 顶级防护, 汽车陶瓷, 悉尼陶瓷",
        "alt_visual": "TITANIUM CERAMIC SHIELD钛金陶瓷护盾", "gradient": "linear-gradient(135deg,#5d4037,#4e342e,#3e2723,#4e342e,#5d4037)",
        "placeholder": "🛡️ TITANIUM", "tag_color": "#4e342e",
        "features": [("军工陶瓷", "军用级别技术"), ("顶级防护", "无与伦比防护"), ("超长寿命", "10年质保"), ("极致光泽", "永久钻石光泽")],
        "applications": ["豪华轿车", "超跑", "收藏车", "VIP用户"], "related": ["graphene-ceramic-pro.html", "pro-9h-ceramic.html"],
    },
    {
        "filename": "quartz-9h-coating.html", "name": "QUARTZ 9H COATING",
        "subtitle": "石英9H涂层 | 石英硬度 | 长效保护",
        "tag": "💠 石英", "title": "QUARTZ 9H COATING - DUMI AUTO | 石英9H涂层",
        "description": "DUMI AUTO QUARTZ 9H石英9H涂层，采用天然石英配方，提供9H硬度与长效保护。性价比之选，效果媲美顶级产品。",
        "keywords": "QUARTZ 9H, 石英涂层, 高性价比, 汽车陶瓷, 悉尼陶瓷, 长效保护",
        "alt_visual": "QUARTZ 9H石英涂层", "gradient": "linear-gradient(135deg,#0097a7,#00838f,#006064,#00838f,#0097a7)",
        "placeholder": "💠 QUARTZ", "tag_color": "#00838f",
        "features": [("石英配方", "天然石英原料"), ("9H硬度", "高抗刮能力"), ("长效保护", "5年质保"), ("性价比高", "平民价位豪华享受")],
        "applications": ["家用车主", "代步车", "性价比用户", "新车主"], "related": ["pro-9h-ceramic.html", "ceramic-ultra.html"],
    },
    {
        "filename": "diamond-coating-pro.html", "name": "DIAMOND COATING PRO",
        "subtitle": "钻石专业涂层 | 至高硬度 | 极致光泽",
        "tag": "💍 钻石", "title": "DIAMOND COATING PRO - DUMI AUTO | 钻石专业涂层",
        "description": "DUMI AUTO DIAMOND COATING PRO钻石专业涂层，行业最高硬度等级10H。永久钻石光泽，无与伦比的豪华感。",
        "keywords": "DIAMOND COATING, 钻石涂层, 10H硬度, 极致光泽, 汽车陶瓷, 顶级涂层",
        "alt_visual": "DIAMOND COATING PRO钻石涂层", "gradient": "linear-gradient(135deg,#e1f5fe,#b3e5fc,#81d4fa,#b3e5fc,#e1f5fe)",
        "placeholder": "💍 DIAMOND", "tag_color": "#0288d1",
        "features": [("10H最高硬度", "超越铅笔9H"), ("钻石光泽", "镜面级反光"), ("永久保护", "10年质保"), ("无与伦比", "行业顶级产品")],
        "applications": ["超跑车主", "豪华车主", "收藏家", "极致追求者"], "related": ["pro-9h-ceramic.html", "graphene-ceramic-pro.html"],
    },
    {
        "filename": "ceramic-boost-spray.html", "name": "CERAMIC BOOST SPRAY",
        "subtitle": "陶瓷增强喷雾 | 即喷即护 | 便捷维护",
        "tag": "💦 即喷", "title": "CERAMIC BOOST SPRAY - DUMI AUTO | 陶瓷增强喷雾",
        "description": "DUMI AUTO CERAMIC BOOST陶瓷增强喷雾，即喷即护的便捷陶瓷产品。可在已施工陶瓷涂层上叠加使用，恢复并增强原有光泽与疏水性能。",
        "keywords": "CERAMIC BOOST, 陶瓷喷雾, 即喷即护, 便捷陶瓷, 汽车保养, 悉尼陶瓷",
        "alt_visual": "CERAMIC BOOST SPRAY陶瓷喷雾", "gradient": "linear-gradient(135deg,#4dd0e1,#26c6da,#00bcd4,#26c6da,#4dd0e1)",
        "placeholder": "💦 BOOST", "tag_color": "#00bcd4",
        "features": [("即喷即护", "无需复杂施工"), ("便捷维护", "DIY即可使用"), ("增强原有涂层", "叠加使用效果倍增"), ("疏水恢复", "恢复旧涂层的疏水")],
        "applications": ["已施工陶瓷车", "DIY爱好者", "日常维护", "短期保护"], "related": ["ceramic-top-coat.html", "pro-9h-ceramic.html"],
    },
    {
        "filename": "ceramic-top-coat.html", "name": "CERAMIC TOP COAT",
        "subtitle": "陶瓷面漆 | 顶层保护 | 终极光泽",
        "tag": "🌟 面漆", "title": "CERAMIC TOP COAT - DUMI AUTO | 陶瓷面漆",
        "description": "DUMI AUTO CERAMIC TOP COAT陶瓷面漆，作为陶瓷涂层的顶层保护层使用。提供极致光泽与额外疏水保护，是完整陶瓷涂层系统的关键。",
        "keywords": "CERAMIC TOP COAT, 陶瓷面漆, 顶层保护, 终极光泽, 汽车陶瓷, 悉尼陶瓷",
        "alt_visual": "CERAMIC TOP COAT陶瓷面漆", "gradient": "linear-gradient(135deg,#ffd54f,#ffca28,#ffc107,#ffca28,#ffd54f)",
        "placeholder": "🌟 TOP", "tag_color": "#ffa000",
        "features": [("顶层保护", "陶瓷系统最终层"), ("极致光泽", "镜面级反光"), ("额外疏水", "二次保护"), ("延长寿命", "底层寿命+50%")],
        "applications": ["完整陶瓷施工", "高端车主", "展示车", "专业级用户"], "related": ["ceramic-boost-spray.html", "diamond-coating-pro.html"],
    },
    {
        "filename": "ceramic-ultra.html", "name": "CERAMIC ULTRA",
        "subtitle": "陶瓷至尊 | 9H+硬度 | 顶级光泽",
        "tag": "👑 至尊", "title": "CERAMIC ULTRA - DUMI AUTO | 陶瓷至尊",
        "description": "DUMI AUTO CERAMIC ULTRA陶瓷至尊，9H+超高硬度，超长7年质保。融合最新陶瓷科技，提供顶级光泽与防护。",
        "keywords": "CERAMIC ULTRA, 陶瓷至尊, 9H+, 顶级陶瓷, 汽车陶瓷, 悉尼陶瓷",
        "alt_visual": "CERAMIC ULTRA陶瓷至尊", "gradient": "linear-gradient(135deg,#311b92,#4527a0,#5e35b1,#4527a0,#311b92)",
        "placeholder": "👑 ULTRA", "tag_color": "#4527a0",
        "features": [("9H+超高硬度", "比普通9H更硬"), ("7年质保", "超长保护期"), ("顶级光泽", "极致镜面反光"), ("最新科技", "2026新配方")],
        "applications": ["豪华车主", "新车主", "完美主义者", "高端展示车"], "related": ["diamond-coating-pro.html", "titanium-ceramic-shield.html"],
    },
    # ===== Window Tint 21-27 =====
    {
        "filename": "ceramic-ir-tint.html", "name": "CERAMIC IR TINT",
        "subtitle": "陶瓷红外隔热膜 | 顶级隔热 | 99%紫外线阻隔",
        "tag": "🌞 IR", "title": "CERAMIC IR TINT - DUMI AUTO | 陶瓷红外隔热膜",
        "description": "DUMI AUTO CERAMIC IR陶瓷红外隔热膜，业界顶级隔热技术。99%紫外线阻隔，85%红外线阻隔，让车内温度降低15度。",
        "keywords": "CERAMIC IR, 陶瓷隔热膜, 红外阻隔, 汽车窗膜, 悉尼窗膜, 顶级隔热",
        "alt_visual": "CERAMIC IR陶瓷红外隔热膜", "gradient": "linear-gradient(135deg,#1976d2,#1565c0,#0d47a1,#1565c0,#1976d2)",
        "placeholder": "🌞 IR", "tag_color": "#1565c0",
        "features": [("99% UV阻隔", "完全保护皮肤"), ("85% IR阻隔", "显著降温"), ("陶瓷科技", "无金属不干扰信号"), ("终身质保", "不变色不褪色")],
        "applications": ["豪华车主", "商务车", "阳光强烈地区", "健康关注者"], "related": ["nano-carbon-tint.html", "crystalline-tint.html"],
    },
    {
        "filename": "nano-carbon-tint.html", "name": "NANO CARBON TINT",
        "subtitle": "纳米碳膜 | 高隔热 | 信号无干扰",
        "tag": "⚫ 碳膜", "title": "NANO CARBON TINT - DUMI AUTO | 纳米碳膜",
        "description": "DUMI AUTO NANO CARBON纳米碳膜，采用碳分子技术，提供高隔热性能同时不干扰手机、GPS、ETC等电子信号。",
        "keywords": "NANO CARBON, 纳米碳膜, 高隔热, 无信号干扰, 汽车窗膜, 悉尼窗膜",
        "alt_visual": "NANO CARBON纳米碳膜", "gradient": "linear-gradient(135deg,#212121,#424242,#616161,#424242,#212121)",
        "placeholder": "⚫ CARBON", "tag_color": "#424242",
        "features": [("碳分子技术", "新一代隔热"), ("无信号干扰", "GPS/手机畅通"), ("高隔热", "75% IR阻隔"), ("哑光质感", "低调奢华")],
        "applications": ["豪华车主", "商务车", "科技配置车", "城市通勤"], "related": ["ceramic-ir-tint.html", "uv400-tint.html"],
    },
    {
        "filename": "uv400-tint.html", "name": "UV400 TINT",
        "subtitle": "UV400全防紫外线膜 | 100%UV阻隔 | 健康保护",
        "tag": "☀️ UV400", "title": "UV400 TINT - DUMI AUTO | UV400全防紫外线膜",
        "description": "DUMI AUTO UV400 UV400全防紫外线膜，100%阻隔UVA/UVB紫外线，是皮肤癌和皮肤老化的高危人群的必备。",
        "keywords": "UV400, 防紫外线, 健康保护, 全UV阻隔, 汽车窗膜, 悉尼窗膜",
        "alt_visual": "UV400全防紫外线膜", "gradient": "linear-gradient(135deg,#ff6f00,#ff8f00,#ffa000,#ff8f00,#ff6f00)",
        "placeholder": "☀️ UV400", "tag_color": "#ff8f00",
        "features": [("100% UV阻隔", "UVA+UVB全防"), ("健康保护", "减少皮肤癌风险"), ("减缓内饰老化", "保护车内装饰"), ("10年质保", "长期效果保证")],
        "applications": ["健康关注者", "女性车主", "儿童家庭", "皮肤敏感者"], "related": ["ceramic-ir-tint.html", "spectrally-selective-tint.html"],
    },
    {
        "filename": "privacy-tint-pro.html", "name": "PRIVACY TINT PRO",
        "subtitle": "隐私专业膜 | 后排专属 | 高隐私度",
        "tag": "🔒 隐私", "title": "PRIVACY TINT PRO - DUMI AUTO | 隐私专业膜",
        "description": "DUMI AUTO PRIVACY TINT PRO隐私专业膜，专为后排设计的高隐私度窗膜。VIP乘客的最佳选择，提供绝对隐私空间。",
        "keywords": "PRIVACY TINT, 隐私窗膜, 后排膜, 高隐私, VIP膜, 汽车窗膜",
        "alt_visual": "PRIVACY TINT PRO隐私专业膜", "gradient": "linear-gradient(135deg,#1a1a1a,#0a0a0a,#000000,#0a0a0a,#1a1a1a)",
        "placeholder": "🔒 PRIVACY", "tag_color": "#0a0a0a",
        "features": [("5% VLT", "极高隐私度"), ("后排专属", "VIP空间设计"), ("单向视觉", "车内看外清晰"), ("防眩光", "夜间也舒适")],
        "applications": ["商务车", "VIP接待", "豪华轿车", "私人空间"], "related": ["limo-black-film.html", "chameleon-tint.html"],
    },
    {
        "filename": "chameleon-tint.html", "name": "CHAMELEON TINT",
        "subtitle": "变色龙窗膜 | 角度变色 | 独特个性",
        "tag": "🦎 变色", "title": "CHAMELEON TINT - DUMI AUTO | 变色龙窗膜",
        "description": "DUMI AUTO CHAMELEON变色龙窗膜，独特角度变色效果，从不同角度看呈现不同颜色。时尚个性之选，让您的车与众不同。",
        "keywords": "CHAMELEON TINT, 变色窗膜, 角度变色, 个性窗膜, 汽车窗膜, 时尚窗膜",
        "alt_visual": "CHAMELEON变色龙窗膜", "gradient": "linear-gradient(135deg,#9c27b0,#e91e63,#3f51b5,#00bcd4,#4caf50)",
        "placeholder": "🦎 CHAMELEON", "tag_color": "#9c27b0",
        "features": [("角度变色", "5种颜色切换"), ("个性独特", "独一无二外观"), ("隔热性能", "不影响隔热效果"), ("吸引眼球", "路上回头率100%")],
        "applications": ["年轻车主", "改装爱好者", "时尚车主", "个性追求者"], "related": ["gradient-smoke-film.html", "spectrally-selective-tint.html"],
    },
    {
        "filename": "crystalline-tint.html", "name": "CRYSTALLINE TINT",
        "subtitle": "水晶透明窗膜 | 几乎透明 | 顶级隔热",
        "tag": "💎 水晶", "title": "CRYSTALLINE TINT - DUMI AUTO | 水晶透明窗膜",
        "description": "DUMI AUTO CRYSTALLINE水晶透明窗膜，革命性的几乎透明窗膜。视觉上几乎看不到膜，但提供顶级隔热效果。",
        "keywords": "CRYSTALLINE TINT, 水晶窗膜, 透明膜, 高隔热, 汽车窗膜, 悉尼窗膜",
        "alt_visual": "CRYSTALLINE水晶透明窗膜", "gradient": "linear-gradient(135deg,#e3f2fd,#bbdefb,#90caf9,#bbdefb,#e3f2fd)",
        "placeholder": "💎 CRYSTAL", "tag_color": "#1976d2",
        "features": [("几乎透明", "视觉上看不到膜"), ("顶级隔热", "60% IR阻隔"), ("保持原车外观", "不影响美观"), ("合法合规", "符合各地法规")],
        "applications": ["原厂外观爱好者", "商务车", "豪华车", "法规严格地区"], "related": ["ceramic-ir-tint.html", "uv400-tint.html"],
    },
    {
        "filename": "spectrally-selective-tint.html", "name": "SPECTRALLY SELECTIVE TINT",
        "subtitle": "光谱选择窗膜 | 选择性阻隔 | 智能隔热",
        "tag": "🔬 光谱", "title": "SPECTRALLY SELECTIVE TINT - DUMI AUTO | 光谱选择窗膜",
        "description": "DUMI AUTO SPECTRALLY SELECTIVE光谱选择窗膜，智能选择性阻隔有害光（UV/IR），透过有益可见光。2026最新科技。",
        "keywords": "SPECTRALLY SELECTIVE, 光谱选择, 智能隔热, 选择性阻隔, 汽车窗膜, 悉尼窗膜",
        "alt_visual": "SPECTRALLY SELECTIVE光谱选择窗膜", "gradient": "linear-gradient(135deg,#4a148c,#7b1fa2,#9c27b0,#7b1fa2,#4a148c)",
        "placeholder": "🔬 SPECTRAL", "tag_color": "#7b1fa2",
        "features": [("光谱选择性", "智能阻隔有害光"), ("透过可见光", "不影响驾驶视野"), ("阻隔UV+IR", "健康又凉快"), ("2026科技", "最新窗膜科技")],
        "applications": ["科技爱好者", "豪华车主", "完美主义者", "新车主"], "related": ["ceramic-ir-tint.html", "crystalline-tint.html"],
    },
    # ===== Wrap Film 28-32 =====
    {
        "filename": "matte-color-shift-wrap.html", "name": "MATTE COLOR SHIFT WRAP",
        "subtitle": "哑光变色车衣 | 角度变色 | 个性定制",
        "tag": "🌈 变色", "title": "MATTE COLOR SHIFT WRAP - DUMI AUTO | 哑光变色车衣",
        "description": "DUMI AUTO MATTE COLOR SHIFT哑光变色车衣，从不同角度呈现不同颜色，哑光质感。彻底改变您的车外观，个性定制。",
        "keywords": "MATTE COLOR SHIFT, 哑光变色, 变色车衣, 个性定制, 汽车改色, 悉尼车衣",
        "alt_visual": "MATTE COLOR SHIFT哑光变色车衣", "gradient": "linear-gradient(135deg,#673ab7,#3f51b5,#2196f3,#03a9f4,#00bcd4)",
        "placeholder": "🌈 SHIFT", "tag_color": "#3f51b5",
        "features": [("哑光质感", "低调奢华"), ("多角度变色", "紫蓝绿渐变"), ("可移除", "不伤原厂车漆"), ("个性定制", "独一无二")],
        "applications": ["改装车主", "年轻用户", "个性化车", "展示车"], "related": ["chameleon-tint.html", "matte-protective-ppf.html"],
    },
    {
        "filename": "gloss-candy-wrap.html", "name": "GLOSS CANDY WRAP",
        "subtitle": "光面糖果车衣 | 鲜艳亮色 | 镜面光泽",
        "tag": "🍬 糖果", "title": "GLOSS CANDY WRAP - DUMI AUTO | 光面糖果车衣",
        "description": "DUMI AUTO GLOSS CANDY光面糖果车衣，鲜艳亮色+镜面光泽。多种糖果色可选：薄荷绿、樱花粉、柠檬黄，让您的车成为街头焦点。",
        "keywords": "GLOSS CANDY, 光面糖果, 鲜艳车衣, 镜面车衣, 汽车改色, 悉尼车衣",
        "alt_visual": "GLOSS CANDY光面糖果车衣", "gradient": "linear-gradient(135deg,#ff4081,#f50057,#c51162,#ff4081,#f50057)",
        "placeholder": "🍬 CANDY", "tag_color": "#f50057",
        "features": [("糖果色系", "8种亮色可选"), ("镜面光泽", "极致反光"), ("鲜艳持久", "5年不褪色"), ("可移除", "无痕换色")],
        "applications": ["年轻女性", "改装爱好者", "展示车", "个性化车"], "related": ["exotic-cherry-red-ppf.html", "matte-color-shift-wrap.html"],
    },
    {
        "filename": "carbon-fiber-wrap.html", "name": "CARBON FIBER WRAP",
        "subtitle": "碳纤维车衣 | 运动风格 | 轻量质感",
        "tag": "🏁 碳纤", "title": "CARBON FIBER WRAP - DUMI AUTO | 碳纤维车衣",
        "description": "DUMI AUTO CARBON FIBER碳纤维车衣，仿碳纤维纹理，运动风格强烈。无需真碳纤维的高价格，即可获得赛车级外观。",
        "keywords": "CARBON FIBER, 碳纤维车衣, 运动风格, 赛车外观, 汽车改色, 悉尼车衣",
        "alt_visual": "CARBON FIBER碳纤维车衣", "gradient": "linear-gradient(135deg,#212121,#424242,#212121,#000000,#212121)",
        "placeholder": "🏁 CARBON", "tag_color": "#212121",
        "features": [("仿碳纤纹理", "真实碳纤外观"), ("运动风格", "赛车级视觉"), ("价格亲民", "仅为真碳纤1/10"), ("可移除", "随时换风格")],
        "applications": ["性能车", "改装车", "运动型车主", "年轻人"], "related": ["gloss-candy-wrap.html", "matte-color-shift-wrap.html"],
    },
    {
        "filename": "brushed-metal-wrap.html", "name": "BRUSHED METAL WRAP",
        "subtitle": "拉丝金属车衣 | 工业质感 | 现代豪华",
        "tag": "🔩 拉丝", "title": "BRUSHED METAL WRAP - DUMI AUTO | 拉丝金属车衣",
        "description": "DUMI AUTO BRUSHED METAL拉丝金属车衣，工业级拉丝纹理，现代豪华风格。适合商务用车与个性化车主。",
        "keywords": "BRUSHED METAL, 拉丝金属, 工业车衣, 现代豪华, 汽车改色, 悉尼车衣",
        "alt_visual": "BRUSHED METAL拉丝金属车衣", "gradient": "linear-gradient(135deg,#90a4ae,#78909c,#607d8b,#546e7a,#455a64)",
        "placeholder": "🔩 BRUSHED", "tag_color": "#607d8b",
        "features": [("拉丝纹理", "工业级精细纹理"), ("现代豪华", "商务风范"), ("金属质感", "高档视觉效果"), ("可移除", "无损换色")],
        "applications": ["商务车", "现代车主", "个性化车", "年轻精英"], "related": ["carbon-fiber-wrap.html", "matte-color-shift-wrap.html"],
    },
    {
        "filename": "satin-pearl-wrap.html", "name": "SATIN PEARL WRAP",
        "subtitle": "缎面珍珠车衣 | 优雅光泽 | 女性首选",
        "tag": "🕊️ 缎面", "title": "SATIN PEARL WRAP - DUMI AUTO | 缎面珍珠车衣",
        "description": "DUMI AUTO SATIN PEARL缎面珍珠车衣，柔和缎面质感搭配珍珠光泽，优雅大气。是女性车主的首选车衣。",
        "keywords": "SATIN PEARL, 缎面珍珠, 优雅车衣, 女性车衣, 汽车改色, 悉尼车衣",
        "alt_visual": "SATIN PEARL缎面珍珠车衣", "gradient": "linear-gradient(135deg,#f8bbd0,#f48fb1,#f06292,#ec407a,#e91e63)",
        "placeholder": "🕊️ SATIN", "tag_color": "#e91e63",
        "features": [("缎面质感", "柔和高贵"), ("珍珠光泽", "优雅大气"), ("女性首选", "专为女性设计"), ("可移除", "随意换风格")],
        "applications": ["女性车主", "优雅车主", "展示车", "礼品车"], "related": ["gloss-candy-wrap.html", "brushed-metal-wrap.html"],
    },
]


def generate_product_page(p):
    """Generate single product HTML page"""
    related_html = ""
    for r in p["related"]:
        related_html += f'<a href="{r}" class="related-card"><span class="related-icon">→</span><span>{r.replace(".html","").replace("-"," ").title()}</span></a>\n'

    features_html = ""
    for title, desc in p["features"]:
        features_html += f'''
        <div class="product-feature-item">
            <span class="feature-icon">✓</span>
            <div><strong>{title}</strong><p>{desc}</p></div>
        </div>'''

    app_html = ""
    for app in p["applications"]:
        app_html += f'<span>{app}</span>'

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p["title"]}</title>
    <meta name="description" content="{p["description"]}">
    <meta name="keywords" content="{p["keywords"]}">
    <meta name="robots" content="index, follow">
    <meta name="last-modified" content="{TODAY}">
    <meta property="article:modified_time" content="{TODAY}T00:00:00+00:00">
    <meta property="og:title" content="{p["title"]}">
    <meta property="og:description" content="{p["description"]}">
    <meta property="og:type" content="product">
    <link rel="canonical" href="https://dumi-auto.com/products/{p["filename"]}">
    <link rel="stylesheet" href="../css/style.css">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Product",
        "name": "{p["name"]}",
        "description": "{p["description"]}",
        "brand": {{"@type": "Brand", "name": "DUMI AUTO"}},
        "offers": {{"@type": "Offer", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "seller": {{"@type": "Organization", "name": "DUMI AUTO"}}}}
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
                        <img src="../images/products/dumi_shield-1.webp" alt="{p["alt_visual"]}" style="width:100%;height:100%;object-fit:cover;border-radius:12px;" onerror="this.style.display='none';this.parentElement.innerHTML='<div style=\\'display:flex;align-items:center;justify-content:center;height:100%;font-size:48px;color:rgba(255,255,255,0.15);\\'>{p["placeholder"]}</div>'">
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
                        <div class="application-tags">{app_html}</div>
                    </div>
                    <div class="product-cta">
                        <a href="../index.html#contact" class="btn-primary">立即预约</a>
                        <a href="tel:+8613164488877" class="btn-secondary">电话咨询</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <section class="related-products">
        <div class="container">
            <h2>相关产品推荐</h2>
            <div class="related-grid">{related_html}</div>
        </div>
    </section>
    <footer class="footer">
        <div class="container">
            <p>© 2026 DUMI ...
            <p class="last-updated">Last updated: {TODAY}</p> AUTO. All Rights Reserved. | Professional Auto Protection</p>
        </div>
    </footer>
    <style>
        .product-detail {{ padding: 60px 0; }}
        .product-detail-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 30px; }}
        .product-detail-visual {{ aspect-ratio: 4/3; border-radius: 12px; display: flex; align-items: center; justify-content: center; }}
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
</html>'''
    return html


def main():
    """Generate 15 products from pool based on today's day-of-year"""
    # Date-based selection: 30+ pool → pick 15 by date hash
    import hashlib
    day_hash = int(hashlib.md5(TODAY.encode()).hexdigest(), 16)
    n = len(PRODUCT_POOL)
    # Rotate: 15 products for today
    start = day_hash % n
    selected = [PRODUCT_POOL[(start + i) % n] for i in range(15)]

    created = []
    for p in selected:
        filepath = os.path.join(BASE_DIR, p["filename"])
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(generate_product_page(p))
        created.append(p["filename"])
        print(f"✅ Created/Updated: {p['filename']}")

    # Generate all 30+ products (in case rotation needs them)
    print(f"\n📦 Pool has {len(PRODUCT_POOL)} products total")
    print(f"🎯 Today's {len(selected)} picked: {created[:5]}... ({len(created)} total)")


if __name__ == "__main__":
    main()
