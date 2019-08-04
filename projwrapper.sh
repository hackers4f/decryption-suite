#!/bin/bash
# Author: Janna Harding
# File:   projwrapper.sh
# Usage:  $ ./projwrapper.sh
# Desc:   this program is an interactive interface for running
#         the various decryption algorithms for the project.
#         not necessarily needed, but convenient for testing.
#         make sure you are in the code/ dir before running!
#

# build function calls for convenient execution
run="python3"
bin="./bin/"
srcpath="./src/proj_ciphertext/"

bcaesar="breakcaesar.py"
bvigenere="breakvigenere.py"
svigenere="solvevigenere.py"
bmyst="breakmystery.py"

caesar="simple-caesar.txt"
vign1="four-character-vigenere.txt"
vign2="six-character-vigenere.txt"
vign3="unknown-length-a-vigenere.txt"
vign4="unknown-length-b-vigenere.txt"
myst="mystery.txt"

script1="$run $bin$bcaesar   $srcpath$caesar  simple-caesar-dcpt.txt"
script2="$run $bin$bvigenere $srcpath$vign1 4 four-character-vigenere-dcpt.txt"
script3="$run $bin$bvigenere $srcpath$vign2 6 six-character-vigenere-dcpt.txt"
script4="$run $bin$bvigenere $srcpath$vign3   unknown-length-a-vigenere-dcpt.txt"
script5="$run $bin$bvigenere $srcpath$vign4   unknown-length-b-vigenere-dcpt.txt"
script6="$run $bin$bvigenere $srcpath$myst    mystery-dcpt.txt"
script7="$run $bin$svigenere $srcpath$myst privacyrules mystery-dcpt.txt"

while [ true ]
do
  # display menu
  echo "What would you like to do? (q to quit)"
  echo "1. Just decrypt all files"
  echo "2. Decrypt a particular file"
  read -sn 1 input

  if [ $input = 'q' ]
  then
    exit
  elif [ $input -eq 1 ]
  then
    echo
    $script1
    echo
    $script2
    echo
    $script3
    echo
    $script4
    echo
    $script5
    echo
    $script6
    echo "Oops! So close! Clearly, the password is 'privacyrules'"
    $script7
    echo
    exit
  elif [ $input -eq 2 ]
  then
    while [ true ]
    do
      echo "Decrypt which file? (q to quit)"
      echo "1. Simple Caesar"
      echo "2. 4-Character Vigenère"
      echo "3. 6-Character Vigenère"
      echo "4. ?-Character Vigenère a"
      echo "5. ?-Character Vigenère b"
      echo "6. Mystery Cipher"
      read -sn 1 input

      if [ $input = 'q' ]
      then
        exit
      elif [ $input -eq 1 ]
      then
        $script1
      elif [ $input -eq 2 ]
      then
        $script2
      elif [ $input -eq 3 ]
      then
        $script3
      elif [ $input -eq 4 ]
      then
        $script4
      elif [ $input -eq 5 ]
      then
        $script5
      elif [ $input -eq 6 ]
      then
        $script6
        echo "Oops! So close! Clearly, the password is 'privacyrules'"
        $script7
      else
        echo Input Error
      fi
      echo
    done
  else
    echo Input Error
  fi
done