class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        
        
        def check_palindrome(text: str) -> bool:
           
            if len(text) <= 1:
                return True
            
            
            if text[0] != text[-1]:
                return False
            
      
            return check_palindrome(text[1:-1])
        
        return check_palindrome(clean_s)
        
        