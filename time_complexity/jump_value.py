from math import ceil

def jump_value(X,Y,D):
    tot_dist = Y - X
    return ceil(tot_dist/D)

print(jump_value(10,85,30))