# kwargs
#This help use to go throw key and value

def print_kwars(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        

print_kwars(name = "hello")