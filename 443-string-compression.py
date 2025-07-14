from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # pointer để ghi vào mảng
        i = 0  # pointer để đọc từ mảng

        while i < len(chars):
            char = chars[i]
            count = 1

            # Đếm số lượng ký tự liên tiếp giống nhau
            while i + count < len(chars) and chars[i + count] == char:
                count += 1

            # Ghi ký tự vào vị trí write
            chars[write] = char
            write += 1

            # Nếu count > 1, ghi các chữ số của count
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1

            # Di chuyển pointer đọc
            i += count

        return write


# Test cases
def test_solution():
    sol = Solution()

    # Test case 1: ["a","a","b","b","c","c","c"]
    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    result1 = sol.compress(chars1)
    print(f"Input: ['a','a','b','b','c','c','c']")
    print(f"Output: {chars1[:result1]}, Length: {result1}")
    print()

    # Test case 2: ["a"]
    chars2 = ["a"]
    result2 = sol.compress(chars2)
    print(f"Input: ['a']")
    print(f"Output: {chars2[:result2]}, Length: {result2}")
    print()

    # Test case 3: ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    result3 = sol.compress(chars3)
    print(f"Input: ['a','b','b','b','b','b','b','b','b','b','b','b','b']")
    print(f"Output: {chars3[:result3]}, Length: {result3}")


# Uncomment to test
test_solution()
