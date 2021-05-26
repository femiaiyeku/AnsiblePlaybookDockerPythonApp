
"""
Algorithm
In order to decide whether two strings are anagrams
we will first count the number of times each character occurs
Since there are 26 possible characters, we can use a list of 26 counters, one for each possible character.
Each time we see a particular character, we will increment the counter at that position.
In the end, if the two lists of counters are identical, the strings must be anagrams.
"""


def anagram(s1: object, s2: object) -> bool:
    c1 = [0] * 26
    c2 = [0] * 26
    i: object
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] +=  1
        for i in range(len(s2)):
            pos = ord(s2[i]) - ord('a')
            c2[pos] += 1
            j = 0
            is_anagram = True
            while j < 26 and is_anagram:
                if c1[j] == c2[j]:
                    j += 1
                else:
                    is_anagram = False
                    return is_anagram
                    




if __name__ == '__main__':
    anagram('apple', 'appel')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
