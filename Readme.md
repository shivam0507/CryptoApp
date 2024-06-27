# Crypto Notification App

We would like you to create a crypto notification app. The features it should include:

Create a server which will be able to take in the following rest APIs

Create a notification. Line items may include current price of BTC, market trade volume, intra day high price, market cap
Send a notification to an email List sent notifications (sent, outstanding, failed etc.)
Sent -> Success
Outstanding -> Scheduled/Pending
Failed -> Failed
Delete a notification

## Project Structure

- `subject.py`: Defines the `Subject` interface.
- `observer.py`: Defines the `Observer` interface.
- `notification.py`: Contains the `Notification` and `NotificationStatus` classes.
- `notification_service.py`: Implements the `NotificationService` class.
- `observers.py`: Implements the concrete observer classes (`LoggingObserver` and `AnalyticsObserver`).
- `repositories.py`: Contains the `InMemoryNotificationRepository` class.
- `services.py`: Contains the `SmtpEmailService` and `ApiCryptoDataService` classes.
- `main.py`: The main application demonstrating the usage of the observer pattern.


### Example Flow

1. **Notification Creation**:
   - A notification is created and marked as `NEW`.
   - Observers are notified of the creation.

2. **Notification Sending**:
   - The notification content is generated using crypto data.
   - An email is sent to the specified email list.
   - The notification status is updated to `SENT` or `FAILED`.
   - Observers are notified of the status update.

3. **Notification Deletion**:
   - The notification is deleted from the repository.
   - Observers are notified of the deletion.
