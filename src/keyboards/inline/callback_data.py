from aiogram.utils.callback_data import CallbackData

navigation_items_callback = CallbackData('navigation_items_btm', 'for_data')
configs_list_callback = CallbackData('configs_list', 'marker', 'category_id', 'brand_id', 'model_id', 'showed_keyboard')
list_catalog_callback = CallbackData('list_catalog', 'action', 'id')