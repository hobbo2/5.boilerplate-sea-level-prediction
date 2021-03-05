import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
   
    # Create first line of best fit
   
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # assign names to linregress values
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    #extend the rand or x-axis to 2049
    #use lists because does not specify use of numpy array
    x2 = list(range(1880,2050))
    # y = mx + c 
    y2 = []
    for year in x2:
        y2.append(intercept + slope*year)
    plt.plot(x2, y2, color = 'r', label = 'line of best fit') 
    
    # Create second line of best fit
    # Create new x and y series for years afte 1999
    x_new = df[df['Year']>=2000]['Year']
    y_new = df[df['Year']>=2000]['CSIRO Adjusted Sea Level']

    # assign regression values to variables
    new_reg = linregress(x_new, y_new)
    new_slope = new_reg.slope
    new_intercept = new_reg.intercept

    x3 = list(range(2000,2050))
    y3 = []
    for year in x3:
        y3.append(new_intercept + new_slope*year)
    plt.plot(x3,y3, color = 'y', label = 'Regression after 1999')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()