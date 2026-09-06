cricket_items = ('Bat', 'Ball', 'Stumps', 'Players') #packing

print(f"cricket item tuple: {cricket_items}");

# unpacking
(item1, item2, item3, item4) = cricket_items

print(f"cricket items: {item1}, {item2}, {item3}, {item4}")

item1_ratio, item2_ratio = 2, 1
print(f"item1 ratio: {item1_ratio} ans item2 ratio: {item2_ratio}")
item1_ratio, item2_ratio = item2_ratio, item1_ratio
print(f"item1 ratio: {item1_ratio} ans item2 ratio: {item2_ratio}")

print(f"is Gloves in cricket item: {'gloves' in cricket_items}")




