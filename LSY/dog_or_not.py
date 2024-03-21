from joblib import load

model_file = '/project/my_modeldog_01.pkl'


model = load(model_file)


print(model)