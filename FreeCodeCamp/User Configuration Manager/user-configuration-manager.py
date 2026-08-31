def add_setting(dict1, tuple1):
    tuple1 = tuple1
    dict1 = dict1
    key,value = tuple1
    key = key.lower()
    value = value.lower()
    if key in dict1.keys():
        return (f'Setting \'{key}\' already exists! Cannot add a new setting with this name.')
    else:
        dict1[f'{key}'] = f'{value}'
        return(f'Setting \'{key}\' added with value \'{value}\' successfully!')

def update_setting(dict2, tuple2):
    key,value = tuple2
    key = key.lower()
    value = value.lower()
    if key in dict2:
        dict2[key] = value
        return(f'Setting \'{key}\' updated to \'{value}\' successfully!')
        dict2[f'key'] = f'{value}'
    else:
        return(f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.')
def delete_setting(dict3, key1):
    key1 = key1.lower()
    if key1 in dict3:
        del dict3[key1]
        return(f'Setting \'{key1}\' deleted successfully!')
    else:
        return('Setting not found!')
def view_settings(dict4):
    if not dict4:
        return('No settings available.')
    else:
        texto_final = 'Current User Settings:\n'

        for key,value in dict4.items():
            texto_final += f"{key.capitalize()}: {value}\n"
        return texto_final


test_settings = {
    'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'
}