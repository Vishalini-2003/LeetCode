from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        pairs = {"1": "", "2": "abc", "3": "def",
         "4": "ghi", "5": "jkl", "6": "mno",
         "7": "pqrs", "8": "tuv", "9": "wxyz" }
        if digits:
            lst = []
            for num in digits:
                lst.append(pairs[num])
            at = list(product(*lst))
            b = ["".join(x) for x in at]

            return b
        return []