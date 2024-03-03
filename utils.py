import pickle
import numpy as np
import config

def predict_drug_type(age, Na_to_K, sex, bp, cholesterol):
   drug_pickle_path = config.MODEL_FILE_PATH
   
    
   with open(drug_pickle_path, 'rb') as f:
        model = pickle.load(f)

   test_array = np.array([[age, Na_to_K, sex, bp, cholesterol]])
   drug_type = model.predict(test_array)[0]

   return drug_type