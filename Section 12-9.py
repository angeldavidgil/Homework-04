'''
Student Name: Angel Gil
Class : CIS 2348
Student ID : 2255154
'''

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]

while name != '-1':
    # The only things that were added were the Try and Except portions.
    try:
        age = int(parts[1]) + 1
        print(f'{name} {age}')

    # Get next line
        parts = input().split()
        name = parts[0]

    except ValueError:
        # Putting age to 0, makes it possible to work, and continues as normal.
        age = 0
        print(f'{name} {age}')

        parts = input().split()
        name = parts[0]
