#Andrey Ilkiv midterm exam question 1

num = 1
count = 1
num = int(input("Please enter an integer (>= 2): "))
while num > 0:
    count == 0
    if num > 1 :
        for i in range(1 , num) :
            if(num % i) == 0 :
                count += 1
                print(i , " is a factor of " , num)
        else:
            print(i + 1 , " is a factor of " , num)
    if count == 2:
        print("\n", end="")
        print(num , "has " , count , "factors")
        print(num , " is a prime number!" , "\n")
    else:
        print("\n", end="")
        print(num , "has" , count - 1, "factors" , "\n")
    num = int(input("Please enter an integer (>= 2): "))
        
print("Finished!")
