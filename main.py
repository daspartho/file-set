import os

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
    file2 = fileToSet(pfile2Path)
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

def takeInput():
    '''Prompts user for input and returns input'''
    while True:    
        file1Path = input("First file's path: ")
        if os.path.exists(file1Path):
            break
        print('File not found! Try Again!')

    while True:
        file2Path = input("Second file's path: ")
        if os.path.exists(file2Path):
            break
        print('File not found! Try Again!')
        
    while True:
        op = (input("Operation: ")).lower()
        if op in ['union', 'intersection', 'difference']:
            break
        print('Not an operation (union, intersection, difference)! Try Again!')
        
    return file1Path, file2Path, op

def printLines(lines):
    '''Prints lines in list lines'''
    for line in lines:
        print(line)
        
def main():
    file1Path, file2Path, op = takeInput()

    if op=='union':
        printLines(union(file1Path, file2Path))

    elif op=='intersection':
        printLines(intersection(file1Path, file2Path))

    elif op=='difference':
        printLines(difference(file1Path, file2Path))

if __name__ == '__main__':
    main()
