#
#  Homework 01 - Complexity
#
#
#  For the following functions, write the expected Time and Auxiliary Space
#  Complexity using what you know about nested loops, hash table look-ups and
#  the runtime of built in functions.
#
#  NOTE: You don't need to code to anything for these problems, just write
#  what you the complexity to be using big-O notation


#  Order of Magnitude
#
#  Reduce the following into it's Big-O order of magnitude.
#
#  1. 5 + N                    // N
#  2. N + N^2                  // N^2
#  3. 15N + 13N                // N
#  4. 10000                    // 1
#  5. log(N) + 1               // log(N)
#  6. log(N) * 3 + 14N + 3     // N
#  7. Nlog(N) + 3N^2           // N^2
#  8. N^3 + log(N^4)           // N^3
#  9. N! + 180000N^2           // N!
#  10. 15002^N                 // 15002^N


#
#  List the time and auxiliary space complexity of each of the following functions.
#


#
#    Index Of
#
#    Given an array of integers and a target value, return the index of the first
#    element that matches the target value. If there are no matches, return -1.
#
#    Parameters
#    Input: arr {Array of Integers}
#    Input: target {Integer}
#    Output: {Integer}
#
#    Examples
#    [1, 2, 3, 4, 5, 6], 5 --> 4
#    [9, 83, 74], 8 --> -1
#    [6, 4, 7, 9, 7, 8, 2, 4, 3], 7 --> 2

# Time Complexity: O(N)
# Auxiliary Space Complexity: O(1)

