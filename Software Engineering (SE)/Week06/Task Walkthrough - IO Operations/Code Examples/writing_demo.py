'''
You are an event organiser. Your client has a list of VIP 
guests for their event. Write a program that creates this 
guest list. Each time you ask the user for a guest name, 
you should write these details into a file, with each entry 
separated by a line.
'''

num_vips = int(input('How many VIPs will be attending? '))

with open('event_vip_guest_list.txt', 'w') as file:

   for _ in range(num_vips):
      name = input('Enter guest name: ')

      file.write(f"{name}\n")