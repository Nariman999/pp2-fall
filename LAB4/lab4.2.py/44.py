from datetime import datetime

date1 = datetime(2025, 10, 1, 12, 0, 0)
date2 = datetime(2025, 10, 7, 12, 0, 0)

diff_seconds = (date2 - date1).total_seconds()
print("Difference in seconds between date1 and date2:", diff_seconds)
