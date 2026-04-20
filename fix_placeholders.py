#!/usr/bin/env python3
"""
修复空白产品图片 - 将占位符替换为真实图片
"""

from pathlib import Path

WEBSITE_DIR = Path("/Users/carstauto/.openclaw/workspace/dumi-auto-website")

# 产品与图片映射 - 使用现有的 DUMI 图片
# 可用图片: dumi_shield-1/2/3/4/6/7, dumi_matte, dumi_red, dumi_tint, dumi_top, dumi_blue, dumi_color-1
IMAGE_MAP = {
    # PPF 产品
    'armor-ppf': '../images/products/dumi_shield-4.webp',      # 厚重感
    'headlight-protection': '../images/products/dumi_top.webp',  # 车灯
    'crystalline-ppf': '../images/products/dumi_shield-1.webp', # 透明
    'gloss-black-ppf': '../images/products/dumi_shield-2.webp', # 黑
    'satin-matte-ppf': '../images/products/dumi_matte.webp',   # 缎面
    'metallic-ppf': '../images/products/dumi_color-1.webp',     # 金属色
    'ultimate-plus-black': '../images/products/dumi_shield-6.webp',  # 黑
    # Window Tint 产品
    'prime-xr-black': '../images/products/dumi_tint.webp',      # 窗膜
    'carbon-tint': '../images/products/dumi_tint.webp',         # 碳
    'security-film': '../images/products/dumi_shield-7.webp',   # 安全膜
    'uv-protection-film': '../images/products/dumi_tint.webp',   # UV
    # Coating
    'graphene-coating': '../images/products/dumi_shield-4.webp', # 涂层
}

# Alt 文本映射
ALT_MAP = {
    'armor-ppf': 'ARMOR PPF',
    'headlight-protection': 'HEADLIGHT PROTECTION',
    'crystalline-ppf': 'CRYSTALLINE PPF',
    'gloss-black-ppf': 'GLOSS BLACK PPF',
    'satin-matte-ppf': 'SATIN MATTE PPF',
    'metallic-ppf': 'METALLIC PPF',
    'ultimate-plus-black': 'ULTIMATE PLUS BLACK',
    'prime-xr-black': 'PRIME XR BLACK',
    'carbon-tint': 'CARBON TINT',
    'security-film': 'SECURITY FILM',
    'uv-protection-film': 'UV PROTECTION FILM',
    'graphene-coating': 'GRAPHENE COATING',
}

def fix_product_html(product_name, html_content):
    """修复单个产品的占位符图片"""
    
    if product_name not in IMAGE_MAP:
        return html_content, False
    
    img_src = IMAGE_MAP[product_name]
    alt_text = ALT_MAP.get(product_name, product_name.upper())
    
    # 找到并替换 product-placeholder
    old_pattern = f'<div class="product-placeholder">{product_name.upper().replace("-", " ")}</div>'
    new_pattern = f'<img src="{img_src}" alt="{alt_text}" style="width:100%;height:100%;object-fit:cover;">'
    
    if old_pattern in html_content:
        html_content = html_content.replace(old_pattern, new_pattern)
        return html_content, True
    
    # 尝试更通用的模式
    import re
    pattern = r'<div class="product-placeholder">[^<]*</div>'
    replacement = f'<img src="{img_src}" alt="{alt_text}" style="width:100%;height:100%;object-fit:cover;">'
    new_content, count = re.subn(pattern, replacement, html_content)
    
    return new_content, count > 0

def main():
    products_dir = WEBSITE_DIR / "products"
    
    print("🖼️ 开始修复空白产品图片...\n")
    
    fixed_count = 0
    for product_file, img_path in IMAGE_MAP.items():
        html_file = products_dir / f"{product_file}.html"
        
        if not html_file.exists():
            print(f"  ⚠️ 文件不存在: {html_file.name}")
            continue
        
        content = html_file.read_text(encoding='utf-8')
        new_content, was_fixed = fix_product_html(product_file, content)
        
        if was_fixed:
            html_file.write_text(new_content, encoding='utf-8')
            fixed_count += 1
            print(f"  ✅ 修复: {html_file.name}")
        else:
            print(f"  ⚠️ 未找到占位符: {html_file.name}")
    
    print(f"\n✅ 完成! 共修复 {fixed_count} 个产品")
    
    # 检查剩余的占位符
    remaining = list(products_dir.glob("*.html"))
    still_have_placeholder = []
    
    for f in remaining:
        if 'product-placeholder' in f.read_text(encoding='utf-8'):
            still_have_placeholder.append(f.name)
    
    if still_have_placeholder:
        print(f"\n⚠️ 仍有 {len(still_have_placeholder)} 个文件含占位符:")
        for name in still_have_placeholder:
            print(f"   - {name}")
    else:
        print("\n✅ 所有占位符已清除!")

if __name__ == "__main__":
    main()
