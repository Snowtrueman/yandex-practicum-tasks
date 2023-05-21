def get_unique(first: list, second: list) -> list:
    return list(set(first) - set(second))


if __name__ == "__main__":
    f_list = [i for i in range(20)]
    s_list = [i for i in range(-20, 10)]

    print(f_list)
    print(s_list)
    print(get_unique(f_list, s_list))
