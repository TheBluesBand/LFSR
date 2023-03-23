class LFSR:
    '''
    A small class implementation of a simple LFSR (Linear-feedback System Register).
    This differs from my previous lsfr implementation since I run the lfsr using 
    boolean values and not char values. I did this hoping to improve the speed of my
    lfsr since I am now working with smaller type class (bool compared to int).

    seed:       Intial binary seed of the lfsr
    taps:       Where we have our XOR taps in the lfsr
    iterations: How long the lfsr will run
    lfsr_state: If True you print the lfsr state instead of just the output
                bit of the current state. If False and you just print the
                output bit in lines of 8.
    '''

    def __init__(self, seed, taps, iterations=20, lfsr_state=False):
        #Check seed is valid
        for x in list(seed):
            if (x != '1'):
                if (x != '0'):
                    raise Exception("Seed contains characters other than 0 and 1")

        #Convert seed into true and false values
        inputed_seed = list(seed)
        array = []
        x = 0
        while x < len(inputed_seed):
            if inputed_seed[x] == '1':
                array.append(True)
            elif inputed_seed[x] == '0':
                array.append(False)
            else:
                raise Exception("Conversion from char to bool has failed")
            x += 1

        
        #Check taps contains valid tap locations
        for x in taps:
            if x > (len(seed) - 1):
                raise Exception("Tap location is invalid")
        i = 0

        #Set class attributes once all values have been checked/converted
        self.seed = array
        self.taps = taps
        self.iterations = iterations
        self.lfsr_state = lfsr_state

    def XOR(self, x, y):
        if x != y:
            return True
        else:
            return False

    def printLFSR(self):
        output_bits = 0
        i = 0
        current_state = self.seed

        #Run the LFSR 'iterations' times
        while (i < self.iterations):
            current_state.insert(0, current_state.pop())
            for x in self.taps:
                current_state[x] = self.XOR(current_state[x], current_state[0])

            #Print out lfsr output        
            if self.lfsr_state == True:
                if i == 0:
                    print("(The last bit is the output bit)")
                print([int(x) for x in current_state])
            else:
                output_bits += 1
                print(int(current_state[-1]), end="")
                if output_bits == 7:
                    print(int(current_state[-1]), end="\n")
                    output_bits = 0
            i += 1

    def outputLFSR(self):
        output_bits = 0
        i = 0
        current_state = self.seed
        output_bits = ""

        #Run the LFSR 'iterations' times
        while (i < self.iterations):
            current_state.insert(0, current_state.pop())
            for x in self.taps:
                current_state[x] = self.XOR(current_state[x], current_state[0])

            #Add the resulting bit to our current string
            output_bits = output_bits + str(int(current_state[-1]))
            i += 1

        #Output our result
        return output_bits

    def __str__(self):
        return "Intial State: {}\nTaps: {}\nIterations: {}".format([int(x) for x in self.seed], self.taps, self.iterations)  

