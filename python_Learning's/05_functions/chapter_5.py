def serve_chai():
  chai_type = "masala"
  print(f"Inside function {chai_type}")

chai_type = "ginger"
serve_chai()
print(f"Ouside function: {chai_type}")

def chai_counter():
  chai_order = "lemon"
  def print_order():
    chai_order = "ginger"
    print("Inner:", chai_order)
  print_order()
  print("Outer:", chai_order)