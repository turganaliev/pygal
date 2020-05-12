import pygal
from choose import Choose

#Бросок кубика
choose = Choose()
results = []
for roll_num in range(1000):
    result = choose.roll()
    results.append(result)
#print(results)

#Анализ результатов
frequencies = []
for value in range(1, choose.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

#Построение гистограммы
hist = pygal.Bar()
hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6', frequencies)
hist.render_to_file('choose_visual.svg')
