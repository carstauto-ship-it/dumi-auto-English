#!/usr/bin/env python3
"""修复剩余5个文件的related products占位符"""

from pathlib import Path
import re

WEBSITE_DIR = Path("/Users/carstauto/.openclaw/workspace/dumi-auto-website")
products_dir = WEBSITE_DIR / "products"

# 每个文件的占位符及替换方案
fixes = {
    'stealth-ppf.html': [
        ('<div class="product-placeholder">PPF</div>', '<img src="../images/products/dumi_shield-1.webp" alt="ULTIMATE PLUS" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">COLOR</div>', '<img src="../images/products/dumi_red.webp" alt="COLOR PPF" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">TINT</div>', '<img src="../images/products/dumi_tint.webp" alt="PRIME Window Film" style="width:100%;height:100%;object-fit:cover;">'),
    ],
    'ultimate-plus.html': [
        ('<div class="product-placeholder">STEALTH</div>', '<img src="../images/products/dumi_matte.webp" alt="STEALTH PPF" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">COLOR</div>', '<img src="../images/products/dumi_red.webp" alt="COLOR PPF" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">TINT</div>', '<img src="../images/products/dumi_tint.webp" alt="PRIME Window Film" style="width:100%;height:100%;object-fit:cover;">'),
    ],
    'color-ppf.html': [
        ('<div class="product-placeholder">STEALTH</div>', '<img src="../images/products/dumi_matte.webp" alt="STEALTH PPF" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">BLACK</div>', '<img src="../images/products/dumi_shield-2.webp" alt="ULTIMATE PLUS BLACK" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">TINT</div>', '<img src="../images/products/dumi_tint.webp" alt="PRIME Window Film" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">PPF</div>', '<img src="../images/products/dumi_shield-1.webp" alt="ULTIMATE PLUS" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">CERAMIC</div>', '<img src="../images/products/dumi_tint.webp" alt="PRIME CERAMIC" style="width:100%;height:100%;object-fit:cover;">'),
    ],
    'ceramic-tint.html': [
        ('<div class="product-placeholder">TINT</div>', '<img src="../images/products/dumi_tint.webp" alt="PRIME Window Film" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">XR</div>', '<img src="../images/products/dumi_tint.webp" alt="PRIME XR BLACK" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">PPF</div>', '<img src="../images/products/dumi_shield-1.webp" alt="ULTIMATE PLUS" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">HEADLIGHT</div>', '<img src="../images/products/dumi_top.webp" alt="HEADLIGHT PROTECTION" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">STEALTH</div>', '<img src="../images/products/dumi_matte.webp" alt="STEALTH PPF" style="width:100%;height:100%;object-fit:cover;">'),
    ],
    'prime-window-film.html': [
        ('<div class="product-placeholder">CERAMIC</div>', '<img src="../images/products/dumi_tint.webp" alt="PRIME CERAMIC" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">XR</div>', '<img src="../images/products/dumi_tint.webp" alt="PRIME XR BLACK" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">PPF</div>', '<img src="../images/products/dumi_shield-1.webp" alt="ULTIMATE PLUS" style="width:100%;height:100%;object-fit:cover;">'),
        ('<div class="product-placeholder">STEALTH</div>', '<img src="../images/products/dumi_matte.webp" alt="STEALTH PPF" style="width:100%;height:100%;object-fit:cover;">'),
    ],
}

total_fixed = 0
for filename, replacements in fixes.items():
    filepath = products_dir / filename
    if not filepath.exists():
        print(f"⚠️ 文件不存在: {filename}")
        continue
    
    content = filepath.read_text(encoding='utf-8')
    original = content
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        fixed_count = sum(1 for old, _ in replacements if old in original)
        total_fixed += fixed_count
        print(f"✅ 修复 {filename}: {fixed_count} 个占位符")

print(f"\n✅ 共修复 {total_fixed} 个占位符")

# 检查是否还有遗留
remaining = []
for html_file in products_dir.glob("*.html"):
    if 'product-placeholder' in html_file.read_text(encoding='utf-8'):
        remaining.append(html_file.name)

if remaining:
    print(f"\n⚠️ 仍有 {len(remaining)} 个文件含占位符:")
    for name in remaining:
        print(f"   - {name}")
else:
    print("\n🎉 所有产品图片占位符已清除!")
