class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        dict_check = {}
        list_check = []
        for i in range(len(s)):
            if s[i] not in dict_check.keys():
                dict_check[s[i]] = t[i]
                if t[i] in list_check:
                    return False
                else:
                    list_check.append(t[i])
            else:
                if dict_check.get(s[i])!=t[i]:
                    return False
        return True