def index_of(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


#    Evens
#
#    Given an array of integers, return an array of only the even values.
#
#    Parameters
#    Input: arr {Array of Integers}
#    Output: {Array of Integers}
#
#    Examples
#    [1, 2, 3, 4, 5, 6] --> [2, 4, 6]
#    [9, 83, 74] --> [74]
#    [6, 4, 7, 9, 7, 8, 2, 4, 3] --> [6, 4, 8, 2, 4]

# Time Complexity: O(N)
# Auxiliary Space Complexity: O(N)

def evens(arr):
    results = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            results.append(arr[i])
    return results



#   Split
#
#   Given a string of characters, return an array with each character separated
#   into its own separate item.
#
#   Parameters
#   Input: str {String}
#   Output: {Array of Characters}
#
#   Examples
#   'hello' --> ['h', 'e', 'l', 'l', 'o']
#   'foo' --> ['f', 'o'. 'o']
#
#
# Time Complexity: O(N)
# Auxiliary Space Complexity: O(N)

def split(string):
    results = []
    for i in range(len(string)):
        results.append(string[i])
    return results

#
#   Sum
#
#   Given an array of integers, return the sum of all the integers.
#
#   Parameters
#   Input: arr {Array of Integers}
#   Output: {Integer}
#
#   Examples
#   [1, 2, 3, 4, 5] --> 15
#   [0, 1, -1] --> 0
#   [] --> 0
#
# Time Complexity: O(N)
# Auxiliary Space Complexity: O(1)

def sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total


#   Merge Arrays

#   Given two sorted arrays of integers, return a merged sorted array of both inputs.
#
#   Parameters
#   Input: arr1 {Array of Integers}
#   Input: arr2 {Array of Integers}
#   Output: {Array of Integers}
#
#   Examples
#   [1, 3, 9], [2, 4, 8] --> [1, 2, 3, 4, 8, 9]
#   [12, 25, 40], [20, 37, 45] --> [12, 20, 25, 37, 40, 45]
#   [10, 13, 24], [12, 35] --> [10, 12, 13, 24, 25]
#
# Time Complexity: O(N + M)
# Auxiliary Space Complexity: O(N + M)


def merge_arrays(left, right):
    sorted_array = []
    p1 = 0
    p2 = 0
    while p1 < len(left) and p2 < len(right):
        if left[p1] <= right[p2]:
            sorted_array.append(left[p1])
            p1 += 1
        else:
            sorted_array.append(right[p2])
            p2 += 1
    if p1 >= len(left):
        sorted_array.extend(right[p2:])
    if p2 >= len(right):
        sorted_array.extend(left[p1:])
    return sorted_array



#    Counting Sort
#
#    Given an array and a range (min and max), use counting sort to sort the input array.
#
#    Parameters
#    Input: arr {Array of Integers}
#    Input: min {Integer}
#    Input: max {Integer}
#    Output: {Array of Integers}

#    Examples
#    [5, 3, 1, 8, 9] --> [1, 3, 5, 8, 9]
#    [8, 1, 3, 4, 6, 9] --> [1, 3, 4, 6, 8, 9]
#    [4, 0, 1, 5, 6] --> [0, 1, 4, 5, 6]

# Time Complexity: O(N + K)
# Auxiliary Space Complexity: O(K)

def counting_sort(arr, min, max):
    count = [0] * (max - min + 1)
    for num in arr:
        count[num - min] = count[num - min] + 1
    index = 0
    for i in range(min, max + 1):
        while count[i - min] > 0:
            arr[index] = i
            index += 1
            count[i - min] = count[i - min] - 1
    return arr


#    Binary Search
#
#    Given a sorted array and a target value, use binary search to return the index of the target in the input array.
#    Return -1 if no such target is found.
#
#    Parameters
#    Input: arr {Array of Integers}
#    Input: val {Integer}
#    Output: {Integer}
#
#    Examples
#    [1, 3, 4, 5, 8, 9], 5 --> 3
#    [5, 7, 10, 12, 14], 7 --> 1
#    [2, 4, 8, 9, 15], 3 --> -1
#
# Time Complexity: O(log(N))
# Auxiliary Space Complexity: O(1)

def binary_search(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] > val:
            high = mid - 1
        elif arr[mid] < val:
            low = mid + 1
        else:
            return mid
    return -1


#    Factorial
#
#    Given an input integer n, return the n factorial value.
#
#    Parameters
#    Input: n {Integer}
#    Output: {Integer}
#
#   Examples
#   5  --> 120 (5 * 4 * 3 * 2 * 1)
#   1 --> 1 (1)
#   9 --> 362880 (9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)

# Time Complexity: O(N)
# Auxiliary Space Complexity: O(N)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)



# Time Complexity: O(1)
# Auxiliary Space Complexity: O(1)
def first_times_last(arr):
    result = None
    if len(arr) < 2:
        return result
    result = arr[0] * arr[len(arr) - 1]
    return result


# Time Complexity: O(N)
# Auxiliary Space Complexity: O(1) - assuming 26 characters in the alphabet
def most_frequent_occurrence(str):
    lower_str = str.lower()
    letters = {}
    most_frequent = []

    for i in range(0, len(lower_str)):
        if lower_str[i] in letters:
            letters[lower_str[i]] += 1
        else:
            letters[lower_str[i]] = 1

    for key in letters:
        if len(most_frequent) == 0 or letters[key] > most_frequent[1]:
            most_frequent = [key, letters[key]]

    return most_frequent[0]


# Time Complexity: O(N^2)
# Auxiliary Space Complexity: O(1)
def print_unordered_pairs(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            print(str(arr[i]) + "," + str(arr[j]))


# Time Complexity: O(log(N))
# Auxiliary Space Complexity: O(log(N))
def sorted_list_search(sorted_list, target):
    def hunt(start, finish):
        if start > finish:
            return False
        mid = (start + finish) / 2
        if sorted_list[mid] == target:
            return True
        if sorted_list[mid] > target:
            return hunt(start, mid-1)
        return hunt(mid + 1, finish)

    return hunt(0, len(sorted_list) - 1)


# Time Complexity: O(MN
# Auxiliary Space Complexity: O(MN)
def make_combined_matrix(list_one, list_two):
    result = []
    for i in range(0, len(list_one)):
        row = []
        for j in range(0, len(list_two)):
            row.append(list_one[i] + list_two[j])
        result.append(row)
    return result


# Time Complexity: O(1)
# Auxiliary Space Complexity: O(1)
def is_there_cat(obj):
    while('cat' in obj):
        print('There is cat!')
        obj.pop('cat', None)
    print('There is no cat!')


# Time Complexity: O(1)
# Auxiliary Space Complexity: O(1)
def power_of_threes(int):
    result = []
    count = 1
    temp = 1

    while(count <= 3):
        temp *= int
        result.append(temp)
        count += 1

    return result


# Time Complexity: O(N^2)
# Auxiliary Space Complexity: O(1)
def find_duplicate(collection):
    length = len(collection)
    for i in range(0, length):
            current = collection[i]
            for j in range(0, length):
                if j != i and current == collection[j]:
                    return True
    return False


# Time Complexity: O(MN)
# Auxiliary Space Complexity: O(MN)
def intersection_points(arr1, arr2):
    result = []
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if (arr1[i] == arr2[j]):
                points = [arr1[i], arr2[j]]
                result.append(points)
    return result


# Time Complexity: O(N)
# Auxiliary Space Complexity: O(N)
def nth_fibonacci(n):
    result = [0, 1]
    for i in range(1, n):
        result.append(result[i] + result[i - 1])
    return result[n]


#  Extra Credit 1:
#
#  Problem: Refactor find_duplicate such that it now finds and returns all
#           repeating elements in O(N) time complexity.
#  Auxiliary Space Complexity: O(N)
def find_duplicate(lst):
    lib = {}
    results = []

    for item in lst:
        if item in lib:
            lib[item] += 1
        else:
            lib[item] = 1

    for key in lib:
        if lib[key] > 1:
            results.append(key)

    return results


# Extra Credit 2:
#
# Time Complexity: O(N)
# Auxiliary Space Complexity: O(N)
def nth_fibonacci(n):
    cache = {}

    def search_fib(index):
        if index in cache:
            return cache[index]
        if index < 2:
            return index
        result = search_fib(index-2) + search_fib(index-1)
        cache[index] = result
        return cache[index]

    return search_fib(n)
