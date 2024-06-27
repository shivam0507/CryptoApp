class NotificationStatus:
    NEW = "New"
    SENT = "Sent"
    OUTSTANDING = "PENDING"
    FAILED = "Failed"


class Notification:
    def __init__(self, id, content, status, scheduled_time):
        self.id = id
        self.content = content
        self.status = status
        self.scheduled_time = scheduled_time

    def __repr__(self):
        return f"Notification(id={self.id}, content={self.content}, status={self.status}, scheduled_time={self.scheduled_time})"
