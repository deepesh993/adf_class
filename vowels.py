name = input("Enter a string: ")
vowels=["a","e","i","o","u","A","E","I","O","U"]

count = 0

for char in name:
    if char in vowels:
        count+=1
    else:
        pass

print(f"the name {name} has {count} vowels")    