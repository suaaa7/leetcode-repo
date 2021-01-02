class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        for i in range(len(s)):
            palindrome_odd = self.longest_palindrome_at_index(s, i, i)
            palindrome_even = self.longest_palindrome_at_index(s, i, i+1)

            longer_palindrome = palindrome_odd if len(palindrome_odd) > len(palindrome_even) else palindrome_even
            longest_palindrome = longest_palindrome if len(longest_palindrome) >= len(longer_palindrome) else longer_palindrome

        return longest_palindrome

    @staticmethod
    def longest_palindrome_at_index(s: str, left: int, right: int) -> str:
        left_index = 0
        right_index = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left_index = left
                right_index = right
            else:
                break
            left -= 1
            right += 1

        return s[left_index:right_index+1]
