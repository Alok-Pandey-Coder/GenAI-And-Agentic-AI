# Set is know for its uniqueness
essential_spices = {"cardmon", "ginger", "cinnamon", "cinnamon"}
print(type(essential_spices))
print(essential_spices);

optional_spices = {"cloves", "ginger", "black pepper"}

# Union of sets
all_spices = essential_spices | optional_spices
print(f"all spices: {all_spices}")

# Intersetion of sets
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

# difference operations in sets
only_essential_in_all_spices = all_spices - optional_spices
print(f"only essential in all spices: {only_essential_in_all_spices}")

# Membership in sets
print(f"id 'Cloves' is in essential spices: {"cloves" in optional_spices}")

