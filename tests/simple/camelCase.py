def camelCase(string):
    """converts a string into camelCase"""
    s = string.title()
    c = s.replace(" ", "")
    print(c)

camelCase("paul hill")