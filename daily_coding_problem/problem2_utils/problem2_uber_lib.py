output = []


def product(input):

    for count in range(len(input)):
        working_list = []
        if count == 0:
            # Add all elements except the 0th element in the working list
            working_list.extend(input[(count + 1):])
        elif count == len(input)-1:
            # Add all elements except the last element in the working list
            working_list.extend(input[:count])
        else:
            # Add all elements before the current element then extend list with all elements after the current element
            # where current element is the element at index 'count'
            working_list.extend(input[:count])
            working_list.extend(input[(count+1):])

        product = 1
        for x in working_list:
            product = product * x

        output.append(product)
    return output


# Alternate and quicker method
def product(user_input):

    for count in range(len(user_input)):
        print(count)
        working_list = user_input.copy()
        current_element = working_list[count]
        working_list.remove(current_element)
        array_product = 1
        for x in working_list:
            array_product = array_product * x
        print(array_product)
        output.append(array_product)
    return output

