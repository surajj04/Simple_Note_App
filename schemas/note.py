def note_entity(item) -> dict:
    return {
        'id': item['_id'],
        'title': item['title'],
        'content': item['content'],
        'category': item['category'],
        'tags': item['tags'],
        'important': item['important']
    }


def notes_entity(items) -> list:
    return [note_entity(item) for item in items]
