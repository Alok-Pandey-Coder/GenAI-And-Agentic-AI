import threading
import time 

def take_orders():
  for i in range(1, 4):
    print(f"Taking the order for #{i}")
    time.sleep(1)


def brew_chai():
  for i in range(1, 4):
    print(f"Brewing the chai for #{i}")
    time.sleep(2);

#create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

#start the threads
order_thread.start()
brew_thread.start()

#wait for both to finish
order_thread.join()
brew_thread.join()

print("All orders taken and brewed!")