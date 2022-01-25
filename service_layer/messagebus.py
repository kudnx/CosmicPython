from adapters import email
from domain import events


def handle(event: events.Event):
    for handler in HANDLERS[type(event)]:
        handler(event)


def send_out_of_stock_notification(event: events.OutOfStock):
    email.send_mail(
        "zluan009@gmail.com",
        f"Out of Stock for {event.sku}"
    )


HANDLERS = {
    events.OutOfStock: [send_out_of_stock_notification],
}
