from datetime import datetime, timedelta
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
def now_iso():
    return datetime.now().isoformat()

def today():
    return datetime.now().date()
