class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')',"[":"]","{":"}"}
        lst = list(s)
        i = 0
        if len(s)%2 == 0:
            while lst:
                try:
                

                    d[lst[i+1]]
                    i +=1
                
                except KeyError:
                    try:
                        a = d[lst[i]]
                    except KeyError:
                        return False
                    if a == lst[i+1]:
                        del lst[i:i+2]
                        i -= 1
                        if i < 0:
                            i =0
                    else:
                        return False
                except IndexError:
                        if len(s) != 0:
                            return False
                        else:
                            return true 
            return True
        else:
            return False





            