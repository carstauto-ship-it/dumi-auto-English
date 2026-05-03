#!/usr/bin/env python3
"""
DUMI AUTO - Google Search Console URL Submission Script
https://dumi-auto.com

2026-05-01: +15 new products submitted
"""

SITE_URL = "https://dumi-auto.com"
SITEMAP_URL = "https://dumi-auto.com/sitemap.xml"

# 15 new products added on 2026-05-01
NEW_PRODUCT_URLS = [
    f"{SITE_URL}/products/holographic-chrome-ppf.html",
    f"{SITE_URL}/products/storm-shield-ppf.html",
    f"{SITE_URL}/products/diamond-glass-tint.html",
    f"{SITE_URL}/products/electric-vehicle-ppf.html",
    f"{SITE_URL}/products/satin-slate-grey-ppf.html",
    f"{SITE_URL}/products/brake-caliper-ppf.html",
    f"{SITE_URL}/products/underbody-protective-film.html",
    f"{SITE_URL}/products/carbon-fiber-window-tint.html",
    f"{SITE_URL}/products/fabric-protection-coating.html",
    f"{SITE_URL}/products/uv-block-ceramic-spray.html",
    f"{SITE_URL}/products/matte-surface-sealer.html",
    f"{SITE_URL}/products/brake-disc-ceramic-coating.html",
    f"{SITE_URL}/products/ultra-gloss-defender-ppf.html",
    f"{SITE_URL}/products/military-grade-urethane-ppf.html",
    f"{SITE_URL}/products/prestige-clear-ceramic-tint.html",
]

if __name__ == "__main__":
    print("DUMI AUTO - Google Search Console Submission")
    print("=" * 50)
    print(f"\n📋 Sitemap: {SITEMAP_URL}")
    print("   ✅ Sitemap 已更新 (2026-05-01) - Google 会自动抓取\n")
    print("🔍 15个新产品页URL (2026-05-01):\n")
    for i, url in enumerate(NEW_PRODUCT_URLS, 1):
        print(f"  {i:2d}. {url}")
    print(f"\n✅ 共 {len(NEW_PRODUCT_URLS)} 个新产品页")
    print("\n📝 操作步骤:")
    print("  1. 登录 Google Search Console: https://search.google.com/search-console")
    print("  2. 选择 dumi-auto.com 属性")
    print("  3. 点击 'Sitemaps' -> 确认 sitemap.xml 已提交")
    print("  4. 点击 'URL Inspection' -> 逐个提交URL -> '请求编入索引'")
    print("\n💡 提示: Sitemap 已更新，Google 通常在24-48小时内自动发现新页面")
