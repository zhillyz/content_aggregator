def is_anagram(string, string2):
    """ checks to see if string is anagram of 2nd string"""   
    if len(string) == len(string2):
        x = sorted(string)
        y = sorted(string2)
        a = ""
        b = ""
        x2 = [a.join(s) for s in x]
        y2 = [b.join(s) for s in y]
        if x2 == y2:
            print("yes " + string + " is an anagram of " + string2 +".")
        else:
           print("no the strings are not anagrams of each other")
    else:
        print("no the strings are not anagrams of each other")

is_anagram("netmal","mental")