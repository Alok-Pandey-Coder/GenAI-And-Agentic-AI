# example 1
for token in range(1, 11):
  print(f"Serving the token #{token}")

#example 2
for batch in range(1, 5):
  print(f"Prepring the batch #{batch}")

# example 3
orders = ["alok", "ayush", "kishan", "yash", "aman"]

for name in orders:
  print(f"Serving order for #{name}")

# example 4
menu = ["Green", "Lemon", "Ginger", "Black"]

for idx, item in enumerate(menu, start= 1):
  print(f"{idx} : {item}")