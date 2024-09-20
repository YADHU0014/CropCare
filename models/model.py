import pickle

# Replace 'your_file.pkl' with the path to your pickle file
with open('D:\ROSPL\HarvestHub\models', 'rb') as file:
    data = pickle.load(file)

print(data)
