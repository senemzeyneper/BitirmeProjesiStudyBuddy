from storage import load, save, next_id
import logging


def create(user_id, name, description):
    decks = load("decks.json")
    decks.append({
        "id": next_id("deck"),
        "user_id": user_id,
        "name": name,
        "description": description
    })
    save("decks.json", decks)
    logging.info(f"DECK CREATED: user={user_id}, name={name}")

def list_by_user(user_id):
    return [d for d in load("decks.json") if d["user_id"] == user_id]

def update(user_id, deck_id, name, description):
    decks = load("decks.json")
    for d in decks:
        if d["id"] == deck_id and d["user_id"] == user_id:
            d["name"] = name
            d["description"] = description
            save("decks.json", decks)
            return
    raise ValueError("Deck bulunamadı")

def delete(user_id, deck_id):
    decks = load("decks.json")
    cards = load("cards.json")
    srs = load("srs_state.json")

    decks = [d for d in decks if not (d["id"] == deck_id and d["user_id"] == user_id)]

    deck_card_ids = [c["id"] for c in cards if c["deck_id"] == deck_id]

    cards = [c for c in cards if c["deck_id"] != deck_id]
    srs = [s for s in srs if s["card_id"] not in deck_card_ids]

    save("decks.json", decks)
    save("cards.json", cards)
    save("srs_state.json", srs)
    logging.info(f"DECK DELETED: user={user_id}, deck_id={deck_id}")

