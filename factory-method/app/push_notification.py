from app.base_notification import Notification

class PushNotification(Notification):

    def send(self, recipient: str, message: str) -> str:
        return f"Sending push notification: {message} to {recipient}"

    def validateRecipient(self, recipient: str) -> bool:
        if not recipient.strip():
            raise ValueError(f"Invalid push notification recipient: {recipient}")
            
        return True