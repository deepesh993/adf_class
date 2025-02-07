#what is a method?

def employee(name):
    print(f"{name} belongs to j2d")

employee("Deepesh")
employee("Pooja")
employee("pradeep")

print()
print("******************\n")


def outer_method(z):
    z=100+z
    def inner_method ():
        nonlocal z
        z= 20
        print(f"this is my inner method value: {z}")
    
    inner_method()
    print(f"this is my outer method value: {z}")

outer_method(100)
print("*******************\n")


## default function
print("*********Default paramater***********")

def employee(name : str, salary : int = 10000):
    print(f"{name} salary is {salary}")
    

employee("deepesh")
employee("Pooja", 60000)