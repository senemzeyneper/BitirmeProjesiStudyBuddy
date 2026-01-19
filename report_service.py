from storage import load
from datetime import date, timedelta



def due_today():
    today = date.today().isoformat()
    return [s for s in load("srs_state.json") if s["due_date"] <= today]

def due_next_7_days(user_id):
    reviews = load("reviews.json")
    today = date.today()
    week_ago = today - timedelta(days=7)

    user_reviews = [
        r for r in reviews
        if r["user_id"] == user_id and week_ago <= date.fromisoformat(r["reviewed_at"][:10]) <= today
    ]

    count = len(user_reviews)
    avg_quality = sum(r["quality"] for r in user_reviews) / count if count else 0

    return {"review_count": count, "average_quality": round(avg_quality, 2)}