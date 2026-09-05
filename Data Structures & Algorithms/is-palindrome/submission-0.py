class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(c for c in s if c.isalnum())
        result = result.lower()
        l = len(result)
        flag = True
        if l%2 == 0:
            for i in range(l):
                if result[i] == result[l-i-1]:
                    pass
                else:
                    return False

        else:
            mid = len(result) // 2
            result = result[:mid] + result[mid+1:]
            l = len(result)
            for i in range(l):
                if result[i] == result[l-i-1]:
                    pass
                else:
                    return False
        

        return True

        