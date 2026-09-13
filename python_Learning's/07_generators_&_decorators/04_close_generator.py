def local_chai():
  yield "Masala chai"
  yield "ginger chai"

def imported_chai():
  yield "Match"
  yield "Oolong"

def full_menu():
  yield from local_chai();
  yield from imported_chai();


# for chai in full_menu():
#   print(chai);

def chai_stall():
  try:
    while True:
      print("Give me your order")
      order = yield "waiting for chai order"
      print(f"{order} prepared , Please take it")
  except:
    print("stall closed, No more chai")

stall = chai_stall()
next(stall)

stall.send("masala")
stall.send("oolong")
stall.close()

