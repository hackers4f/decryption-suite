# Author: Janna Harding
# File:   vigeneregen.py
# Usage:  $ python3 vigneregen.py to_encrypt.txt passphrase
# Desc:   this program reads a source text file and encrypts it
#           using a vignere cipher with the given passphrase
#

# import necessary packages
import sys
sys.path.append(sys.path[0] + "/../lib/")
from cryptotools import caesar, chunk, unchunk
from cryptotools import LOWERCASE_A_ASCII, special, numbers

# check for correct argument list
if len(sys.argv) < 3:
  print("Error: arguments should be file to encrypt, then a passphrase")
  sys.exit()

# define some important things
PSWD 	= list(sys.argv[2].lower())
SRC     = sys.argv[1]
OUT     = sys.path[0] + "/../src/vcipher.txt"
infile  = open(SRC, 'r')
outfile = open(OUT, 'w')

# provide some output
print("Encrypting file code/" + SRC + "...")

# get source text from file
srcStr = str(infile.read()).lower()

# convert password to integers for shifting
for index, char in enumerate(PSWD):
  PSWD[index] = ord(char) - LOWERCASE_A_ASCII

# break source text into as many chunks as the password has chars
subsect, punct = chunk(srcStr, len(PSWD))

# encrypt subsections
for index, string in enumerate(subsect):
  subsect[index] = caesar(string, PSWD[index])

# rebuild full encrypted string
result = unchunk(subsect, punct)

# write result to file, clean up, provide output
outfile.write(result)
infile.close()
outfile.close()
print("Encrypted file path: code/src/vcipher.txt")