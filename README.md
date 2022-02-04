CLI tool that can be used to do set operations like union on files considering them as a set of lines.

### Notes
- It ignores all empty lines with whitespaces.
- Each output line occurs only once, because we're treating the files as sets and the lines as their elements.
- List data type has been used instead of set to maintain the order of lines.
- It ignores all lines endings (`\r\n` or `\n`) when comparing lines, so two
  input lines compare the same if their only difference is that one ends in
  `\r\n` and the other in `\r`.

### Operations
- `union x y` outputs the lines that occur in either `x` or `y` or both.
- `intersection x y` outputs the lines that occur in both `x` and `y`.
- `difference x y` outputs the lines that occur in `x` but not in `y`.
- `is-subset x y` outputs whether all the lines in `x` are present in `y`.
- `is-superset x y` outputs whether all the lines in `y` are present in `x`.
- `is-equal x y` outputs whether all the lines in `x` are present in `y` and vice-versa.
- `is-disjoint x y` outputs whether there are no lines in common in `x` and `y`.
- `symmetric-difference x y` outputs the lines that occur in `x` but not in `y` and vice-versa.

### Installation
```
git clone https://github.com/daspartho/file-set.git
```
```
cd file-set
```
### Usage
```
python main.py <operation> <first file> <second file>
```
### Example
```
python main.py union test.py temp.txt
```