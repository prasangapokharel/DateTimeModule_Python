from datetime import datetime
import pytz

zones = pytz.all_timezones
timezone = pytz.timezone('Africa/Tripoli')
current_time = datetime.now(timezone).time()

print(f'The time zone of Africa is {timezone} {current_time}')
