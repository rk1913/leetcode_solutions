class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        a = []
        for i in order:
            if i in friends:
                a.append(i)
        return a
        
