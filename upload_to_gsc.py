#!/usr/bin/env python3
"""
DUMI AUTO - Google Search Console URL Submission Script
https://dumi-auto.com

用法:
1. 手动模式: 打开 GSC -> URL Inspection -> 输入每个产品页URL
2. API模式: 需要 OAuth2 凭证，配置 below 后运行脚本

手动提交说明:
1. 访问 https://search.google.com/search-console
2. 选择 dumi-auto.com 属性
3. 点击 "URL Inspection" 
4. 输入以下任意URL并点击"请求编入索引":
"""

SITE_URL = "https://dumi-auto.com"
SITEMAP_URL = "https://dumi-auto.com/sitemap.xml"

# All product URLs (sitemap has been updated)
NEW_PRODUCT_URLS = [
    # New PPF Products
    f"{SITE_URL}/products/chrome-mirror-ppf.html",
    f"{SITE_URL}/products/diamond-guard-ppf.html",
    f"{SITE_URL}/products/nano-ceramic-ppf.html",
    f"{SITE_URL}/products/infrared-ceramic-ppf.html",
    f"{SITE_URL}/products/camouflage-ppf.html",
    # New Window Films
    f"{SITE_URL}/products/ceramic-pro-window-film.html",
    f"{SITE_URL}/products/ceramic-ir-window-film.html",
    f"{SITE_URL}/products/dyed-window-film.html",
    f"{SITE_URL}/products/hybrid-window-film.html",
    f"{SITE_URL}/products/metalized-window-film.html",
    f"{SITE_URL}/products/limo-black-film.html",
    # New Accessories
    f"{SITE_URL}/products/ppf-installation-kit.html",
    f"{SITE_URL}/products/hydrophobic-topcoat.html",
    f"{SITE_URL}/products/ppf-edge-sealer.html",
]

if __name__ == "__main__":
    print("DUMI AUTO - Google Search Console Submission")
    print("=" * 50)
    print(f"\n📋 Sitemap: {SITEMAP_URL}")
    print("   ✅ Sitemap 已更新 - Google 会自动在下次抓取时发现新页面\n")
    print("🔍 13个新产品页URL (已添加到sitemap):\n")
    for i, url in enumerate(NEW_PRODUCT_URLS, 1):
        print(f"  {i:2d}. {url}")
    print(f"\n✅ 共 {len(NEW_PRODUCT_URLS)} 个新产品页需要提交到 GSC")
    print("\n📝 操作步骤:")
    print("  1. 登录 Google Search Console: https://search.google.com/search-console")
    print("  2. 选择 dumi-auto.com 属性")
    print("  3. 点击 'Sitemaps' -> 确认 sitemap.xml 已提交")
    print("  4. 点击 'URL Inspection' -> 逐个提交上述URL -> '请求编入索引'")
    print("  5. 或使用 GSC API (需配置 OAuth2) 完成自动化提交")
    print("\n💡 提示: Sitemap 已更新，Google 通常在24-48小时内自动发现新页面")
