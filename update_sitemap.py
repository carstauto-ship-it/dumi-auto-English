#!/usr/bin/env python3
"""Update /tmp/dumi-publish-dumi-auto/sitemap.xml with all current product pages"""
import os
from datetime import datetime

BASE_DIR = "/tmp/dumi-publish-dumi-auto/products"
SITEMAP = "/tmp/dumi-publish-dumi-auto/sitemap.xml"
TODAY = datetime.now().strftime("%Y-%m-%d")

products = sorted([f for f in os.listdir(BASE_DIR) if f.endswith(".html")])
print(f"Found {len(products)} product pages")

lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

# Home
for path, prio in [("https://dumi-auto.com/", "1.0"), ("https://dumi-auto.com/products.html", "0.9"),
                    ("https://dumi-auto.com/index-cn.html", "0.9"), ("https://dumi-auto.com/privacy.html", "0.3"),
                    ("https://dumi-auto.com/terms.html", "0.3")]:
    lines.append('  <url>')
    lines.append(f'    <loc>{path}</loc>')
    lines.append(f'    <lastmod>{TODAY}</lastmod>')
    lines.append('    <changefreq>weekly</changefreq>')
    lines.append(f'    <priority>{prio}</priority>')
    lines.append('  </url>')

# Products
for product in products:
    slug = product.replace(".html", "")
    if "tint" in slug or "ceramic" in slug or "coating" in slug:
        priority = "0.9"
    else:
        priority = "0.8"
    lines.append('  <url>')
    lines.append(f'    <loc>https://dumi-auto.com/products/{product}</loc>')
    lines.append(f'    <lastmod>{TODAY}</lastmod>')
    lines.append('    <changefreq>monthly</changefreq>')
    lines.append(f'    <priority>{priority}</priority>')
    lines.append('  </url>')

lines.append('</urlset>')

with open(SITEMAP, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"✅ sitemap.xml updated: {len(products)} products + 5 pages = {len(products)+5} URLs")
