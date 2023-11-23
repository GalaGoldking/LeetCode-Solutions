class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        square = num**0.5
        if square == int(square):
            return True
        else:
            return False