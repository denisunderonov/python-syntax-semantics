def data_types():
    integer_value = 10
    string_value = "string"
    float_value = 3.14
    boolean_value = True
    list_value = [1, 2, 3]
    dictionary_value = {"name": "Denis"}
    tuple_value = (1, 2, 3)
    set_value = {1, 2, 3}

    values = [
        integer_value,
        string_value,
        float_value,
        boolean_value,
        list_value,
        dictionary_value,
        tuple_value,
        set_value,
    ]

    types_list = []

    for value in values:
        types_list.append(type(value).__name__)

    result = f"[{", ".join(types_list)}]"

    print(result)


if __name__ == "__main__":
    data_types()