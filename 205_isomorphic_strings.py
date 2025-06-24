"""
Problem:
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t:str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = dict()
        t_to_s = dict()
        for sc, tc in zip(s, t):
            if sc in s_to_t:
                if s_to_t[sc] != tc:
                    return False
            else:
                s_to_t[sc] = tc

            if tc in t_to_s:
                if t_to_s[tc] != sc:
                    return False
            else:
                t_to_s[tc] = sc

        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.isIsomorphic("egg", "add") == True
    assert solution.isIsomorphic("foo", "bar") == False
    assert solution.isIsomorphic("paper", "title") == True
    assert solution.isIsomorphic("badc", "baba") == False

    print("All tests passed.")