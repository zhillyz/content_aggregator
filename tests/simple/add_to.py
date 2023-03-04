def add_to(val):
    """ Add all integer values up to the input integer."""
    return sum(x for x in range(1,val+1))

print(add_to(68))