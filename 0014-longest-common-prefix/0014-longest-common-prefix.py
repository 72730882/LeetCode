class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return("")
        if len(strs) == 1:
            return(strs[0])
        prefix = strs[0]
        p_len = len(prefix)

        for i in strs[1:]:
             while prefix != i[0:p_len]:
                 prefix = prefix[0:(p_len-1)]
                 p_len -= 1

                 if p_len == 0:
                     return("")
        return(prefix)

        