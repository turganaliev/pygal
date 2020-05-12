import pygal
from choose import Choose

#Создание двух кубиков D6
choose_1 = Choose()
choose_2 = Choose()

#Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):
    result = choose_1.roll() + choose_2.roll()
    results.append(result)

#Анализ результатов
frequencies = []
max_result = choose_1.num_sides + choose_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Визуализация результатов
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
