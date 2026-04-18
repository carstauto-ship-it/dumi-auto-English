#!/usr/bin/env python3
"""
DUMI AUTO - Google Search Console URL Submission Script
https://dumi-panel.com

用法:
1. 手动模式: 打开 GSC -> URL Inspection -> 输入每个产品页URL
2. API模式: 需要 OAuth2 凭证，配置 below 后运行脚本

手动提交说明:
1. 访问 https://search.google.com/search-console
2. 选择 dumi-panel.com 属性
3. 点击 "URL Inspection" 
4. 输入以下任意URL并点击"请求编入索引":
"""

SITE_URL = "https://dumi-panel.com"
SITEMAP_URL = "https://dumi-panel.com/sitemap.xml"

PRODUCT_URLS = [
    f"{SITE_URL}/products/gloss-black-ppf.html",
    f"{SITE_URL}/products/metallic-ppf.html",
    f"{SITE_URL}/products/satin-matte-ppf.html",
    f"{SITE_URL}/products/crystalline-ppf.html",
    f"{SITE_URL}/products/graphene-coating.html",
    f"{SITE_URL}/products/security-film.html",
    f"{SITE_URL}/products/carbon-tint.html",
    f"{SITE_URL}/products/uv-protection-film.html",
]

if __name__ == "__main__":
    print("DUMI AUTO - Google Search Console Submission")
    print("=" * 50)
    print(f"\n📋 Sitemap: {SITEMAP_URL}\n")
    print("🔍 产品页面URL列表:\n")
    for i, url in enumerate(PRODUCT_URLS, 1):
        print(f"  {i}. {url}")
    print(f"\n✅ 共 {len(PRODUCT_URLS)} 个产品页需要提交到 GSC")
    print("\n📝 操作步骤:")
    print("  1. 登录 Google Search Console: https://search.google.com/search-console")
    print("  2. 选择 dumi-panel.com 属性")
    print("  3. 点击 'Sitemaps' -> 提交: sitemap.xml")
    print("  4. 点击 'URL Inspection' -> 逐个提交产品页URL")
    print("  5. 或使用 GSC API (需配置 OAuth2) 完成自动化提交")
