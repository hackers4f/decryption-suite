# Author: Janna Harding
# File:   breakvigenere.py
# Usage:  $ python3 breakvigenere.py to_decrypt.txt ?pswd_length output_name.txt
# Desc:   this program decrypts data encoded by a vigenere cipher; works for
#           passwords of known and unknown length
#         omitting the optional pwd_length argument assumes unknown length
#

# import necessary packages
import sys
sys.path.append(sys.path[0] + "/../lib/")
from cryptotools import getShift, findPswdLen, caesar, chunk, unchunk
from cryptotools import special, numbers, LOWERCASE_A_ASCII

# check for correct argument list
if len(sys.argv) != 3 and len(sys.argv) != 4:
  print("Argument Error! Expected format:\n" +
        "python3 breakvigenere.py to_decrypt.txt ?pswd_length output_name.txt")
  sys.exit()

# define some important things
SRC  = sys.argv[1]
OUT  = sys.path[0] + "/../output/"

if len(sys.argv) == 3:   OUTFILENAME = sys.argv[2]
elif len(sys.argv) == 4: OUTFILENAME = sys.argv[3]
else:
  print("Unknown Error. Aborting...")
  sys.exit()
OUT += OUTFILENAME

infile  = open(SRC, 'r')
outfile = open(OUT, 'w')

# provide some output
print("Breaking encryption on file " + sys.argv[1] + "...")

# get data to decrypt
data = str(infile.read()).lower()

# determine length of password, if necessary
if len(sys.argv) == 4: PSWDLEN = int(sys.argv[2])
else: 
  PSWDLEN = findPswdLen(data)
  print("Most probable password length: " + str(PSWDLEN))

# break source text into as many chunks pswd length, store punctuation data
subsect, punct = chunk(data, PSWDLEN)

# determine the shift value for each chunk of text
shifts = []
for string in subsect: shifts.append(getShift(string))

# provide some output
pswd = "".join([ chr(char + LOWERCASE_A_ASCII) for char in shifts ])
print("Passphrase found: \'" + pswd + "\'")

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