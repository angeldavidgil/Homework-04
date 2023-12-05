'''
Student Name: Angel Gil
Class : CIS 2348
Student ID : 2255154
'''

def get_age():
    try:
        age = int(input())
        #  Gets the Age that requested, and checks if its within the range.
        if (age > 18) and (age < 75):
            heart = fat_burning_heart_rate(age)
            # Gets the valuable, by using the function.
            print(f"Fat burning heart rate for a {age} year-old: {heart:.1f} bpm")
            return age
        else:
            raise ValueError
        # If it doesnt fit our criteria, so it brings up an error.
    except ValueError as lol:
        # The varible (lol), will save the text to share below.
        raise ValueError("Could not calculate heart rate info.\n") from lol


def fat_burning_heart_rate(age):
    heart_rate = .7 * (220 - age)
    # omg math
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
    except ValueError as lol:
        print(f"Invalid age.\n{lol}")
        # lol will be spitting out the saved text to be said.
