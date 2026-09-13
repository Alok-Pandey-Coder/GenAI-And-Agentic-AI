chai_type = "ginger"

def front_desk():
  def kitchen():
    global chai_type
    chai_type = "elaichi"

  kitchen()

front_desk()
print(f"chai after update: {chai_type}")