# Skill: Image Generation

## When to use
Any request to create, generate, or design images, illustrations, diagrams, social media visuals, thumbnails, or creative artwork.

## Tool: FAL.ai — ALWAYS use the terminal command below, NEVER use the built-in image_generate tool

The built-in `image_generate` tool cannot select models. Use this terminal command instead:

### GPT Image 2 — DEFAULT for all image requests
```
python3 /usr/local/bin/fal_generate.py fal-ai/gpt-image-1 "YOUR PROMPT HERE"
```

### FLUX dev — fast photorealistic
```
python3 /usr/local/bin/fal_generate.py fal-ai/flux/dev "YOUR PROMPT HERE"
```

### Video clip
```
python3 /usr/local/bin/fal_generate.py fal-ai/kling-video/v1.6/standard/text-to-video "YOUR PROMPT HERE"
```

**The command prints `SAVED:/tmp/fal_output_xxx.png` — send that file to the user via Telegram.**

Model reference:
| Model | FAL ID | Best for |
|---|---|---|
| GPT Image 2 | `fal-ai/gpt-image-1` | Data slides, text, professional |
| FLUX dev | `fal-ai/flux/dev` | Photorealistic, general |
| FLUX schnell | `fal-ai/flux/schnell` | Fast drafts |
| Recraft V3 | `fal-ai/recraft-v3` | Logos, design, icons |
| Kling video | `fal-ai/kling-video/v1.6/standard/text-to-video` | Video clips |

## Prompt Engineering for Best Results
1. Always write detailed, specific prompts
2. Include: subject, style, mood, lighting, composition, color palette
3. Specify aspect ratio based on use case:
   - Square (1:1): social media posts, profile images
   - Landscape (16:9): blog headers, presentations, YouTube thumbnails
   - Portrait (9:16): Instagram Stories, mobile wallpapers
   - Wide (3:1): LinkedIn banners, website headers

## Style Presets by Use Case

### Professional / Business
"Professional corporate style, clean composition, modern design, subtle colors, white background, high quality"

### Tech / AI Content
"Futuristic tech aesthetic, dark background, glowing elements, digital art style, blue and purple tones"

### Data Visualization Art
"Abstract data visualization, flowing lines, network nodes, clean infographic style, professional"

### Social Media (Thai audience)
"Vibrant colors, modern Southeast Asian aesthetic, clean typography space, social media optimized"

## Workflow
1. Understand what Oui needs the image FOR (context matters)
2. Craft a detailed prompt
3. Generate with FAL
4. Describe the result and offer variations if needed

## Examples
- "Generate a LinkedIn banner for an AI automation talk"
- "Create a thumbnail for a blog post about FinTech data"
- "Make a professional headshot background, clean office setting"
- "Generate an illustration of AI agents working together"
