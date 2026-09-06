seat_type = input("Enter seat type (sleeper/AC/luxury/general)").lower()

match seat_type:
  case "sleeper":
    print("No AC but beds are available")
  case "ac":
    print("AC beds are available")
  case "general":
    print("cheapest option, no reservation")
  case "luxury":
    print("Full Air conditioned cabins with food available!")
  case _:
    
