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
        merged = []
        min_len = min(len(word1), len(word2))

        # Add characters alternately up to the shorter length
        for i in range(min_len):
            merged.append(word1[i])
            merged.append(word2[i])

        # Add the remaining part of the longer string
        merged.append(word1[min_len:])
        merged.append(word2[min_len:])

        return "".join(merged)


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.mergeAlternately('abc', 'pqr') == 'apbqcr'
    assert solution.mergeAlternately('ab', 'pqrs') == 'apbqrs'
    assert solution.mergeAlternately('abcd', 'pq') == 'apbqcd'

    print("All tests passed.")
