#!/usr/bin/env python3
"""Update sitemap.xml with all current product pages"""
import os
from datetime import datetime

BASE_DIR = "/Users/carstauto/.openclaw/workspace/dumi-auto-website/products"
SITEMAP = "/Users/carstauto/.openclaw/workspace/dumi-auto-website/sitemap.xml"
TODAY = datetime.now().strftime("%Y-%m-%d")

# Get all product HTML files
products = sorted([f for f in os.listdir(BASE_DIR) if f.endswith(".html") and f != "index.html"])
print(f"Found {len(products)} product pages")

# Build sitemap
lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
lines.append('        xmlns:xhtml="http://www.w3.org/1999/xhtml">')

# Home pages
lines.append('  <url>')
lines.append('    <loc>https://dumi-auto.com/</loc>')
lines.append('    <xhtml:link rel="alternate" hreflang="en" href="https://dumi-auto.com/"/>')
lines.append('    <xhtml:link rel="alternate" hreflang="zh-CN" href="https://dumi-auto.com/index-cn.html"/>')
lines.append(f'    <lastmod>{TODAY}</lastmod>')
lines.append('    <changefreq>weekly</changefreq>')
lines.append('    <priority>1.0</priority>')
lines.append('  </url>')

lines.append('  <url>')
lines.append('    <loc>https://dumi-auto.com/index-cn.html</loc>')
lines.append('    <xhtml:link rel="alternate" hreflang="en" href="https://dumi-auto.com/"/>')
lines.append('    <xhtml:link rel="alternate" hreflang="zh-CN" href="https://dumi-auto.com/index-cn.html"/>')
lines.append(f'    <lastmod>{TODAY}</lastmod>')
lines.append('    <changefreq>weekly</changefreq>')
lines.append('    <priority>0.9</priority>')
lines.append('  </url>')

# Products
for product in products:
    slug = product.replace(".html", "")
    if slug in ["ultimate-plus", "stealth-ppf", "color-ppf"]:
        priority = "0.9"
    elif "window" in slug or "tint" in slug or "ceramic" in slug or "coating" in slug:
        priority = "0.9"
    elif "index" in slug:
        priority = "0.5"
    else:
        priority = "0.8"
    
    lines.append('  <url>')
    lines.append(f'    <loc>https://dumi-auto.com/products/{product}</loc>')
    lines.append(f'    <lastmod>{TODAY}</lastmod>')
    lines.append('    <changefreq>monthly</changefreq>')
    lines.append(f'    <priority>{priority}</priority>')
    lines.append('  </url>')

lines.append('</urlset>')

xml = "\n".join(lines) + "\n"

with open(SITEMAP, "w") as f:
    f.write(xml)

print(f"Sitemap updated: {len(products)} products + 2 home pages")
print(f"Date: {TODAY}")
