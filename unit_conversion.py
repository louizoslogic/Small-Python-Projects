def convert_units(distance,starting_unit,ending_unit):

    comparison = {
        'm' : 1,
        'km' : 1000,
        'ft' : 0.3048,
        'mi' : 1609.34,
        'in' : 0.0254,
        'yd' : 0.9144
        }

    conversion = distance * comparison[starting_unit]

    converted_distance = conversion / comparison[ending_unit]

    return converted_distance

distance = float(input('how long is your measurement? '))

starting_unit = input('what unit is it in? ')

ending_unit = input('what unit do you want it in? ')

converted_distance = convert_units(distance,starting_unit,ending_unit)

print(converted_distance)