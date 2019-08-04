# Author: Janna Harding
# File:   breakcaesar.py
# Usage:  $ python3 breakcaesar.py to_decrypt.txt output_name.txt
# Desc:   this program takes data encrypted by a simple caesar cipher and
#           performs frequency analysis to break the encryption. 
#         output is placed in code/output/ under the name of 3rd arg specified.
#

# import necessary packages
import sys
sys.path.append(sys.path[0] + "/../lib/")
from cryptotools import caesar, getShift
from cryptotools import LOWERCASE_A_ASCII

# check for correct argument list
if len(sys.argv) != 3:
  print("Argument Error! Expected format:\n" + 
        "python3 breakcaesar.py to_decrypt.txt output_name.txt")
  sys.exit()

# define some important things
OUTFILENAME = sys.argv[2]
SRC         = sys.argv[1]
OUT         = sys.path[0] + "/../output/" + OUTFILENAME
infile      = open(SRC, 'r')
outfile     = open(OUT, 'w+')

# provide some output
print("Breaking encryption on file " + SRC + "...")

# get data to decrypt
data = str(infile.read()).lower()

# determine shift value
shift = getShift(data)

# provide some output
print("Shift value found: " + chr(shift + LOWERCASE_A_ASCII))

# perform decryption
result = caesar(data, -shift)

# write result to file, clean up, provide output
outfile.write(result)
infile.close()
outfile.close()
print("Decrypted file path: ./output/" + OUTFILENAME)