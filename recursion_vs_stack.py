from custom_stack import BoundedArrayStack

def fact_loop(target_num):
    product = 1
    for stepping_val in range(2, target_num + 1):
        product *= stepping_val
    return product

def fact_recurse(target_num):
    if target_num <= 1:
        return 1
    return target_num * fact_recurse(target_num - 1)

def fact_stack_adt(target_num):
    adt_stack = BoundedArrayStack(limit=1000)
    
    while target_num > 1:
        adt_stack.push(target_num)
        target_num -= 1
        
    accumulated_total = 1
    while not adt_stack.is_empty():
        accumulated_total *= adt_stack.pop()
        
    return accumulated_total
