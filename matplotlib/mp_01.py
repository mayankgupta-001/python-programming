import matplotlib.pyplot as plt

marks1 = [12,13,15,11,14]
marks2 = [13,12,14,11,14]

# for i, marks in enumerate(marks, 1):
#     print(i, marks)

plt.plot([1,2,3,4,5],marks1)
plt.plot([1,2,3,4,5],marks2)
plt.title('Marks')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.grid()

for i, mark in enumerate(marks1,1):
    plt.text(i, mark, str(mark))

for i, mark in enumerate(marks2,1):
    plt.text(i, mark, str(mark))

plt.axhline(y = 10.5, color = 'red')
plt.legend(('a1', 'a2'))
plt.xticks(range(1,6), ['English', 'Maths', 'CP', 'DB', 'AI'])
plt.show()