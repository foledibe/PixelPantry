// Flip a card on click
document.getElementById("recipe-list").addEventListener("click", (e) => {
  const card = e.target.closest(".index-card");
  if (card) card.classList.toggle("flipped");
});

// Surprise Me — picks a random visible card and flips it into view
document.getElementById("surprise-btn").addEventListener("click", () => {
  const cards = Array.from(document.querySelectorAll(".index-card")).filter(
    (c) => c.style.display !== "none",
  );
  if (cards.length === 0) return;

  cards.forEach((c) => c.classList.remove("flipped"));

  const pick = cards[Math.floor(Math.random() * cards.length)];
  pick.scrollIntoView({ behavior: "smooth", block: "center" });
  setTimeout(() => pick.classList.add("flipped"), 300);
});

// Live search
document.getElementById("search-bar").addEventListener("input", (e) => {
  const query = e.target.value.toLowerCase();
  document.querySelectorAll(".index-card").forEach((card) => {
    const name = card.getAttribute("data-name");
    card.style.display = name.includes(query) ? "" : "none";
  });
});
