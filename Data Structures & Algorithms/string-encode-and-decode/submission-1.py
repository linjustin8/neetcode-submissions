class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            for c in s:
                out  = out + str(ord(c)) + ","
            out += "_"
        return out

    def decode(self, s: str) -> List[str]:
        arr = s.split("_")
        arr = arr[:-1]
        for i in range(len(arr)):
            original = ""
            character = ""
            for c in arr[i]:
                if(c == ","):
                    original += chr(int(character))
                    character = ""
                    continue
                character += c
            arr[i] = original
        return arr