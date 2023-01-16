class LFSR:
    def __int__(self, seed, taps, iterations=20, lfsr_state=False):
        self.seed = seed
        self.taps = taps
        self.iterations = iterations
        self.lfsr_state = lfsr_state

    def __str__(self):
        return "Intial State: {self.seed}\nTaps: {self.taps}\nIterations: {self.iterations}"

def XOR(x, y):
    if x != y:
        return '1'
    else:
        return '0'

def lfsr(seed, taps, iterations=20, lfsr_state=False):
    '''
    A small implementation of a simple LFSR (Linear-feedback System Register)
    that takes in the intial seed, an array of where the taps are wanted, how
    many iterations of the lfsr you want (Default is 20) and if you want to
    print the LFSR State instead of just the output bits.

    seed:       Intial binary seed of the lfsr
    taps:       Where we have our taps in the lfsr
    iterations: How long the lfsr will run
    lfsr_state: If True you print the lfsr state instead of just the output
                bit of the current state. If False and you just print the
                output bit in lines of 8.
    '''

    #Check seed is valid
    for x in list(seed):
        if (x != '1'):
            if (x != '0'):
                raise Exception("Seed contains characters other than 0 and 1")
    
    #Check taps contains valid tap locations
    for x in taps:
        if x > (len(seed) - 1):
            raise Exception("Tap location is invalid")
    
    i = 0
    array = list(seed)
    output_bits = 0
    #Run the LFSR 'iterations' times
    while (i < iterations):
        array.insert(0, array.pop())
        for x in taps:
            array[x] = XOR(array[x], array[0])
                
        if lfsr_state == True:
            print(str(array) + " <-- Output Bit")
        else:
            if (output_bits < 7):
                print(array[-1], end="")
                output_bits += 1
            else:
                print(array[-1], end='\n')
                output_bits = 0
        i += 1

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
    LFSR = lfsr(IS, taps, IT, Bool)

def example_lfsr():
    print("Intial State:\t1001101")
    print("XOR Taps:\t[1, 3, 5]")
    print("Iterations:\t16")
    print("LFSR State:\tTrue")
    LFSR = lfsr("1001101", [1, 3, 5], 16, True)

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
            print("Input selection again")

def main():
    #Interactive menu for the user
    menu()
    

if __name__ == '__main__':
    main()
