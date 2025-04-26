import matplotlib.pyplot as plt

'''question 1'''
# Years = [2018, 2019, 2020, 2021, 2022]
# Marks = [65, 70, 72, 78, 85]
# plt.title( "Student Marks Growth")
# plt.xlabel('Year')
# plt.ylabel('Marks')
# plt.plot(Years, Marks, linewidth=3,color='Red')
# plt.show()

'''question 2'''
# Years = [2016, 2017, 2018, 2019, 2020]
# Profit = [100, 120, 150, 180, 200]
# plt.title( " Company’s profit over time")
# plt.xlabel('Year')
# plt.ylabel('Profit')
# plt.plot(Years, Profit, linewidth=3,  color='Red', linestyle='--')
# plt.grid()
# plt.show()

'''question 3'''
# Months = [1, 2, 3, 4, 5, 6]
# City1_Temp = [30, 32, 35, 37, 40, 42]
# City2_Temp = [20, 22, 24, 27, 30, 33]
# plt.title("Temperature Comparison")
# plt.xlabel('Temp')
# plt.ylabel('Month')
# plt.legend(('City1_Temp', 'City2_Temp'))
# plt.plot(City1_Temp, Months, linewidth=3, color='Red')
# plt.plot(City2_Temp, Months, linewidth=3, color='yellow')
# plt.show()

'''question 4'''
# Days = [1, 2, 3, 4, 5, 6, 7]
# Distance = [2, 3, 5, 6, 5, 7, 8]
# plt.xlabel('Days')
# plt.ylabel('Distance')
# plt.plot(Days, Distance, linewidth=3, color='blue', marker='o')
# plt.show()

'''question5'''
# Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# Stock_Value = [100, 105, 102, 108, 110]
# plt.title("Stock Market Variation")
# plt.xlabel('Days')
# plt.ylabel('Stock_Value')
# plt.plot(Days, Stock_Value, linewidth=3,  color='blue', marker='o')
# plt.show()

''''question 6'''
# Months = [1, 2, 3, 4, 5, 6]
# Consumption = [300, 280, 290, 310, 320, 330]
# plt.title("consumption")
# plt.xlabel('Days')
# plt.ylabel('Stock_Value')
# plt.plot(Months, Consumption, linewidth=3, color='brown', marker='s')
# plt.grid()
# plt.show()

'''question 7'''
# Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# Sales = [200, 220, 250, 230, 240, 260]
# plt.title("Sales per month")
# plt.xlabel('Days')
# plt.ylabel('Sales')
# plt.plot(Months, Sales, linewidth=3, color='orange', marker='s')
# plt.xticks(rotation = 45)
# plt.grid()
# plt.show()

'''question 8'''
# Days = [1, 2, 3, 4, 5]
# Production = [400, 420, 450, 470, 500]
# plt.title("production")
# plt.xlabel('Days')
# plt.ylabel('Production')
# plt.plot(Days, Production, linewidth=3, color='teal', marker='o')
# plt.annotate("max value", xy=(5, 500), xytext=(4.3, 500))
# plt.grid()
# plt.show()

'''question 9'''
# x = range(-10, 11)
# y = x**2
# plt.title("Graph of y = x²")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.plot(x, y, linewidth=3, color='teal', marker='o')
# plt.annotate("max value", xy=(5, 500), xytext=(4.3, 500))
# plt.grid()
# plt.show()

'''practise sheet 2'''

'''question 1'''
# Days = [1, 2, 3, 4, 5]
# Height = [2, 3, 5, 7, 11]
# plt.xlabel("Days")
# plt.ylabel("Height")
# plt.plot(Days, Height, linewidth=3, color='teal')
# plt.show()

'''question 2'''
# Students =  [1, 2, 3, 4, 5]
# Marks = [88, 92, 75, 85, 90]
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.plot(Students, Marks, linewidth=3, color='teal', marker = 'o')
# plt.show()

'''question 3'''
# Months = ['Jan', 'Feb', 'Mar', 'Apr']
# Sales = [2500, 2700, 3000, 2800]
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.bar(Months, Sales, color= 'green')
# plt.show()

'''question 4'''
# Days = ['Mon', 'Tue','Wed', 'Thu', 'Fri']
# City_A = [22, 24, 19, 23, 25]
# City_B = [18, 20, 17, 21, 22]
# plt.xlabel("Days")
# plt.ylabel("Temp")
# plt.plot([1,2,3,4,5],City_A, marker = 'o')
# plt.plot([1,2,3,4,5],City_B, marker = 's')
# for i, c in enumerate(City_A,1):
#     plt.text(i, c, str(c))

# for i, c in enumerate(City_B,1):
#     plt.text(i, c, str(c))
# plt.legend(('City A', 'City B'))
# plt.show()

'''question 5'''
# Fruits = ['Apple', 'Banana', 'Cherry', 'Mango']
# Votes = [40, 25, 20, 15]
# plt.pie(Votes, labels= Fruits)
# plt.show()

'''question 6'''
# Ages = [22, 25, 30, 22, 29, 40, 35, 25, 28, 30, 32, 40, 22]
# plt.hist(Ages, bins=5, edgecolor = 'black', color='lightblue')
# plt.xlabel('Age')
# plt.ylabel('Number of People')
# plt.show()

'''question 7'''
# Students = [1, 2, 3, 4, 5]
# Attendance = [90, 85, 80, 95, 70]
# Marks = [88, 75, 70, 95, 60]
# plt.subplot(1,2,1)
# plt.bar(Students, Attendance, color='green')
# plt.subplot(1,2,2)
# plt.bar(Students, Marks, color='red')
# plt.show()

'''question 8'''
# days = [1, 2, 3, 4, 5, 6, 7]
# high = [30, 32, 33, 35, 36, 34, 33]
# low = [20, 21, 19, 22, 23, 21, 20]
# plt.plot(days, high, label='High Temp', color='red')
# plt.plot(days, low, label='Low Temp', color='blue')
# plt.fill_between(days, low, high, color='lightgrey', alpha=0.4)
# plt.grid()
# plt.show()

'''question 9'''
