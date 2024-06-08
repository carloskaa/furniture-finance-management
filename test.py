import json

# Cargar el archivo JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Filtrar duplicados en contenttypes
seen = set()
filtered_data = []
for obj in data:
    if obj['model'] == 'contenttypes.contenttype':
        key = (obj['fields']['app_label'], obj['fields']['model'])
        if key not in seen:
            seen.add(key)
            filtered_data.append(obj)
    else:
        filtered_data.append(obj)

# Guardar el archivo JSON filtrado
with open('data_filtered.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)
