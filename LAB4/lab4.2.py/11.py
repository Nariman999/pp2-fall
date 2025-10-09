from datetime import datetime, timedelta

today = datetime.now()
five_days_ago = today - timedelta(days=5)
print("5 days ago:", five_days_ago)
