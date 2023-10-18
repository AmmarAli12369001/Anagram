"""
Anagrams
You are given a list of N words (strings containing only lower case letters of the English alphabet).
We consider two words to be equivalent if they contain the same letters, i.e.
we can rearrange the letters of one word in order to obtain the other word.
Compute the size of the largest subset of equivalent words.
Desired solution
You should assume the input is quite large (there are about 10^5 letters in total).

Standard input
The first line contains a single integer value N.
Each of the following N lines contains a single string, representing one of the words.

Standard output
The output should contain a single integer representing the size of the largest subset of equivalent words.
"""


def word2dict(N):
    words = {}
    for i in range(N):
        word = input()
        lst = []
        for letter in word.lower():
            lst.append(letter)
        # words.append(set(lst))
        lst.sort()
        s = ''
        for j in lst:
            if j not in s:
                s += j
        words[word] = s
    return words


def find_keys_with_same_value(input_dict):
    result = {}
    for key, value in input_dict.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]
    return result


N = int(input())
words = word2dict(N)
result = find_keys_with_same_value(words)
cnt = []
for value in result.values():
    cnt.append(len(value))

print(max(cnt))
