#!/usr/bin/env python3
"""Remove all XPEL references and replace with factory direct messaging."""
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Files to process
HTML_FILES = []
for root, dirs, files in os.walk(BASE_DIR):
    for f in files:
        if f.endswith('.html'):
            HTML_FILES.append(os.path.join(root, f))

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # --- Title / Meta / SEO replacements ---
    content = re.sub(
        r'<title>.*?XPEL.*?</title>',
        '<title>DUMI AUTO | Professional PPF Manufacturer - Factory Direct</title>',
        content
    )
    content = re.sub(
        r'<meta name="description" content="[^"]*XPEL[^"]*"',
        '<meta name="description" content="DUMI AUTO - Professional PPF manufacturer and factory direct supplier. Paint protection film (PPF), ceramic coating, window tint & color change film. 5000+ cars protected. Free quote today!">',
        content
    )
    content = re.sub(
        r'<meta name="keywords" content="[^"]*XPEL[^"]*"',
        '<meta name="keywords" content="PPF manufacturer, paint protection film, ceramic coating, car window tint, color change film, car wrap, Los Angeles PPF installer, PPF factory direct, stealth PPF, ceramic coating Los Angeles">',
        content
    )
    content = re.sub(
        r'<meta property="og:title" content="[^"]*XPEL[^"]*"',
        '<meta property="og:title" content="DUMI AUTO | Professional PPF Manufacturer Factory Direct">',
        content
    )
    content = re.sub(
        r'<meta property="og:description" content="[^"]*XPEL[^"]*"',
        '<meta property="og:description" content="Professional PPF manufacturer and factory direct supplier. PPF, ceramic coating, window tint and color film installation.">',
        content
    )

    # --- JSON-LD structured data ---
    content = re.sub(
        r'"description":\s*"[^"]*XPEL[^"]*"',
        '"description": "Professional PPF Manufacturer - Factory Direct. Paint Protection Film, Window Tint, Ceramic Coating and Color Change Film in Los Angeles"',
        content
    )
    content = re.sub(
        r'"name":\s*"XPEL"',
        '"name": "DUMI AUTO"',
        content
    )
    # Replace XPEL product names in JSON-LD
    content = re.sub(r'"name":\s*"XPEL\s+(ULTIMATE PLUS[^"]*)"', r'"name": "\1"', content)
    content = re.sub(r'"name":\s*"XPEL\s+(PRIME[^"]*)"', r'"name": "\1"', content)
    content = re.sub(r'"name":\s*"XPEL\s+(STEALTH[^"]*)"', r'"name": "\1"', content)
    content = re.sub(r'"name":\s*"XPEL\s+(COLOR[^"]*)"', r'"name": "\1"', content)
    content = re.sub(r'"name":\s*"XPEL\s+(Armor[^"]*)"', r'"name": "\1"', content)
    content = re.sub(r'"name":\s*"XPEL\s+([^"]*)"', r'"name": "\1"', content)
    # Remove brand from JSON-LD
    content = re.sub(r'"brand":\s*\{[^}]*XPEL[^}]*\}', '"brand": {"@type": "Brand", "name": "DUMI AUTO"}', content)

    # --- Body text replacements (order matters - do longer/more specific first) ---
    replacements = [
        # Hero
        (r'Protect Your Car with XPEL', 'Protect Your Car with Premium PPF'),
        (r'Premium XPEL Protection for Your Vehicle', 'Premium PPF Protection for Your Vehicle'),
        # Badges
        (r'🔥\s*XPEL Authorized Dealer', '🏭 Factory Direct Manufacturer'),
        # Feature cards
        (r'<h3>XPEL Authorized Dealer</h3>', '<h3>Professional PPF Manufacturer</h3>'),
        (r'Official XPEL authorized dealer with genuine products and factory warranty',
         'Direct from manufacturer with full factory warranty on all products'),
        (r'All XPEL products come with manufacturer\'s warranty',
         'All our PPF products come with manufacturer\'s warranty'),
        # About section
        (r'As an official XPEL authorized dealer, we specialize',
         'As a professional PPF manufacturer and factory direct supplier, we specialize'),
        (r'each certified through XPEL\'s official training program',
         'each trained through our manufacturer\'s certification program'),
        (r'✅ XPEL Authorized Dealer', '🏭 Factory Direct'),
        (r'XPEL Authorized Dealer', 'Professional PPF Manufacturer / Factory Direct'),
        # About text
        (r'PPF is a transparent urethane film[^.]*XPEL PPF features self-healing[^.]*\.',
         'PPF is a transparent urethane film applied to a vehicle\'s paint surface to protect it from rock chips, scratches, road debris, and environmental damage. Our PPF features self-healing technology that repairs minor scratches with heat.'),
        (r'XPEL ULTIMATE PLUS comes with a 10-year warranty[^.]*',
         'Our premium PPF comes with a 10-year warranty against yellowing, cracking, peeling, and delamination.'),
        (r'XPEL PPF can protect your vehicle\'s paint for 10\+\s*years',
         'Our PPF can protect your vehicle\'s paint for 10+ years'),
        # Footer
        (r'Professional Auto Protection Film Expert · XPEL Authorized Dealer',
         'Professional Auto Protection Film Expert · Factory Direct'),
        (r'is an authorized XPEL dealer\.?\s*Product information sourced from XPEL official materials\.?',
         'is a professional PPF manufacturer and factory direct supplier. We specialize in premium automotive protection products.'),
        # Copyright
        (r'XPEL is a registered trademark of XPEL Technologies Corp\.',
         ''),
        # Any remaining XPEL text in body
        (r'XPEL\s+authorized dealer', 'factory direct supplier'),
        (r'XPEL\s+dealer', 'factory direct supplier'),
        (r'XPEL\s+PPF', 'PPF'),
        (r'XPEL\s+', ''),
        (r'\bXPEL\b', 'DUMI AUTO'),
    ]
    
    for old, new in replacements:
        content = re.sub(old, new, content, flags=re.IGNORECASE)
    
    # Clean up double spaces
    content = re.sub(r'\s{2,}', ' ', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Fixed: {filepath}")
        return True
    else:
        print(f"⏭️  No changes: {filepath}")
        return False

print(f"Processing {len(HTML_FILES)} HTML files...\n")
changed = 0
for f in sorted(HTML_FILES):
    if fix_file(f):
        changed += 1

print(f"\nDone! Changed {changed}/{len(HTML_FILES)} files.")
