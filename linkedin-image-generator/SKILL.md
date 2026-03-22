---
name: linkedin-image-pro
description: "Generate 5 radically different LinkedIn post image concepts using a Synthetic Viewer Panel — 5 AI creative director personas each propose a distinct visual direction. Use when the user says things like 'linkedin image pro', 'image panel', 'creative directions for linkedin', 'linkedin pro image', '5 concepts for linkedin'."
user-invocable: true
---

# LinkedIn Image Pro — Synthetic Viewer Panel

Generate 5 radically different LinkedIn post image concepts by simulating a panel of 5 AI creative director personas. Each persona proposes a distinct visual direction — like a creative agency pitch.

## Configuration

| Variable | Description | Example |
|----------|-------------|---------|
| `$GEMINI_API_KEY` | Google AI Studio API key | `AIzaSy...` |

## Prerequisites

- Tools: `curl`, `jq`, `base64`.
- This is a **global skill** — works from any directory.

## What This Skill Does

When the user shares a LinkedIn post and asks for an image:

1. Analyze the post content for themes, emotions, audience, and visual opportunities.
2. Generate a **Synthetic Viewer Panel** — 5 creative director personas dynamically tailored to this specific post.
3. Each persona crafts a unique image prompt with a fundamentally different visual concept.
4. Generate 5 images — one per persona — each a genuinely different creative direction.
5. Review all 5, rank them, and refine the top 2.
6. Present the full panel to the user with persona labels and a recommendation.
7. Save metadata JSON for downstream use.

## Step-by-step Instructions

### Step 1: Analyze the Post

Read the LinkedIn post content. Extract:
- **Core theme** (transformation, growth, hiring, humor, technical tip, etc.)
- **Key phrase** for the headline text (keep under 10 words)
- **Secondary text** (optional, under 8 words)
- **Emotional tone** (inspirational, provocative, reflective, urgent, humorous)
- **Target audience** (developers, founders, marketers, general professionals)

### Step 2: Generate the Synthetic Viewer Panel

This is the core innovation. You (Claude) must generate 5 creative director personas, each bringing a FUNDAMENTALLY different creative perspective to the same post.

For each persona, define:

```
Persona N: "The [Archetype Name]"
- Philosophy: [1-sentence creative philosophy]
- Scene type: [e.g., aerial landscape, close-up object, abstract pattern, human scene, architectural, metaphorical still life]
- Composition: [e.g., dramatic split, center focal, rule of thirds, vast negative space, layered depth, bird's eye]
- Color mood: [e.g., warm golden dawn, cool blue steel, vibrant high-contrast, muted earth tones, neon electric, monochrome with accent]
- Visual metaphor: [The specific metaphor this persona would use for the post's message]
- Prompt fragment: [50-word scene description specific to this persona]
```

**CRITICAL DIVERSITY RULES:**
- No two personas may share the same `scene_type`
- No two personas may share the same `composition` style
- No two personas may use the same `color mood`
- At least one persona must use a CONTRARIAN or UNEXPECTED visual approach
- At least one persona must be MINIMALIST (bold typography, simple scene)

**Example persona sets by post type:**

**For a tech/AI post:**
1. "The Cartographer" — Epic aerial landscape, person drawing a glowing map over a valley
2. "The Minimalist" — Stark dark background, massive bold typography, one small symbolic object
3. "The Workshop" — Warm interior scene, analog meets digital through a window
4. "The Provocateur" — Unexpected metaphor (e.g., ancient scroll for a coding post), visual irony
5. "The Architect" — Construction/blueprint scene, 2D becoming 3D, building metaphor

**For a humor/critique post:**
1. "The Satirist" — Visual punchline, before/after split showing absurdity
2. "The Photojournalist" — Documentary-style moment, dramatic lighting on a real-world scene
3. "The Pop Artist" — Bold colors, comic/pop art influence, oversized objects
4. "The Cinematographer" — Movie-poster composition, dramatic angles, silhouettes
5. "The Abstract Expressionist" — Emotion through color and form, minimal literal content

