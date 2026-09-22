chai_menu = {"masala": 30, "ginger": 40}

try:
  chai_menu["Oolong"]
except KeyError:
  print("The key doesn't exist")

print("Codes execution doesnt stop due to error")