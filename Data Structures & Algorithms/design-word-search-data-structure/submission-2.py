class Node():
    def __init__(self):
        self.chars = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.chars:
                curr = curr.chars[c]
            else:
                curr.chars[c] = Node()
                curr = curr.chars[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word):
                return curr.end
            
            if word[i] == ".":
                for c in curr.chars.keys():
                    if dfs(i + 1, curr.chars[c]):
                        return True
                return False

            if word [i] not in curr.chars:
                return False

            curr = curr.chars[word[i]]
            return dfs(i + 1, curr)
        return dfs(0, self.root)
