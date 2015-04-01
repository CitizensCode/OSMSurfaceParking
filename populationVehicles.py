from pandas import DataFrame, Series
import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *

# Locate the cansim data
adultPopulation = "./Data/NBAdultPopulationCansim.csv"
vehicleRegistrations = "./Data/NBVehicleRegistrationsCansim.csv"


# Read in the population data
pop_df = pd.read_csv(adultPopulation)
pop_df = pop_df.drop(['GEO', 'SEX', 'AGE'], axis=1).set_index('Ref_Date')
pop_df.columns = ['New Brunswick Population 18+']
pop_df

# Read in the registration data
reg_df = pd.read_csv(vehicleRegistrations)
reg_df = reg_df.drop(['REGION', 'TYPE'], axis=1).set_index('Ref_Date')
reg_df.columns = ['Vehicles Registered in NB < 4500kg']
reg_df

# Merge them both together
merged = pd.merge(reg_df, pop_df, left_index=True, right_index=True)
merged

# Calculate the number of vehicles per adult
vehic_per_adult = merged.ix[:,0] / merged.ix[:,1]
vehic_per_adult

# Makes it possible to plot a pandas DataFrame in plotly
def df_to_plotly(df):
    
    '''
    Coverting a Pandas Data Frame to Plotly interface
    '''
    x = df.index.values
    lines={}
    for key in df:
        lines[key]={}
        lines[key]["x"]=x
        lines[key]["y"]=df[key].values
        lines[key]["name"]=key

    #Appending all lines
    lines_plotly=[lines[key] for key in df]
    return lines_plotly

# Convert the data using the above function
plotly_data = df_to_plotly(merged)

# Plot it
py.plot(plotly_data)
