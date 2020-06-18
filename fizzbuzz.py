# Ios are the factors and their outputs
ios = {3: "Fizz", 5: "Buzz", 7: "Bizz", 11: "Fuzz"}

# E.G. if the number is a factor of 3: output fizz. Same with the others.

for x in range(105):
    x+= 1
    output = ""

    for n in ios:
        if x % n == 0:
            output += ios[n]
            
    if not output:
        print(x)
    else:
        print(output)
