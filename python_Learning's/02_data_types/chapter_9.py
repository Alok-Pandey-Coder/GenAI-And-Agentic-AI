# dictionary creation
chai_order = dict(type="Masala chai", size="Large", sugar=2)
print(f"chai order: {chai_order}")
print(type(chai_order))

# dictionary creation
chai_recipe = {}

# adding the key-value pairs
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

# accesing the vaule corresponding to key
print(f"chai recipe: {chai_recipe}")
print(f"chai base: {chai_recipe['base']}");

# membership checkin in dictionary
print(f"is 'black tea' in chai recipe: {"base" in chai_recipe}")

# how to get keys and values from the dictionary
chai_order = {"type":"Ginger", "size":"medium", "sugar":1} 
print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (keys): {chai_order.values()}")
print(f"Order items: {chai_order.items()}")

# pop last item
last_item = chai_order.popitem()
print(f"last_item: {last_item}")



