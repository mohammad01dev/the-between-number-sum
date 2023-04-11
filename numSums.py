numberRange = input("Please The Spicife Number: ")

latinLetters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q","r","s","t","u","v","w","x","y","z")


if str(numberRange):
    if numberRange in latinLetters:
        print("please the String")
    else:
        int(numberRange)
        sum = 0
        for i in range(1,int(numberRange)+1):
            sum += i
        print(sum)
else:
    print("False")
