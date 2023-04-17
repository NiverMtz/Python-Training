def alarm(item):
    match item:
        case ['evening', action]:
            print(f'You almost finished the day! Now {action}!')
        case [time, action]:
            print(f'Good {time}! It is time to {action}!')
        case _:
            print('The time is invalid.')


alarm(['evening', 'play video games'])

alarm(['work'])
