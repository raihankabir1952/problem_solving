class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative number always not palindrome
        if x < 0:
            return False
        
        # Save original number
        original = x
        reversed_num = 0
        
        # Reverse the number
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # Compare original and reversed
        return original == reversed_num
