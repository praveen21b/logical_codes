def create_generator(index):
    month = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'] 
    yield month[index]

month = (create_generator(3))

print(next(month))
# print(next(month))