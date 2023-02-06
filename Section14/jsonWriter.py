
import json

dict_list = [
    {
        'name': 'james',
        'age': 20,
        'spec': [
            175.5,
            70.5
        ]
    },
    {
        'name': 'alice',
        'age': 21,
        'spec': [
            168.5,
            60.5
        ]
    }
]

json_string = json.dumps(dict_list, indent=4)

with open('dictList.json', 'w') as file:
    file.write(json_string)

print('dictList.json 파일이 생성되었습니다.')

