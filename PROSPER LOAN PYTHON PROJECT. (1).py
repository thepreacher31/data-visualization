#!/usr/bin/env python
# coding: utf-8

# In[5]:


# PROSPER LOAN DATASET EXPLORATION
## BY JACOB DANIEL



import pandas as pd
### import pandas helps to import the libary to this notebook so i can perform task neccessary for cleaning my data.


# In[6]:


jade=pd.read_csv('Prosper loan.csv')

## This code here says let 'jade' be the name of my dataframe.
### pd.read_csv (prosper loan.csv) is the format of the document and helps to to load the document into this notebook.


# In[7]:


jade

## jade is my df and when run its dispays the document "prosper loan"


# In[8]:


## I realize i need to delete some columns because i do not need them for my visualization,they are just values of zero all through so its invaluable to me these are :(LP_CollectionFees','LP_GrossPrincipalLoss','LP_NetPrincipalLoss','LP_NonPrincipalRecoverypayments','InvestmentFromFriendsAmount').


jade=jade.drop(columns=['LP_CollectionFees','LP_GrossPrincipalLoss','LP_NetPrincipalLoss','LP_NonPrincipalRecoverypayments','InvestmentFromFriendsAmount'])


# In[9]:


## Here i am trying to see the details and the counts of values for each parameter stated in the column of the credit grade column seeing that there a lot non avalable (NAN)value in that column.
jade.CreditGrade.value_counts()


# In[10]:


jade


# In[11]:


### this shows/describe the datatypes and number of  column rows

print(jade.dtypes)


# In[ ]:





# jade

# 
# 

# In[12]:


jade.columns


# In[13]:


selected_columns = jade[['IncomeRange', 'LoanOriginalAmount', 'Occupation', 'DebtToIncomeRatio', 'EmploymentStatus','IsBorrowerHomeowner','LoanStatus']]
print(selected_columns)


# Above i was trying to check the relationship between these variables,so i had to check out these columns first. 

# In[14]:


# The code below replaces the 00:00 component from the loan originationn date seeing that the time doesnt really have valuable input to my insight.
  # jade['LoanOriginationDate'] = jade['LoanOriginationDate'].str.replace(' 00:00', '') 


# In[15]:


jade['LoanOriginationDate'] = jade['LoanOriginationDate'].str.replace(' 00:00', '')


# In[16]:


jade


# In[17]:


jade.describe()
#I requested this environmrnt to show me a statistical summary of my dataframe.


# In[18]:


## i want to check the data types so as to ensure data consistency, optimize performance, enable appropriate data manipulation, validating data integrity, facilitating interpretation and visualization, and ensuring compatibility with other systems.

jade.dtypes.all


# In[19]:


if 'CreditGrade' in jade.columns:
    del jade['CreditGrade']
    print("Column 'CreditGrade' deleted successfully.")
else:
    print("Column 'CreditGrade' does not exist in the DataFrame.")


# In[20]:


### bit by bit i am realizing the variables i do not want for my visualization so i am deleting them. 

jade


# In[21]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[22]:


jade['ListingCreationDate'] = jade['ListingCreationDate'].astype(str).str.replace(':', '/').str.replace('.', '/').fillna(jade['ListingCreationDate'])


# In[23]:


## the column 'ListingCreationDate' had some iregularities and i had to change the data type and and replace the : sign that separates the date with a / so as to make it look more like a date and not a timestamp.


jade['ListingCreationDate'] = jade['ListingCreationDate'].str.replace(' ', '/')


# In[24]:


jade.drop_duplicates(subset=['Occupation', 'StatedMonthlyIncome', 'IncomeRange', 'MonthlyLoanPayment','DebtToIncomeRatio','LoanOriginalAmount'], keep='first', inplace=True)


# In[25]:


columns_to_check = ['Occupation', 'StatedMonthlyIncome', 'IncomeRange','MonthlyLoanPayment','DebtToIncomeRatio','LoanOriginalAmount'] 

# Specify the columns you want to check for NaN values ,because pandas do not read NaN values i would have to invoke/print out for column with such values and delete them if i do not have the correct values.However what i plan to do is crosscheck for any column that has more tha 55% of NaN values in them and delete them. 

jade.dropna(subset=columns_to_check, inplace=True)


# In[26]:


jade = jade[~jade.apply(lambda row: row.astype(str).str.contains('Other').any(), axis=1)]
# lamda here is a function here i used to calculate anonymous functions index by undex.


# # UNIVARIATE VISUALIZATION .
# 

# In[27]:


import matplotlib.pyplot as plt


# In[28]:


import seaborn as sns


# In[29]:


