from choose import Choose

import pygal

choose_1 = Choose()
choose_2 = Choose(10)

results = []
for roll_num in range(50000):
    result = choose_1.roll() + choose_2.roll()
    results.append(result)

frequencies = []
max_result = choose_1.num_sides + choose_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
    '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice.svg')
