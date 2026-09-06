device_status = "active"
temperature = 34

if device_status == "active":
  if temperature > 35:
    print("Warn!: High temperature")
  else:
    print("Normal Temperature")
else:
  print("Device is offline!")