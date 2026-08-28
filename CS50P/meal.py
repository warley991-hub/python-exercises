# breakfast = 7:00 - 8:00
# lunch = 12:00 - 13:00
# dinner = 18:00 - 19:00

breakfast_hours = [7,8]
lunch_hours = [12,13]
dinner_hours = [18,19]


'''
Criar uma função que receba o texto (STRING) pura de horas, exemplo:
"07:30" e devolta o valor de FLOAT desse horário, exemplo "7.5"
'''

def main():
    time_str = input('What time is it?')
    hours = convert(time_str)

    if 7.0 <= hours <= 8.0:
        print('breakfast time')
    elif 12.0 <= hours <= 13.0:
        print('lunch time')
    elif 18.0 <= hours <= 19.0:
        print('dinner time')

def convert(time):
    time = time.split(':')
    time = [float(x) for x in time]

    hours = time[0]
    minutes = time[1]/60

    return hours+minutes

if __name__ == "__main__":
    main()
