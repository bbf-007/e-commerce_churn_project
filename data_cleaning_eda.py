
import pandas as pd

df = pd.read_csv("e_commerce_shopper_behaviour_and_lifestyle.csv")


#check for duplicates

df.duplicated().sum() 


df['user_id'].duplicated().sum() #no duplicates

#check for missing values
df.isnull().sum()

#checking the age column for outliers
plt.scatter(df['age'], df['age']); #no outliers

#check the categorical columns

df['gender'].value_counts()

df['urban_rural'].value_counts()

df['employment_status'].value_counts()

df['education_level'].value_counts()


df['relationship_status'].value_counts()

df['has_children'].value_counts()

df['device_type'].value_counts()

df['preferred_payment_method'].value_counts()

df['shopping_time_of_day'].value_counts()

df['budgeting_style'].value_counts()



# how to determine churn
#return_frequency

df['churn'] = [1 if value > 1 else 0 for value in df['return_frequency']]

