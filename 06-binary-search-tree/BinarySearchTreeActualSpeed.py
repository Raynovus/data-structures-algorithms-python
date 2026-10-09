# Name: Jon Luerssen
# Date: 4/10/2022

from BinarySearchTree import BinarySearchTree
from Client import Client
from datetime import date
import time
import random
import sys

# display name and date in the output
print("Name: Jon Luerssen")
print("Date:", date.today())
print()

clients = []

input_file_name = "ClientData.csv"
with open(input_file_name) as infile:
    for line in infile:
        s = line.split(',')
        client_id = int( s[0] )
        f_name = s[1]
        l_name = s[2]
        phone = s[3]
        email = s[4]
        # create client object using data from line
        clt = Client(client_id, f_name, l_name, phone, email)
        # add client object to the list
        clients.append(clt)
        
# numver of client objects
num_records = len(clients)

# create binary search tree to test real-world speeds
my_bst = BinarySearchTree()

# Scenario 1: Printer queue or call queue or service queue
section_title = "Scenario: Printer Queue or Call Queue or Service Queue"
print(section_title)
print("-" * len(section_title))

# how long does it take to add the client records to the BST
start_time = time.time()

for i in range(num_records):
    my_bst.insert(clients[i])
    
end_time = time.time()
total_time = end_time - start_time
print("Seconds to add records: {0:.6f}".format(total_time))

# how long does it take to remove records from the front of the BST
start_time = time.time()

for i in range(num_records):
    my_bst.remove_minimum()
    
end_time = time.time()
total_time = end_time - start_time
print("Seconds to remove records: {0:.6f}".format(total_time))

# Scenario 2: Customer Service Center
answer = input("Continue (y/n)? ")
if answer.lower() != "y":
    sys.exit()

section_title = "Scenario: Customer Service Center"
print(section_title)
print("-" * len(section_title))

# add clients to BinarySearchTree
for i in range(num_records):
    my_bst.insert(clients[i])

# how long does it take to randomly display 1000 client records to the BST
start_time = time.time()

for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print( my_bst.search(Client(random_num)))
    
end_time = time.time()
total_time = end_time - start_time
print("Seconds to display 1000 random records: {0:.6f}".format(total_time))

# Scenario 3: Call Center
answer = input("Continue (y/n)? ")
if answer.lower() != "y":
    sys.exit()

section_title = "Scenario: Call Center"
print(section_title)
print("-" * len(section_title))

# add clients to BinarySearchTree
for i in range(num_records):
    my_bst.insert(clients[i])

# how long does it take to add more client records to the BST
# randomly display 1000 records and randomly remove 1000 records from the BST
start_time = time.time()

# add records
current_id = 100001 + num_records + 1
for i in range(1000):
    my_bst.insert(Client(current_id))
    current_id += 1

# display records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print( my_bst.search(Client(random_num)))
    
# remove 1000 random records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    my_bst.remove(Client(random_num))
    
end_time = time.time()
total_time = end_time - start_time
print("Seconds to add records,")
print("display 1000 random records,")
print("and remove 1000 random records: {0:.6f}".format(total_time))
    
    











