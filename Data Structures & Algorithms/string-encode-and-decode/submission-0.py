class Solution:
    stringLen = []

    def encode(self, strs: List[str]) -> str:
        outputStr = ""
        self.stringLen = []

        for s in strs: 
            self.stringLen.append(len(s))
            outputStr +=s
        return outputStr

    def decode(self, s: str) -> List[str]:
        output = []

        idx = 0 
        for slen in self.stringLen:
            output.append(s[idx:slen+idx])
            idx +=slen
        return output
