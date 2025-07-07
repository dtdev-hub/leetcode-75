"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        current_word = ""

        for char in s:
            if char != ' ':
                current_word += char
            else:
                if current_word:
                    words.append(current_word)
                    current_word = ""

        if current_word:
            words.append(current_word)

        return " ".join(reversed(words))

    # Alternative method 3: Using two pointers (most efficient)
    def reverseWords_optimal(self, s: str) -> str:
        # Convert to list for easier manipulation
        chars = list(s.strip())

        # Reverse the entire string
        self.reverse(chars, 0, len(chars) - 1)

        # Reverse each word back
        start = 0
        for end in range(len(chars) + 1):
            if end == len(chars) or chars[end] == ' ':
                self.reverse(chars, start, end - 1)
                start = end + 1

        # Clean up multiple spaces
        return self.clean_spaces(chars)

    def reverse(self, chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    def clean_spaces(self, chars):
        result = []
        for char in chars:
            if char != ' ' or (result and result[-1] != ' '):
                result.append(char)
        return ''.join(result).strip()

# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    assert solution.reverseWords("  hello world  ") == "world hello"
    assert solution.reverseWords("a good   example") == "example good a"

    print("All tests passed.")
