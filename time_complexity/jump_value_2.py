def jump_value(X,Y,D):
    tot_dist = Y - X
    jumps = int(tot_dist/D)
    if (tot_dist/D) != 0:
        jumps+=1
    return jumps

print(jump_value(10,85,30))