# List Deduplication 

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
seen = set()

for point in data:
    if point not in seen:
        unique_data.append(point)
        seen.add(point)
        
print(unique_data == [4, 2, 1, 3]) # order not guaranteed