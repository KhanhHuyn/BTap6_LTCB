# 1. Write a Python program to sum all the items in a list.
def sum_list(lst):
    return sum(lst)
print(sum_list([1, 2, 3, 4]))

# 2. Write a Python program to multiply all the items in a list.
import math
def multiply_list(lst):
    return math.prod(lst)
print(multiply_list([1, 2, 3, 4]))

# 3. Write a Python program to get the largest number from a list.
def max_list(lst):
    return max(lst)
print(max_list([1, 8, 3, 7]))

# 4. Write a Python program to get the smallest number from a list.
def min_list(lst):
    return min(lst)
print(min_list([1, 8, 3, 7]))

# 5. Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.
def count_strings(lst):
    return len([s for s in lst if len(s) >= 2 and s[0] == s[-1]])
print(count_strings(['abc', 'xyz', 'aba', '1221']))

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple.
def sort_by_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])
print(sort_by_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# 7. Write a Python program to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# 8. Write a Python program to check if a list is empty or not.
def is_empty(lst):
    return len(lst) == 0
print(is_empty([]))
print(is_empty([1, 2]))

# 9. Write a Python program to clone or copy a list.
def clone_list(lst):
    return lst.copy()
print(clone_list([1, 2, 3]))

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def words_longer_than_n(words, n):
    return [w for w in words if len(w) > n]
print(words_longer_than_n(["one", "three", "seven", "two"], 3))

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def common_member(lst1, lst2):
    return any(i in lst1 for i in lst2)
print(common_member([1, 2, 3], [3, 4, 5]))

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
def remove_indices(lst):
    return [x for i, x in enumerate(lst) if i not in (0, 4, 5)]
print(remove_indices(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
def generate_array():
    return [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
print(generate_array())

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
def remove_even(lst):
    return [x for x in lst if x % 2 != 0]
print(remove_even([1, 2, 3, 4, 5, 6]))

# 15. Write a Python program to shuffle and print a specified list.
import random
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list([1, 2, 3, 4, 5]))

# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30.
def squares_list():
    squares = [x**2 for x in range(1, 31)]
    return squares[:5] + squares[-5:]
print(squares_list())

# 17. Write a Python program to check if each number is prime in a given list of numbers.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def all_primes(lst):
    return all(is_prime(x) for x in lst)
print(all_primes([3, 5, 7, 13]))
print(all_primes([0, 3, 4, 7, 9]))

# 18. Write a Python program to generate all permutations of a list in Python.
import itertools
def list_permutations(lst):
    return list(itertools.permutations(lst))
print(list_permutations([1, 2, 3]))

# 19. Write a Python program to calculate the difference between the two lists.
def list_difference(lst1, lst2):
    return list(set(lst1) - set(lst2)) + list(set(lst2) - set(lst1))
print(list_difference([1, 2, 3], [2, 4, 5]))

# 20. Write a Python program to access the index of a list.
def access_index(lst):
    return [(i, v) for i, v in enumerate(lst)]
print(access_index(['a', 'b', 'c']))

# 21. Write a Python program to convert a list of characters into a string.
def chars_to_string(lst):
    return ''.join(lst)
print(chars_to_string(['H', 'e', 'l', 'l', 'o']))

# 22. Write a Python program to find the index of an item in a specified list.
def find_index(lst, item):
    return lst.index(item)
print(find_index([10, 20, 30, 40], 30))

# 23. Write a Python program to flatten a shallow list.
import itertools
def flatten_list(lst):
    return list(itertools.chain.from_iterable(lst))
print(flatten_list([[1, 2], [3, 4], [5]]))

# 24. Write a Python program to append a list to the second list.
def append_list(lst1, lst2):
    return lst1 + lst2
print(append_list([1, 2, 3], [4, 5, 6]))

# 25. Write a Python program to select an item randomly from a list.
import random
def random_item(lst):
    return random.choice(lst)
print(random_item([1, 2, 3, 4, 5]))

# 26. Write a Python program to check whether two lists are circularly identical.
def circularly_identical(lst1, lst2):
    return len(lst1) == len(lst2) and any(lst1 == lst2[i:] + lst2[:i] for i in range(len(lst2)))
print(circularly_identical([1, 2, 3], [2, 3, 1]))
print(circularly_identical([1, 2, 3], [3, 1, 2]))

# 27. Write a Python program to find the second smallest number in a list.
def second_smallest(lst):
    return sorted(set(lst))[1]
print(second_smallest([1, 2, 3, 4, 5]))

# 28. Write a Python program to find the second largest number in a list.
def second_largest(lst):
    return sorted(set(lst))[-2]
print(second_largest([1, 2, 3, 4, 5]))

# 29. Write a Python program to get unique values from a list.
def unique_values(lst):
    return list(set(lst))
print(unique_values([1, 2, 2, 3, 4, 4, 5]))

# 30. Write a Python program to get the frequency of elements in a list.
from collections import Counter
def frequency(lst):
    return dict(Counter(lst))
print(frequency([1, 2, 2, 3, 3, 3]))

# 31. Write a Python program to count the number of elements in a list within a specified range.
def count_in_range(lst, min_val, max_val):
    return len([x for x in lst if min_val <= x <= max_val])
print(count_in_range([1, 5, 8, 10, 12, 15], 5, 10))

# 32. Write a Python program to check whether a list contains a sublist.
def contains_sublist(lst, sublst):
    for i in range(len(lst) - len(sublst) + 1):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False
print(contains_sublist([1, 2, 3, 4], [2, 3]))

# 33. Write a Python program to generate all sublists of a list.
def all_sublists(lst):
    sublists = [[]]
    for i in range(len(lst)+1):
        for j in range(i+1, len(lst)+1):
            sublists.append(lst[i:j])
    return sublists
print(all_sublists([1, 2, 3]))

# 34. Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes
print(sieve_of_eratosthenes(30))

# 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
def concat_with_range(lst, n):
    return [x+str(i) for i in range(1, n+1) for x in lst]
print(concat_with_range(['p', 'q'], 5))

# 36. Write a Python program to get a variable with an identification number or string.
def variable_id(x):
    return id(x)
print(variable_id("hello"))

# 37. Write a Python program to find common items in two lists.
def common_items(lst1, lst2):
    return list(set(lst1) & set(lst2))
print(common_items([1, 2, 3], [2, 3, 4]))

# 38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
def swap_n(lst):
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
print(swap_n([0, 1, 2, 3, 4, 5]))

# 39. Write a Python program to convert a list of multiple integers into a single integer.
def list_to_int(lst):
    return int(''.join(map(str, lst)))
print(list_to_int([11, 33, 50]))

# 40. Write a Python program to split a list based on the first character of a word.
from collections import defaultdict
def split_by_first_char(lst):
    d = defaultdict(list)
    for word in lst:
        d[word[0]].append(word)
    return dict(d)
print(split_by_first_char(["apple", "banana", "apricot", "cherry", "blueberry"]))

# 41. Write a Python program to create multiple lists.
def create_multiple_lists(n):
    return [[] for _ in range(n)]
print(create_multiple_lists(3))

# 42. Write a Python program to find missing and additional values in two lists.
def missing_additional(lst1, lst2):
    missing = list(set(lst1) - set(lst2))
    additional = list(set(lst2) - set(lst1))
    return missing, additional
print(missing_additional(['a','b','c','d'], ['b','c','d','e','f']))

# 43. Write a Python program to split a list into different variables.
def split_list(lst):
    return tuple(lst)
a, b, c = split_list([1, 2, 3])
print(a, b, c)

# 44. Write a Python program to generate groups of five consecutive numbers in a list.
def consecutive_groups(n):
    return [list(range(i, i+5)) for i in range(1, n+1, 5)]
print(consecutive_groups(20))

# 45. Write a Python program to convert a pair of values into a sorted unique array.
def pair_to_sorted_array(pair):
    return sorted(set(pair))
print(pair_to_sorted_array((5, 2)))

# 46. Write a Python program to select the odd items from a list.
def odd_items(lst):
    return [lst[i] for i in range(len(lst)) if i % 2 == 1]
print(odd_items([1, 2, 3, 4, 5]))

# 47. Write a Python program to insert an element before each element of a list.
def insert_before(lst, elem):
    result = []
    for x in lst:
        result.extend([elem, x])
    return result
print(insert_before([1, 2, 3], 0))

# 48. Write a Python program to print nested lists (each list on a new line) using the print() function.
def print_nested_lists(lst):
    for sublist in lst:
        print(sublist)
print_nested_lists([[1, 2], [3, 4], [5, 6]])

# 49. Write a Python program to convert a list to a list of dictionaries.
def list_to_dicts(colors, codes):
    return [{"color_name": c, "color_code": code} for c, code in zip(colors, codes)]
print(list_to_dicts(["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]))

# 50. Write a Python program to sort a list of nested dictionaries.
def sort_nested_dicts(lst, key):
    return sorted(lst, key=lambda x: x[key])
print(sort_nested_dicts([{'name': 'Tom', 'age': 20}, {'name': 'Jerry', 'age': 18}], 'age'))
