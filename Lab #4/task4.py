import re

r = open('timetable4.yaml', encoding='utf-8', mode='w')

def get_indent(dash, gap):
    if dash > 0 and gap > 0:
        return ' '*(gap - 2) + '- '
    return ' '*gap

def json_to_one_line(file):
    return ''.join([i.strip() for i in file])

def check_figure_staples(line):
    return '{' in line and '}' in line

def check_square_staples(line):
    return '[' in line and ']' in line

def convert_to_yaml(line, dash=0, gap=0):
    is_figure, is_square = check_figure_staples(line), check_square_staples(line)


    if is_figure and is_square:
        figure_index = line.index('{')
        square_index = line.index('[')
        if figure_index < square_index:
            convert_to_yaml(line[1:len(line) - 1], dash=0, gap=gap+2)
        else:
            convert_to_yaml(line[:square_index], dash=1, gap=gap)
            cnt = 0
            start = square_index + 1
            for i in range(square_index + 1, len(line)):
                if line[i] == '{':
                    cnt += 1
                elif line[i] == '}':
                    cnt -= 1
                if cnt == 0 and i > start:
                    if '{' not in line[start:]:
                        break
                    convert_to_yaml(line[start + 1:i], dash=1, gap=gap+2)
                    start = i + 2
            convert_to_yaml(line[start + 1:], gap=gap)


    elif is_figure:
        start = 0
        cnt = 0
        for i in range(len(line)):
            if line[i] == '{':
                cnt += 1
            elif line[i] == '}':
                cnt -= 1
            if cnt == 0 and i > start:
                convert_to_yaml(line[start + 1:i], gap=gap)
                start = i + 2

    elif is_square:
        lindex = line.index('[')
        rindex = line.rindex(']')
        if lindex + 1 == rindex:
            indent = get_indent(0, gap)
            print(indent + line.replace('"', '', 2), file=r)
            return
        if lindex - 1 >= 0:
            convert_to_yaml(line[:lindex], gap=gap)

        convert_to_yaml(line[lindex + 1:rindex], dash=line.count(',') + 1, gap=gap+2)

    else:
        if ':' in line:
            for i in re.split(r',(?=\")', line):
                indent = get_indent(dash, gap)
                dash -= 1
                sub = i.replace('"', '', 2)
                print(indent + sub, file=r)
        else:
            for i in line.split(','):
                indent = get_indent(dash, gap)
                dash -= 1
                print(indent + i, file=r)


def json_to_yaml(file):
    json_line = json_to_one_line(file)
    convert_to_yaml(json_line, gap=-2)

def task4():
    with open('timetable.json', encoding='utf-8', mode='r') as json_file:
        r.seek(0)
        json_to_yaml(json_file)


task4()
