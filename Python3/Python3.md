# Write Python Script
You need to define in your .py file 2 things:
- Language use with ``` #!/usr/bin/python ```
- Coding ``` # -*- coding: utf-8 -*- ```

# Debug Python program

Module PDB (Python Debugger) is very usefull because he permit to debug each line of the code.
First you need to download it with : pip3 install pdb

After that, put on the very beginning of you script:
```
improt pdb
pdb.set_trace()
```
Now if you start your script, you will see which lie is execute and what is the output

# ArgParse
This module permit to read parameters entered when you execute the program.
```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("test",help="This is a test")
args ) parser.parse_args()
print(args)
```
