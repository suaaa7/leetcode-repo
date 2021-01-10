class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        current_sub_string_start = 0
        current_len = 0
        longest = 0

        for i, char in enumerate(s):
            if char in char_dict and char_dict[char] >= current_sub_string_start:
                current_sub_string_start = char_dict[char] + 1
                current_len = i - char_dict[char]
                char_dict[char] = i
            else:
                char_dict[char] = i
                current_len += 1
                if current_len > longest:
                    longest = current_len

        return longest
