import pickle
import os


class MyPickle:
    def __init__(self, file_to_pickle, pickle_name):
        self.file_to_pickle = file_to_pickle
        self.pickle_name = pickle_name
        print('Starting Pickle...')

    def make_pickle(self):
        pickle_file = open(self.pickle_name, 'wb')
        pickle.dump(self.file_to_pickle, pickle_file)  # remove classes
        print(self.file_to_pickle + ' has been stored as ' + self.pickle_name)
        pickle_file.close()

    def unmake_pickle(self):
        pickle_file = open(self.pickle_name, 'rb')
        load_file = pickle.load(pickle_file)
        print(load_file)
        f = open(load_file, 'r')
        print(f.read())
        pickle_file.close()

    def delete_pickle(self):
        os.remove(self.pickle_name)
        print(self.pickle_name + ' deleted!')
