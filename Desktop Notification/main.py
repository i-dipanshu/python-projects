from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Drink Water",
            message="Please drink water",
            # app_icon=""
            timeout=5
        )
        time.sleep(5)