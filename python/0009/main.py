class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse_x = 0
        digit = 0

        while x // (10**digit) != 0:
            reverse_x = (reverse_x * 10) + (x // (10**digit) % 10)
            digit += 1

        return x == reverse_x
