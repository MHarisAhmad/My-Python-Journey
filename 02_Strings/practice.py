# Working with strings

#-----------------------------------------

# Task 1: Checking whether a word lies in the sentence or not
#---------------------------------------------

def check_word(sentence,word):                                               # general function
    return word in sentence.split()
def main():                                                                  # main_function
    sentence = input("Enter sentence here:")
    word = input("Enter word here:")
    if check_word(sentence,word):
        print(f"Your word \'{word}\' exists in \'{sentence}\'")
    else:
        print(f"Your word \'{word}\' does not exist in \'{sentence}\'")

if __name__ == "__main__":                                                  # (Optional) Runs the code only if it is executed directly, does not run imported file
    main()                                                                  # function call


