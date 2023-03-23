from bool_lfsr import LFSR

if __name__ == '__main__':
    #Using the LFSR as a random number generator
    #Create and run the LFSR function that outputs a value
    example = LFSR("1101101", [1, 3, 5], 32, True)
    print(example)
    number = example.outputLFSR()

    #Print the output bits we get from the LFSR
    print("Bit value: " + number)

    #Print the output bits as a integer
    print("Integer value: " + str(int(number, 2)))