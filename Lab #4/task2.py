import json
import yaml


def task2():
    f = open('timetable.json', mode='r', encoding='utf-8')
    json_data = json.load(f)

    r = open('timetable2.yaml', mode='w')

    yaml_data = yaml.dump(json_data)

    r.write(yaml_data)


task2()
