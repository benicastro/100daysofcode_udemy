from art_files import treasure_art

print(treasure_art)
print("Welcome to Milyastroc's Treasure Island!")
print("Your mission is to find the treasure.")

# Island Adventure
print("You suddenly wake up from a deep sleep and found yourself in the middle"
      "of nowhere. You tried to look for familiar places but you ended being stuck "
      "at a crossroad")
ans_1 = input('Where do you want to go? Type "left" or "right": ')
if ans_1 == "left":
    print("Good choice! You suddenly hear weird noises from the other direction.")
    ans_2 = input("Now you've arrived at mysteriously-looking house. Do you want to enter? "
                  'Type "yes" or "no": ')
    if ans_2 == "yes":
        print("That was close! Monsters then came from all directions. Luckily, you're safe... for now.")
        ans_3 = input("Now there's an elevator that suddenly opened. It seemed like it wants you to ride it."
                      "Upon entering, you see that there are five floors to choose from. Would you stay of go"
                      'higher? Please choose floor, type a number from 1-5: ')
        if ans_3 == "5":
            print("It's wise you went to the top. Tons of weapons and treasures await you!")
        else:
            print("Oops! Wrong floor, you've been stabbed.")
    else:
        print("You're now being chased by tons of monsters and you regret not entering the house for shelter."
              "This is the end for you.")
else:
    print("You arrived at a monsters' den. With nowhere to run to, you were devoured by them.")

