from NotificationStatus import NotificationStatus as Status
import Notification

class User:
    def __int__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.new_notification_queue = []
        self.read_notification_queue = []

    def add_notification_to_queue(self, notification: Notification):
        notification.update_status(Status.get_sent_success_status())
        self.new_notification_queue.append(notification)

    def read_notification(self, notification: Notification):
        self.new_notification_queue.remove(notification)
        notification.update_status(Status.get_read_status())
        self.read_notification_queue.append(notification)
