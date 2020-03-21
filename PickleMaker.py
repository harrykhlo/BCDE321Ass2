import pickle


class MyPickle:
    def __init__(self, file_to_pickle, pickle_name):
        self.file_to_pickle = file_to_pickle
        self.pickle_name = pickle_name

    def make_pickle(self):
        pickle_file = open(self.pickle_name, 'wb')
        pickle.dump(self.file_to_pickle, pickle_file)  # remove classes
        pickle_file.close()

    def unmake_pickle(self):
        pickle_file = open(self.pickle_name, 'rb')
        load_file = pickle.load(pickle_file)
        print(load_file)
        pickle_file.close()
