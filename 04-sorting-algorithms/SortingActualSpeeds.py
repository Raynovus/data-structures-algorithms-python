# Name: Jon Luerssen
# Date: 3/27/2022

from MergeSort import MergeSort
from Client import Client
from datetime import date
import time

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

# Scenario: Sorting records from a data file
section_title = "Secenario: Sorting " + str(num_records) + " Records"
print(section_title)
print("-" * len(section_title))

# how long does it take to sort the records
start_time = time.time()

# Call the static sort method
MergeSort.sort(clients)
    
end_time = time.time()
total_time = end_time - start_time
print("Seconds to sort {0} records: {1:.6f}".format(num_records, total_time))

# Display the sorted list
#for clt in clients:
#    print(clt)













