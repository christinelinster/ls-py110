# Inventory Item Availability 

def is_item_available(id, transactions):
    all_transactions = transactions_for(id, transactions)

    total_quantity = 0
    for transaction in all_transactions:
        if transaction["movement"] == "in":
            total_quantity += transaction["quantity"]
        else:
            total_quantity -= transaction["quantity"]
    
    if total_quantity <= 0:
        return False
    return True


def transactions_for(id, transactions):
    result = [transaction for transaction in transactions if transaction["id"] == id]
    return result

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True