import re


def task3():
    def correct_form(substring):
        substring = re.sub(pattern1, r'\1', substring.lstrip())
        substring = re.sub(pattern2, r'', substring)

        res = ' '*level
        res += '- ' if count > 0 else ''
        res += substring

        return res


    f = open('timetable.json', encoding='utf-8', mode='r')
    r = open('timetable3.yaml', encoding='utf-8', mode='w')

    level = 0
    count = 0

    pattern1 = r'\"(\w+)\"(?=:)'
    pattern2 = r',|(\[(?!\]))'

    for i in f:
        if re.search(r'{', i):
            count = 1 if count > 0 else 0
            continue
        elif re.search(r'}', i):
            if re.search(r'},', i):
                count = 1
            level -= 2
            continue
        elif re.search(r'\[', i):
            r.write(correct_form(i))
            count = 1_000**1_000
            continue
        elif re.search(r']', i):
            count = 0
            continue

        r.write(correct_form(i))
        count -= 1
        if count == 0:
            level += 2

    f.close()
    r.close()

task3()