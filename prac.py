def print_items(name = 'Darshit', bg = 'O+ve'):
    print(name, bg)
d = { 'name' : 'Ragi', 'bg' : 'A+ve' }
print_items(*d)   
print_items(**d)  
d = dict()
print_items(**d)