class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
    
        def compute(left, right, op):
            # left, right를 계산해서 반환
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l)+op+str(r)))
            return results
        
        if expression.isdigit():
            return [int(expression)]

        results = []
        
        for index, value in enumerate(expression):
            if value in "+-*":
                # divide and conquer
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])

                results.extend(compute(left, right, value))

        return results