def chai_customer():
  print("Welcome ! what would you like to order")
  order = yield
  while True:
    print(f"prepraing the {order}")
    order = yield

stall = chai_customer();
next(stall);
stall.send("Masala chai")
stall.send("Lemon tea")