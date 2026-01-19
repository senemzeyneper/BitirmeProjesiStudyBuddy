from storage import load, save, next_id
from utils import now_iso
import logging


def create(deck_id, front, back):
    cards = load("cards.json")

    cid = next_id("card")

    cards.append({
        "id": cid,
        "deck_id": deck_id,
        "front": front,
        "back": back,
        "created_at": now_iso()
    })
    save("cards.json", cards)
    logging.info(f"CARD CREATED: deck_id={deck_id}, card_id={cid}")

    srs = load("srs_state.json")
    srs.append({
        "id": next_id("srs"),
        "card_id": cid,
        "repetition": 0,
        "interval_days": 1,
        "ef": 2.5,
        "due_date": now_iso()[:10],
        "last_quality": 0
    })
    save("srs_state.json", srs)


def list_by_deck(deck_id):
    return [c for c in load("cards.json") if c["deck_id"] == deck_id]


def update(card_id, front, back):
    cards = load("cards.json")

    for c in cards:
        if c["id"] == card_id:
            c["front"] = front
            c["back"] = back
            save("cards.json", cards)
            return

    raise ValueError("Kart bulunamadı")


def delete(card_id):
    cards = load("cards.json")
    srs = load("srs_state.json")

    cards = [c for c in cards if c["id"] != card_id]
    srs = [s for s in srs if s["card_id"] != card_id]

    save("cards.json", cards)
    save("srs_state.json", srs)
    logging.info(f"CARD DELETED: card_id={card_id}")

