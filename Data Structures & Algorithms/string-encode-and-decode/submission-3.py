class Solution:

    def encode(self, strs: List[str]) -> str:
        return "/./".join(strs) if strs else "dont decode"

    def decode(self, s: str) -> List[str]:
        return s.split("/./") if s != "dont decode" else []