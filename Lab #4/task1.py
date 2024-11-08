# Вариант №26
# json to yaml
# Среда, Пятница

def write(s):
    if '"' not in s and s[len(s) - 3] not in '0987654321':
        return ''
    res = (' '*(level - 2) + '- ') if (flag_array and count > 0) else ' '*level
    s = s.lstrip()
    for j in range(len(s)):
        if s[j] == '[':
            if s[j + 1] == ']':
                res += '[]'
            continue
        elif s[j] == ']':
            continue
        elif s[j] == '"':
            if s[j + 1] == '"':
                res += "''"
            continue
        if j == len(s) - 2:
            continue
        res += s[j]
    return res


f = open('timetable.json', encoding='utf-8')
r = open('timetable1.yaml', mode='w', encoding='utf-8')
count = 0
level = -2
flag_array = False

for i in f:
    if '{' in i:
        level += 2
        if flag_array:
            count = 1
        continue
    elif '}' in i:
        level -= 2
        if '},' in i:
            count = 1
            flag_array = True
        continue

    r.write(write(i))
    count -= 1
    if '[' in i:
        flag_array = True
        count = 1000000000
    if ']' in i:
        flag_array = False
        count = 0

f.close()
r.close()
