def ladderLength(beginWord, endWord, wordList):
    length = len(wordList)
    ans = []
    validate = [0 for i in range(length)]

    def digui(validate, after_word, count, skip):
        if after_word == endWord:
            ans.append(count)
        for i in range(len(after_word)):
            if i in skip:
                continue
            for j in range(len(wordList)):
                if validate[j] != 1 and after_word[i] != wordList[j][i]:
                    temp = after_word[:i] + wordList[i] + after_word[i + 1:]
                    validate[j] = 1
                    skip.append(i)
                    if skip == None:
                        skip = []
                    digui(validate, temp, count + 1, skip)
        return 0

    digui(validate, beginWord, 0, [])
    print(ans)
if __name__ == '__main__':
    ladderLength("hit", "cog",  ["hot","dot","dog","lot","log","cog"])
