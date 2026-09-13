# generator function
def serve_chai():
  yield "cup 1: masala chai"
  yield "cup 2: ginger chai"
  yield "cup 3: lemon tea"

stall = serve_chai();
# for cup in stall:
#   print(cup);
print(next(stall));
print(next(stall));
print(next(stall));
# print(next(stall)) // StopIteration Error
