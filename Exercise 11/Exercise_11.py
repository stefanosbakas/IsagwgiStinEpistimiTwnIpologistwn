#BEST TESTED WITH input: [x,x,3,4,5,6]
numbers=[]
#ask for numbers
print("Give numbers in order of priority")

#check if input is digit and add it in a list
i=0
while i <6:
    _input=input()
    if(_input.isdigit()):
        numbers.append(int(_input))
        i+=1
    else:     
        print("Please, give only numbers")
    

print("Given numbers are " + str(numbers)) 

#save the 3 quadruples in another list
quadros=[0,0,0]
final=[]
x=0
while x<3:
    for i in range(4):
        #each digit in the first list represents a digit in a 
        # single number in the second list by multiplying it with 
        # the corresponding power of 10 and adding it in the sum
        quadros[x]+=numbers[i+x]*(10**i)
    #reverse the created number and add it in the final list    
    final.append(str(quadros[x])[::-1])
    x+=1

words = []
# open the given file
t = open(r'testText.txt', "r")

# scan through it and save each "word" in a list
for line in t:
    for word in line.split():
        words.append(word)

i=0
found = False
while i<3:
    #compare each "word" in our list with each of the 3 quadruples
    for x in range(len(words)):
        if(words[x] == final[i]):
            found = True
            print("In the .txt file here is a match for quadruple number " + str(i+1))
    i+=1
if(found == False):
    print("No match found in the .txt file")       