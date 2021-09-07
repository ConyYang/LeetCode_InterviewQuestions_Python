def checkDict(s, wordDict, memory):
    if s in memory:
        return memory[s]

    if s in wordDict:
        memory[s] = True
        return True

    for i in range (len(s)):
        if s[i:] in wordDict and checkDict(s[:i], wordDict, memory):
            memory[s] = True
            return True

    memory[s] = False
    return False


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    memory = {}
    result = checkDict(s, wordDict, memory)
    return result


if __name__ == '__main__':
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(wordBreak(s, wordDict))