class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output +=  str(len(s)) + "," + s

        return output

    def decode(self, s: str) -> List[str]:
        output = []

        idx = 0

        while idx < len(s):
            termIdx = s.find(",", idx)
            strlen = int(s[idx:termIdx])
            output.append(s[termIdx+1: termIdx+1+strlen])
            idx = termIdx+1+strlen
        return output