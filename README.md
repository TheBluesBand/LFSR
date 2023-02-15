# Linear-feedback System Register (LFSR)
Here we have a simple python implementation of a binary LFSR (Linear-feedback System Register). An LFSR is a simple way to generate long and seemingly random sequence of bits which can be used as a pseudorandom number generator in stream ciphers.  
  
## Implemenation  
The implementation you see here is what is called an Xorshift LFSR which uses XOR's and shift operations to change the state of the LFSR. It uses an inputted seed which is used as the intial state of the LFSR. An array called taps where we input the indexes of where the XOR gates tap into. The number of iterations the LFSR will run for and a boolean input which when True prints out the current state of the LFSR rather than just the output bit of the current state.

### Difference in file
There are two files in the main folder one label lfsr.py and the other bool_lfsr.py. The first is my first implementation where I save the seed as an array of chars. That however seemed like it would be inificant since I go back and forth comparing it as a char then an int elseware so I then decided to make the second. The second (bool_lfsr.py) instead simplifies the process since we treat 0's and 1's as boolean values saving memory space and hopefully increase the speed of the lfsr.

### Comparing the two
I intended on comparing how quickly these go against each other when I have some spare time.

## Why I made this?  
In my Introduction to Cryptography coarse we learn about different cryptographic system across history and I thought implementing some of these would help my understanding of how they work and to see them actually implemented rather just on lecture slides
