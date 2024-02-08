import utils

def main():
    operations = utils.load_operations('operations.json')
    operations = utils.filter_operations(operations)
    operations = utils.sort_operations(operations)
    operations = utils.cut_operations(operations)
    for operation in operations:
        try:
            print(f"{utils.formatter_date(operation['date'])} {operation['description']}\n"
                  f"{utils.mask_account(operation.get('from'))[0]}{utils.mask_account(operation.get('from'))[1]}-> "
                  f"{utils.mask_account(operation.get('to'))[0]}{utils.mask_account(operation.get('to'))[1]}\n"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
        except KeyError:
            operation['date'] = None
            operation['from'] = None
            operation['to'] = None
            operation['operationAmount']['amount'] = None
            operation['operationAmount']['currency']['name'] = None





if __name__ == '__main__':
    main()