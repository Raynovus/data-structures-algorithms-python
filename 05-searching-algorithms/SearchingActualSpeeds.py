# Name: Jon Luerssen
# Date: 4/3/2022

from LinearSearch import LinearSearch
from BinarySearch import BinarySearch
from Quicksort import Quicksort
from Client import Client
from datetime import date
import random
import time
import sys

# display name and date in output
print("Name:", "Jon Luerssen")
print("Date:", date.today())
print()

input_file_name = 'ClientData100.csv'
#input_file_name = 'ClientData1000.csv'
#input_file_name = 'ClientData10000.csv'
#input_file_name = 'ClientData100000.csv'

# create a list
clients = []

# read records from ClientData
with open(input_file_name) as infile:
    for line in infile:
        # split line based on the commas
        s = line.split(',')
        client_id = int( s[0] )
        f_name = s[1]
        l_name = s[2]
        phone = s[3]
        email = s[4]
        # client object
        clt = Client(client_id, f_name, l_name, phone, email)
        # add client object to list
        clients.append(clt)

# number of client objects
num_records = len(clients)

# Scenario: Search for # of records from a data file
section_title = "Secenario: Searching through " + str(num_records) + " Records"
print(section_title)
print("-" * len(section_title))

# must sort data for binary search
Quicksort.sort(clients)

# start and end record numbers
start_record = 100001
end_record = start_record + num_records

# how long does it take to search records
start_time = time.time()

# How long does it take to do a random search through the records
for i in range(1000):
    client_id = random.randint(start_record, end_record)
    clt = Client(client_id)
    result = BinarySearch.search(clients, clt)
    if result is None:
        print(clt, "was not found.")
    else:
        print(result)
    
end_time = time.time()
total_time = end_time - start_time
print("Seconds to search for 1000 random records: {:.6f}".format(total_time))

# display name and date in output
print("\nName:", "Jon Luerssen")
print("Date:", date.today())
print()













