class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        prefix_length = len(prefix)

        for s in strs[1:]:
            while prefix != s[0:prefix_length]:
                if prefix_length == 1:
                    return ""

                prefix_length -= 1
                prefix = prefix[0:prefix_length]

        return prefix
