import math
import argparse

def numberOfIncrements_sliding_window( arr ):
    count = 0
    prev = math.inf

    if len(arr) < 3:
        print('array is too small to process with sliding window!')
        return 0
    sums = list()
    indices = [0, 1, 2]
    while( indices[2] < len(arr) ):
        sums.append( sum( [ arr[i] for i in indices ] ) )
        indices = [ i + 1 for i in indices ]

    for i in sums:
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
    
    print( numberOfIncrements_sliding_window( arr ) )

if __name__ == '__main__':
    main()
