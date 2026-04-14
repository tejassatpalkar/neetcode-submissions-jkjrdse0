class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out+=f"{len(s)}#"
            out+=s
        return out



    def decode(self, s: str) -> List[str]:
        out = []
        i = 0

        while i < len(s):           
            delimitIdx = s.find("#", i)
            wl = int(s[i:delimitIdx])
            wordIdx = delimitIdx+1
            out.append(s[wordIdx: wordIdx+wl])
            i = wordIdx+wl
        return out
        
       

