"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # Slide window
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_vowels -= 1

            if s[i] in vowels:
                current_vowels += 1

            max_vowels = max(max_vowels, current_vowels)

        return max_vowels


def run_tests() -> None:
    solution = Solution()
    assert solution.maxVowels("weallloveyou", 7) == 4
    assert solution.maxVowels("abciiidef", 3) == 3
    assert solution.maxVowels("aeiou", 2) == 2
    assert solution.maxVowels("leetcode", 3) == 2

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
