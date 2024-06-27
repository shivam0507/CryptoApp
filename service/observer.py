from abc import ABC, abstractmethod
from CryptoApp.model.Notification import Notification


class Observer(ABC):
    @abstractmethod
    def notify(self, notification: Notification):
        pass