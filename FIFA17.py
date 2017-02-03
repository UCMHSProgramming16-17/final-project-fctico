import csv 
import pandas as pd

#creates a list called player_stats
player_stats = []

#opens the csv file, and read it
ifile = open ('FIFA17final.csv')
read = csv.reader(ifile)

#prints the player stats only
for row in read:
    (row)
    player_stats.append(row[3])
    
print(player_stats)
  
#makes the datafranme
df = pd.DataFrame({
    'Ability': player_stats
})


#import bar chart commands
from bokeh.charts import Bar, output_file, save

#Create and format the chart that will be in FIFA17.html
Barchart = Bar(df, 'Ability', values = 'Ability', agg = 'count', title = 'Number of Players with Overalls from 85-95', legend = False, ylabel = 'Number of Players')

#make the file the chart will be in FIFA.html
output_file('FIFA17.html')
save(Barchart)
