from pydantic import ValidationError

from app.schemas import TicketCreate, TicketStatus

ticket = TicketCreate(
    subject="Не работает вход",
    description="Ошибка при входе в приложение",
    customer_email="client@example.com",
)
print(ticket)
print(ticket.model_dump())

try:
    TicketCreate(subject="ab", description="", customer_email="client@example.com")
except ValidationError as error:
    print(error)

print(TicketStatus("new"))
