def flatten_list(nested):
    stack = [nested]      
    result = []

    while stack:
        current = stack.pop()  

        if type(current) == list:
        
            for item in reversed(current):
                stack.append(item)
        else:
            result.append(current)

    return result
main_list = [[['KOHLI', 'SACHIN'], 'PANTH'],
             ['dravid', 'ravi', 'rahul', 'jasprit'],
             ['KAPIL', 'Jadeja', 'kohli', 'irfan', 'Hardik']]

print(flatten_list(main_list))
