# Lessons learned


## EXTRACT VALUE FROM TXT
```Python
with open("input.txt", 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    print(lines)
```
if "input.txt" is on the same folder it can find it by name, otherwise provide full path.
**If using path remember to use doble backslash.**
 In Windows paths, backslashes are used as escape characters, so you need to either use raw strings or double the backslashes. 

