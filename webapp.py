# -*- coding: utf-8 -*-

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# creating a function for Prediction

def Saving_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not Saving'
    else:
      return 'The person is Saving'
  
    
  
def main():
    
    
    # giving a title
    st.title('Optimizing Savings Prediction')
    
    
    # getting the input data from the user
    
    income = st.number_input("Enter your Income:")  
    rent = st.number_input("Enter your Rent:")  
    insurance = st.number_input("Enter your Insurance:")  
    groceries = st.number_input("Enter your Groceries Spend:")  
    transport = st.number_input("Enter your Transport Spend:")  
    entertainment = st.number_input("Enter your Entertainment Spend:")  
    dependents = st.number_input("Enter the Number of Dependents:")  
    age = st.number_input("Enter Your Age:")

    
    
    # code for Prediction
    Prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Saving Result'):
        Prediction = Saving_prediction([income, rent, insurance, groceries, transport, entertainment, dependents, age])
        
        
    st.success(Prediction)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  