class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        if expression.isdigit():
            return [int(expression)]
        
        def compute(left, right, op):
            result = []
            print(left, right)
            for l in left:
                for r in right:
                    result.append(eval(str(l)+op+str(r)))
            return result

        # div and conquer
        results = []
        for idx, val in enumerate(expression):
            if val in "+-*":
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx+1:])
                
                results.extend(compute(left, right, val))
        return results