def find_item(item_list, target):
    for i in range(len(item_list)):
        if item_list[i] == target:
            return i
        
print(find_item([1,2,3,4,5], 4))