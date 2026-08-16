import argparse

from app.factory import (
    EmailNotificationService,
    SmsNotificationService,
    PushNotificationService,
)

SERVICES = {
    "email": EmailNotificationService,
    "sms": SmsNotificationService,
    "push": PushNotificationService,
}

DEFAULT_RECIPIENTS = {
    "email": "test@example.com",
    "sms": "+15551234567",
    "push": "device-token-abc123",
}

EPILOG = """
Examples:
  Send an email notification:
    python main.py --channel email
  Send an SMS notification:
    python main.py --channel sms
  Send a push notification:
    python main.py --channel push
"""

def parse_args():
    parser = argparse.ArgumentParser(
        description="Send a notification via email, SMS, or push.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EPILOG,
    )
    parser.add_argument(
        "--channel",
        default="email",
        help="Notification channel: email, sms, or push (default: email)",
    )
    parser.add_argument(
        "--recipient",
        default=None,
        help="Recipient for the channel. Defaults to a sample email, phone, or device token.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    channel = args.channel
    if channel not in SERVICES:
        raise ValueError(f"Invalid channel: {channel}")

    recipient = args.recipient or DEFAULT_RECIPIENTS[channel]
    service = SERVICES[channel]()
    result = service.deliver(
        recipient=recipient,
        template="Hello, {name}!",
        context={"name": "John"},
    )
    print(result)


if __name__ == "__main__":
    main()
