import utils
def main():
    test = [
        {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'},
        {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'},
        {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    ]
    df = utils.def_list_to_pandas(test, drop_columns=['key2'])
    print('done')


if __name__ == "__main__":
    main()