#!/usr/bin/env python3
"""Download all Canva site images and create mapping."""
import subprocess
import re
import json
import os

print("Downloading Canva site images...")

# Create directory structure
os.makedirs('assets/images/portfolio', exist_ok=True)
os.makedirs('assets/images/about', exist_ok=True)
os.makedirs('assets/images/courses', exist_ok=True)

# Fetch page
result = subprocess.run(['curl', '-sL', 'https://linzihyang.my.canva.site/home'], capture_output=True, text=True)
html = result.stdout

# Extract all image URLs
images = re.findall(r'"url":"([^"]*(?:jpg|jpeg|png|webp)[^"]*)"', html)
unique_images = list(dict.fromkeys(images))

print(f"Found {len(unique_images)} unique images")

# Download first 50 images for portfolio/about
download_count = 0
image_mapping = {}

for i, img_url in enumerate(unique_images[:50], 1):
    ext = img_url.split('.')[-1]
    filename = f"{i:03d}.{ext}"
    
    # Determine destination based on category
    if i <= 20:
        dest_dir = 'assets/images/portfolio'
    elif i <= 35:
        dest_dir = 'assets/images/about'
    else:
        dest_dir = 'assets/images/courses'
    
    dest = f"{dest_dir}/{filename}"
    full_url = f"https://linzihyang.my.canva.site/home/{img_url}"
    
    try:
        result = subprocess.run(
            ['curl', '-sL', '-o', dest, '-w', '%{size_download}', full_url],
            capture_output=True, text=True, timeout=15
        )
        size = int(result.stdout) if result.stdout.isdigit() else 0
        
        if size > 1000:  # Valid download
            download_count += 1
            image_mapping[filename] = f"{dest_dir}/{filename}"
            if download_count % 10 == 0:
                print(f"Downloaded {download_count}/50 images...")
    except:
        pass

print(f"\n✅ Successfully downloaded {download_count} images")

# Save mapping
with open('/tmp/image_mapping.json', 'w') as f:
    json.dump(image_mapping, f, indent=2)

print("Image mapping saved to /tmp/image_mapping.json")
