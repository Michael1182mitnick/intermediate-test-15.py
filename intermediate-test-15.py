# Write a program to find all duplicate elements in an array.

def find_duplicates(arr):
    seen = set()        # Set to store unique elements
    duplicates = set()  # Set to store duplicate elements

    for num in arr:
        if num in seen:
            # If num is already in 'seen', it's a duplicate
            duplicates.add(num)
        else:
            seen.add(num)  # Otherwise, add it to 'seen'

    return list(duplicates)


# Example usage
arr = [1, 2, 3, 4, 5, 5, 2, 6, 3, 7, 8, 9, 1]
result = find_duplicates(arr)
print(f"Duplicate elements are: {result}")
