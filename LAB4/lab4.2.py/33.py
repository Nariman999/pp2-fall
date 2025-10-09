from datetime import datetime

today = datetime.now()
no_microseconds = today.replace(microsecond=0)
print("Datetime without microseconds:", no_microseconds)
