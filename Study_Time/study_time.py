import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Study Time",
            message = "Study hard to achieve your future goals.",
            app_icon = "Study.ico",
            timeout = 12
            )
        time.sleep(60*60)
