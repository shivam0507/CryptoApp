class NotificationStatus:
    def __int__(self):
        self._new = 'New'
        self._sent = 'Success'
        self._outstanding = 'Scheduled'
        self._failed = 'Failed'
        self._read = 'Read'

    @staticmethod
    def get_new_status(self):
        return self._new

    @staticmethod
    def get_sent_success_status(self):
        return self._sent

    @staticmethod
    def get_scheduled_status(self):
        return self._outstanding

    @staticmethod
    def get_failed_status(self):
        return self._failed

    @staticmethod
    def get_read_status(self):
        return self._read
