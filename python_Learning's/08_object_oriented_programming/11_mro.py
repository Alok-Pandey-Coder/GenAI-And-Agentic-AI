class A:
  message = "Hi, I am talking from A"

class B(A):
  message =  "Hi, I am talking from B"

class C(A):
  message =  "Hi, I am talking from C"

class D(B, C):
  pass

var = D()
print(var.message)
print(D.__mro__);