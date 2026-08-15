document.getElementById("surprise-btn").addEventListener("click", () => {
  const cards = document.querySelectorAll(".recipe-card");
  if (cards.length === 0) return;

  // Remove any old highlight
  cards.forEach((card) => card.classList.remove("highlight"));

  // Pick a random card
  const randomCard = cards[Math.floor(Math.random() * cards.length)];
  randomCard.classList.add("highlight");
  randomCard.scrollIntoView({ behavior: "smooth", block: "center" });
});
