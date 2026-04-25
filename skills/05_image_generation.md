# Skill: Image Generation

## When to use
Any request to create, generate, or design images, illustrations, diagrams, social media visuals, thumbnails, or creative artwork.

## Tool: FAL.ai
Use the FAL image generation tool with these EXACT model IDs:

| Use Case | FAL Model ID | Notes |
|---|---|---|
| **Default / photorealistic** | `fal-ai/flux/dev` | Best general purpose |
| **OpenAI GPT Image 2** | `fal-ai/gpt-image-1` | Highest quality, best text rendering, use when user asks for "OpenAI image" or "GPT Image" |
| **Fast/cheap** | `fal-ai/flux/schnell` | Quick iterations |
| **Professional design** | `fal-ai/recraft-v3` | Logos, icons, UI |
| **Consistent style** | `fal-ai/flux-pro` | Commercial quality |
| **Video** | `fal-ai/kling-video/v1.6/standard/text-to-video` | Text to video |
| **Image to video** | `fal-ai/kling-video/v1.6/standard/image-to-video` | Animate an image |

**Default to `fal-ai/gpt-image-1` unless Oui specifies otherwise — it produces the best results.**

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
