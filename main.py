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

def is_subset(file1Path, file2Path):
    '''Return whether file1Path is a subset of file2Path'''
    if intersection(file1Path, file2Path) == fileToSet(file1Path):
        return [True]
    return [False]

def is_superset(file1Path, file2Path):
    '''Return whether file1Path is a superset of file2Path'''
    return is_subset(file2Path, file1Path)

def is_equal(file1Path, file2Path):
    '''Return whether the files are equal'''
    if is_subset(file1Path, file2Path)[0] and is_superset(file1Path, file2Path)[0]:
        return [True]
    return [False]

def is_disjoint(file1Path, file2Path):
    '''Return whether files are disjoint'''
    if intersection(file1Path, file2Path)==[]:
        return [True]
    return [False]

def symmetric_difference(file1Path, file2Path):
    '''Returns symmetric difference of files'''
    return difference(file1Path, file2Path) + difference(file2Path, file1Path)

def printLines(lines):
    '''Prints lines in list lines'''
    for line in lines:
        sys.stdout.write(f'{line}\n')
   
def result(args):
    '''Takes argument and returns the result of the set operation'''
    if args.op=='union':
        return union(args.file1Path, args.file2Path)
    elif args.op=='intersection':
        return intersection(args.file1Path, args.file2Path)
    elif args.op=='difference':
        return difference(args.file1Path, args.file2Path)
    elif args.op=='is-subset':
        return is_subset(args.file1Path, args.file2Path)
    elif args.op=='is-superset':
        return is_superset(args.file1Path, args.file2Path)
    elif args.op=='is-equal':
        return is_equal(args.file1Path, args.file2Path)
    elif args.op=='is-disjoint':
        return is_disjoint(args.file1Path, args.file2Path)
    elif args.op=='symmetric-difference':
        return symmetric_difference(args.file1Path, args.file2Path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('op', help='What operation?')
    parser.add_argument('file1Path', help='First file path?')
    parser.add_argument('file2Path', help='Second file path?')
    args = parser.parse_args()
    printLines(result(args))
        
if __name__ == '__main__':
    main()