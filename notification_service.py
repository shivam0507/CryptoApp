from subject import Subject
from observer import Observer
from notification import NotificationStatus
from typing import List

class NotificationService(Subject):
    def __init__(self, notification_repository, email_service, crypto_data_service):
        self.notification_repository = notification_repository
        self.email_service = email_service
        self.crypto_data_service = crypto_data_service
        self.observers: List[Observer] = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, notification):
        for observer in self.observers:
            observer.update(notification)

    def create_notification(self, notification):
        notification.status = NotificationStatus.OUTSTANDING
        self.notification_repository.save(notification)
        self.notify(notification)

    def send_notification(self, notification):
        try:
            content = self.generate_notification_content()
            self.email_service.send_email(notification.email_list, content)
            notification.status = NotificationStatus.SENT
        except Exception as e:
            notification.status = NotificationStatus.FAILED
        finally:
            self.notification_repository.update(notification)
            self.notify(notification)

    def get_notifications_by_status(self, status):
        return self.notification_repository.find_by_status(status)

    def delete_notification(self, notification_id):
        self.notification_repository.delete(notification_id)
        self.notify(None)

    def generate_notification_content(self):
        data = self.crypto_data_service.get_crypto_data()
        return f"BTC Price: {data['price']}, Volume: {data['volume']}, High: {data['high']}, Market Cap: {data['market_cap']}"
