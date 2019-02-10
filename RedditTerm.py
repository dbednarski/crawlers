#!/usr/bin/env python
#

import argparse, sys
from readReddit import readReddit

if __name__ == "__main__":

    # Description for the help parameter (-h | --help)
    parser = argparse.ArgumentParser(description="Program to edit the text from \"file\" text file, fitting its content into lines with a maximum length. The output is the modified text printed on the terminal.")

    # Required argument
    parser.add_argument("subredds", help="List of subreddits separeted by semicolons (;)", type=str)
    args = parser.parse_args()

    # Call readReddit() function (from readReddit.py)
    printings = readReddit(args.__dict__["subredds"])
    print(printings)

    if printings[:4] == "ERROR":
        sys.exit(1)
    else:
        sys.exit(0)        
        
