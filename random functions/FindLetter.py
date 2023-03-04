with open('smallBiG.txt') as f:
    text = f.read()
ans = []
for idx, line in enumerate(text[3:-3]):
    bodyguards = text[idx:idx+7]
    if bodyguards[:3].isupper() and bodyguards[4:].isupper() and bodyguards[3].islower():
        print(bodyguards)