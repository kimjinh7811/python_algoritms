

def diffWaysToCompute(input: str):
    def compute(left, right, op):
        
        results = [eval(str(x) + op + str(y)) for x in left for y in right]
        return results
    
    if input.isdigit():
        return [int(input)]

    results = []
    for idx, ch in enumerate(input):
        if ch in '+-*':
            left = diffWaysToCompute(input[:idx])
            right = diffWaysToCompute(input[idx+1:])

            results += compute(left, right, ch)


    return results

input_str = "12*3-4"
