import csv
import matplotlib.pyplot as plt
import numpy as np

dateTime = []
wattsPerTime = []
with open('June2017.csv', 'r') as fil:
    data = csv.DictReader(fil, delimiter=',')
    print(data)
    for row in data:
        day = row['date']
        dateTime.append(day)
        watts = float(row['watts'])
        wattsPerTime.append(watts)
        print("On {} we generated {:.3f} KWHs".format(day, watts/1000))
print(dateTime)
print(wattsPerTime)

fig, ax = plt.subplots()
ax.plot(dateTime, wattsPerTime)

ax.set(xlabel ='dates/times', ylabel='Watts', title='Watts Per Time from Solar Panel')
ax.grid()

plt.show()