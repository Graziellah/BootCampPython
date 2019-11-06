def ft_reduce(function_to_apply, list_of_inputs):
    try:
        value
        if isinstance(list_of_inputs, list)  and hasattr(function_to_apply, '__call__'):
            for i in list_of_inputs:
                value +=function_to_apply(list_of_inputs[i])
            return newArray
        else:
            raise ValueError('check parameter')
    except ValueError  as err:
        print(err)
    
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

print(product)