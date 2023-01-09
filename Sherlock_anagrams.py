def sherlockAndAnagrams(s):
    freq = {}
    
    count = 0
    
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = ''.join(sorted(s[i:j]))
            
            if sub in freq:
                freq[sub] += 1
            else:
                freq[sub] = 1
                
    for  value in freq.values():
        
        if value > 1:
            count += value * (value-1) //2
            

            
            
from collections import defaultdict

def sherlockAndAnagrams2(s):
    # Create a dictionary to store the count of each substring
    substr_count = defaultdict(int)

    # Iterate through all substrings of s
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            # Sort the substring to create a unique key for anagrams
            substr = "".join(sorted(s[i:j]))
            substr_count[substr] += 1

    # Initialize a counter to keep track of the number of anagram pairs
    anagram_pairs = 0

    # Iterate through the dictionary to count the number of anagram pairs
    for count in substr_count.values():
        anagram_pairs += count * (count-1) // 2

    return anagram_pairs


#             Explanation:

#     The defaultdict(int) is a dictionary subclass that returns a default value of 0 for any key that is not found in the dictionary. This is useful for counting the number of occurrences of something.

#     The outer loop iterates through the start index i of the substring, and the inner loop iterates through the end index j of the substring. This creates a nested loop that generates all substrings of s.

#     The sorted function is used to sort the characters of the substring in alphabetical order, which creates a unique key for anagrams. For example, the substrings "ab" and "ba" would both be sorted to "ab", so they would be counted as the same substring in the dictionary.

#     The count of each substring is incremented in the dictionary using the substr_count[substr] += 1 statement.

#     The anagram_pairs counter is initialized to 0, and then the loop iterates through the dictionary to count the number of anagram pairs. For each count c in the dictionary, the number of pairs is calculated as c * (c-1) // 2. This formula is based on the fact that there are c choices for the first element of the pair and c-1 choices for the second element, and the // 2 is used to divide by 2 to avoid double-counting (since the order of the pair does not matter).
