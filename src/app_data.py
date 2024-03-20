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


# %% [markdown]
# DATA CLEANING AND SCALING

# %%
# dataset reading
df_nse = pd.read_csv("data/TATACONSUM.NS_historical_data.csv")
df = pd.read_csv("data/stock_data.csv")
df_pred = pd.read_csv("data/lstm_predictions.csv")

# %%
# index formatting
df_nse["Date"]=pd.to_datetime(df_nse.Date,format="%Y-%m-%d")
df_nse.index=df_nse['Date']
df_nse = df_nse.sort_index(ascending=False, axis=0)
df_nse = df_nse.drop('Date', axis=1)

df_pred["Date"]=pd.to_datetime(df_pred.Date,format="%Y-%m-%d")
df_pred.index = df_pred['Date']
df_pred = df_pred.sort_index(ascending=False, axis=0)
df_pred = df_pred.drop('Date', axis=1)


recent_data = df_pred.head(4)

recent_data['Close'] = pd.to_numeric(recent_data['Close'], errors='coerce')
recent_data['Predictions'] = pd.to_numeric(recent_data['Predictions'], errors='coerce')

recent_data.loc[:, 'Close'] = recent_data['Close'].apply(lambda x: round(x,2))
recent_data.loc[:, 'Predictions'] = recent_data['Predictions'].apply(lambda x: round(x,2))

recent_data['Percentage Change'] = ((recent_data['Predictions'] - recent_data['Close']) / recent_data['Close']) * 100
recent_data['Percentage Change'] = recent_data['Percentage Change'].apply(lambda x: round(x,2))
recent_data['Date'] = recent_data.index

# %%
regression_metrics = {
    'MAE': mae,
    'MSE': mse,
    'RMSE': rmse,
    'R2': r2
}