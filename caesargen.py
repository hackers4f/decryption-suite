# Author: Janna Harding
# File:   caesargen.py
# Usage:  $ python3 caesargen.py to_encrypt.txt [a-z]
# Desc:   this program reads a source text file and generates a
#           caesar cipher with the given shift character

import sys
sys.path.append(sys.path[0] + "/../lib/")
from cryptotools import caesar
from cryptotools import LOWERCASE_A_ASCII

# check for correct argument list
if len(sys.argv) < 3:
  print("Error: arguments should be file to encrypt, then a shift value")
  sys.exit()

# define some important things
SHIFT   = sys.argv[2]
SRC     = sys.argv[1]
OUT     = sys.path[0] + "/../src/ccipher.txt"
infile  = open(SRC, 'r')
outfile = open(OUT, 'w')

# provide some output
print("Encrypting file code/" + SRC + "...")

# gets a string to encrypt, then performs encryption
srcStr = str(infile.read()).lower()
result = caesar(srcStr, ord(SHIFT) - LOWERCASE_A_ASCII)

# write result to file, clean up, provide output
outfile.write(result)
infile.close()
outfile.close()
print("Encrypted file path: code/src/ccipher.txt")