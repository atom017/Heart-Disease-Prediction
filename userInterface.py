import numpy as np
import pickle
import streamlit as st



loaded_model= pickle.load(open('model_rf.sav','rb'))

def prediction(input_data):
    input_arr = np.asarray(input_data)
    # reshape the array to predict for one instance
    input_reshaped = input_arr.reshape(1, -1)
    predicted = loaded_model.predict(input_reshaped)
    return predicted

def main():
    result = ''

    #title of the app
    st.title('Heart Disease Prediction')
    c1, c2 = st.columns([1,1])
    #input parameters
    with c1:
        age = st.number_input('Age', min_value=1, max_value=120)
        cp = st.selectbox(
            'Chest Pain Type',
            (0, 1, 2, 3)
        )
        chol = st.number_input('Serum cholestoral in mg/dl',min_value=1,value=126)
        restecg = st.selectbox(
            'Resting electrocardiographic results',
            (0, 1)
        )
        exang = st.selectbox(
            'Excercise induced angina',
            (0, 1)
        )
    with c2:
        gender = st.selectbox(
            'Gender',
            ('Male', 'Female')
        )
        trestbps = st.number_input('Resting Blood Pressure',value=94)
        fbs = st.selectbox(
            'Fasting blood sugar &gt; 120 mg/dl',
            (0, 1)
        )
        thalach = st.number_input('Maximum heart rate achieved',min_value=50,value=71)
        oldpeak = st.number_input('ST depression induced by exercise relative to rest', step=1., format="%.2f")

    sex = 1 if gender=='Male' else 0



    slope= st.selectbox(
        'The slope of the peak exercise ST segment',
        (0,1,2)
    )

    ca = st.selectbox(
        'Number of major vessels(0-3) colored by flourosopy',
        (0,1,2,3)
    )

    thal = st.selectbox(
        'A blood disorder called thalassemia: 1 = normal; 2 = fixed defect; 3 = reversable defect',
        (1,2,3)
    )

    input_data = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    #create button
    if(st.button('Test Result')):
        result = prediction(input_data)
        text=''

        if (result ==0):
            text= '<p style="color:#196d15;font-size:24px;">Good News! The person has no Heart Disease</p>'
        else:
            text = '<p style="color:#ff0000;font-size:24px;">The person has Heart Disease!</p>'
        st.markdown(text, unsafe_allow_html=True)


if __name__ == '__main__':
    main()