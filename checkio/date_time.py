import calendar
def date_time(time: str) -> str:
    month = calendar.month_name
    print(int(time[11:13]))
    h = 'hour' if int(time[11:13]) == 1 else 'hours'
    m = 'minute' if int(time[14:16]) == 1 else 'minutes'


    return time[0:2].lstrip('0') + ' ' + month[int(time[3:5])] + ' ' + time[6:10] + ' year ' + time[11:12].lstrip('0') + time[12:13] + ' ' + h + ' ' + time[14:15].lstrip('0') + time[15:16] + ' ' + m

# THE BEST SOLUTION
# from datetime import datetime


# def checkio(time):
#     dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
#     hour = 'hour' if dt.hour == 1 else 'hours'
#     minute = 'minute' if dt.minute == 1 else 'minutes'
#     return dt.strftime(f'%-d %B %Y year %-H {hour} %-M {minute}')


if __name__ == '__main__':
    print("Example:")
    print(date_time('20.01.2000 01:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
