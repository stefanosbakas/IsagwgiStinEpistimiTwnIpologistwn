numberIsValide=False

print("Give Creadit Card number")

# check input
while numberIsValide != True: 
    creditCardNumber=input()
    try:
        # check if input is numbers
        x=int(creditCardNumber)

        # check if input is 16 numbers long
        if len(creditCardNumber)==16:
            numberIsValide=True
        else:
            print("Please give a valid credit card number")
    except:
        print("Please give a valid credit card number")
        
# add the digits if necessairy
def add_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

def validate(num):
    # reverse the credit card number (cannot use .reverse() in strings)
    num = num[::-1]
    print(num)
    
    # convert to integer list
    num = [int(x) for x in num]
    # double every second digit
    final_list = list()
    digits = list(enumerate(num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            final_list.append(digit * 2)
        else:
            final_list.append(digit)

    # add the digits if any number is more than 9
    final_list = [add_digits(x) for x in final_list]
    # sum all digits
    totalSum = sum(final_list)
    # return True or False
    return totalSum % 10 == 0


print(validate(creditCardNumber))