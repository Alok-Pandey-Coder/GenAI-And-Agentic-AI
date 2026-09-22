# file = open('orders.txt', 'w')
# try:
#   file.write("Mai likh raha hun")
# finally:
#   file.close()

with open('orders.txt', 'w') as file:
  file.write("ginger tea - 4 cups")