string = input('Enter sentence: ')
strl = string.split(' ')
strls = set(strl)
strls = list(strls)
strls.sort()
counter = []
for i in strls:
    counter.append(strl.count(i))
for i in range(len(strls)):
    print(strls[i], ':', counter[i])
