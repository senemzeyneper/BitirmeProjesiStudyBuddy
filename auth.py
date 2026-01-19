import hashlib, os
from storage import load, save, next_id
from utils import now_iso
import logging


def hash_pw(pw, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        pw.encode(),
        salt,
        100000
    ).hex()

def register(email, pw):
    users = load("users.json")
    if any(u["email"] == email for u in users):
        raise ValueError("Email exists")

    salt = os.urandom(16)
    users.append({
        "id": next_id("user"),
        "email": email,
        "salt": salt.hex(),
        "password_hash": hash_pw(pw, salt),
        "created_at": now_iso()
    })
    save("users.json", users)
    logging.info(f"REGISTER SUCCESS: {email}")


def login(email, pw):
    users = load("users.json")
    for u in users:
        if u["email"] == email:
            salt = bytes.fromhex(u["salt"])
            if hash_pw(pw, salt) == u["password_hash"]:
                logging.info(f"LOGIN SUCCESS: {email}")
                return u
    logging.warning(f"LOGIN FAILED: {email}")
    raise ValueError("Login failed")
