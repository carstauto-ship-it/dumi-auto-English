#!/usr/bin/env python3
"""Fix Chinese index-cn.html - remove XPEL references."""
import re

with open('/Users/carstauto/.openclaw/workspace/dumi-auto-website/index-cn.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# Chinese XPEL replacements
replacements = [
    ('守护爱车 · 始于XPEL', '守护爱车 · 源自工厂'),
    ('🔥 XPEL官方授权', '🏭 工厂直营'),
    ('XPEL官方授权', '工厂直营品牌'),
    ('正规XPEL授权经销商', '正规工厂授权经销商'),
    ('所有产品均享XPEL原厂质保', '所有产品均享工厂原厂质保'),
    ('XPEL授权经销商', '工厂直营经销商'),
    ('DUMI AUTO坐落于洛杉矶，是一家专业从事高端汽车保护膜施工与销售的服务机构。作为XPEL官方授权经销商',
     'DUMI AUTO坐落于洛杉矶，是一家专业从事高端汽车保护膜施工与销售的工厂直营服务机构。作为专业PPF生产厂家'),
    ('我们的团队由经验丰富的技师组成，每位技师都经过XPEL官方培训认证',
     '我们的团队由经验丰富的技师组成，每位技师都经过专业培训认证'),
    ('✅ XPEL授权经销商', '🏭 工厂直营'),
    ('官方培训技师', '专业培训技师'),
    ('本网站上展示的产品信息来自XPEL官方资料，我们为XPEL授权经销商',
     '本网站上展示的产品由我们自家工厂生产，品质有保障'),
    ('专业汽车保护膜专家 · XPEL授权经销商', '专业汽车保护膜专家 · 工厂直营'),
    ('全球顶级汽车保护膜', '顶级汽车保护膜'),
    # Remove any remaining XPEL
    ('XPEL', 'DUMI AUTO'),
]

for old, new in replacements:
    content = content.replace(old, new)

# Clean double spaces
content = re.sub(r'\s{2,}', ' ', content)

if content != original:
    with open('/Users/carstauto/.openclaw/workspace/dumi-auto-website/index-cn.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Fixed index-cn.html")
else:
    print("⏭️  No changes in index-cn.html")
