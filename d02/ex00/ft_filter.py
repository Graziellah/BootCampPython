def ft_filter(function_to_apply, list_of_inputs):
    try:
        newArray = []
        if isinstance(list_of_inputs, list)  and hasattr(function_to_apply, '__call__'):
            for i in list_of_inputs:
                if function_to_apply(list_of_inputs[i]):
                    newArray.append(list_of_inputs[i])
            return newArray
        else:
            raise ValueError('check parameter')
    except ValueError  as err:
        print(err)


def by2(a):
    return a * 2
number_list = range(-5, 5)
less_than_zero = list(ft_filter(lambda x: x < 0, number_list))
print(less_than_zero)
#fe = by2
#print(ft_map(fe,"0,1,2,3,4,5"))