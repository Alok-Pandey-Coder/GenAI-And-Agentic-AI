class OutOfIngredients(Exception):
  pass

def make_chai(milk, sugar):
  if milk == 0 or sugar == 0:
    raise OutOfIngredients("Missing milk or sugar")
  print("Chai is reday...")

make_chai(0, 0)