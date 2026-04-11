import time
from datetime import datetime

# on get la date avec grace a time.
seconds = time.time()


date = datetime.now().strftime("%b %d %Y")

#print(f""")
print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
print(date)
