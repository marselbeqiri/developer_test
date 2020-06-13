haystack = 'vnk2435kvabco8awkh125kjneytbcd12qjhb4acd123xmnbqwnw4t'
needle = 'abcd1234'
threshold = 3


def needle_in_haystack(needle, haystack, threshold):
    print_results = []
    max_value = threshold
    min_value = 0
    while max_value - min_value >= 3 and max_value < len(needle) + 1:

        temp_threshold = threshold
        while temp_threshold < len(needle) + 1:
            if temp_threshold - min_value >= 3:
                current_max = temp_threshold
                res = [i for i in range(len(haystack)) if haystack.startswith(needle[min_value:current_max], i)]

                if res:
                    print_results.append(
                        {'sequence of length = {} found at haystack offset {}, needle offset {}. Text: {}  '.format(
                            current_max,
                            str(res),
                            min_value, needle[min_value:current_max])})

            temp_threshold += 1

        min_value += 1
        max_value += 1

    return print(print_results)


needle_in_haystack(needle, haystack, threshold)
