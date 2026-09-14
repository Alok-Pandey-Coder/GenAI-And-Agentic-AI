from functools import wraps
def my_decorator(func):
  @wraps(func)
  def wrapper():
    print(f"Performing all operations before excuting the main function")
    func()
    print(f"Framing out the answers comes from the model")
  return wrapper


@my_decorator
def greet():
  print(f"GOOD MORNING ALOK SIR!")

greet()
print(greet.__name__)
