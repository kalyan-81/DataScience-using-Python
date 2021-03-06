# -*- coding: utf-8 -*-
"""data science part-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17p-EbATQ3MC_nRYDtlZwf8bLq5cZWkR1

# Data visualization

* visualization is showing the data in the form of pictures.
* it becomes easy for the user to understand it.
# representing the data in the form of pictures or graphs is called  'data visualization'.

for this purpose we have to install matplotlib module. we can use pyplot submodule of the matplotlib module.
"""

pip install matplotlib

import matplotlib.pyplot as plt
import pandas as pd

dfm=pd.read_csv('E:\\my youtube channel\\master python\\first page\\students.csv')
dfm

"""# Bar Graph
* Bar graph represents the data in the form of vertical or horizontal bars.
* it is useful to compare the quantities.
"""

x=dfm['name'][0:5] #defining x- axis data
y=dfm["maths"][0:5]    #defining y- axis data

plt.bar(x,y,label='maths',color='red')

#set x and y axis labels
plt.xlabel('names')
plt.ylabel('marks')

#set title 
plt.title('NITK college')

#show legend
plt.legend()
plt.show()

# Bar graphs for multiple data
x=dfm['name'][0:5] #defining x- axis data
y=dfm["maths"][0:5]    #defining y- axis data

y1=dfm['physics'][0:5]

plt.bar(x,y,label='maths',color='red')
plt.bar(x,y1,width=0.3,label='physics',color='green')

#set x and y axis labels
plt.xlabel('names')
plt.ylabel('marks')

#set title 
plt.title('NITK college')

#show legend
plt.legend()
plt.show()

"""# histogram plot

histogram shows distribution of values. historgram is similar to bar graph but it is useful to show values grouped in bins or intervals.

example we can collect the chemistry marks of each student and show it in the form of histogram to know how many students are there in the range of 40-70 marks,0-10 marks..etc. for this purpose we have to take bins as range of marks.
"""

bins=[40,70]
chem=dfm['chemistry']
plt.hist(chem,bins,histtype='bar',label='chemistry',rwidth=0.5,color='cyan')
plt.ylabel('no of students')
plt.xlabel('range of marks')
plt.title('NITK')
plt.legend()
plt.show()

"""the bins lis contains 0,10,20,....This indicates the ranges from 0 to 9, 10 to 19, 20 to 29, etc.,"""

bins=[0,10,20,30,40,50,60,70,80,90,100]
chem=dfm['chemistry']
plt.hist(chem,bins,histtype='bar',label='chemistry',rwidth=0.8,color='cyan')#histtype='bar' or 'barstacked' or 'step' or 'stepfilled'
plt.ylabel('no of students')
plt.xlabel('range of marks')
plt.title('NITK')
plt.legend()
plt.show()

"""# the option rwidth=0.8 indicates that the bar's width is 80%. there will be a gap of 10% space before and after the bar.

# pie chart

A pie chart shows a circle that is divided into sectors and each sector represents a proportion of the whole.
"""

slices=[50,20,30]#percentage of students
subjects=['maths','physics','chemistry']# takes the subject names
cols=['magenta','cyan','brown','gold'] #takes the colors for each subject

#create a pie chart
plt.pie(slices,labels=subjects,colors=cols,startangle=90,explode=(0,0.2,0),shadow=True,autopct='%.1f%%')

#set titles and legend
plt.title('NITK')
#show the pie chart
plt.show()

"""startangle=90 indicates that the pie chart will start at 90 degrees(12 o'clock position). if this option is not mentioned, then
starts by default at 0 degrees( 3 o'clock position)

the option explode(0,0.20,0) indicates whether the slices in the pie chart should stand out or not. here, 0 indicates that the corresponding slide will not come out slightly. its value 0.1 to 1 indicates how much it should come out of chart.

the option shadow = True indicates that the pie chart should be displayed with a shadow. this will improve the look of the chart.

the option autopct='%.1f%%' indicates how to display the percentages on the slices. here %.1 indicates that the percentage value should be displayed with a 1 digit after decimal point. the next two % symbols indicate that only one symbol is to be displayed.
"""





"""# Line Graph

A line graph is a simple graph that shows the results in the  form of lines. To create a line graph we need x and y coordinates. Here the plot() function creates teh line graph.
"""

x=[1,2,3,4,5,6,7,8]
y=[40,20,50,60,90,54,23,67]
plt.plot(x,y,'blue',label='chemistry')

plt.xlabel='Roll no'
plt.ylabel='marks'
plt.title('line graph')
plt.legend()
plt.show()

"""# points to remember
* A data  warehouse is a central repository of integrated data from different sources.
* Data analysis or data analytics involves the data to be analyzed to answer the questions raised by the management of the organization.
* Data visualization is to communicate information clearly and efficiently using statistical graphs,plot and diagrams.
* Data science is a term used for techniques to extract information from the data warehouse, analyze them and present the necessary data to the business.
* Data frame is an object in the pandas module that is useful to represent data in the form of rows and columns.
* Data frames are generally created form .csv(comma-separated values) files, Excel spreadsheet files, Python dictionaries, list of tuples or list of dictionaries.
* once the data frame is created, we can retrieve data from the data frame and perform various operations on it.
* the matplotlib.pyplot package is the module used in data visualization.
* the bar() function is useful to create bar graphs
* the hist() function is useful to create histograms
* the pie() function is useful to create pie charts
* the plot() function is useful to creae line graphs.
"""











