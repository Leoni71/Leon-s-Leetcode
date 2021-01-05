class Solution:
    def myAtoi(self, str: str) -> int:
        result,sign = 0,1
        MAX, MIN = 2**31-1, -2**31
        str = str.strip(" ")
        if not str:
            return result
        
        for i in range(len(str)):
            if not i:
                if str[i].isdigit():
                    result = 10*result+(ord(str[i])-ord('0'))
                elif str[i] == '+':
                    continue
                elif str[i] == '-':
                    sign = -1
                else:
                    return 0
            else:
                if str[i].isdigit():
                    result = 10*result+(ord(str[i])-ord('0'))
                else:
                    if sign*result > MAX:
                        return MAX
                    elif sign*result < MIN:
                        return MIN
                    else:
                        return sign*result
        if sign*result > MAX:
            return MAX
        elif sign*result < MIN:
            return MIN
        else:       
            return sign*result
