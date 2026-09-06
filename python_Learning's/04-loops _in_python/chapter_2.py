names = ["Kishan", "alok", "aman", "ayush", "yash"]
bills = [4000.30, 0, 120, 0, 0]

for name, amount in zip(names, bills):
  print(f"{name} has to spend(kharcha) of Rs.{amount}")