**For a thought leadership post:**
1. "The Philosopher" — Solitary figure contemplating vastness, epic scale
2. "The Data Visualizer" — Information as landscape, flowing streams of structured light
3. "The Storyteller" — Narrative scene with characters on a journey, warm human moment
4. "The Futurist" — Tomorrow's world rendered today, clean lines, optimistic atmosphere
5. "The Old Master" — Renaissance/classical painting aesthetic applied to modern concepts

### Step 3: Craft 5 Prompts

For each persona, build a complete image generation prompt using this template:

```
Wide 16:9 cinematic LinkedIn thought leadership image.
[PERSONA-SPECIFIC SCENE from prompt_fragment — 50-80 words of rich visual detail]
[PERSONA-SPECIFIC COMPOSITION — how elements are arranged]
[PERSONA-SPECIFIC COLOR MOOD]. Atmospheric depth, painterly photorealistic quality.
Premium, professional, NOT sci-fi, NOT cartoonish, NOT stock photo.

Bold white text [position based on composition]: "[HEADLINE — same across all 5]"
[Optional secondary text in contrasting warm/cool tone]: "[SUBHEAD]"
Clean modern sans-serif font, strong contrast, readable at thumbnail size.
No logos. Ultra wide cinematic format, professional LinkedIn quality.
```

The **headline text is SHARED** across all 5 personas (same post = same headline). Only the visual concept changes.

### Step 4: Generate 5 Images

Generate one image per persona sequentially using `gemini-3.1-flash-image-preview`:

```bash
MODEL="gemini-3.1-flash-image-preview"

for P in 1 2 3 4 5; do
  CFILE="/tmp/linkedin-pro-persona-${P}.png"
  PAYLOAD_FILE=$(mktemp /tmp/gen-payload-XXXXXX.json)

  # Use the prompt for persona $P (set PROMPT to the appropriate persona prompt before this)
  jq -n --arg prompt "$PROMPT" '{
    contents: [{parts: [{text: ("Generate an image: " + $prompt)}]}],
    generationConfig: {responseModalities: ["TEXT", "IMAGE"]}
  }' > "$PAYLOAD_FILE"

  RESPONSE=$(curl -s -X POST \
    "https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d @"$PAYLOAD_FILE" 2>&1)
  rm -f "$PAYLOAD_FILE"

  IMAGE_DATA=$(echo "$RESPONSE" | jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' 2>/dev/null)
  if [ -z "$IMAGE_DATA" ] || [ "$IMAGE_DATA" = "null" ]; then
    echo "Persona $P: FAILED"
    continue
  fi
  echo "$IMAGE_DATA" | base64 -d > "$CFILE"
  echo "Persona $P: saved ($(wc -c < "$CFILE") bytes)"
done
```

### Step 5: Review and Rank

Use the Read tool to view all 5 persona images. Present a summary table:

```
| # | Persona | Concept | Typography | Composition | Impact | Theme Match | Overall |
|---|---------|---------|------------|-------------|--------|-------------|---------|
| 1 | The X   | ...     | Good/Fair  | Strong/Weak | High/Med/Low | ...    | Rank    |
```

Select the **top 2** based on:
1. Typography readability (most important for LinkedIn)
2. Visual distinctiveness and stop-scroll power
3. Theme alignment with the post
4. Composition balance at thumbnail size

### Step 6: Refine Top 2

For each of the top 2 picks, regenerate with an improvement prompt:

Append to the original persona prompt:
```
CRITICAL FIX: [specific improvement — usually typography size, contrast, or composition balance]
DO NOT CHANGE: [what was excellent — the core concept, color mood, scene]
```

Save refined images to `/tmp/linkedin-pro-refined-1.png` and `/tmp/linkedin-pro-refined-2.png`.

### Step 7: Present the Full Panel

Build an HTML gallery page at `/tmp/linkedin-pro-gallery.html` showing all images:

