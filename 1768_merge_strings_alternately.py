"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        bigger_len = len(word1) if len(word1) >= len(word2) else len(word2)
        new_order_chars = list()
        for i in range(bigger_len):
            try:
                new_order_chars.append(word1[i])
            except IndexError:
                pass
            try:
                new_order_chars.append(word2[i])
            except IndexError:
                pass
        new_str = "".join(c for c in new_order_chars)
        return new_str


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.mergeAlternately('abc', 'pqr') == 'apbqcr'
    assert solution.mergeAlternately('ab', 'pqrs') == 'apbqrs'
    assert solution.mergeAlternately('abcd', 'pq') == 'apbqcd'

    print("All tests passed.")
