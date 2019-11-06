def ft_map(function_to_apply, list_of_inputs):
    try:
        newArray = []
        if isinstance(list_of_inputs, list)  and hasattr(function_to_apply, '__call__'):
            for i in list_of_inputs:
                newArray.append(function_to_apply(list_of_inputs[i]))
            return newArray
        else:
            raise ValueError('check parameter')
    except ValueError  as err:
        print(err)


def by2(a):
    return a * 2

fe = by2
print(ft_map(fe,"0,1,2,3,4,5"))