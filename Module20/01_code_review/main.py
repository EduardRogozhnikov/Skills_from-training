students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests(dictionary):
    lst = []
    string = ''
    for i in dictionary:
        lst += dictionary[i]['interests']
        string += dictionary[i]['surname']
    count = 0
    for s in string:
        count += 1
    return lst, count


pairs = [] #список пар
for i in students:
    tuple_pairs = (i, students[i]["age"])
    pairs.append(tuple_pairs)

my_lst = interests(students)[0]
long_family = interests(students)[1]

print('Список пар "ID студента - возраст": ', pairs)
print("Полный список интересов всех студентов:", my_lst)
print('Общая длина всех фамилий студентов:', long_family)

# TODO исправить код