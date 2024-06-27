class InMemoryNotificationRepository:
    def __init__(self):
        self.notifications = []

    def save(self, notification):
        self.notifications.append(notification)

    def update(self, notification):
        for i, n in enumerate(self.notifications):
            if n.id == notification.id:
                self.notifications[i] = notification
                break

    def find_by_status(self, status):
        return [n for n in self.notifications if n.status == status]

    def delete(self, notification_id):
        self.notifications = [n for n in self.notifications if n.id != notification_id]
