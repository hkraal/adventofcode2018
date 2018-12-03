from inputs.day_1 import INPUT


def change_frequency(frequency, frequency_change):
    method = frequency_change[0]
    difference = int(frequency_change[1:])

    if method == '-':
        frequency_result = frequency - difference
    elif method == '+':
        frequency_result = frequency + difference

    print('Current frequency {}, change of {}; resulting frequency {}.'.format(
        frequency,
        frequency_change,
        frequency_result,
    ))

    return frequency_result


def test_change_frequency_2():
    f = 0
    for x in ['+1', '+1', '-2']:
        f = change_frequency(f, x)
    assert f == 0

def test_change_frequency_3():
    f = 0
    for x in ['-1', '-2', '-3']:
        f = change_frequency(f, x)
    assert f == -6


if __name__ == '__main__':
    frequency = 0
    for frequency_change in INPUT.splitlines():
        frequency = change_frequency(frequency, frequency_change)
