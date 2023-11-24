class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        alice = []
        me = []
        bob = []
        piles.sort()
        index = 0
        while len(piles)>0:
            if index % 3 == 0:
                alice.append(piles.pop())
            elif index % 3 == 1:
                me.append(piles.pop())
            else:
                bob.append(piles.pop(0))
            index += 1

        return sum(me)
            