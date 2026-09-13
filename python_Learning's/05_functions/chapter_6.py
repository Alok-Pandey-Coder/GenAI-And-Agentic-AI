def update():
  chai_type = "Elaichi"
  def kitchen():
    nonlocal chai_type
    chai_type = "kesar"
  kitchen()
  print(f"chai after update: {chai_type}")

update();