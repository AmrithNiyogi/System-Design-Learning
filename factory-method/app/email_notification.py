from app.base_notification import Notification

class EmailNotification(Notification):

    def send(self, recipient: str, message: str) -> str:
        return f"Sending email notification: {message} to {recipient}"

    def validateRecipient(self, recipient: str) -> bool:
        if "@" not in recipient:
            raise ValueError(f"Invalid email address: {recipient}")

        local, _, domain = recipient.partition("@")
        if not local or not domain or "." not in domain:
            raise ValueError(f"Invalid email address: {recipient}")

        return True