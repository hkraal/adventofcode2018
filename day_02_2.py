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

def split(line):
    return [x for x in line]

def parse_ids(lines):
    for left in lines:
        for right in lines:
            diff_count = 0
            i = 0
            matches = []
            for i in range(len(left)):
                if left[i] != right[i]:
                    diff_count += 1
                else:
                    matches.append(left[i])
            if diff_count == 1:
                return ''.join(matches)



def test_checksum():
    assert 'fgij' == parse_ids([
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz',
    ])

if __name__ == '__main__':
    print(parse_ids(INPUT.splitlines()))
