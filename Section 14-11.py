def selection_sort_descend_trace(numbers):
    count = 0
    # To make sure, the list is not printing incorrectly. .


    if not numbers:
        numbers = [5, 2, 8, 1, 6]
    # This was as a just in case, if there were no numbers implemented.
    for i in range(len(numbers)):
        beeg = i
        # beeg, this is the big number being sorted.
        for j in range(i + 1, len(numbers)):
            # If the number is greater than the initilized beeg, it will become the new beeg number.
            # the i variable, will allow the next biggest number and conitnue to be sorted from there.
            if numbers[j] > numbers[beeg]:
                # This is to continue to sort the algorithem and finding the biggest number in the list.
                # The if function also allows for comparasion of the numbers.
                beeg = j

        if count >= 1:
            for display in numbers:
                print(display, end=" ")
                # The other print was added, to make a newline. Its more there for Zybooks
            print()

        # Swap the elements
        temp = numbers[i]
        numbers[i] = numbers[beeg]
        numbers[beeg] = temp
        count += 1

if __name__ == "__main__":
    calibrated = input().split()
    input_numbers= [int(x) for x in calibrated]
    # Turns the string elements into int.
    selection_sort_descend_trace(input_numbers)