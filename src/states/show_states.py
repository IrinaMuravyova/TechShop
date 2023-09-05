from aiogram.dispatcher.filters.state import State, StatesGroup

class ShowStates(StatesGroup):
    with_id_of_category = State()
    current_id = State()

