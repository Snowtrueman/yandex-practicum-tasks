from random import randint


def remove_nulls(initial_list: list) -> list:
    zeros_counter = 0
    total_counter = 0
    for i in range(len(initial_list)):
        while initial_list[i] == 0:
            if len(initial_list) == total_counter:
                break
            zeros_counter += 1
            total_counter += 1
            temp = initial_list.pop(i)
            initial_list.append(temp)
        if len(initial_list) == total_counter:
            break
        total_counter += 1
    return initial_list[:-zeros_counter] if zeros_counter else initial_list


if __name__ == "__main__":

    sample_list = [randint(-10, 10) for _ in range(20)]

    print(sample_list)
    print(remove_nulls(sample_list))