```bash
cat > /tmp/linkedin-pro-gallery.html << 'HTMLEOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Synthetic Viewer Panel</title>
<style>
body { background: #1a1a2e; color: #eee; font-family: -apple-system, sans-serif; margin: 0; padding: 40px; }
h1 { text-align: center; color: #f0c040; margin-bottom: 6px; }
p.sub { text-align: center; color: #aaa; margin-bottom: 40px; }
.grid { max-width: 1200px; margin: 0 auto; }
.card { background: #16213e; border-radius: 12px; margin-bottom: 24px; overflow: hidden; border: 2px solid transparent; transition: border-color 0.2s; }
.card:hover { border-color: #f0c040; }
.label { padding: 14px 18px 4px; font-size: 18px; font-weight: 700; }
.label .num { color: #f0c040; }
.label .name { color: #fff; margin-left: 6px; }
.desc { padding: 0 18px 10px; color: #9aa5b4; font-size: 13px; }
.tag { display: inline-block; padding: 3px 10px; border-radius: 6px; font-size: 12px; margin-left: 10px; font-weight: 600; }
.tag.top { background: #2d6a4f; color: #b7e4c7; }
.tag.ref { background: #7B2FBE33; color: #c4b5fd; }
img { width: 100%; display: block; cursor: pointer; }
h2 { color: #c4b5fd; margin-top: 40px; }
</style>
</head>
<body>
<h1>Synthetic Viewer Panel</h1>
<p class="sub">5 AI Creative Directors. 5 Radically Different Concepts.</p>
<div class="grid">
<!-- Cards will be populated per persona -->
</div>
</body>
</html>
HTMLEOF
```

Then dynamically add the persona cards to the HTML. Use the Read tool to show each image to the user inline, and provide the gallery link.

Start a local server if needed:
```bash
cd /tmp && nohup python3 -m http.server 8888 > /dev/null 2>&1 &
```

Gallery URL: `http://localhost:8888/linkedin-pro-gallery.html`

### Step 8: Save Metadata

Write a JSON file capturing the full session:

```bash
cat > /tmp/linkedin-pro-metadata.json << 'EOF'
{
  "post_text": "...",
  "post_date": "YYYY-MM-DD",
  "headline": "...",
  "secondary_text": "...",
  "personas": [
    {
      "number": 1,
      "name": "The [Archetype]",
      "philosophy": "...",
      "scene_type": "...",
      "composition": "...",
      "color_mood": "...",
      "visual_metaphor": "...",
      "prompt": "full prompt used",
      "image_file": "/tmp/linkedin-pro-persona-1.png",
      "rank": 3,
      "notes": "strengths and weaknesses"
    }
  ],
  "winner": 2,
  "refinements": [
    {"source_persona": 2, "image_file": "/tmp/linkedin-pro-refined-1.png"},
    {"source_persona": 4, "image_file": "/tmp/linkedin-pro-refined-2.png"}
  ]
}
EOF
```

## Style Guidelines

LinkedIn images should be:
- **Cinematic and painterly** — dramatic perspectives, atmospheric depth
- **Premium and professional** — NOT clip art, NOT stock photo, NOT cartoonish, NOT sci-fi
- **Wide landscape** format (16:9 or 1200x628)
- **Bold typography** — headline text must be readable at thumbnail size
- **Split/contrast compositions** work well for "before/after" or "problem/solution" posts
- **No logos, no faces** unless specifically requested

## Models

| Model | When to use |
|-------|-------------|
| `gemini-3.1-flash-image-preview` (default) | Best balance of quality and speed |
| `gemini-3-pro-image-preview` | Highest quality, use for important posts |

## Tips

- **Text readability is king** — LinkedIn images are viewed on mobile at small sizes.
- **Dark backgrounds with bright text** work better than light backgrounds for LinkedIn feed.
- **The diversity is the feature** — if two personas produce similar-looking images, the panel has failed. Rethink the persona definitions.
- **Avoid cluttered images** — one clear visual concept per persona.
- **No CTA buttons or badges** — this is LinkedIn, not a website banner.
- **Save metadata** — always write the JSON file so results can be used for the showcase website.
