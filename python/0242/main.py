class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for char in s:
            if hash_map.get(char) is None:
                hash_map[char] = 0
            hash_map[char] += 1

        for char in t:
            if hash_map.get(char) is None:
                hash_map[char] = 0
            hash_map[char] -= 1

        for key in hash_map.keys():
            if hash_map[key] != 0:
                return False

        return True
