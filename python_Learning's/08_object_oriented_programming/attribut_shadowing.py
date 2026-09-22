class Chai:
  temp = "hot"
  strength = "strong"

cutting = Chai()
print(cutting.strength)
print(cutting.temp)

cutting.strength = "Mild"
print(cutting.strength)
print(Chai.strength)

del cutting.strength
print(cutting.strength)
