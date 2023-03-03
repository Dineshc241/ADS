import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
earthquakes= pd.read_csv('earthquake_data.csv')
earthquakes['date_time']=pd.to_datetime(earthquakes['date_time'])
earthquakes.info()

earthquakes.set_index('date_time',inplace=True)

# Visualization 1
def average_magnitude(earthquakes):
    '''
    The funtion is used to plot the average magnitude of the earthquakes in each year with 
    - lower magnitude less than 7
    - medium magnitude more than 7 and less than 8 
    - Higher magnitude more than 8
    The function takes input as earthquakes data and the calculates the various magnitudes and there averages each year 
    and then plots them in the line graph.
    
    '''
    #slicing the data into required magnitudes
    x= earthquakes[earthquakes['magnitude']<7]
    y= earthquakes[(earthquakes['magnitude']>7) & (earthquakes['magnitude']<8) ]
    z= earthquakes[(earthquakes['magnitude']>8)]
    plt.figure(figsize=(10,5))
    
    #plotting the line plots and using groupby and mean() to find the average on each year in each types of magnitude.
    plt.plot(x['magnitude'].groupby(x.index.year).mean(),label='Magnitude <7')
    plt.plot(y['magnitude'].groupby(y.index.year).mean(),label='Magnitude >7 and <8')
    plt.plot(z['magnitude'].groupby(z.index.year).mean(),label= 'Magnitude >8')
    plt.legend()
    plt.title("Average magnitude of earthquakes each year.")
    plt.xlabel('Year')
    plt.ylabel('Magnitude of earthquakes')
    plt.show()

average_magnitude(earthquakes)


# Visualization 2
new_data = earthquakes[earthquakes.index.year >2013]
green = new_data[new_data['alert']=='green']
yellow = new_data[new_data['alert']=='yellow']
green = green['alert'].groupby(green.index.year).count()
yellow = yellow['alert'].groupby(yellow.index.year).count()

def alerts(green,yellow):
    '''
    This function takes the input of two alerts yellow and green and plots the count of each alert in each year.
    Input: Green, yellow.
    output: Bar graph.
    '''
    n=9
    r = np.arange(n)
    width = 0.25
    plt.bar(r, green, color = 'green',
            width = width,
            label='green alerts')
    plt.bar(r + width, yellow, color = 'yellow',
            width = width,
            label='yellow alerts')
    plt.xlabel("Year")
    plt.ylabel("Count of alerts")
    plt.title("Count of each type of alerts")
    plt.xticks(r + width/2,green.index,rotation=90)
    plt.legend()
    plt.show()
alerts(green,yellow)


# Visualization 3
def pie_continent(data):
    '''
    The function takes earthquake data as input and produces a pie chart with percentage of earthquakes which have occured in 
    each continent from 2000 to 2022.
    Input: Earthquake data
    Ouput: pie chart.
    '''
    continent = data['continent'].groupby(data.continent).count()
    plt.pie(continent,labels=continent.index,autopct='%1.1f%%',startangle=70)
    plt.title("Percentage of earthquakes in each coutinent form 2000 to 2022")
    plt.show()
pie_continent(earthquakes)