import matplotlib.pyplot as plt

# Данни за токените и техните проценти
labels = ['XLM', 'HBAR', 'SUI', 'ATOM', 'ALGO', 'STX', 'UNI', 'CAKE', 'SBET', 'LINK']
sizes = [15, 15, 15, 10, 10, 10, 5, 5, 5, 10]  # Проценти
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC', '#CC99FF', '#FFFF99', '#99FFCC', '#FFCCCC', '#CCFF99']  # Различни цветове
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # Няма отделяне на сегментите (може да се промени за ефект)

# Създаване на кръгова диаграма
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # За да е кръгла диаграмата
plt.title('Разпределение на токените')
plt.show()