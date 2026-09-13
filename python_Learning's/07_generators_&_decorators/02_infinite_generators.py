def infinite_chai():
  count = 1
  while True:
    yield f"refill #{count}"
    count += 1

refill = infinite_chai()

for _ in range(3):
  print(next(refill))