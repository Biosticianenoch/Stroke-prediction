import pandas as pd
import numpy as np
df = pd.read_csv('https://github.com/Biosticianenoch/data/blob/main/breast%20cancer.csv')
df
 xgboost import XGBClassifier

xgb = XGBClassifier(objective = 'binary:logistic', learning_rate = 0.5, max_depth = 5, n_estimators = 180)

xgb.fit(X_train, y_train)

y_pred = xgb.predict(X_test)

# Breast prediction page
if (selected == "Breast Diseases"):

    #page title
    st.title("BREAST DISEASE PREDICTION")

    # Getting the input data from the user
    # Columns for input fileds

    col1,col2,col3 = st.columns(3)

    with col1:
        meanradius = st.text_input('Mean radius of tumor')
    with col2:
        meantexture = st.text_input('Mean texture of tumor')
    with col3:
        meanperimeter = st.text_input('Mean perimeter of tumor')
    with col1:
        meanarea  = st.text_input('Mean area of tumor')
    with col2:
        meansmoothness = st.text_input('Mean smoothness of tumor')
    with col3:
        meancompactness = st.text_input('Mean compactness of tumor')
    with col1:
        meanconcavity = st.text_input('Mean concavity of tumor')
    with col2:
        meanconcavepoints = st.text_input('Mean number of concave portions')
    with col3:
        meansymmetry = st.text_input('symmetry_mean')
    with col1:
        meanfractaldimension = st.text_input('fractal_dimension_mean')
    with col2:
        radiuserror = st.text_input('Radius error')
    with col3:
        textureerror = st.text_input('Text error')
    with col1:
        perimetererror  = st.text_input('Perimeter Error')
    with col2:
        areaerror = st.text_input('Area Error')
    with col3:
        smoothnesserror = st.text_input('Smoothnness error')
    with col1:
        compactnesserror = st.text_input('Compactness error')
    with col2:
        concavityerror = st.text_input('Concavity error')
    with col3:
        concavepointserror = st.text_input('Concave point error')
    with col1:
        symmetryerror = st.text_input('Symmetry error')
    with col2:
        fractaldimensionerror = st.text_input('Fractional Dimension error')
    with col3:
        worstradius = st.text_input('Worst Radius')
    with col1:
        worsttexture  = st.text_input('Worst Texture')
    with col2:
        worstperimeter = st.text_input('Worst Perimeter')
    with col3:
        worstarea = st.text_input('Worst Area')
    with col1:
        worstsmoothness = st.text_input('Worst Smoothness')
    with col2:
        worstcompactness = st.text_input('Worst commpactness')
    with col3:
        worstconcavity = st.text_input('Worst concavity')
    with col1:
        worstconcavepoints = st.text_input('Worst concave points')
    with col2:
        worstsymmetry = st.text_input('Worst symmetry')
    with col3:
        worstfractaldimension = st.text_input('Worst fractional dimension')


    # code for prediction
    breast_cancer_prediction = ''

    #creating button for prediction
    if st.button('Diagnose'):

        user_input = [meanradius, meantexture, meanperimeter, meanarea, meansmoothness, meancompactness, meanconcavity, meanconcavepoints, meansymmetry, meanfractaldimension, radiuserror, textureerror, perimetererror, areaerror, smoothnesserror, compactnesserror, concavityerror, concavepointserror, symmetryerror, fractaldimensionerror, worstradius, worsttexture, worstperimeter, worstarea, worstsmoothness, worstcompactness, worstconcavity, worstconcavepoints, worstsymmetry, worstfractaldimension]

        user_input = [float(x) for x in user_input]

        breast_cancer_prediction = breast_disease_model.predict([user_input])

        if(breast_cancer_prediction[0]==1):
            breast_cancer_prediction = 'SUFFERING FROM BEGNIN'
        else:
            breast_cancer_prediction = "SUFFERING FROM MALIGNANT"

    st.success(breast_cancer_prediction)
