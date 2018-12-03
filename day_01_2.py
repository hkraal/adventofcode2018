from inputs.day_1 import INPUT


def change_frequency(frequency, frequency_change):
    method = frequency_change[0]
    difference = int(frequency_change[1:])

    if method == '-':
        frequency_result = frequency - difference
    elif method == '+':
        frequency_result = frequency + difference

    return frequency_result


def find_duplicate_frequency(frequency_changes):
    frequency = 0
    frequency_history = [0]
    loop = 0
    while True:
        print('Starting loop {}'.format(loop))
        for frequency_change in frequency_changes:
            frequency_result = change_frequency(frequency, frequency_change)

            if frequency_result in frequency_history:
                print(
                    'Current frequency {}, change of {}; resulting frequency {}, which has already been seen.'.format(
                        frequency,
                        frequency_change,
                        frequency_result,
                    ))
                return frequency_result
            frequency = frequency_result
            frequency_history.append(frequency_result)
        loop += 1


def test_find_duplicate_frequencies_1():
    assert find_duplicate_frequency(['+1', '-1']) == 0

def test_find_duplicate_frequencies_2():
    assert find_duplicate_frequency(['+3', '+3', '+4', '-2', '-4']) == 10

def test_find_duplicate_frequencies_3():
    assert find_duplicate_frequency(['-6', '+3', '+8', '+5', '-6']) == 5

def test_find_duplicate_frequencies_4():
    assert find_duplicate_frequency(['+7', '+7', '-2', '-7', '-4']) == 14


if __name__ == '__main__':
    frequency_changes = INPUT.splitlines()
    find_duplicate_frequency(frequency_changes)
