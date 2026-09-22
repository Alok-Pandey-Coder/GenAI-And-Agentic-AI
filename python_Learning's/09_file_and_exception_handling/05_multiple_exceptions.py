def process_order(item, qty):
  try:
    price = {"masala": 20}[item]
    cost = price * qty
    print(f"Total cost: {cost}")
  except KeyError:
    print("Quantity must be in number")

process_order("ginger", 2)
process_order("masala", None)