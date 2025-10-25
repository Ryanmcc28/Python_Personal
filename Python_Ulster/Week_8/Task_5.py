import matplotlib.pyplot as plt

costs_file = open('expenses', 'r')

labels = []
values = []

for expense in costs_file:
    temp1, temp2 = expense.split()
    labels.append(temp1)
    values.append(temp2)


plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

plt.axis('equal')

plt.title('Pie Chart Example')

plt.show()