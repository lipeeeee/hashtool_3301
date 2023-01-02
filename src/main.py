import os
import argparse
from utils import SUPPORTED_ALGOS, DEEPWEB_HASH
from functions.Blake512 import Blake512
from functions.SHA512 import SHA512

'''
    COMMAND LINE TOOL TO ASSIST IN DECODING THE DEEP WEB
    HASH IN THE PAGE 56 LIBER PRIMUS, THE HASH COMES FROM
    A 512bit HASH FUNCTION 
    (THE CURRENTLY SUPPORTED HASH FUNCTIONS
    ON THIS TOOL ARE IN utils.py)
'''
def main(args):
    pass

def process_args(args):
    bruteforce = args.bruteforce
    encode = args.encode
    message = args.message
    algorithm = None
    if args.algorithm:
        if args.algorithm.upper() in [x.upper() for x in SUPPORTED_ALGOS]:
            index = [x.upper() for x in SUPPORTED_ALGOS].index(args.algorithm.upper())
            algorithm = SUPPORTED_ALGOS[index]

    # Default Cases
    if (not encode or not bruteforce):
        encode = False
        bruteforce = True
    if (message is None):
        message = DEEPWEB_HASH

    if (encode and bruteforce):
        print("Cannot encode(-e) and bruteforce(-b) at the same time")
        return -1
    elif (algorithm is None):
        print("No/Invalid algorithm(-a) provided, supported algorithms: " + ", ".join(SUPPORTED_ALGOS))
        return -1
    
    return [bruteforce, encode, message, algorithm]

# Entry Point
if __name__ == "__main__":
    os.system("cls")

    # CMD Argument Parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "-M", "--message", help="message to be processed")
    parser.add_argument("-a", "-A", "--algorithm", help="algorithm to be used")
    parser.add_argument("-b", "-B", "--bruteforce", action="store_true", help="flag to know to bruteforce a message")
    parser.add_argument("-e", "-E", "--encode", action="store_true", help="flag to know to encode a message")

    # send processed args
    args = process_args(parser.parse_args())
    if args != -1:
        main(args)