import json
import os
import pickle


def read_json(path):
    file_name = path
    with open(file_name) as f:
        data = json.load(f)

    print(data)
read_json('/Users/amishra/DEV/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json')


def read_all_json_files(path):
 all_dicts = []
 for full_file in os.listdir(path):
  full_filename = os.path.join(path, path, full_file)
  with open(full_filename, 'r') as fi:
   dictionary = json.load(fi)
   all_dicts.append(dictionary)
 return all_dicts

def write_pickle(path, data):
    path = os.path.join(path, path, 'super_smash_characters.pickle')
    pickle_one = pickle.dump(data, path, protocol=3.7)
    print(pickle_one)

    def load_pickle()

