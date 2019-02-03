
def compare_values(path, val, other_json):
	try:
		for key in path:
			if key.isdigit():
				other_json = other_json[int(key)]
			else:
				other_json = other_json[key] 
	except KeyError:
		raise KeyError('во втором json-е нет ключа словаря по адресу ['+"][".join(path)+']')
	except IndexError:
		raise IndexError('во втором json-е нет объекта в списке по адресу ['+"][".join(path)+']')
	if isinstance(val, float) and isinstance(other_json, float):
		val, other_json = round(val, 5), round(other_json, 5)
	if val!=other_json:
		raise ValueError("по адресу [{}] в первом json-е {} а во втором {}".format("][".join(path), str(val), str(other_json)))
		
def compare_len_lists(path, json, other_json):
	try:
		for key in path:
			if key:
				if key.isdigit():
					other_json = other_json[int(key)]
				else:
					other_json = other_json[key] 
	except KeyError:
		raise KeyError('во втором json-е нет ключа словаря по адресу ['+"][".join(path)+']')
	if len(json)!=len(other_json):
		raise KeyError('длина списка по пути  [{}] для первого json-а {} а для второго {}'.format("][".join(path), len(json), len(other_json)))
		

def tree_traversal(json, other_json, path=''):
	if isinstance(json, list):
		compare_len_lists(path.split('/'), json, other_json)
		for i, el in enumerate(json):
			if isinstance(el, list) or isinstance(el, dict):
				tree_traversal(el, other_json, path=path+str(i)+'/')
			else:
				compare_values((path + str(i)).split('/'), el, other_json)
	elif isinstance(json, dict):
		compare_len_lists(path.split('/'), json, other_json)
		for key in json:
			if isinstance(json[key], list) or isinstance(json[key], dict):
				tree_traversal(json[key], other_json, path = path + key + '/')
			else:
				compare_values((path + key).split('/'), json[key], other_json)
	else:
		compare_values(json, other_json)


def compare_jsons(json, other_json):
	try:
		tree_traversal(json, other_json)
		print('Эти json-ы одинаковые')
		return True
	except Exception as e:
		print('Эти json-ы разные')
		print(e.args[0])
		return False
