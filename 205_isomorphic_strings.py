"""
Problem:
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}
        for s_char, t_char in zip(s, t):
            if (s_char in s_to_t and s_to_t[s_char] != t_char) or \
               (t_char in t_to_s and t_to_s[t_char] != s_char):
                return False
            s_to_t[s_char] = t_char
            t_to_s[t_char] = s_char
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.isIsomorphic("egg", "add") is True
    assert solution.isIsomorphic("foo", "bar") is False
    assert solution.isIsomorphic("paper", "title") is True
    assert solution.isIsomorphic("badc", "baba") is False

    print("All tests passed.")