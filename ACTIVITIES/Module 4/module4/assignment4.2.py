# # LIST
# print("List to Tuple")
# list = [1,2,3,4,5]
# print(f"List: {list}")
# c_tuple = tuple(list)
# print(f"Tuple: {c_tuple}")
#
# print("\nList to Sets")
# list = [1,2,3,4,5]
# print(f"List: {list}")
# c_sets = set(list)
# print(f"Set: {c_sets}")
#
# print("\nList to Dictionary")
# list = ['one',1,'two',2,'three',3]
# print(f"List: {list}")
# iterate = iter(list)
# c_dict = dict(zip(iterate, iterate))
# print(f"Dictionary: {c_dict}")

# # TUPLE
# print("Tuple to List")
# o_tuple = (1,2,3,4,5)
# print(f"Tuple: {o_tuple}")
# c_list = list(o_tuple)
# print(f"List: {c_list}")
#
# print("\nTuple to Sets")
# o_tuple = (1,2,3,4,5)
# print(f"Tuple: {o_tuple}")
# c_sets = set(o_tuple)
# print(f"Sets: {c_sets}")
#
# print("\nTuple to Dictionary")
# o_tuple = ('one',1,'two',2,'three',3)
# print(f"Tuple: {o_tuple}")
# iterate = iter(o_tuple)
# c_dict = dict(zip(iterate, iterate))
# print(f"Dictionary: {c_dict}")

#
# # SETS
# print("Sets to List")
# o_sets = {1,2,3,4,5}
# print(f"Sets: {o_sets}")
# c_list = list(o_sets)
# print(f"List: {c_list}")
#
# print("\nSets to Tuple")
# o_sets = {1,2,3,4,5}
# print(f"Sets: {o_sets}")
# c_tuple = tuple(o_sets)
# print(f"Tuple: {c_tuple}")
#
# print("\nSets to Dictionary")
# o_sets = {'one',1,'two',2,'three',3}
# print(f"Sets: {o_sets}")
# iterate = iter(o_sets)
# c_dict = dict(zip(iterate, iterate))
# print(f"Dictionary: {c_dict}")

#
# # DICTIONARY
# print("Dictionary to List")
# o_dict = {'one': 1, 'two': 2, 'three': 3}
# print(f"Dictionary: {o_dict}")
# c_list = list(o_dict.keys()) + list(o_dict.values())
# print(f"List: {c_list}")
#
# print("\nDictionary to Tuple")
# o_dict = {'one': 1, 'two': 2, 'three': 3}
# print(f"Dictionary: {o_dict}")
# c_tuple = tuple(o_dict.keys()) + tuple(o_dict.values())
# print(f"Tuple: {c_tuple}")
#
# print("\nDictionary to Sets")
# o_dict = {'one': 1, 'two': 2, 'three': 3}
# print(f"Dictionary: {o_dict}")
# c_set = set(o_dict.keys())
# c_set.update(o_dict.values())
# print(f"Sets: {c_set}")
