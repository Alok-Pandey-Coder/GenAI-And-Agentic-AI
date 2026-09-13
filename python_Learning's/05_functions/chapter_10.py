chai_types = ["kadak ginger", "ginger", "oolong", "kadak masala"]

strong_chai = list(filter(lambda chai: chai.startswith('kadak'), chai_types))
print(strong_chai)