#!/usr/bin/env python3
"""Usage: fal_generate.py <model_id> <prompt> [--size WxH]
Example: fal_generate.py fal-ai/gpt-image-1 "a futuristic city" --size 1536x1024
"""
import sys, os, json, urllib.request, time

model = sys.argv[1]
prompt = sys.argv[2]
size = "1536x1024"
for i, a in enumerate(sys.argv):
    if a == "--size" and i + 1 < len(sys.argv):
        size = sys.argv[i + 1]

try:
    import fal_client
except ImportError:
    os.system("pip install fal-client -q")
    import fal_client

width, height = (int(x) for x in size.split("x")) if "x" in size else (1536, 1024)

args = {"prompt": prompt}
# model-specific size params
if "gpt-image" in model:
    args["image_size"] = size
elif "flux" in model or "recraft" in model or "kling" not in model:
    args["image_size"] = {"width": width, "height": height}

result = fal_client.run(model, arguments=args)

# Extract image URL
url = None
if isinstance(result, dict):
    if "images" in result and result["images"]:
        url = result["images"][0].get("url") or result["images"][0]
    elif "image" in result:
        url = result["image"].get("url") or result["image"]
    elif "url" in result:
        url = result["url"]
    elif "video" in result:
        url = result["video"].get("url") or result["video"]

if not url:
    print(json.dumps(result))
    sys.exit(1)

# Download to /tmp/
ext = "mp4" if "video" in model or (url and ".mp4" in url) else "png"
out = f"/tmp/fal_output_{int(time.time())}.{ext}"
urllib.request.urlretrieve(url, out)
print(f"SAVED:{out}")
print(f"URL:{url}")
