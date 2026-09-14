from functools import wraps

def auth_decorator(func):
  @wraps(func)
  def wrapper(user_role):
    if user_role != "admin":
      print("Access denied: Admins only")
    else:
      return func(user_role)
  return wrapper

@auth_decorator
def access_tea_inventory(role):
  print("Access granted to tea inventory")

access_tea_inventory("aam_admi");
access_tea_inventory("admin");