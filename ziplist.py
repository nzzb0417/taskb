# ziplist.py

# Name: Abdimalik Hussein
# Username: nzzb0417

# Lists contents of a zip archive [1]
# usage: python ziplist.py <zipfile> [1]
# eg. python ziplist.py tests/test.zip [1]
# You must use the error messages precisely as defined below. [1]

# Hint: look at the documentation for the "zipfile" module [1]

import sys [1]
import zipfile   # tools in this module can be used [1, 2]
# filename is a command line argument [1, 2]
try: [1, 2]
    file_name = sys.argv[2] [1, 2]
except: [1, 2]
    sys.exit("Usage: python ziplist.py <file.zip>") [1, 2]


# if zipfile.is_zipfile(file_name) == True: [1-3]
#     sys.exit(f"Bad zip file: python ziplist.py {file_name}") [1-3]

# if zipfile.is_zipfile(file_name) == True: [2-4]
#     sys.exit(f"Bad zip file: python ziplist.py {file_name}") [2-4]

if ".zip" in file_name: [1-4]
    try: [1-4]
        with zipfile.ZipFile(file_name, "r") as f: [1-4]
            list = f.namelist() [1-4]
            print(f"The contents of {file_name} are {list}") [1-4]
    except: [2-4]
        sys.exit(f"File not found: python ziplist.py {file_name}") [2-4]
else: [2-4]
    sys.exit(f"Bad zip file: python ziplist.py {file_name}") [2-4]



# Error message: "Usage: python ziplist.py <filename.zip>" [2-4]

# Error message: "File not found: python ziplist.py {file_name}" [2-4]


# Error message: "Bad zip file: python ziplist.py {file_name}" [2-4]
# Hint: there is an exception for this defined in the zipfile module [2-4]

# Use zipfile methods to list the contents of the zip file. [3, 4]
# Test your script on the zip example.zip file. The response should be: [3, 4]
# hi.py [3, 4]
# and_line.py [3, 4]
# find_file.py [3, 4]
# password.py [3, 4]
# rockpaperscissors.py [3, 4]


# file_line_count.py [4]
