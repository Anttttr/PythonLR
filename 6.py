result = []
count = []
resstr = ''
for i in range(95632, 95701):
    for _ in range(2, i//2+1, 2):
        if i % _ == 0:
            count.append(str(_))
    if len(count) == 5:
        count.append(str(i))
        result.append(count)
    count = []
for _ in result:
    resstr = ' '.join(_)
    print(resstr)
