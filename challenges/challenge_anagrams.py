def merge(char_set, start, end):
    last_char = char_set[end]
    next_char = start - 1

    for i in range(start, end):
        if char_set[i] <= last_char:
            next_char += 1

            char_set[i], char_set[next_char] = (
                char_set[next_char],
                char_set[i],
            )

    char_set[next_char + 1], char_set[end] = (
        char_set[end], 
        char_set[next_char + 1]
    )

    return next_char + 1


def merge_sort(char_set, start, end):
    if start < end:
        aux = merge(char_set, start, end)
        merge_sort(char_set, aux + 1, end)
        merge_sort(char_set, start, aux - 1)


def order_string(char_set):
    start = 0
    end = len(char_set) - 1

    return merge_sort(char_set, start, end)


def order_word(string):
    char_set = list(string.lower())

    order_string(char_set)

    ordered = "".join(char_set)

    return ordered


def is_anagram(first_string, second_string):
    first_string_chars = order_word(first_string)
    second_string_chars = order_word(second_string)

    result = first_string_chars == second_string_chars

    if not first_string and not second_string:
        result = False

    return (first_string_chars, second_string_chars, result)
