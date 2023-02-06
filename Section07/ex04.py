# for문과 dict

person = {"name":"홍길동", "age":25}

for key in person:
    print(key, person[key])
    print(key, person.get(key))
    