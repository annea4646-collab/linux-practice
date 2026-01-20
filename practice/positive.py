# positive.py
def positive(I):
    result = []
    for i in I:
        if i > 0:
            result.append(i)
    return result
    
print(positive([1,-3,2,0,-5,6]))