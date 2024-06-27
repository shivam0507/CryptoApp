from CryptoApp.model.Notification import Notification
from CryptoApp.model.NotificationStatus import NotificationStatus as Status
from observer import Observer
from CryptoApp.model.user import User


class EmailNotification(Observer):

    def __int__(self):
        self.users = []
        self.sent_notification = []
        self.failed_notification = []

    def subscribe_to_email_notification(self, user: User):
        self.users.append(user)

    def notify(self, notification: Notification):
        for user in self.users:
            try:
                user.add_notification_to_queue(notification)
                self.sent_notification.append(notification)
            except:
                notification.update_status(Status.get_failed_status())
                self.failed_notification.append(notification)

