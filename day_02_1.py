from inputs.day_2 import INPUT

def id_to_dict(id):
    result = {}
    data_list = [x for x in id]
    for x in set(data_list):
        count = 0
        for y in data_list:
            if x == y:
                count += 1
        result[x] = count
    return result


def parse_ids(lines):
    two = 0
    three = 0

    for id in lines:
        has_two = False
        has_three = False
        result = id_to_dict(id)
        print(result)
        for key in result:
            if result[key] == 2:
                has_two = True
            elif result[key] == 3:
                has_three = True

        if has_three:
            three += 1
        if has_two:
            two += 1
    return two * three


def test_checksum():
    assert 12 == parse_ids([
        'abcdef',
        'bababc',
        'abbcde',
        'abcccd',
        'aabcdd',
        'abcdee',
        'ababab',
    ])

if __name__ == '__main__':
    print(parse_ids(INPUT.splitlines()))
