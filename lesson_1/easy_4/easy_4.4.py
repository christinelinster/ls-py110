# Arrange a Dictionary

# def order_by_value(my_dict):
#     sorted_items = sorted(my_dict.items(), key=sort_by_value)
#     return [key for key, value in sorted_items]
        
    
# def sort_by_value(item):
#     return item[1]

def order_by_value(my_dict):
    return sorted(my_dict, key=my_dict.get)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True