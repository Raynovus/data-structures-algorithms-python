# Name: Jon Luerssen
# Date: 3/20/2022

from Queue import Queue
from Call import Call
from datetime import date
import time
import random

print("Name:", "Jon Luerssen")
print("Date:", date.today())
print()

calls = []

imput_file_name = "CallsData.csv"
with open(imput_file_name) as infile:
    for line in infile:
        # split line based on commas
        s = line.split(',')
        client_id = int( s[0] )
        client_name = s[1]
        client_phone = s[2]
        # create a Call object
        a_call = Call(client_id, client_name, client_phone)
        # add the Call object to list
        calls.append(a_call)
        
# Queue object for calls
calls_waiting = Queue()
call_number = 0

# length of simulation
seconds = int( input("How many seconds do you want to simulate? "))

# run the simulation for given # of seconds
for i in range(seconds):
    print("-" * 40)
    time.sleep(2)
    random_event = random.randint(1, 3)
    # event based on random number gen
    if random_event == 1:
        print("Call recieved. Caller added to queue.")
        calls_waiting.enqueue( calls[call_number] )
        call_number += 1
        print("\tNumber of calls waiting in queue:", calls_waiting.get_length())
    elif random_event == 2:
        print("Call sent to representative for service.")
        if calls_waiting.get_length() > 0:
            print("Caller information:")
            print(calls_waiting.dequeue())
        else:
            print("The call waiting queue is empty.")
        print("\tNumber of calls waiting in queue:", calls_waiting.get_length())
    else:
        print("Nothing haappened during this second in time.")
        print("\tNumber of calls waiting in queue", calls_waiting.get_length())
        
print("\nThe 'Automatic Call Distributor' simulation has completed.")