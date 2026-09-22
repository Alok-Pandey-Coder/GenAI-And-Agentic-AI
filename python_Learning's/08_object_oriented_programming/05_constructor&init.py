class ChaiOrder():

  def __init__(self, type_, size):
    self.type = type_
    self.size = size;

  def summary(self):
    return f"{self.size},l of {self.type} chai"

order = ChaiOrder("Masala", 200)
print(order.summary())