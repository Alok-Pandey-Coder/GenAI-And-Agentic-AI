users = [
  {"id": 1, "total": 100, "coupon": "P20"},
  {"id": 2, "total": 150, "coupon": "G20"},
  {"id": 3, "total": 200, "coupon": "L20"}
]

discounts = {
  "P20": (0.20, 0),
  "G20": (0.50, 0),
  "L20": (0, 10)
}

for user in users:
  percent, fixed = discounts.get(user["coupon"], (0, 0))
  discount = user["total"] * percent + fixed
  print(f"{user["id"]} paid {user["total"] - discount}")
