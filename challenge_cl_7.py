# senario 1 print 10 to 5 tables in reverse order 

for i in range(10,4,-1):
    for j in range(10,0,-1):
        print(f"{i} * {j} = {i*j}")
    print("-"*20)