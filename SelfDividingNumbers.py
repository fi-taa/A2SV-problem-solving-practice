class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(number):
            for num in str(number):
                if int(num) == 0 or number % int(num) != 0:
                    return False
            return True
        
        output = []
        for i in range(left,right+1):
            if(isSelfDividing(i)):
                output.append(i)
        

        return output

                


