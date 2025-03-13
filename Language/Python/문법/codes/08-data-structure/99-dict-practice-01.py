# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    blood_types_dic = {}
    # blood_types_dic['A'] = blood_types.count('A')
    # blood_types_dic['B'] = blood_types.count('B')
    # blood_types_dic['O'] = blood_types.count('O')
    # blood_types_dic['AB'] = blood_types.count('AB')
    for blood in blood_types:
        if blood in blood_types_dic:
            blood_types_dic[blood] += 1
        else:
            blood_types_dic[blood] = 1 

    return blood_types_dic

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types_2(blood_types):
    blood_types_dic = {}
    # blood_types_dic['A'] = blood_types_dic.get('A', blood_types.count('A'))
    # blood_types_dic['B'] = blood_types_dic.get('B', blood_types.count('B'))
    # blood_types_dic['O'] = blood_types_dic.get('O', blood_types.count('O'))
    # blood_types_dic['AB'] = blood_types_dic.get('AB', blood_types.count('AB'))
    for blood in blood_types:
        blood_types_dic[blood] = blood_types_dic.get(blood, 0) + 1

    return blood_types_dic

print(count_blood_types_2(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
