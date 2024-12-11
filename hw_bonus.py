"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""


def longest_consecutive(my_list: list[int]) -> int:
    # write your code here
    if not my_list:
        return 0

    num_set = set(my_list)  # Use a set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Only check for the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""


def find_missing(my_list: list[int]) -> int:
    if not my_list or len(my_list) < 2:
        # If the list is empty or contains a single element, return None
        return None

    n = len(my_list) + 1  # Total elements including the missing one
    expected_sum = n * (n + 1) // 2  # Sum of the first n natural numbers
    actual_sum = sum(my_list)
    missing_number = expected_sum - actual_sum

    # Validate the missing number falls within the expected range
    if 1 <= missing_number <= n:
        return missing_number
    return None


"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""


def find_duplicate(my_list: list[int]) -> int:
    # write your code here
    # Floyd's Tortoise and Hare (Cycle Detection)
    slow, fast = my_list[0], my_list[0]

    while True:
        slow = my_list[slow]
        fast = my_list[my_list[fast]]
        if slow == fast:
            break

    # Find the entrance to the cycle
    slow = my_list[0]
    while slow != fast:
        slow = my_list[slow]
        fast = my_list[fast]

    return slow


"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    # write your code here
    from collections import defaultdict

    groups = defaultdict(list)

    for word in words:
        # Sort the word to form the key
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())
