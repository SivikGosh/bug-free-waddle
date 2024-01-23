from bill import addresses


def get_unique_streets():
    array = []
    for i in addresses:
        array.append(i["Улица"])
    return list(set(array))


def get_unique_addresses():
    array = []
    for i in addresses:
        array.append(f'{i["Улица"]}, {i["Дом"]}')
    return list(set(array))


def get_addresses_dict(s, a):
    addresses_dict = {}

    for street in s:
        addresses_dict.update({
            street: [i.split(', ')[1] for i in a if street == i.split(', ')[0]]
        })

    return addresses_dict


def get_result_sets(d):
    result = []

    for street, build in d.items():
        print(street)
        res = street.split() + build
        result.append(set(res))

    return result


unique_streets = get_unique_streets()
unique_addresses = get_unique_addresses()
dict_addresses = get_addresses_dict(unique_streets, unique_addresses)

result = get_result_sets(dict_addresses)
