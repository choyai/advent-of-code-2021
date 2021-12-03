import math
import argparse

def numberOfIncrements( arr ):
    count = 0
    prev = math.inf

    for i in arr:
        if i > prev:
            count += 1
        prev = i
    return count

def main():

    parser = argparse.ArgumentParser(description = 'counts number of increases in list')
    parser.add_argument( 'file_path', help = 'path of file' )

    args = parser.parse_args()
    
    arr = []

    with open( args.file_path, 'r' ) as f:
        arr = [ int(x) for x in f ]
    
    print( numberOfIncrements( arr ) )

if __name__ == '__main__':
    main()
