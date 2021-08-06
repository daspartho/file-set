import os
import argparse
import sys

def removeTrails(lines):
    '''Removes trailing whitespaces from strings in list lines and returns list'''
    return [line.rstrip() for line in lines]

def removeEmptyLines(lines):
    '''Removes empty string with whitespaces from list lines and returns list'''
    return [line for line in lines if line.strip()]

def removeDuplicates(lines):
    '''Removes duplicate elements from list lines and returns list'''
    return [i for n, i in enumerate(lines) if i not in lines[:n]]

def fileToSet(filePath):
    '''Returns a set of lines from file'''
    with open(filePath) as file:
        return removeTrails(removeDuplicates(removeEmptyLines(file.readlines())))

def union(file1Path, file2Path):
    '''Returns union of files'''
    file1 = fileToSet(file1Path)
    file2 = fileToSet(file2Path)
    return file1 + [line for line in file2 if line not in file1]

def intersection(file1Path, file2Path):
    '''Returns intersection of files'''
    file1 = fileToSet(file1Path)
    file2 = fileToSet(file2Path)
    return [line for line in file1 if line in file2]

def difference(file1Path, file2Path):
    '''Returns difference of files'''
    file1 = fileToSet(file1Path)
    file2 = fileToSet(file2Path)
    return [line for line in file1 if line not in file2]

def printLines(lines):
    '''Prints lines in list lines'''
    for line in lines:
        sys.stdout.write(line+'\n')
   
def result(args):
    '''Takes argument and returns the result of the set operation'''
    if args.op=='union':
        return union(args.file1Path, args.file2Path)

    elif args.op=='intersection':
        return intersection(args.file1Path, args.file2Path)

    elif args.op=='difference':
        return difference(args.file1Path, args.file2Path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('op', help='What operation? Can choose union, intersection, or difference')
    parser.add_argument('file1Path', help='First file path?')
    parser.add_argument('file2Path', help='Second file path?')
    args = parser.parse_args()
    printLines(result(args))
        
if __name__ == '__main__':
    main()
