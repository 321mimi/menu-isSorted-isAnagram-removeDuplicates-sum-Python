# Lab 7
# By Michelle Cantin

# Option 1: isSorted
def isSorted(xs):
    if sorted(xs) == xs:
        return True
    else:
        return False

# Option 2: isAnagram
def isAnagram(stringOne, stringTwo):
    stringOne = stringOne.replace(" ", "")
    stringTwo = stringTwo.replace(" ", "")
    if sorted(stringOne) == sorted(stringTwo):
        return True
    else:
        return False

# Option 3: removeDuplicates
def removeDuplicates(xs):
    xs = set(xs)
    return xs

# Option 4: sumOfSquares
def sumOfSquares(xs):
    finalSum = xs[0] + xs[1] + xs[2] + xs[3]
    return finalSum

# Inputs for 1, 3, 4
def inputs():
    first = input("Insert the first value of the list ")
    second = input("Insert the second value of the list ")
    third = input("Insert the third value of the list ")
    fourth = input("Insert the fourth value of the list ")
    xs = [first, second, third, fourth]
    return xs

# Menu
def main():
    choice ='0'
    while choice =='0':
        choice = input ("Menu: \nChoose which function you would like to test.\nOption 1: isSorted\nOption 2: isAnagram\nOption 3: removeDuplicates\nOption 4: sumOfSquares\nOption 5: Exit\nPlease make a choice: ")

        # Test function isSorted
        if choice == "1":
            xs = inputs()
            if isSorted(xs):
                print("The list is sorted!")
            else:
                print("The list is not sorted!")

        # Test function isAnagram
        elif choice == "2":
            stringOne = input("Insert the first word ")
            stringTwo = input("Insert the second word ")
            if isAnagram(stringOne, stringTwo):
                print("The two words are anagrams!")
            else:
                print("The two words are not anagrams!")

        # Test function removeDuplicates
        elif choice == "3":
            xs = inputs()
            xs = list(map(int, xs))
            print("With only unique elements, the list returns as follows:", removeDuplicates(xs))
            
        # Test function sumOfSquares
        elif choice == "4":
            xs = inputs()
            xs = list(map(int, xs))
            print("The sum of the four numbers is", sumOfSquares(xs))

        # Exit
        elif choice == "5":
            exit()

        # Invalid choice
        else:
            print("I don't understand your choice.")
            
        # Return to menu
        key = input("Press enter to return to the main menu")
        main()
main()
