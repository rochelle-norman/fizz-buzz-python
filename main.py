
#for loop to iterate over numbers passed in 100
for fizzbuzz in range(100):
    #if statement check if divisble by 3 and by 5
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
        # if only divisible by 3 print fizz
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
        # if only divisible by 5 print buzz
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)