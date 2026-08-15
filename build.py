import json

with open("recipes.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

paperclip_svg = """<svg class="paperclip" viewBox="0 0 24 44" fill="none">
  <path d="M6 8 C6 4 10 2 14 4 C18 6 18 12 14 15 L8 22 C6 24 6 27 8 29 C10 31 13 31 15 29 L20 24"
        stroke="#8a8a8a" stroke-width="2.5" stroke-linecap="round"/>
</svg>"""

rotations = [-3, 2, -2, 3, -1, 1]
cards = ""

for i, r in enumerate(recipes):
    ingredients_html = "".join(f"<li>{item}</li>" for item in r["ingredients"])
    steps_html = "".join(f"<li>{step}</li>" for step in r["steps"])
    rotation = rotations[i % len(rotations)]
    clip = paperclip_svg if i % 3 == 0 else ""

    cards += f"""    <div class="index-card" style="--rot: {rotation}deg;" data-name="{r['name'].lower()}">
      <div class="card-inner">
        <div class="card-face card-front">
          {clip}
          <span class="stamp {r['difficulty'].lower()}">{r['difficulty']}</span>
          <div class="card-emoji">{r['emoji']}</div>
          <h3>{r['name']}</h3>
          <p class="meta">{r['time']} &middot; serves {r['servings']}</p>
          <p class="flip-hint">tap to see recipe &rarr;</p>
        </div>
        <div class="card-face card-back">
          <h4>Ingredients</h4>
          <ul>{ingredients_html}</ul>
          <h4>Steps</h4>
          <ol>{steps_html}</ol>
          <p class="flip-hint">&larr; tap to flip back</p>
        </div>
      </div>
    </div>
"""

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

marker = "<!-- build.py fills this in -->"
html = html.replace(marker, cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ index.html updated with {len(recipes)} flip-cards!")