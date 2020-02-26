print("Give a string")

string = input()

def StringToAscii(target_string):
    # transform string to ascii
    target_string_ascii_code = ''.join(str(ord(c)) for c in target_string)
    print(target_string_ascii_code)

    # make ascii string an int
    ascii_code_int = int(target_string_ascii_code)

    isPrime = True
    #check if number is prime
    if ascii_code_int > 1: 
        # iterate from 2 to n / 2  
        for i in range(2, ascii_code_int//2): 
            # if num is divisible by any number between 2 and n / 2, it is not prime  
            if (ascii_code_int % i) == 0: 
                print(ascii_code_int, "is not a prime number") 
                isPrime=False
                break
        if(isPrime==True):
            print(ascii_code_int, "is  a prime number")    
  
    else: 
        print(ascii_code_int, "is not a prime number") 

StringToAscii(string)
