# decryption-suite
Implements basic encryption schemea such as the Caesar cipher and the Vigenere Cipher, and includes algorithms for breaking these schema.
Author: Janna Harding
File:   readme.md
Desc:   this file contains instructions for running
        the project's various decryption algorithms


In order to execute the decryption algorithms for the project, you may either run
the projwrapper.sh script, or manually run the python scripts in the ./bin dir.

If you intend to use the wrapper (recommended), you may need to 
allow execute permissions. ex:
  $  chmod +x projwrapper.sh

To run the wrapper, simply do
  $  ./projwrapper.sh

This will open a menu that allows for easy execution of the scripts; just 
follow the prompts and it will describe the output path for each script.

If you intend to run an individual script, the wrapper's menu provides
functionality for that. However, if you'd prefer to not use the wrapper, do
  $  python3 ./bin/your_choice.py ./src/source_file.txt

Specific instructions for individual scripts are included at the top of the files.
All output will appear in the ./output dir, named based on the original files.

If you're curious, the text in ./src/source.txt comes from a loreum ipsum generator
that generates an endless amount of business jargon instead of the typical Latin.
  http://officeipsum.com/