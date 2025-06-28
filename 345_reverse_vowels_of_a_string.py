"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        reverse = list()
        temp_vowels = list()
        temp_idx = list()

        for i, char in enumerate(s):
            if char.lower() in vowels:
                reverse += "_"
                temp_vowels.append(char)
                temp_idx.append(i)
            else:
                reverse += char

        for i, v in zip(temp_idx, reversed(temp_vowels)):
            reverse[i] = v

        reverse_string = "".join(reverse)

        return reverse_string

