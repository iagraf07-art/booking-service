def create_booking(user, slot):
    """Создаёт бронь для пользователя на указанный слот."""
    return {"user": user, "slot": slot, "status": "confirmed"}