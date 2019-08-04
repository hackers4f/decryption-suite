# Author: Janna Harding
# File:   solvevigenere.py
# Usage:  $ python3 solvevigenere.py to_decrypt.txt passphrase output_name.txt
# Desc:   this program solves a vigenere cipher with a given passphrase
#

# import necessary packages
import sys
sys.path.append(sys.path[0] + "/../lib/")
from cryptotools import caesar, chunk, unchunk
from cryptotools import LOWERCASE_A_ASCII

# check for correct argument list
if len(sys.argv) != 4:
  print("Argument Error! Expected format:\n" + 
        "python3 solvevigenere.py to_decrypt.txt passphrase output_name.txt")
  sys.exit()

# define some important things
OUTFILENAME = sys.argv[3]
PSWD	    = sys.argv[2].lower()
SRC         = sys.argv[1]
OUT         = sys.path[0] + "/../output/" + OUTFILENAME
infile      = open(SRC, 'r')
outfile     = open(OUT, 'w+')

# provide some output
print("Solving Vigenère cipher " + SRC + " with passphrase \'" + PSWD + "\'")

# get data to decrypt
data = str(infile.read()).lower()

# break source text into as many chunks pswd length, store punctuation data
subsect, punct = chunk(data, len(PSWD))

# get the shift value for each chunk of text
shifts = []
for item in list(PSWD):
  shifts.append(ord(item) - LOWERCASE_A_ASCII)

# decrypt subsections
for index, string in enumerate(subsect): 
  subsect[index] = caesar(string, -shifts[index])

# rebuild full decrypted string
result = unchunk(subsect, punct)

# write result to file, clean up, provide output
outfile.write(result)
infile.close()
outfile.close()
print("Decrypted file path: ./output/" + OUTFILENAME)