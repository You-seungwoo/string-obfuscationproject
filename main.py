import random

BaseTable = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
KeyTable = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Type = int(input('문자를 난독화 하려면 0, 복호화 하려면 1를 입력해주세요. : '))

if Type == 0:
    count = 0
    seed = int(input('난독화 SEED 숫자를 입력해주세요. : '))
    seed = str(seed)

    for i in seed:
        if int(i) > 10:
            print('seed는 10 이하 1 이상의 숫자이여야만 합니다.')
            break

    random.seed(seed)
    random.shuffle(KeyTable)

    msg = input('난독화할 문자열을 입력해주세요. : ')
    result = ''

    for i in range(len(msg)):
        if msg[i] == ' ':
            result = result + ' '
            continue
    
        if msg[i].lower() not in BaseTable:
            print('영어만 지원됩니다.')
            break

        result = result + KeyTable[BaseTable.index(msg[i].lower())]

if Type == 1:
    seed = int(input('난독화 SEED 숫자를 입력해주세요. : '))
    seed = str(seed)

    random.seed(seed)
    random.shuffle(KeyTable)

    msg = input('복호화할 문자열을 입력해주세요. : ')
    result = ''

    for i in range(len(msg)):
        if msg[i] == ' ':
            result = result + ' '
            continue
    
        if msg[i].lower() not in BaseTable:
            print('영어만 지원됩니다.')
            break

        result = result + BaseTable[KeyTable.index(msg[i].lower())]

print(result)
