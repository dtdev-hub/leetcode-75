"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""


class Solution:
    @staticmethod
    def find_divisors(s):
        div = ""
        divisors = list()

        for char in s:
            div += char

            if len(div) == len(s):
                continue

            quotient = len(s) // len(div)
            remainder = len(s) % len(div)

            if remainder != 0:
                continue

            test_str = div * quotient

            if test_str == s:
                divisors.append(div)

        if divisors:
            return divisors

        return []

    @staticmethod
    def is_text_a_divisor_of_text_b(txt_a, txt_b):
        quotient = len(txt_b) // len(txt_a)
        remainder = len(txt_b) % len(txt_a)

        if type(quotient) is int and remainder == 0 and txt_b == txt_a * quotient:
            return True

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if self.is_text_a_divisor_of_text_b(str1, str2):
            return str1
        if self.is_text_a_divisor_of_text_b(str2, str1):
            return str2

        divs_1 = self.find_divisors(str1)
        divs_2 = self.find_divisors(str2)

        biggest_div = ""
        for div in divs_1:
            if div in divs_2:
                biggest_div = div

        return biggest_div


# Test Case
if __name__ == "__main__":
    solution = Solution()
    # print(f"Found divisor: {solution.find_divisors('ABABAB')}")
    # print(f"Found divisor: {solution.find_divisor('CODE')}")
    # print("main: ", solution.gcdOfStrings("ABABAB", "ABAB"))

    assert solution.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert solution.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert solution.gcdOfStrings("LEET", "CODE") == ""
    assert solution.gcdOfStrings("A", "A") == "A"
    assert solution.gcdOfStrings("ABABCABCD", "ABAB") == ""
    assert solution.gcdOfStrings("ABCABCABCABC", "ABCABC") == "ABCABC"
    assert solution.gcdOfStrings("A", "B") == ""
    assert solution.gcdOfStrings("ABCABCABC", "B") == ""
    assert (
        solution.gcdOfStrings(
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        )
        == "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    )

    print("All test passed.")
