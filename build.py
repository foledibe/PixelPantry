import json

# Step 1: Read the recipe data
with open("recipes.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

# Step 2: Turn each recipe into an HTML card
cards = ""
for i, recipe in enumerate(recipes):
    ingredients_html = "".join(f"<li>{item}</li>" for item in recipe["ingredients"])
    steps_html = "".join(f"<li>{step}</li>" for step in recipe["steps"])

    cards += f"""    <div class="recipe-card" data-index="{i}">
      <h3>{recipe['name']}</h3>
      <p class="meta">⏱ {recipe['time']} · 🍽 serves {recipe['servings']}</p>
      <strong>Ingredients</strong>
      <ul>{ingredients_html}</ul>
      <strong>Steps</strong>
      <ol>{steps_html}</ol>
    </div>
"""

# Step 3: Insert the cards into index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

marker = "<!-- build.py fills this in -->"
html = html.replace(marker, cards)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ index.html updated with {len(recipes)} recipes!")