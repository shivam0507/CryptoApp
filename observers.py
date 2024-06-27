from observer import Observer
from notification_service import NotificationService

class LoggingObserver(Observer):
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def update(self, notification):
        if notification:
            content = self.notification_service.generate_notification_content()
            print(f"LoggingObserver: Notification updated: {notification}, Content: {content}")
        else:
            print("LoggingObserver: Notification deleted")
