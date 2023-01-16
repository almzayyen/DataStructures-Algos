# ##    Create an empty dictionary to store the count of each character in the substring.
#     Initialize two pointers, left and right, to the first character of the string.
#     Initialize a variable, max_length, to store the length of the longest substring with 'K' distinct characters.
#     Iterate through the string, moving the right pointer one character at a time.
#     For each character, add it to the dictionary and increment its count.
#     If the number of distinct characters in the dictionary exceeds 'K', move the left pointer one character at a time and remove the characters from the dictionary until the number of distinct characters is equal to 'K'.
#     Update the max_length variable if the current substring is longer than the previous longest substring.
#     Return the max_length variable.


def longest_substring_with_k_distinct_characters(string, k):
    char_count = {}
    max_length = 0
    left = 0
    for right in range(len(string)):
        char = string[right]
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
        
        while len(char_count) > k:
            left_char = string[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

print(longest_substring_with_k_distinct_characters("abcba", 2))
