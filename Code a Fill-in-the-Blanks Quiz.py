# The easy empty fill-in-the-blank and its corresponding answers.
# It will take the input from user and place the answers in blanks#
easy_fib = ["Two balls and two", "___1___", "on him. Here's the pitch on the "
            "way. A swing and a belt! Left field...way back...BLUE JAYS WIN "
            "IT! The Blue Jays are", "___2___", "Series Champions, as Joe",
            "___3___", "hits a three-run home run in the ninth", "___4___",
            "and the Blue Jays have repeated as World Series Champions!",
            "___5___", "'em all, Joe! You'll never hit a bigger home run in "
            "your life!"]
#The below mention correct answers of the easy fill in blanks#
easy_answers = ["strikes", "World", "Carter", "inning", "Touch"]

# The medium empty fill-in-the-blank and its corresponding answers.
medium_fib = ["1 and 1 on Jose. All eyes on the mound and the bearded Sam",
              "___1___", ". Now he comes set. Kicks, the 1-1 pitch. FLY BALL, "
              "DEEP", "___2___", "FIELD! YES SIR!", "___3___", "!", "___4___",
              "!", "___5___", "! Blue Jays 6,", "___6___", "3. Jose",
              "___7___", "is unbelievable!"]
medium_answers = ["Dyson", "LEFT", "THERE", "SHE", "GOES", "Rangers",
                  "Bautista"]

# The hard empty fill-in-the-blank and its corresponding answers.
hard_fib = ["Deux balles deux prises a Russell", "___1___", "et voila le "
            "signal de", "___2___", ". La balle est frappee avec force au "
            "champ gauche et...ELLE EST", "___3___", "!", "___4___", "!",
            "___5___", "!", "___6___", "!", "___7___", "! Le Quebec danse! Le",
            "___8___", "danse! Et RUSSELLLLL quel chef d'orchestre. Bonsoir, "
            "elle est partie."]
hard_answers = ["Martin", "McCann", "PARTIE", "RUSSELL", "RUSSELL", "RUSSELL",
                "RUSSELL", "Canada"]

#This fundtion will check the difficuly level and return it as per user inputs easy, medium or hard#
# This function is also take input from the user #

def load_fib_difficulty():

    level = raw_input("\nPlease select a difficulty level"
                      "(easy, medium, or hard): ")
    if level.lower() == "easy":
        return easy_fib, easy_answers, "easy"
    if level.lower() == "medium":
        return medium_fib, medium_answers, "medium"
    if level.lower() == "hard":
        return hard_fib, hard_answers, "hard"
    else:
        print "You selected an invalid difficulty level!"
        return load_fib_difficulty()

#This function will remove the soacess from the string#

def remove_spaces_before_punc(fib_string):

    fib_string = fib_string.replace(" .", ".")
    fib_string = fib_string.replace(" !", "!")
    return fib_string


#This function check compare the answers from user and will place it#

def guess_check(blank_number, fib, answers, answer):

    blank = "___" + str(blank_number) + "___"
    guess = raw_input("Please fill in blank #" + str(blank_number) +
                      " (case-sensitive): ")
    if guess == answer:
        fib[fib.index(blank)] = answer
        print remove_spaces_before_punc(" ".join(fib)) + "\n"
        blank_number += 1
        return blank_number
    else:
        print "Incorrect. Please try again.\n"
        return guess_check(blank_number, fib, answers, answer)

#This function  will print after join the string#

def play_game():

    fib, answers, level = load_fib_difficulty()
    print ("\nHere is the fill-in-the-blank for the " + level + " difficulty "
           "level:")
    print remove_spaces_before_punc(" ".join(fib)) + "\n"

    blank_number = 1
    for answer in answers:
        blank_number = guess_check(blank_number, fib, answers, answer)

    print ("Congratulations, you have filled in all of the blanks!")

#Call the function play game#
play_game()