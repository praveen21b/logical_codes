def find_pairs(values:list,target:int)->str:
    # checking for targete and duplicates
    if target > 1:
        # create a dictionary
        check_dict = {}
        for val in values:
            if val in check_dict:
                check_dict[val]+=1
            else:
                check_dict[val] = 1
        
        # find compliment pair
        for value in values:
            comp_pair = target - value
            # checking presence
            if comp_pair in check_dict:
                if comp_pair == value:
                    if not check_dict[val] > 1:
                        continue
                return f'The target value is {target}, Pairs are {value} and {comp_pair}'
    
    return f"No valid pairs found"

print(find_pairs([14,13,6,7,8,10,1,2],3))
print(find_pairs([14,13,6,7,8,10,1],3))
print(find_pairs([2,2],4))
print(find_pairs([2],4))
print(find_pairs([14,13,6,7,8,10,1],0))
print(find_pairs([14,13,6,7,8,10,1],1))