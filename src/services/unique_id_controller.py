import json


def get_database_object():
  database_file = open('databases/unique_id.json')
  file_data = database_file.read()
  return json.loads(file_data)


def generate_unique_id():
  database = get_database_object()
  unique_id = database['id']

  updated_id = str(int(unique_id) + 1)
  database['id'] = updated_id
  update_unique_id(database)
  return unique_id


def update_unique_id(updated_database):
  database_file = open('databases/unique_id.json', 'w')
  json.dump(updated_database, database_file, indent=2)