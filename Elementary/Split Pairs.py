def split_pairs(a):
    # your code here
    str_len = len(a)
    if str_len % 2 == 1:
        a += '_'
        str_len += 1

    output = []
    swap = ''

    for idx, letter in enumerate(a):
        swap += letter
        if idx % 2 == 1:
            output += [''.join(swap)]
            swap = ''


    # for index in range(0, str_len, 2):
    #     output = output + (a[index:index + 2])


    # output = [a[0:round(str_len/2)], a[round(str_len/2):str_len]]
    return output


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcdf')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
