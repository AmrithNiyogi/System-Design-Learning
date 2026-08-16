**Scenario:** Build a notification delivery module for an e-commerce platform. The existing system sends only email order updates, but product now requires SMS and push notifications—with more channels expected later.

### Requirements
- Support `Email`, `SMS`, and `Push` notifications.
- Every channel must expose a common interface:
  - `send(recipient, message)`
  - `validateRecipient(recipient)`
- The core workflow must be shared:
  1. Validate recipient
  2. Render message from a template
  3. Send notification
  4. Record delivery result
- The workflow must **not** depend on `EmailNotification`, `SmsNotification`, or `PushNotification` directly.
- Adding `WhatsAppNotification` later should require new classes, not edits to existing delivery workflow logic.
- Invalid channels and invalid recipients must produce clear errors.
- Assume channel credentials/configuration are supplied at application startup.

### Your Task
Design the classes and interactions using the **Factory Method** pattern.

Include:
- A `Notification` product interface.
- Concrete products: `EmailNotification`, `SmsNotification`, `PushNotification`.
- A `NotificationService`/creator abstraction that owns the shared delivery workflow.
- Concrete creators whose factory methods select the correct notification product.
- Application bootstrap code that chooses the appropriate creator from configuration.

### Expected Outcome
Your design should allow this:

```text
EmailNotificationService.deliver(...)
SmsNotificationService.deliver(...)
PushNotificationService.deliver(...)
```

Each call runs the same workflow but uses a channel-specific notification implementation.

### Constraints
- Do not put a growing `switch(channel)` inside the delivery workflow.
- Do not make the client instantiate concrete notification products.
- Use inheritance only for choosing the product; keep the core workflow centralized.
- Keep the design open for a new channel without modifying existing creator/product classes.

### Discussion Prompts
1. Why is a simple `NotificationFactory.create(channel)` less aligned with Factory Method here?
2. Which class is the **Creator**, which are **Concrete Creators**, and what is the **Product**?
3. How would you support retries without duplicating retry logic in every notification channel?
4. At what point would several related channel-specific objects justify moving to **Abstract Factory**?