import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load models and preprocessor
lr_model = joblib.load('C:/Users/sefon/OneDrive/Documents/WTAMU/Spring24/Capstone/Project/logistic_regression_model.pkl')
nb_model = joblib.load('C:/Users/sefon/OneDrive/Documents/WTAMU/Spring24/Capstone/Project/naive_bayes_model.pkl')
lgbm_model = joblib.load('C:/Users/sefon/OneDrive/Documents/WTAMU/Spring24/Capstone/Project/lightgbm_model.pkl')
preprocessor = joblib.load('C:/Users/sefon/OneDrive/Documents/WTAMU/Spring24/Capstone/Project/preprocessor.pkl')

# Streamlit user interface for the app
st.title("Online Shopper Intent Predictor")
st.write("""
The Online Shopper Intention Prediction App is designed to empower online retailers by predicting potential sales opportunities based on user behavior on their websites. By inputting data related to user interactions, the app utilizes advanced machine learning models to forecast whether a session will result in a sale. To demonstrate typical user interactions, we have pre-entered some values across various fields. You can adjust these values based on your specific data or use cases. What's most important for your analysis?
- **Catch Every Opportunity**: Focus on capturing as many potential sales as possible, even if it means some false alerts.
- **Avoid False Alarms**: Focus on ensuring alerts for potential sales are always accurate, even if some opportunities are missed.
- **Balanced Approach**: A balanced focus on both capturing opportunities and minimizing false alarms.
""")

# User choice on what's crucial
preference = st.selectbox('Select what is most crucial to you:', ['Catch Every Opportunity', 'Avoid False Alarmss', 'Balanced Approach'])



# User inputs for the model prediction
# Numeric inputs
administrative = st.number_input('Number of Administrative Pages Visited', value=2, help="Number of administrative pages visited by the user during the session.")
administrative_duration = st.number_input('Time on Administrative Pages (in seconds)', value=80.0, help="Total amount of time (in seconds) spent on administrative pages.")
informational = st.number_input('Number of Informational Pages Visited', value=0, help="Number of informational pages visited by the user during the session.")
informational_duration = st.number_input('Time on Informational Pages (in seconds)', value=0.0, help="Total amount of time (in seconds) spent on informational pages.")
product_related = st.number_input('Number of Product Related Pages Visited', value=31, help="Number of product-related pages visited by the user during the session.")
product_related_duration = st.number_input('Time on Product Pages (in seconds)', value=1194.0, help="Total amount of time (in seconds) spent on product pages.")
bounce_rates = st.number_input('Bounce Rate', value=0.02, format="%.2f", help="Percentage of visitors who enter the site and then leave ('bounce') without viewing other pages.")
exit_rates = st.number_input('Exit Rate', value=0.04, format="%.2f", help="Percentage of how often users exit from a page after viewing it.")
page_values = st.number_input('Page Value', value=5.9, format="%.1f", help="Average value of the page aggregated over the browsing session.")

# Define mappings for categorical variables
browser_mapping = {'Chrome': 1, 'Firefox': 2, 'Safari': 3, 'Edge': 4, 'Opera': 5}
region_mapping = {'North America': 1, 'Europe': 2, 'Asia': 3, 'South America': 4, 'Africa': 5, 'Australia': 6}
traffic_type_mapping = {'Direct': 1, 'Email': 2, 'Referral': 3, 'Paid Search': 4, 'Social Media': 5}
os_mapping = {'Windows': 1, 'MacOS': 2, 'Linux': 3, 'Android': 4, 'iOS': 5}

#catvar
month = st.selectbox('Month', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], index=4)
operating_systems = st.selectbox('Operating System', list(os_mapping.keys()), index=1, help='Which operating system does the shopper use?')
browser = st.selectbox('Browser', list(browser_mapping.keys()), index=1, help='Which browser does the shopper use?')
region = st.selectbox('Region', list(region_mapping.keys()), index=0, help='Which region is the shopper from?')
traffic_type = st.selectbox('Traffic Type', list(traffic_type_mapping.keys()), index=1, help='How did the shopper get to our website?')
visitor_type = st.selectbox('Visitor Type', ['Returning_Visitor', 'New_Visitor', 'Other'], index=0, help='Is the shopper a returning visitor or not?')
weekend = st.checkbox('Weekend', value=False, help='Is it done over the weekend?')

# Prepare input DataFrame
input_values = [administrative, administrative_duration, informational, informational_duration,
                product_related, product_related_duration, bounce_rates, exit_rates, page_values,
                month, os_mapping[operating_systems], browser_mapping[browser], region_mapping[region],
                traffic_type_mapping[traffic_type], visitor_type, weekend]

feature_names = ['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration',
                 'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues',
                 'Month', 'OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType', 'Weekend']

input_df = pd.DataFrame([input_values], columns=feature_names)

# Preprocess input data
transformed_input = preprocessor.transform(input_df)

# Button to make prediction
if st.button('Predict'):
    # Select the model based on user preference
    if preference == 'Catch Every Opportunity':
        model = nb_model
        transformed_input = transformed_input.toarray()  # Converting to dense array for Naive Bayes
    elif preference == 'Avoid False Alarms':
        model = lr_model
    else:
        model = lgbm_model

    prediction = model.predict(transformed_input)
    result = 'There is high probability that the user will make a purchase.' if prediction[0] else 'The user is not likely to make a purchase.'
    st.subheader('Prediction results:')
    st.write(result)