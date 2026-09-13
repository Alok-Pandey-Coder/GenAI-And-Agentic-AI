#parameters and arguments
# def greeting(name):
#   print(f"Hello : {name}")

# greeting("alok") 

# def greeting(salutation, name, date, place="noida"):
#   print(f"{salutation} {name} on {date} at {place}")

# greeting("Good morning", "alok", date="7-sep", place="agra")


def greeting(*args, **kwargs):
  print(f"{args[0]} {args[1]} on {kwargs.get('date')} at {kwargs.get('place')}")
  print(f"args: {args} ans kwargs: {kwargs}")

greeting("Good morning", "alok", date="7-sep", place="noida")
