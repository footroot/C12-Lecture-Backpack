'''
You are an event organiser. You have a file with 
the names of people you work with and the service
they offer. Our goal is to read the file and 
display the services offered by the people in your
contact list.
'''

# Open and read the file
with open('event_items.txt', 'r') as file:
    lines = file.readlines()
    # print(lines)

# Initialise list for services we extract
services = []

for line in lines:
    name, service = line.strip().split(':')
    services.append(service.strip())

# print(services)

for item in services:
    print(item)