# I Plotted a histogram of the income range.


import seaborn as sns

plt.figure(figsize=(12, 8))
sns.histplot(data=jade, x='IncomeRange', color='skyblue', edgecolor='black')
plt.xlabel('Income Range')
plt.ylabel('Proportion')
plt.title('Distribution of Income Range')
plt.show()


# Below is a univariate visualization that shows the frequency of income range that varies. 





# ## This is a uni variate visual
# QUESTION?
#            1. since defaulted payment is on low percentage can we still afford to give out more loans? 

# In[30]:


import seaborn as sns
import matplotlib.pyplot as plt

# Count the occurrences of each unique value in the 'LoanStatus' column
loan_status_counts = jade['LoanStatus'].value_counts()

# Determine the number of slices in the pie chart
num_slices = len(loan_status_counts)

# Create an array to explode the slices
explode = [0.1] + [0] * (num_slices - 1)  # Explode the first slice (Completed) slightly

# Plot a pie chart
plt.figure(figsize=(10, 10))  # Increase the figure size to create more space
plt.pie(loan_status_counts, labels=loan_status_counts.index, autopct='%1.1f%%', startangle=140, explode=explode, textprops={'fontsize': 10})
plt.title('Loan Status Distribution')
plt.show()


# # Above we can see percentage of clients loan status so as to make better informed decision when lending a new client.
# 
# 
# ## 

# # BI VARIATE VISUALIZATION.
# 
#  I am going to create a bi variate visualization  to show the relationship between two variable which are the loan original amount  variables and the occupation variable. 

# In[31]:


jade[['LoanOriginalAmount','Occupation']]


# In[32]:


import seaborn as sns
import matplotlib.pyplot as plt

# Calculate average loan amount for each occupation
avg_loan_by_occupation = jade.groupby('Occupation')['LoanOriginalAmount'].mean().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(75, 10))
sns.barplot(x=avg_loan_by_occupation.index, y=avg_loan_by_occupation.values, palette='viridis')
plt.xlabel('Occupation')
plt.ylabel('Average Loan Original Amount')
plt.title('Average Loan Original Amount by Occupation')
plt.show()


##  We can see the average amount for each occupation so as to understand the correlation between that and the loan amount. we would need to understand if the laon amount increases depending on your occupation.


# In[33]:


jade.columns


# In[34]:


## I deleted the ""LoanFirstDefaultedCycleNumber""  here because i planned to make use of it ,rather 85% percent of value in it is NaN .
# del jade['LoanDefaultedCycleNumber']
jade.columns


# In[35]:


# Here i want to delete columns with NaN values that is more than the average number of the rows in my dataframe.
# Having that kind of NaN number will make my insightful data/findings invalid and false.

# Count NaN values in each column
nan_counts = jade.isna().sum()

# Filter columns with more than 500 NaN values
columns_with_lots_of_nan = nan_counts[nan_counts > 56500]

# Display columns with lots of NaN values
print("Columns with lots of NaN values:")
print(columns_with_lots_of_nan)

# Delete columns with more than 500 NaN values
jade_cleaned = jade.drop(columns_with_lots_of_nan.index, axis=1)

# Display the cleaned DataFrame
print("\nDataFrame after removing columns with lots of NaN values:")
print(jade_cleaned)


# In[36]:


# List of columns to delete
columns_to_delete = ['InvestmentFromFriendsCount', 'Recommendations', 'ClosedDate']

# Drop the specified columns
jade_cleaned = jade.drop(columns=columns_to_delete, inplace=True)

# Display the cleaned DataFrame
print(jade)

# Above i have some columns that are irrelevant to my findings ,so i delete them. They are 'investmentfromfriendscounts,closeddate,recommendations ' , because they have 0 values and lots of Nan values.


# In[37]:


import matplotlib.pyplot as plt

# Group by BorrowerState and sum LoanOriginalAmount
state_loan_amount = jade.groupby('BorrowerState')['LoanOriginalAmount'].sum().sort_values(ascending=False)

## Select top 10 states with highest loan amounts
top_10_states = state_loan_amount.head(10)

### Create stacked bar chart
plt.figure(figsize=(12, 8))
bars = top_10_states.plot(kind='bar', stacked=True, color='black')
plt.title('Loan Amount Borrowed by Top 10 States')
plt.xlabel('Borrower State')
plt.ylabel('Total Loan Amount')
plt.xticks(rotation=25)

#### This code is written to Display exact loan amounts on top of each bar without overlapping
for bar, amount in zip(bars.patches, top_10_states):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 50000, f"${amount:,.0f}", ha='center')

