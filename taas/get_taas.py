import pickle
def get_taas():
    with open("mosabeghe.taas","rb") as data_file:
        data = pickle.load(data_file)
    for taas in data:
         yield taas
