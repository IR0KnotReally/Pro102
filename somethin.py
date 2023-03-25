import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "**Please take care of your stomach problems",
            message = "Time to go on a walk",
            timeout = 20
        )
        time.sleep(60*60)
