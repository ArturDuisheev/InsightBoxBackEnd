from meditation import models as med_mod


def get_count(card_id, field):
    card = med_mod.MetaphoricalСards.objects.filter(pk=card_id).first()
    if not card:
        return None
    return getattr(card, field).count()


def toggle_status(card_id, user, field, add_message, remove_message):
    card = med_mod.MetaphoricalСards.objects.filter(pk=card_id).first()
    if not card:
        return False, 'Карта не найдена'

    field_instance = getattr(card, field)
    if user in field_instance.all():
        field_instance.remove(user)
        return True, remove_message
    else:
        field_instance.add(user)
        return True, add_message


def get_favorite_count(card_id):
    return get_count(card_id, 'likes')


def toggle_favorite_status(card_id, user):
    return toggle_status(card_id, user, 'likes', 'Добавлено в избранные', 'Удалено из избранных')


def get_count_meditation(meditation_id, field):
    meditation = med_mod.Meditation.objects.filter(pk=meditation_id).first()
    if not meditation:
        return None
    return getattr(meditation_id, 'likes')


def toggle_status_meditation(meditation_id, user, field, add_message, remove_message):
    meditation = med_mod.Meditation.objects.filter(pk=meditation_id).first()
    if not meditation:
        return False, 'Обьект не найден'
    field_instance = getattr(meditation, field)
    if user in field_instance.all():
        field_instance.remove(user)
        return True, remove_message
    else:
        field_instance.add(user)
        return True, add_message


def get_favorite_count_meditation(meditation_id):
    return get_count_meditation(meditation_id, 'likes')


def toggle_favorite_status_meditation(meditation_id, user):
    return toggle_status_meditation(meditation_id, user, 'likes', 'Добавлено в избранные', 'Удалено из избранных')