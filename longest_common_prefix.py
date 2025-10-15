from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # if the list is empty
            return ""

        # Assume the first string is the prefix
        prefix = strs[0]

        # Compare prefix with every string
        for s in strs[1:]:
            # Reduce prefix until it matches the beginning of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # shorten prefix
                if prefix == "":
                    return ""  # no common prefix

        return prefix
