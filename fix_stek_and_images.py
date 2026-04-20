#!/usr/bin/env python3
"""
修复 dumi-auto.com 的 STEK 标识和空白图片问题
执行前请备份！
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime as dt

WEBSITE_DIR = Path("/Users/carstauto/.openclaw/workspace/dumi-auto-website")
STEKS_DIR = WEBSITE_DIR / "images" / "steks"
BACKUP_DIR = WEBSITE_DIR / "website-backup-stek"

def backup_stek_folder():
    """备份 steks 文件夹"""
    if STEKS_DIR.exists():
        backup_path = WEBSITE_DIR / f"steks_backup_{dt.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copytree(STEKS_DIR, backup_path)
        print(f"✅ 已备份 STEK 图片到: {backup_path}")
        return backup_path
    return None

def rename_stek_images():
    """重命名 steks 文件夹为 products，保持 DUMI 品牌"""
    new_dir = WEBSITE_DIR / "images" / "products"
    if not new_dir.exists():
        new_dir.mkdir(parents=True, exist_ok=True)
    
    if STEKS_DIR.exists():
        for f in STEKS_DIR.iterdir():
            new_name = f.name.replace('dyno', 'dumi_').replace('DYN', 'DUMI')
            new_path = new_dir / new_name
            shutil.copy2(f, new_path)
            print(f"  📋 复制: {f.name} -> {new_name}")
        print(f"✅ 图片已复制到: {new_dir}")

def update_html_references():
    """更新 HTML 中的 STEK/DYNO 引用"""
    products_dir = WEBSITE_DIR / "products"
    
    # 替换映射表
    replacements = {
        'images/steks/': 'images/products/',
        'dynoshield': 'dumi_shield',
        'dynomatte': 'dumi_matte',
        'dynored': 'dumi_red',
        'dynotint': 'dumi_tint',
        'dynoblue': 'dumi_blue',
        'dynocolor': 'dumi_color',
        'dynotop': 'dumi_top',
        'DYNOmatte': 'DUMI Matte',
        'DYNOshield': 'DUMI Shield',
        'DYN': 'DUMI',
    }
    
    files_updated = 0
    for html_file in products_dir.glob("*.html"):
        content = html_file.read_text(encoding='utf-8')
        original = content
        
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        if content != original:
            html_file.write_text(content, encoding='utf-8')
            files_updated += 1
            print(f"  ✅ 更新: {html_file.name}")
    
    # 更新 index.html
    index_html = WEBSITE_DIR / "index.html"
    if index_html.exists():
        content = index_html.read_text(encoding='utf-8')
        original = content
        for old, new in replacements.items():
            content = content.replace(old, new)
        if content != original:
            index_html.write_text(content, encoding='utf-8')
            files_updated += 1
            print(f"  ✅ 更新: index.html")
    
    print(f"✅ 共更新 {files_updated} 个 HTML 文件")

def fix_placeholder_images():
    """修复空白产品图片占位符问题"""
    products_dir = WEBSITE_DIR / "products"
    
    # 空白产品对应的渐变背景和图标
    placeholders = {
        'armor-ppf': {
            'gradient': 'linear-gradient(135deg,#1a3a3a,#0d1a1a)',
            'emoji': '🛡️',
            'color': '#1a3a3a'
        },
        'headlight-protection': {
            'gradient': 'linear-gradient(135deg,#1a2a1a,#0d1a0d)',
            'emoji': '💡',
            'color': '#1a2a1a'
        },
        'crystalline-ppf': {
            'gradient': 'linear-gradient(135deg,#e0f7fa,#b2ebf2)',
            'emoji': '💎',
            'color': '#00838f'
        },
        'gloss-black-ppf': {
            'gradient': 'linear-gradient(135deg,#0a0a0a,#2d2d2d)',
            'emoji': '🖤',
            'color': '#1a1a1a'
        },
        'satin-matte-ppf': {
            'gradient': 'linear-gradient(135deg,#8a8a8a,#b0b0b0)',
            'emoji': '🪶',
            'color': '#6a6a6a'
        },
        'metallic-ppf': {
            'gradient': 'linear-gradient(135deg,#4a4a4a,#7a7a7a)',
            'emoji': '✨',
            'color': '#4a4a4a'
        },
        'prime-xr-black': {
            'gradient': 'linear-gradient(135deg,#0a0a0a,#2a2a2a)',
            'emoji': '🌑',
            'color': '#1a1a1a'
        },
        'carbon-tint': {
            'gradient': 'linear-gradient(135deg,#1a1a1a,#3a3a3a)',
            'emoji': '🏁',
            'color': '#2d2d2d'
        },
        'security-film': {
            'gradient': 'linear-gradient(135deg,#1a2a3a,#2d4a5a)',
            'emoji': '🔒',
            'color': '#1a2a3a'
        },
        'uv-protection-film': {
            'gradient': 'linear-gradient(135deg,#ff8c00,#ff4500)',
            'emoji': '☀️',
            'color': '#ff6b35'
        },
        'graphene-coating': {
            'gradient': 'linear-gradient(135deg,#0f2027,#203a43)',
            'emoji': '⚡',
            'color': '#203a43'
        },
    }
    
    for html_file in products_dir.glob("*.html"):
        name = html_file.stem
        if name in placeholders:
            content = html_file.read_text(encoding='utf-8')
            # 替换占位符为渐变背景（保留样式但去掉占位符文字）
            placeholder = placeholders[name]
            old_pattern = f'<div class="product-placeholder">{placeholder["emoji"]}</div>'
            new_pattern = f'<div style="background: {placeholder["gradient"]}; width:100%; height:100%; display:flex; align-items:center; justify-content:center; border-radius:8px;"><span style="font-size:48px; opacity:0.3;">{placeholder["emoji"]}</span></div>'
            
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                html_file.write_text(content, encoding='utf-8')
                print(f"  ✅ 修复空白图片: {html_file.name}")

def check_seo_issues():
    """检查 SEO 问题"""
    products_dir = WEBSITE_DIR / "products"
    issues = []
    
    for html_file in products_dir.glob("*.html"):
        content = html_file.read_text(encoding='utf-8')
        
        # 检查 title
        if '<title>' not in content:
            issues.append(f"❌ {html_file.name}: 缺少 <title> 标签")
        
        # 检查 meta description
        if '<meta name="description"' not in content:
            issues.append(f"❌ {html_file.name}: 缺少 meta description")
        
        # 检查图片 alt
        imgs_without_alt = re.findall(r'<img[^>]*src=[^>]*>', content)
        for img in imgs_without_alt:
            if 'alt=' not in img:
                issues.append(f"⚠️ {html_file.name}: 图片缺少 alt 属性 - {img[:80]}")
        
        # 检查 H1
        h1_count = len(re.findall(r'<h1', content, re.IGNORECASE))
        if h1_count == 0:
            issues.append(f"❌ {html_file.name}: 缺少 <h1> 标签")
        elif h1_count > 1:
            issues.append(f"⚠️ {html_file.name}: 有 {h1_count} 个 <h1> 标签（建议只有1个）")
    
    return issues

if __name__ == "__main__":
    print("=" * 60)
    print("🔧 DUMI AUTO 网站修复工具")
    print("=" * 60)
    
    # 1. 备份
    print("\n📦 步骤1: 备份 STEK 图片...")
    backup_stek_folder()
    
    # 2. 重命名并复制图片
    print("\n📸 步骤2: 重命名图片为 DUMI 品牌...")
    rename_stek_images()
    
    # 3. 更新 HTML 引用
    print("\n🔄 步骤3: 更新 HTML 中的 STEK/DYNO 引用...")
    update_html_references()
    
    # 4. 修复空白图片
    print("\n🖼️ 步骤4: 修复空白产品图片...")
    fix_placeholder_images()
    
    # 5. SEO 检查
    print("\n🔍 步骤5: 检查 SEO 问题...")
    issues = check_seo_issues()
    if issues:
        print("\n发现以下 SEO 问题:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("  ✅ 未发现明显 SEO 问题")
    
    print("\n" + "=" * 60)
    print("✅ 修复完成!")
    print("=" * 60)
    print("\n⚠️ 重要提醒:")
    print("  1. 请检查 images/products/ 文件夹中的图片是否正确")
    print("  2. 建议在测试环境验证后再发布")
    print("  3. 如有问题，可从备份恢复")
