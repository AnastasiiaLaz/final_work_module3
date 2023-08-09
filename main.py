from arrs import functions

from path import PATH_TO_JSON


def main():
    operations = functions.get_data(PATH_TO_JSON)
    ex_operations = functions.get_executed_operations(operations)
    five_operations = functions.get_recent_five_operations(ex_operations)
    for operation in five_operations:
        if operation:
            print(functions.validate_operation(operation))


print(main())

if __name__ == '__main__':
    main()
