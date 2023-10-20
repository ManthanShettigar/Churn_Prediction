import joblib

def transform(data):

    encoder = joblib.load('./config/target_encoder.pkl')
    scaler = joblib.load('./config/scaler.pkl')

    data['Gender_Male'] = data['Gender'].map({'Male':True , 'Female':False})
    data.drop(['Gender'],axis=1,inplace = True)
    
    #  Billing per Usage
    data['Billing_Per_Usage'] = data['Monthly_Bill'] / data['Total_Usage_GB']

    #  Tenure
    max_subscription_length = 24
    data['Tenure'] = max_subscription_length - data['Subscription_Length_Months']
    
    
    data['Location'] = encoder.transform(data['Location'])
    
    
    numerical_columns = ['Age', 'Subscription_Length_Months', 'Monthly_Bill', 'Total_Usage_GB','Tenure','Billing_Per_Usage','Location']
    
    data[numerical_columns] = scaler.transform(data[numerical_columns])
    
    return data