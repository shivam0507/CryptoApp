from notification import Notification, NotificationStatus
from notification_service import NotificationService
from observers import LoggingObserver
from repositories import InMemoryNotificationRepository
from services import SmtpEmailService, ApiCryptoDataService
import datetime

if __name__ == "__main__":
    notification_repository = InMemoryNotificationRepository()
    email_service = SmtpEmailService()
    crypto_data_service = ApiCryptoDataService()

    notification_service = NotificationService(notification_repository, email_service, crypto_data_service)

    # Attach observers
    logging_observer = LoggingObserver(notification_service)
    notification_service.attach(logging_observer)

    # Create a notification
    notification = Notification("1", "Sample Notification", NotificationStatus.NEW, datetime.datetime.now())
    notification_service.create_notification(notification)

    # Send the notification
    notification_service.send_notification(notification)

    # Delete the notification
    notification_service.delete_notification(notification.id)
