from abc import ABC, abstractmethod
from app.base_notification import Notification
from app.email_notification import EmailNotification
from app.sms_notification import SMSNotification
from app.push_notification import PushNotification

class NotificationService(ABC):

    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def deliver(self, recipient: str, template: str, context: dict) -> dict:
        notification = self.create_notification()
        notification.validateRecipient(recipient)
        message = template.format(**context)
        result = notification.send(recipient, message)
        return {
            "recipient": recipient,
            "message": message,
            "result": result
        }


class EmailNotificationService(NotificationService):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SmsNotificationService(NotificationService):
    def create_notification(self) -> Notification:
        return SMSNotification()


class PushNotificationService(NotificationService):
    def create_notification(self) -> Notification:
        return PushNotification()