plt.subplots_adjust(bottom=0.3)  # Adjust spacing between bars and x-axis labels
plt.show()

# These 10 states are the top 10 states that has borrowed more money from prosper loans.


# # Above is a stacked barchart 
# ### The chart above shows the total loan amount disbursed to the top 10 states.
# which means that these 10 states receive more loans than the other states and we can see the total amount of the loan being given out to individuals from each states.
# 
# So it turns out "CALIFORNIA" has the total highest amount borrowed by clients.

# In[38]:


jade


# #### here is a visualization to check estimated yield for each states.
# 

# In[39]:


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Calculate the mean of 'estimated effective yield' for each state
mean_yield = jade.groupby('BorrowerState')['EstimatedEffectiveYield'].mean()

# Sort the series in descending order and select the top 5 states
top_5_states = mean_yield.sort_values(ascending=False).head(5)

# Create a bar plot
top_5_states.plot(kind='bar', figsize=(10, 10))

# Set labels and title
plt.xlabel('Borrower State')
plt.ylabel('Mean Estimated Effective Yield')
plt.title('Bar Chart of Mean Estimated Effective Yield by Top 5 Borrower States')

# Show the plot
plt.show()


# In[40]:


import matplotlib.pyplot as plt

# Calculate the mean of 'BorrowerAPR' for each state
mean_apr = jade.groupby('BorrowerState')['BorrowerAPR'].mean()

# Get the top 10 states with the highest mean BorrowerAPR
top_10_states = mean_apr.nlargest(10)

# Create a horizontal bar plot
top_10_states.sort_values().plot(kind='barh', figsize=(10, 6))

# Set labels and title
plt.xlabel('Mean Borrower APR')
plt.ylabel('Borrower State')
plt.title('Top 10 States with Highest Mean Borrower APR')

# Show the plot
plt.show()


# In[41]:


import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.scatter(jade['StatedMonthlyIncome'], jade['LoanOriginalAmount'])
plt.title('Relationship between Monthly Income and Loan Amount')
plt.xlabel('Stated Monthly Income')
plt.ylabel('Loan Original Amount')
plt.show()


# In[45]:


# My thoughts
# Q1). What if the loan amount approved depends on wether the borrower owns a home or not? lets visualize this to be sure of this assumption.

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.violinplot(x='IsBorrowerHomeowner', y='LoanOriginalAmount', data=jade)

plt.title('Loan Amount by Home Ownership')
plt.xlabel('Is Borrower Home Owner')
plt.ylabel('Original Loan Amount')
plt.show()

# MY conclusion: we observed a  Wider Range  in this violin plot which refers to the spread of the data from the lowest to the highest value. When we say that homeowners have a wider range emphasis on wider range, it means that the smallest and largest loan amounts among homeowners are further apart compared to non-homeowners. This could indicate that there is more variability in the loan amounts that homeowners apply for or are granted.
    #(2). The Higher Median Loan Amount- The “median” is basically the middle value in a group of numbers, meaning that half of the numbers are above the median and half are below. according to this plot  "a higher median loan amount for homeowners means that the middle value of loan amounts for homeowners is higher than that of non-homeowners. Which suggest that homeowners, on average are granted larger loans.


# # My findings:
#     1. The  borrower APR refers to the yearly interest generated by a sum that's charged to borrowers or paid to investors whichs means that ALABAMA which is a short code for AL , generated more yearly interest by the sum thats charged to the borowers in that sttae.
#     2. California recorded the highest Loan amount received from prosper loan.
#     3. For the frequency of loan status we have more current loans to be paid,aside the past due dates wether one month and above. 
#     4. Those who earn above 100,000+ are not up to 17,000 people 
#     5. Accordng to my scatterplot above of which i had to check the relationship between 2 quantitative variables 'stated monthly income and the original loan amount'
#     (a). the plot is showing the relationship between monthly the income and loan amount.
#     (b). The data points are concentrated at the lower end of the stated monthly income which indicates that individuals with lower incomes tend to have varying loan amounts.
#     (c) in as much as the plot does not show a clear positive or negative correlation between monthly income and loan amount it also doesn’t clearly show that a higher monthly income is associated with a higher loan amount or vice versa.
#     (d). thereby we cannot definitively say that there is a strong relationship between monthly income and loan amount which means the loan amount does not affect the monthly income. Therefore the income of prosper loan clients does not completely affect the loan amount that will be given to them.

# I HOPE YOU ENJOY THIS PROJECT. HAPPY READING AND UNDERSTANDING. IF YOU HAVE ANY QUESTIONS PLEASE GO AHEAD TO ASK. CHEERS

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




