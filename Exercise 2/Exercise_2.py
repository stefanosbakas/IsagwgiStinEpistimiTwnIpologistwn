# define which consonants are "good"
good_consonants = "qwtpsdghjzlxvbnm"

# define which consonants are "bad" 
bad_constants = "ckfr"

# open the given file
t = open(r'testText.txt', "r")

# scan through it
for line in t:
    for word in line.split():
        bad_consonants_count = 0
        good_consonants_count=0
        for x in word.lower():
            # count the consonants by category
            if x in bad_constants:
                   bad_consonants_count+=1
            if x in good_consonants:
                    good_consonants_count+=1

        # name each word approprietly           
        if bad_consonants_count>good_consonants_count:
            print("the word " + word + " is bad")
        else: print("the word " + word + " is good")
            