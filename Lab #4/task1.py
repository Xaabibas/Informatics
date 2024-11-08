# Вариант №26
# json to yaml
# Среда, Пятница
def task1():
    def correct_form(s):

        s = s[s.index('"') + 1::] if '"' in s else s.lstrip()
        res = ' ' * level
        res += '- ' if count > 0 else ''

        for a in range(len(s)):
            if s[a] == ',' and s[a + 1] == '\n':
                continue
            elif s[a] == '"' and s[a + 1] == ':':
                continue
            elif s[a] == '[':
                if s[a + 1] == ']':
                    res += '['
                continue
            res += s[a]
        return res

    f = open('timetable.json', encoding='utf-8', mode='r')

    r = open('timetable1.yaml', encoding='utf-8', mode='w')

    level = 0
    count = 0
    for i in f:
        if '{' in i:
            count = 1 if count > 0 else 0
            continue
        elif '}' in i:
            if '},' in i:
                count = 1
            level -= 2
            continue
        elif '[' in i:
            r.write(correct_form(i))
            count = 1_000 ** 1_000
            continue
        elif ']' in i:
            continue

        r.write(correct_form(i))
        count -= 1
        if count == 0:
            level += 2

    f.close()
    r.close()


task1()
