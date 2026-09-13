favourite_chai = [
  "masala chai", "ginger tea", "masala chai", "iced black tea", "ginger tea", "oolong tea"
]

unique_chai = {chai for chai in favourite_chai};
print(unique_chai);

recipes = {
  "masala chai": ["ginger", "cardmom", "clove"],
  "elaichi chai": ["cardmom", "milk"],
  "spicy chai": ["ginger", "black_pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices);