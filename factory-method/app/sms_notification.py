from app.base_notification import Notification

class SMSNotification(Notification):

    def send(self, recipient: str, message: str) -> str:
        return f"Sending SMS notification: {message} to {recipient}"

    def validateRecipient(self, recipient: str) -> bool:
        number = recipient[1:] if recipient.startswith("+") else recipient
        if not number.isdigit() or not (8 <= len(number) <= 15):
            raise ValueError(f"Invalid phone number: {recipient}")

        return True