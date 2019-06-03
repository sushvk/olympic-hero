# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file

data  = pd.read_csv(path)

data.rename(columns = {'Total':'Total_Medals'},inplace = True)

print(data.head())

#Code starts here



# --------------
#Code starts here

#Creating new column 'Better_Event'
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'] , 'Both', data['Better_Event'])

#Finding the value with max count in 'Better_Event' column
better_event=data['Better_Event'].value_counts().index.values[0]

#Printing the better event
print('Better_Event=', better_event)

    
#Code ends here    


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries[:-1]
#print(top_countries.tail())

def top_ten(data,column_name):
    #country_list =[]
    top_country_data_frame = data.nlargest(10, column_name)
    top_country_list = list(top_country_data_frame['Country_Name'])
    return top_country_list

top_10_winter = top_ten(top_countries,'Total_Winter')
print("Top 10 winter countries:\n",top_10_winter)

top_10_summer = top_ten(top_countries,'Total_Summer')
print("Top 10 Summer countries:\n",top_10_summer)


top_10 = top_ten(top_countries,'Total_Medals')
print("Top 10 countries:\n",top_10)

common = list(set(top_10_winter) & set(top_10_summer) & set(top_10))
print('common coutries :\n',common)



# --------------
#Code starts here

#top_winter_coutries  
winter_mask =data['Country_Name'].isin(top_10_winter)
winter_df =data[winter_mask]
winter_df.plot(kind ='barh',x='Country_Name',y='Total_Winter',sort_columns=True)

#top_summer_coutries  
summer_mask =data['Country_Name'].isin(top_10_summer)
summer_df= data[summer_mask]
summer_df.plot(kind ='barh',x='Country_Name',y='Total_Summer',sort_columns=True)
#print(summer_df)


top_10 
top_10_mask = data['Country_Name'].isin(top_10)
top_df =data[top_10_mask]
top_df.plot(kind ='barh',x ='Country_Name',y ='Total_Medals',sort_columns =True)















# --------------
#Code starts here


winter_df['Golden_Ratio'] =winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold  = winter_df.loc[winter_df['Golden_Ratio'].idxmax()]['Country_Name']
print(winter_country_gold)
print(winter_max_ratio)


summer_df['Golden_Ratio'] =summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold  = summer_df.loc[summer_df['Golden_Ratio'].idxmax()]['Country_Name']
print(summer_country_gold)
print(summer_max_ratio)

top_df['Golden_Ratio'] =  top_df['Gold_Total'] /top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold  = top_df.loc[top_df['Golden_Ratio'].idxmax()]['Country_Name']
print(top_country_gold)
print(top_max_ratio)


# --------------
#Code starts here


#Removing the last column of the dataframe
data_1=data[:-1]

#Creating a new column 'Total_Points'
data_1['Total_Points']= data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1  # Use of position index to handle the ambiguity of having same name columns


#Finding the maximum value of 'Total_Points' column
most_points=max(data_1['Total_Points'])

#Finding the country assosciated with the max value of 'Total_Column' column
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print('The maximum points achieved is ', most_points, ' by ', best_country )

#Code ends here


# --------------
#Code starts here

#Subsetting the dataframe
best=data[data['Country_Name']==best_country]
best.reset_index(drop = True, inplace = True)
best=best[['Gold_Total','Silver_Total','Bronze_Total']]


#Plotting bar plot
best.plot.bar(stacked=True)

#Changing the x-axis label
plt.xlabel('United States')

#Changing the y-axis label
plt.ylabel('Medals Tally')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

#Updating the graph legend
l=plt.legend()
l.get_texts()[0].set_text('Gold_Total :' + str(best['Gold_Total'].values))
l.get_texts()[1].set_text('Silver_Total :' + str(best['Silver_Total'].values))
l.get_texts()[2].set_text('Bronze_Total :' + str(best['Bronze_Total'].values))



#Code ends here


