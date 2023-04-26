def root(number: float, root_value: float):
    return number ** (1/root_value)

def pover(number: float, pover: float):
    return number ** pover

# Manual testing
# print(round(pover(10, 6)))
# print(round(root(10**6, 6)))

# Automated testing
try:
    assert print() is bool, 'Print test'
    
except AssertionError as e:
    print(e)
print(round(pover(10, 6)))
print(round(root(10**6, 6)))