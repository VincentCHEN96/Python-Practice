from collections import OrderedDict


dictionary = OrderedDict()
dictionary['and'] = "与"
dictionary['or'] = "或"
dictionary['in'] = "包含"
dictionary['not in'] = "不包含"
dictionary['#'] = "注释"

for key in dictionary.keys():
    print(key + ":")
    print("\t" + dictionary[key])