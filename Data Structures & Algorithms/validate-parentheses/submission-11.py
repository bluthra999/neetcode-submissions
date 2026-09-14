class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(',"[","{"}
        d2= {')',"]","}"}
        d3 = {'(':')',"[":"]","{":"}"}

        lst = []
        ls1 = []
        if len(s)%2 == 0 and len(s)!=0:
            for i in s:
                if i in d:
                    lst.append(i)
                elif i in d2:
                    try:
                        a = lst[-1]
                        if d3[a] == i:
                            if len(s) !=0:
                                lst.pop()
                        else:
                            return False 
                    except:
                        return False  
            if len(lst) ==0:
                return True 
            else:
                return False
        else:
            return False









            