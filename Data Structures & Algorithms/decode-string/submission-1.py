class Solution:
    def decodeString(self, s: str) -> str:
        stk = [] # num
        currNum = ""
        currStr = ""
        for c in s:
            if c.isdigit():
                currNum += c
            elif c == "[":
                currNum = int(currNum) if currNum else 1
                stk.append([currNum, currStr])
                currNum = ""
                currStr = ""
            elif c == "]":
                count, lastString = stk.pop()
                currStr = lastString + (count * currStr)
            else:
                currStr += c

        return currStr