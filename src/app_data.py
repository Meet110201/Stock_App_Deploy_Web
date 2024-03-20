# %% [markdown]
## PYTHON LIBRARIES

# %% [markdown]
# LOADING PYTHON LIBRARIES
# %%
# libraries
import pandas as pd


# %%
# %% [markdown]
## DATA PREPROCESSING
# %%
# LOADING THE CSV FILE
df=pd.read_csv("data/TATACONSUM.NS_historical_data.csv")

# %%
# changing the index to Date
df["Date"]=pd.to_datetime(df.Date,format="%Y-%m-%d")
df.index=df["Date"]

# %%
# data sorting 
data=df.sort_index(ascending=True,axis=0)
new_dataset=pd.DataFrame(index=range(0,len(df)),columns=['Date','Close'])
new_dataset = data[['Date', 'Close']].copy()
new_dataset.index=new_dataset.Date
new_dataset.drop("Date",axis=1,inplace=True)
final_dataset=new_dataset.values

# %%
# DATA SPLIT INTO TEST AND TRAIN
train_split = 0.8
valid_split = 0.1
total_sample = final_dataset.shape[0]
train_size = int(train_split * total_sample)
valid_size = int(valid_split * train_size)


# %%
# saving the predictions to csv
train_data=new_dataset[:train_size-valid_size]
test_data=new_dataset[train_size-valid_size:train_size]
valid_data=new_dataset[train_size:]


# %%

excel_file = 'data/model_performance.xlsx'

# Specify the columns you want to read
columns_to_read = ['MAE', 'MSE', 'RMSE', 'R2']

# Read the entire file, skipping the headers
data = pd.read_excel(excel_file, usecols=columns_to_read)

# Get the last row of the DataFrame
last_row = data.iloc[[-1]]

# Extract values from the last row and assign them to variables
mae = last_row['MAE'].values[0]
mse = last_row['MSE'].values[0]
rmse = last_row['RMSE'].values[0]
r2 = last_row['R2'].values[0]
