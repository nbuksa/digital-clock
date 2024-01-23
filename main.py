from datetime import datetime as dt
from dateutil import tz
import time
import os
import locale


def digital_clock(custom_locale='hr-HR', 
                  time_zone='Europe/Zagreb') -> str:
    """Function returns current time in predefined locale and time zone

    Args:
        custom_locale (str, optional): locale in which will be desplayed the name of the day in a week. Defaults to 'hr-HR'.
        time_zone (str, optional): time zone in which will be displayed time. Defaults to 'Europe/Zagreb'.

    Returns:
        str: Returns constructed string from datetime object in format: week_day, day.month.year hour:minutes:seconds
    """
    locale.setlocale(locale.LC_TIME, locale=custom_locale)
    custom_tz = tz.gettz(time_zone)
    current_datetime = dt.now().astimezone(custom_tz)
    return f'{current_datetime.strftime('%A').capitalize()}, {current_datetime.strftime('%d.%m.%Y. %H:%M:%S')}'
        
#u funkciji ne printamo jer mozemo funkciju ispisati na više mjesta, 
    #ali  ako je unutar funkcije print
    #onda smo definirali da se uvijek ispisuje u konzolu
    #ako funkcija vraća nešto to možemo ispisati i u bazi...

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(digital_clock())
    time.sleep(1)