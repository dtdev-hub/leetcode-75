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


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    assert solution.reverseWords("  hello world  ") == "world hello"
    assert solution.reverseWords("a good   example") == "example good a"

    print("All tests passed.")
