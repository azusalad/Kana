def readfile(desired_file):
    '''
    loads a file containing flashcard information
    outputs a tuple
    '''
    import ast
    
    f = open(desired_file,'r')
    file_index = [x for x in f.readlines() if x != '']
    f.close()
    
    # index 0 is term_dict
    # index 1 is pp_dict
    # index 2 is wrong_list
    # index 3 is playtime 
    
    # get term dictionary
    data = []
    data.append(ast.literal_eval(file_index[0]))
    if len(file_index) > 1:
        # get pp dictionary if exists
        data.append(ast.literal_eval(file_index[1]))
        if len(file_index) > 2:
            # get wrong list if exists
            data.append(ast.literal_eval(file_index[2]))
            if len(file_index) > 3:
                # get playtime if exists
                data.append(int(ast.literal_eval(file_index[3])))
    
    # add false to remaining items in list if things dont exist
    while len(data) < 4:
        data.append(False)
        
    return tuple(data)
    
