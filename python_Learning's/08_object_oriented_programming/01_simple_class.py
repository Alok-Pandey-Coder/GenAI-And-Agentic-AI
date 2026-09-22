class Chai:
  pass

class ChaiTime:
  pass

print(type(Chai))

ginger_chai = Chai()
print(type(ginger_chai))
print(type(ginger_chai) is Chai)
print(type(ginger_chai) is ChaiTime)