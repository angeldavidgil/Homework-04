# global variable
num_calls = 0

def partition(user_ids, low, high):
    # This makes sure to get the middle value of the list.
    midpoint = (low + high) // 2
    pivot = user_ids[midpoint]
    # done, is a failsafe so that it wont be stuck in a forever loop.
    done = False

    while not done:
        while user_ids[low] < pivot:
            # This part of the code finds the first element from the left,
            # and adds itself to compare the next element seeing what will be greater than or equal too.
            low += 1
        while pivot < user_ids[high]:
            # This does the same thing as above, but will find a number that is equal or lower to the pivot.
            high -= 1
        if low >= high:
            done = True
            # If its done correctly, low should be greater than high, making it true and stopping the loop.
        else:
            # If its not done right, it will flip and continue to go from there.
            user_ids[low], user_ids[high] = user_ids[high], user_ids[low]
            low += 1
            high -= 1

    return high
# once its done it will return high.

def quicksort(user_ids, low, high):
    global num_calls
    num_calls += 1

    if low < high:
        # gets the position of the pivot in the array. 
        pivot_index = partition(user_ids, low, high)

        # sorts the arrays on the left.
        quicksort(user_ids, low, pivot_index)
        # sorts the arrays on the right.
        quicksort(user_ids, pivot_index + 1, high)


if __name__ == "__main__":

    user_ids = []
    user_id = input()

    # Gets the users id to formulate a list, and will stop with -1.
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user in user_ids:
        print(user)
