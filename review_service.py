from storage import load, save
from datetime import datetime, timedelta
from utils import now_iso
import logging


def review(user_id, card_id, quality):
    srs_list = load("srs_state.json")

    for s in srs_list:
        if s["card_id"] == card_id:
            ef = s["ef"]
            ef = ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
            if ef < 1.3:
                ef = 1.3

            if quality < 3:
                s["repetition"] = 0
                s["interval_days"] = 1
            else:
                s["repetition"] += 1
                if s["repetition"] == 1:
                    s["interval_days"] = 1
                elif s["repetition"] == 2:
                    s["interval_days"] = 6
                else:
                    s["interval_days"] = round(s["interval_days"] * ef)

            s["ef"] = ef
            s["last_quality"] = quality
            s["due_date"] = (datetime.now() + timedelta(days=s["interval_days"])).date().isoformat()
            break

    save("srs_state.json", srs_list)


    reviews = load("reviews.json")
    review_id = max([r["id"] for r in reviews], default=0) + 1
    reviews.append({
        "id": review_id,
        "user_id": user_id,
        "card_id": card_id,
        "quality": quality,
        "reviewed_at": now_iso()
    })
    save("reviews.json", reviews)
    logging.info(f"REVIEW: user={user_id}, card={card_id}, quality={quality}")
