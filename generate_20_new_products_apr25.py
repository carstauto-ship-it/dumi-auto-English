#!/usr/bin/env python3
"""DUMI AUTO - Generate 20 new SEO-optimized product pages (Batch 2026-04-25)"""
import os
import json

BASE_DIR = "/Users/carstauto/.openclaw/workspace/dumi-auto-website/products"
CSS_LINK = "../css/style.css"

PRODUCTS = [
    # ========== PPF 1-7 ==========
    {
        "filename": "ninja-matte-ppf.html",
        "name": "NINJA MATTE PPF",
        "subtitle": "忍者哑光漆面保护膜 | 极致哑光 | 军事级防护",
        "tag": "🥷 忍者",
        "title": "NINJA MATTE PPF - DUMI AUTO | 忍者哑光漆面保护膜",
        "description": "DUMI AUTO NINJA MATTE忍者哑光漆面保护膜，采用顶级哑光处理技术，为车漆提供如忍者般神秘低调的哑光外观。融合军事级TPU防护与哑光美学，是追求极致个性车主的不二之选。",
        "keywords": "忍者哑光PPF, 哑光车衣, 军事级PPF, 低调车衣, 汽车保护膜, 悉尼PPF, 洛杉矶PPF",
        "alt_visual": "NINJA MATTE忍者哑光PPF效果展示",
        "gradient": "linear-gradient(135deg,#1a1a1a,#2d2d2d,#3d3d3d,#2d2d2d,#1a1a1a)",
        "placeholder": "🥷 NINJA",
        "tag_color": "#1a1a1a",
        "features": [
            ("极致哑光质感", "特殊哑光处理，表面如忍者般神秘低调"),
            ("军事级TPU基材", "10mil顶级基材，顶级抗冲击性能"),
            ("自修复功能", "轻微划痕热修复，哑光表面持久如新"),
            ("抗化学腐蚀", "抵抗酸雨、虫子、鸟粪等腐蚀性物质"),
        ],
        "applications": ["改装车主", "性能轿车", "商务哑光车型", "个性车主"],
        "related": ["stealth-matte-black-ppf.html", "matte-protective-ppf.html", "stealth-ppf.html"],
    },
    {
        "filename": "racing-green-ppf.html",
        "name": "RACING GREEN PPF",
        "subtitle": "赛车绿漆面保护膜 | 经典英伦 | 运动风范",
        "tag": "🏎️ 赛车绿",
        "title": "RACING GREEN PPF - DUMI AUTO | 经典赛车绿漆面保护膜",
        "description": "DUMI AUTO RACING GREEN赛车绿漆面保护膜，灵感源自经典英国赛车绿，为您的车辆注入纯正的赛车血统。深邃的绿色在光线下呈现宝石般的光泽，同时提供顶级PPF防护。",
        "keywords": "赛车绿PPF, 绿色车衣, 英伦风格, 运动车衣, 汽车保护膜, 悉尼PPF, 洛杉矶PPF",
        "alt_visual": "RACING GREEN赛车绿PPF效果展示",
        "gradient": "linear-gradient(135deg,#004225,#006b3c,#008f4c,#006b3c,#004225)",
        "placeholder": "🏎️ RACING",
        "tag_color": "#006b3c",
        "features": [
            ("经典赛车绿", "纯正英伦赛车色泽，彰显不凡品位"),
            ("宝石光泽", "特殊调色，光线下呈现宝石般深邃光泽"),
            ("顶级TPU防护", "10mil厚度，有效抵御碎石与划痕"),
            ("自修复涂层", "轻微划痕自动修复，持久如新"),
        ],
        "applications": ["性能轿车", "英伦风格车主", "经典车爱好者", "个性化改装"],
        "related": ["midnight-blue-ppf.html", "metallic-ppf.html", "color-ppf.html"],
    },
    {
        "filename": "aurora-silver-ppf.html",
        "name": "AURORA SILVER PPF",
        "subtitle": "极光银漆面保护膜 | 科技银光 | 未来感十足",
        "tag": "🌌 极光银",
        "title": "AURORA SILVER PPF - DUMI AUTO | 极光银漆面保护膜",
        "description": "DUMI AUTO AURORA SILVER极光银漆面保护膜，以北欧极光为灵感，呈现银蓝色调的科技感光泽。在不同光线下呈现微妙变化的极光效果，让您的车辆成为科技与艺术的完美结合。",
        "keywords": "极光银PPF, 银色车衣, 科技感PPF, 汽车保护膜, 悉尼PPF, 洛杉矶PPF, 未来感车衣",
        "alt_visual": "AURORA SILVER极光银PPF效果展示",
        "gradient": "linear-gradient(135deg,#c0c0c0,#a8b5c4,#d4dde8,#a8b5c4,#c0c0c0)",
        "placeholder": "🌌 AURORA",
        "tag_color": "#78909c",
        "features": [
            ("极光银蓝色调", "银蓝极光色，在不同光线下呈现微妙变化"),
            ("科技感光泽", "如北欧极光般的神秘科技美感"),
            ("顶级防护", "10mil TPU基材，军工级抗冲击"),
            ("自修复功能", "轻微划痕热修复，保持完美外观"),
        ],
        "applications": ["科技爱好者", "电动车车主", "现代简约风格", "改装车主"],
        "related": ["crystalline-ppf.html", "pearl-white-ppf.html", "gloss-black-ppf.html"],
    },
    {
        "filename": "sunset-orange-ppf.html",
        "name": "SUNSET ORANGE PPF",
        "subtitle": "落日橙漆面保护膜 | 活力橙调 | 热情奔放",
        "tag": "🌅 落日",
        "title": "SUNSET ORANGE PPF - DUMI AUTO | 落日橙漆面保护膜",
        "description": "DUMI AUTO SUNSET ORANGE落日橙漆面保护膜，以落日余晖为灵感，呈现温暖奔放的橙调光泽。让您的车辆如沐浴在金色阳光中，充满活力与激情，是追求个性表达的车主首选。",
        "keywords": "落日橙PPF, 橙色车衣, 活力车衣, 改装车衣, 汽车保护膜, 悉尼PPF, 洛杉矶PPF",
        "alt_visual": "SUNSET ORANGE落日橙PPF效果展示",
        "gradient": "linear-gradient(135deg,#ff4500,#ff6a00,#ff8c00,#ff6a00,#ff4500)",
        "placeholder": "🌅 SUNSET",
        "tag_color": "#ff6a00",
        "features": [
            ("落日橙调", "温暖橙色渐变，如落日余晖般绚烂"),
            ("高饱和色彩", "色彩饱满艳丽，视觉冲击力强"),
            ("顶级防护", "TPU基材有效保护车漆免受伤害"),
            ("自修复功能", "轻微划痕自动修复，色彩持久如新"),
        ],
        "applications": ["年轻车主", "改装爱好者", "橙色系车辆", "个性车主"],
        "related": ["exotic-cherry-red-ppf.html", "color-ppf.html", "metallic-ppf.html"],
    },
    {
        "filename": "electric-blue-ppf.html",
        "name": "ELECTRIC BLUE PPF",
        "subtitle": "电光蓝漆面保护膜 | 电能蓝 | 未来美学",
        "tag": "⚡ 电光",
        "title": "ELECTRIC BLUE PPF - DUMI AUTO | 电光蓝漆面保护膜",
        "description": "DUMI AUTO ELECTRIC BLUE电光蓝漆面保护膜，以电能蓝色为主题，呈现充满未来科技感的视觉体验。深邃的蓝色中透着电光般的闪动，是电动车车主和科技爱好者的完美选择。",
        "keywords": "电光蓝PPF, 蓝色车衣, 电动车PPF, 科技感车衣, 汽车保护膜, 悉尼PPF, 洛杉矶PPF",
        "alt_visual": "ELECTRIC BLUE电光蓝PPF效果展示",
        "gradient": "linear-gradient(135deg,#0047ab,#0055cc,#0066ee,#0055cc,#0047ab)",
        "placeholder": "⚡ ELECTRIC",
        "tag_color": "#0055cc",
        "features": [
            ("电光蓝色调", "电能蓝主题，充满未来科技感"),
            ("电光闪动效果", "光线下呈现电光般的微妙闪动"),
            ("电动车专属", "完美契合电动车的科技形象"),
            ("顶级防护", "10mil TPU，有效抵御各类伤害"),
        ],
        "applications": ["电动车车主", "科技爱好者", "蓝色系车辆", "年轻车主"],
        "related": ["midnight-blue-ppf.html", "aurora-silver-ppf.html", "infrared-ceramic-ppf.html"],
    },
    {
        "filename": "luxury-gold-ppf.html",
        "name": "LUXURY GOLD PPF",
        "subtitle": "奢华金漆面保护膜 | 金色光泽 | 尊贵典雅",
        "tag": "👑 奢华金",
        "title": "LUXURY GOLD PPF - DUMI AUTO | 奢华金漆面保护膜",
        "description": "DUMI AUTO LUXURY GOLD奢华金漆面保护膜，专为顶级豪华车型设计的金色光泽保护膜。低调而不失奢华，金色光泽恰到好处，彰显车主的尊贵身份与非凡品位。",
        "keywords": "奢华金PPF, 金色车衣, 豪华车衣, 尊贵车衣, 汽车保护膜, 悉尼PPF, 洛杉矶PPF",
        "alt_visual": "LUXURY GOLD奢华金PPF效果展示",
        "gradient": "linear-gradient(135deg,#b8860b,#daa520,#ffd700,#daa520,#b8860b)",
        "placeholder": "👑 GOLD",
        "tag_color": "#b8860b",
        "features": [
            ("低调金色光泽", "恰到好处的金色，不过分张扬"),
            ("尊贵典雅", "专为豪华车型设计，彰显品位"),
            ("顶级TPU基材", "10mil厚度，军工级防护"),
            ("自修复功能", "轻微划痕自动修复，持久如新"),
        ],
        "applications": ["豪华轿车", "超豪华车型", "商务人士", "追求品位的车主"],
        "related": ["crystalline-ppf.html", "pearl-white-ppf.html", "ultimate-plus.html"],
    },
    {
        "filename": "evo-matte-ppf.html",
        "name": "EVO MATTE PPF",
        "subtitle": "EVO竞技哑光保护膜 | 竞技级别 | 赛道基因",
        "tag": "🏁 EVO",
        "title": "EVO MATTE PPF - DUMI AUTO | EVO竞技哑光保护膜",
        "description": "DUMI AUTO EVO MATTE竞技哑光保护膜，源自赛道的基因，专为高性能车辆设计的竞技级别哑光PPF。提供极致防护的同时呈现纯粹的竞技哑光风格，是赛车手和性能爱好者的终极选择。",
        "keywords": "EVO竞技PPF, 赛道PPF, 竞技级别车衣, 高性能车衣, 汽车保护膜, 悉尼PPF, 洛杉矶PPF",
        "alt_visual": "EVO MATTE竞技哑光PPF效果展示",
        "gradient": "linear-gradient(135deg,#212121,#424242,#616161,#424242,#212121)",
        "placeholder": "🏁 EVO",
        "tag_color": "#424242",
        "features": [
            ("竞技级别防护", "赛道级TPU配方，极致抗冲击"),
            ("纯粹哑光风格", "不含任何光泽，呈现最纯粹的竞技哑光"),
            ("耐高温性能", "特殊配方，可承受赛道高温环境"),
            ("自修复功能", "轻微划痕热修复，赛场归来依旧如新"),
        ],
        "applications": ["赛车手", "高性能车辆", "赛道日爱好者", "性能改装车"],
        "related": ["armor-ppf.html", "ninja-matte-ppf.html", "stealth-matte-black-ppf.html"],
    },
    # ========== WINDOW TINT 8-14 ==========
    {
        "filename": "stealth-ceramic-tint.html",
        "name": "STEALTH CERAMIC TINT",
        "subtitle": "隐形陶瓷窗膜 | 陶瓷隔热 | 信号无阻",
        "tag": "🔮 隐形",
        "title": "STEALTH CERAMIC TINT - DUMI AUTO | 隐形陶瓷窗膜",
        "description": "DUMI AUTO STEALTH CERAMIC隐形陶瓷窗膜，采用最先进纳米陶瓷技术，实现极致透明度与顶级隔热的完美平衡。完全不影响手机、GPS、蓝牙信号，是注重科技体验车主的最优选择。",
        "keywords": "隐形陶瓷窗膜, 纳米陶瓷窗膜, 信号无阻窗膜, 汽车窗膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "STEALTH CERAMIC隐形陶瓷窗膜效果展示",
        "gradient": "linear-gradient(135deg,#1a237e,#1a237e,#283593,#1a237e)",
        "placeholder": "🔮 CERAMIC",
        "tag_color": "#1a237e",
        "features": [
            ("纳米陶瓷技术", "最先进陶瓷粒子，顶级隔热性能"),
            ("信号完全无阻", "非金属，不干扰任何电子设备信号"),
            ("极致透明度", "高透光率，视野清晰如透明玻璃"),
            ("阻隔紫外线", "99%以上UVA/UVB，全天侯防护"),
        ],
        "applications": ["科技爱好者", "商务人士", "电动车车主", "经常使用手机GPS的车主"],
        "related": ["ceramic-tint.html", "ceramic-pro-window-film.html", "infrared-rejection-tint.html"],
    },
    {
        "filename": "arctic-white-tint.html",
        "name": "ARCTIC WHITE TINT",
        "subtitle": "北极白窗膜 | 清新白色 | 独特个性",
        "tag": "❄️ 北极白",
        "title": "ARCTIC WHITE TINT - DUMI AUTO | 北极白时尚窗膜",
        "description": "DUMI AUTO ARCTIC WHITE北极白窗膜，清新的白色调为车窗带来独特的视觉体验。在保持隐私和隔热的同时，让您的车辆与众不同，成为道路上最独特的存在。",
        "keywords": "北极白窗膜, 白色窗膜, 时尚窗膜, 个性窗膜, 汽车窗膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "ARCTIC WHITE北极白窗膜效果展示",
        "gradient": "linear-gradient(135deg,#f5f5f5,#e0e0e0,#fafafa,#e0e0e0,#f5f5f5)",
        "placeholder": "❄️ ARCTIC",
        "tag_color": "#bdbdbd",
        "features": [
            ("清新北极白色", "独特白色调，道路上的独特风景"),
            ("良好隐私保护", "白色有效遮挡车内视野"),
            ("隔热性能", "阻隔太阳热量，降低车内温度"),
            ("信号无干扰", "陶瓷技术，不影响电子设备"),
        ],
        "applications": ["个性车主", "年轻用户", "白色系车辆", "改装车主"],
        "related": ["ice-blue-tint.html", "ceramic-tint.html", "gradient-smoke-film.html"],
    },
    {
        "filename": "midnight-purple-tint.html",
        "name": "MIDNIGHT PURPLE TINT",
        "subtitle": "午夜紫窗膜 | 神秘紫色 | 低调华丽",
        "tag": "🌌 午夜紫",
        "title": "MIDNIGHT PURPLE TINT - DUMI AUTO | 午夜紫窗膜",
        "description": "DUMI AUTO MIDNIGHT PURPLE午夜紫窗膜，深邃的紫色在暗处呈现神秘的黑色，在光线下则透出优雅的紫色光泽。为车窗增添低调而不失个性的神秘气质，深受改装车主喜爱。",
        "keywords": "午夜紫窗膜, 紫色窗膜, 神秘窗膜, 改装窗膜, 汽车窗膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "MIDNIGHT PURPLE午夜紫窗膜效果展示",
        "gradient": "linear-gradient(135deg,#1a0033,#3d0066,#660099,#3d0066,#1a0033)",
        "placeholder": "🌌 PURPLE",
        "tag_color": "#660099",
        "features": [
            ("神秘午夜紫调", "暗处呈黑，光线透紫，神秘优雅"),
            ("深度隐私保护", "有效阻挡外界视线"),
            ("阻隔红外线", "减少太阳热量，保持车内凉爽"),
            ("独特个性表达", "与众不同的车窗色调选择"),
        ],
        "applications": ["改装车主", "紫色系车辆", "个性车主", "神秘风格爱好者"],
        "related": ["limo-black-film.html", "deep-black-tint.html", "stealth-matte-tint.html"],
    },
    {
        "filename": "military-grade-tint.html",
        "name": "MILITARY GRADE TINT",
        "subtitle": "军用级窗膜 | 最高防护 | 坚不可摧",
        "tag": "🎖️ 军用",
        "title": "MILITARY GRADE TINT - DUMI AUTO | 军用级防护窗膜",
        "description": "DUMI AUTO MILITARY GRADE军用级窗膜，采用军事级材料和工艺，提供最高级别的安全防护与隔热性能。防弹级别抗冲击，有效阻挡紫外线和红外线，是需要最高级别保护的车主的终极选择。",
        "keywords": "军用级窗膜, 军用窗膜, 安全窗膜, 防弹窗膜, 汽车窗膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "MILITARY GRADE军用级窗膜效果展示",
        "gradient": "linear-gradient(135deg,#1b5e20,#2e7d32,#388e3c,#2e7d32,#1b5e20)",
        "placeholder": "🎖️ MILITARY",
        "tag_color": "#1b5e20",
        "features": [
            ("军事级材料", "采用军事规格材料和工艺"),
            ("防弹级抗冲击", "多层复合结构，有效抵御冲击"),
            ("顶级隔热", "阻隔95%以上红外线热量"),
            ("完全阻隔UV", "99%以上UVA/UVB全面防护"),
        ],
        "applications": ["商务要员", "安全需求高的人士", "军用车辆", "VIP保护"],
        "related": ["security-film.html", "clear-protective-tint.html", "ceramic-pro-window-film.html"],
    },
    {
        "filename": "sport-red-tint.html",
        "name": "SPORT RED TINT",
        "subtitle": "运动红窗膜 | 热血红调 | 赛道激情",
        "tag": "🏁 运动红",
        "title": "SPORT RED TINT - DUMI AUTO | 运动红窗膜",
        "description": "DUMI AUTO SPORT RED运动红窗膜，充满热血的运动红色调，为您的车窗注入赛道激情。在提供隐私保护和隔热的同时，让您的车辆散发运动气息，彰显驾驶者的运动基因。",
        "keywords": "运动红窗膜, 红色窗膜, 赛道风格窗膜, 汽车窗膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "SPORT RED运动红窗膜效果展示",
        "gradient": "linear-gradient(135deg,#8b0000,#b71c1c,#d32f2f,#b71c1c,#8b0000)",
        "placeholder": "🏁 RED",
        "tag_color": "#b71c1c",
        "features": [
            ("热血运动红", "充满激情的红色调，彰显运动基因"),
            ("隐私保护", "深红色调有效遮挡车内视野"),
            ("隔热性能", "阻隔太阳热量，降低车内温度"),
            ("信号无干扰", "陶瓷技术，不影响电子设备"),
        ],
        "applications": ["运动车型车主", "赛道爱好者", "红色系车辆", "年轻车主"],
        "related": ["carbon-tint.html", "gradient-smoke-film.html", "color-stable-film.html"],
    },
    {
        "filename": "platinum-privacy-tint.html",
        "name": "PLATINUM PRIVACY TINT",
        "subtitle": "铂金隐私窗膜 | 极致隐私 | 铂金品质",
        "tag": "🔒 铂金隐私",
        "title": "PLATINUM PRIVACY TINT - DUMI AUTO | 铂金隐私窗膜",
        "description": "DUMI AUTO PLATINUM PRIVACY铂金隐私窗膜，以铂金级品质为您提供极致隐私保护。超深色设计有效阻挡外界视线，同时保持优雅的车窗外观，是注重隐私的高端车主的首选。",
        "keywords": "铂金隐私窗膜, 隐私窗膜, 高端窗膜, 深色窗膜, 汽车窗膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "PLATINUM PRIVACY铂金隐私窗膜效果展示",
        "gradient": "linear-gradient(135deg,#0d0d0d,#1a1a1a,#2c2c2c,#1a1a1a,#0d0d0d)",
        "placeholder": "🔒 PLATINUM",
        "tag_color": "#424242",
        "features": [
            ("极致隐私保护", "铂金色泽，极致深色，隐私无死角"),
            ("铂金级品质", "精选材料和工艺，品质卓越"),
            ("优雅外观", "铂金色调，优雅大方"),
            ("隔热节能", "阻隔太阳热量，降低空调能耗"),
        ],
        "applications": ["高端车主", "商务人士", "家庭用车", "注重隐私的人士"],
        "related": ["limo-black-film.html", "deep-black-tint.html", "privacy-smoke-film.html"],
    },
    {
        "filename": "smart-tint-adaptive.html",
        "name": "SMART TINT ADAPTIVE",
        "subtitle": "智能变色窗膜 | 自动调节 | 科技前沿",
        "tag": "🧠 智能",
        "title": "SMART TINT ADAPTIVE - DUMI AUTO | 智能变色窗膜",
        "description": "DUMI AUTO SMART TINT ADAPTIVE智能变色窗膜，采用先进电致变色技术，能够根据光线强度自动调节透光率。白天强光下自动变深，夜间自动变浅，始终为您提供最佳视觉体验。",
        "keywords": "智能变色窗膜, 电致变色窗膜, 自动调光窗膜, 汽车窗膜, 悉尼窗膜, 洛杉矶窗膜",
        "alt_visual": "SMART TINT ADAPTIVE智能变色窗膜效果展示",
        "gradient": "linear-gradient(135deg,#4a148c,#6a1b9a,#7b1fa2,#6a1b9a,#4a148c)",
        "placeholder": "🧠 SMART",
        "tag_color": "#6a1b9a",
        "features": [
            ("电致变色技术", "根据光线自动调节透光率"),
            ("白天自动变深", "强光下自动加深，阻挡更多热量"),
            ("夜间自动变浅", "夜间自动变浅，保持清晰视野"),
            ("一键手动调节", "也可手动设置您喜欢的透光率"),
        ],
        "applications": ["科技爱好者", "经常不同光线环境驾驶", "豪华车型", "追求极致体验的车主"],
        "related": ["ceramic-tint.html", "electrochromic-film.html", "stealth-ceramic-tint.html"],
    },
    # ========== CERAMIC COATING 15-20 ==========
    {
        "filename": "quartz-ceramic-coating.html",
        "name": "QUARTZ CERAMIC COATING",
        "subtitle": "石英陶瓷镀晶 | 晶体硬度 | 持久保护",
        "tag": "🔷 石英",
        "title": "QUARTZ CERAMIC COATING - DUMI AUTO | 石英陶瓷镀晶",
        "description": "DUMI AUTO QUARTZ CERAMIC石英陶瓷镀晶，采用高纯度石英晶体与先进陶瓷配方的完美结合。提供接近钻石的硬度与持久的光泽保护，单次施工可维持3-5年，是长效车漆保护的终极方案。",
        "keywords": "石英陶瓷镀晶, 石英镀晶, 长效镀晶, 汽车镀晶, 悉尼镀晶, 洛杉矶镀晶",
        "alt_visual": "QUARTZ CERAMIC石英陶瓷镀晶效果展示",
        "gradient": "linear-gradient(135deg,#e8eaf6,#c5cae9,#9fa8da,#c5cae9,#e8eaf6)",
        "placeholder": "🔷 QUARTZ",
        "tag_color": "#5c6bc0",
        "features": [
            ("高纯度石英晶体", "纯天然石英，高硬度高光泽"),
            ("3-5年长效保护", "单次施工，长期保护，省心省钱"),
            ("9H顶级硬度", "石英+陶瓷复合硬度，有效抵御划痕"),
            ("疏水自洁", "水珠滚落，污渍不易附着"),
        ],
        "applications": ["豪华车型", "追求长效保护的车主", "懒人车主", "高品质车主"],
        "related": ["diamond-ceramic-coating.html", "graphene-coating.html", "fusion-ceramic-coating.html"],
    },
    {
        "filename": "titanium-ceramic-coating.html",
        "name": "TITANIUM CERAMIC COATING",
        "subtitle": "钛金陶瓷镀晶 | 钛金光泽 | 航天科技",
        "tag": "🛩️ 钛金",
        "title": "TITANIUM CERAMIC COATING - DUMI AUTO | 钛金陶瓷镀晶",
        "description": "DUMI AUTO TITANIUM CERAMIC钛金陶瓷镀晶，融合航天级钛金材料与先进陶瓷技术。呈现独特的钛金属光泽，提供超越传统的硬度与耐久性，是车漆保护领域的技术巅峰。",
        "keywords": "钛金陶瓷镀晶, 钛金镀晶, 航天级镀晶, 汽车镀晶, 悉尼镀晶, 洛杉矶镀晶",
        "alt_visual": "TITANIUM CERAMIC钛金陶瓷镀晶效果展示",
        "gradient": "linear-gradient(135deg,#546e7a,#78909c,#90a4ae,#78909c,#546e7a)",
        "placeholder": "🛩️ TITANIUM",
        "tag_color": "#546e7a",
        "features": [
            ("航天级钛金材料", "源自航天科技的特殊材料"),
            ("独特钛金光泽", "金属感光泽，与众不同的视觉效果"),
            ("超耐久性", "钛金+陶瓷，持久度超越传统镀晶"),
            ("抗化学腐蚀", "特殊配方，抵抗各类腐蚀性物质"),
        ],
        "applications": ["豪华车型", "航天科技爱好者", "追求高科技车主", "超跑车主"],
        "related": ["graphene-coating.html", "diamond-ceramic-coating.html", "quartz-ceramic-coating.html"],
    },
    {
        "filename": "marine-ceramic-coating.html",
        "name": "MARINE CERAMIC COATING",
        "subtitle": "航海陶瓷镀晶 | 盐雾防护 | 沿海专用",
        "tag": "⚓ 航海",
        "title": "MARINE CERAMIC COATING - DUMI AUTO | 航海陶瓷镀晶",
        "description": "DUMI AUTO MARINE CERAMIC航海陶瓷镀晶，专为沿海地区和海洋环境设计的特殊配方。卓越的抗盐雾腐蚀能力，有效抵御海风中的盐分对车漆的侵蚀，是海边车主的必备保护。",
        "keywords": "航海陶瓷镀晶, 盐雾防护镀晶, 沿海专用镀晶, 汽车镀晶, 悉尼镀晶, 海洋环境镀晶",
        "alt_visual": "MARINE CERAMIC航海陶瓷镀晶效果展示",
        "gradient": "linear-gradient(135deg,#006064,#00838f,#00acc1,#00838f,#006064)",
        "placeholder": "⚓ MARINE",
        "tag_color": "#00838f",
        "features": [
            ("抗盐雾配方", "特殊配方，有效抵御海风盐分侵蚀"),
            ("沿海环境专用", "专为海边和海洋气候设计"),
            ("防腐蚀保护", "阻隔盐雾、酸雨等腐蚀性环境因素"),
            ("持久光泽", "保持车漆光泽，延缓老化"),
        ],
        "applications": ["沿海地区车主", "海岛度假车主", "游艇车主", "海洋气候地区"],
        "related": ["anti-oxidation-coating.html", "graphene-coating.html", "hydrophobic-topcoat.html"],
    },
    {
        "filename": "nano-scratch-coating.html",
        "name": "NANO SCRATCH COATING",
        "subtitle": "纳米抗划镀晶 | 超级硬度 | 极致防护",
        "tag": "🛡️ 纳米抗划",
        "title": "NANO SCRATCH COATING - DUMI AUTO | 纳米抗划镀晶",
        "description": "DUMI AUTO NANO SCRATCH纳米抗划镀晶，采用最新纳米技术，在车漆表面形成超级硬度的保护层。硬度超过传统镀晶产品，有效抵御日常使用中的各类划痕，是车漆防护的最强盾牌。",
        "keywords": "纳米抗划镀晶, 抗划痕镀晶, 超级硬度镀晶, 汽车镀晶, 悉尼镀晶, 洛杉矶镀晶",
        "alt_visual": "NANO SCRATCH纳米抗划镀晶效果展示",
        "gradient": "linear-gradient(135deg,#1a237e,#283593,#3949ab,#283593,#1a237e)",
        "placeholder": "🛡️ SCRATCH",
        "tag_color": "#3949ab",
        "features": [
            ("纳米超级硬度", "最新纳米技术，硬度超越传统产品"),
            ("抗日常划痕", "有效抵御钥匙、树枝等日常划痕"),
            ("透明保护层", "不影响原厂车漆颜色和光泽"),
            ("长效保护", "单次施工，维持1-2年"),
        ],
        "applications": ["密集停车环境", "多车辆家庭", "新手车主", "注重车漆保护的车主"],
        "related": ["diamond-ceramic-coating.html", "quartz-ceramic-coating.html", "self-leveling-coating.html"],
    },
    {
        "filename": "crystal-glass-topcoat.html",
        "name": "CRYSTAL GLASS TOPCOAT",
        "subtitle": "水晶玻璃顶涂层 | 玻璃质感 | 极致光滑",
        "tag": "🪟 水晶玻璃",
        "title": "CRYSTAL GLASS TOPCOAT - DUMI AUTO | 水晶玻璃顶涂层",
        "description": "DUMI AUTO CRYSTAL GLASS水晶玻璃顶涂层，在车漆表面形成如水晶般透明的玻璃保护层。极致光滑的表面让污渍无处附着，雨水冲刷即可清洁，是最便捷的车漆保护方案。",
        "keywords": "水晶玻璃顶涂层, 玻璃镀晶, 光滑车漆涂层, 汽车镀晶, 悉尼镀晶, 洛杉矶镀晶",
        "alt_visual": "CRYSTAL GLASS水晶玻璃顶涂层效果展示",
        "gradient": "linear-gradient(135deg,#e0f7fa,#b2ebf2,#80deea,#b2ebf2,#e0f7fa)",
        "placeholder": "🪟 GLASS",
        "tag_color": "#4dd0e1",
        "features": [
            ("水晶玻璃质感", "透明如水晶，极致光滑的玻璃触感"),
            ("超级疏水性", "水珠快速滚落，带走污渍"),
            ("防污自洁", "污渍无处附着，清水即可清洁"),
            ("增强光泽", "提升车漆光泽，呈现镜子般效果"),
        ],
        "applications": ["懒人车主", "经常户外停车", "追求便捷的车主", "雨季地区车主"],
        "related": ["hydrophobic-topcoat.html", "glass-ceramic-topcoat.html", "nano-ceramic-coating-spray.html"],
    },
    {
        "filename": "uv-guard-topcoat.html",
        "name": "UV GUARD TOPCOAT",
        "subtitle": "紫外线防护顶涂层 | 防晒老化 | 色彩保鲜",
        "tag": "☀️ 防晒",
        "title": "UV GUARD TOPCOAT - DUMI AUTO | 紫外线防护顶涂层",
        "description": "DUMI AUTO UV GUARD紫外线防护顶涂层，专为防止车漆老化褪色设计。特殊UV抑制剂形成透明保护层，100%阻隔有害紫外线，是保护爱车原厂色泽、延缓老化的最佳选择。",
        "keywords": "紫外线防护涂层, 防晒涂层, 防老化镀晶, 汽车镀晶, 悉尼镀晶, 洛杉矶镀晶",
        "alt_visual": "UV GUARD紫外线防护顶涂层效果展示",
        "gradient": "linear-gradient(135deg,#ff8f00,#ffa000,#ffb300,#ffa000,#ff8f00)",
        "placeholder": "☀️ UV GUARD",
        "tag_color": "#ffa000",
        "features": [
            ("100% UV阻隔", "特殊配方，完全阻隔有害紫外线"),
            ("防止褪色老化", "保护原厂车漆颜色，长久如新"),
            ("延缓氧化", "阻隔空气接触，防止车漆氧化"),
            ("透明无色", "不影响原厂车漆色泽"),
        ],
        "applications": ["户外停车车辆", "强烈日晒地区", "白色车漆", "注重保值的车主"],
        "related": ["anti-oxidation-coating.html", "uv-protection-film.html", "solar-defense-film.html"],
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
    "diamond-ceramic-coating.html": ("💎 钻石", "DIAMOND CERAMIC", "钻石陶瓷镀晶"),
    "stealth-matte-black-ppf.html": ("🖤 哑光黑", "STEALTH MATTE BLACK", "哑光黑PPF"),
    "infrared-ceramic-ppf.html": ("🌡️ 红外陶瓷", "INFRARED CERAMIC", "红外陶瓷PPF"),
    "fusion-ceramic-coating.html": ("⚡ 融合", "FUSION CERAMIC", "融合陶瓷镀晶"),
    "glass-ceramic-topcoat.html": ("🪟 玻璃", "GLASS CERAMIC", "玻璃陶瓷顶涂层"),
    "electrochromic-film.html": ("🔮 电致变色", "ELECTROCHROMIC", "电致变色窗膜"),
}

def get_related_html(related_files):
    html = '<div class="products-grid">\n'
    for fname in related_files:
        if fname in RELATED_PRODUCTS_MAP:
            tag, name, desc = RELATED_PRODUCTS_MAP[fname]
            gradient = "#1a1a2e"
            if "PPF" in fname or fname in ["ultimate-plus.html", "stealth-ppf.html", "armor-ppf.html", "matte-protective-ppf.html", "urban-shield-ppf.html"]:
                gradient = "#1a1a2e"
            if "COLOR" in name.upper() or "改色" in desc or "CHERRY" in name.upper() or "RED" in name.upper():
                gradient = "#8B0000"
            if "STEALTH" in name.upper():
                gradient = "#2c2c2c"
            if "ARMOR" in name.upper():
                gradient = "#1a3a3a"
            if "CERAMIC" in name.upper() and "TINT" not in fname and "COATING" not in fname:
                gradient = "#1a3a5c"
            if "CERAMIC" in name.upper() and "COATING" in fname:
                gradient = "#1a3a5c"
            if "SATIN" in name.upper():
                gradient = "#6a6a6a"
            if "GRAPHENE" in name.upper():
                gradient = "#0f2027"
            if "UV" in name.upper() or "SOLAR" in name.upper():
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
            if "PRIME" in name.upper():
                gradient = "#1565c0"
            if "PRIVACY" in name.upper():
                gradient = "#1a1a1a"
            if "SMART" in name.upper() or "ELECTROCHROMIC" in name.upper():
                gradient = "#4a148c"
            if "FUSION" in name.upper():
                gradient = "#0d47a1"
            if "QUARTZ" in name.upper():
                gradient = "#5c6bc0"
            if "TITANIUM" in name.upper():
                gradient = "#546e7a"
            if "MARINE" in name.upper():
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
            <h2>相关产品</h2>
            {get_related_html(p["related"])}
        </div>
    </section>
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand"><h3>DUMI<span>AUTO</span></h3><p>专业汽车保护膜专家 | 洛杉矶 & 悉尼</p></div>
                <div class="footer-links"><a href="../index.html">首页</a><a href="../index.html#products">产品中心</a><a href="../index.html#services">服务项目</a><a href="../index.html#about">关于我们</a><a href="../index.html#contact">联系我们</a></div>
                <div class="footer-contact"><p>📧 info@dumi-auto.com</p><p>📞 +1 (949) 000-0000</p><p>📍 Los Angeles, CA</p></div>
            </div>
            <div class="footer-copy"><p>&copy; 2026 DUMI AUTO. All rights reserved.</p></div>
        </div>
    </footer>
</body>
</html>'''
    return html

def main():
    print("🎯 DUMI AUTO - Generating 20 New Products (Batch 2026-04-25)")
    print("=" * 60)
    generated = []
    for i, p in enumerate(PRODUCTS, 1):
        filepath = os.path.join(BASE_DIR, p["filename"])
        html = generate_product_page(p)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        generated.append(p["filename"])
        print(f"  [{i:02d}/20] ✅ {p['filename']}")

    print(f"\n✅ Successfully generated {len(generated)} product pages!")
    print("\nNew products:")
    for f in generated:
        print(f"  - {f}")
    return generated

if __name__ == "__main__":
    main()
