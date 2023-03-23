from bool_lfsr import LFSR

def input_arguments():
    #Get user input for how the LFSR works
    IS = input("Input Intial State: ")
    taps = [int(x) for x in input("Enter XOR taps: ").split()]
    IT = int(input("Iterations: "))
    state = input("Do you want to see LFSR state? Y/N: ")
    Bool = False
    if state == 'Y':
        Bool = True

    #Create the LFSR using the LFSR function
    inputted_LFSR = LFSR(IS, taps, IT, Bool)
    print(inputted_LFSR)
    inputted_LFSR.printLFSR()

def example_lfsr():
    example = LFSR("1001101", [1, 3, 5], 16, True)
    print(example)
    example.printLFSR()

def menu():
    #Ask the user to see if they want to choose the lfsr or have an example
    print("Here is a python implementation of a binary Xorshift LFSR.")
    menu = True
    while (menu):
        input_ = input("Do you want to input an lfsr? Y/N: ")
        if input_ == "Y":
            input_arguments()
            menu = False
        elif input_ == "N":
            example_lfsr()
            menu = False
        else:
            print("Invalid Input, please select a valid object")

def main():
    #Interactive menu for the user
    menu()
    

if __name__ == '__main__':
    main()