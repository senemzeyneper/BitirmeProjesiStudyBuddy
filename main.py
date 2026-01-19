from auth import register, login
from deck_service import create, list_by_user, update, delete
from card_service import create as create_card, list_by_deck, update as update_card, delete as delete_card
from review_service import review
from storage import load
from report_service import due_today, due_next_7_days
'''zeynep@gmail.com - 12345
kudret@gmail.com - 98765
hatice@gmail.com - 456
merve@gmail.com - 852
aras@gmail.com - 951
ali@gmail.com - 789
harun@gmail.com - 753
gece@gmail.com - 000
bulut@gmail.com - 321
 '''
user = None

while True:
    print("1-Kayıt  2-Giriş  3-Çıkış")
    c = input("> ")

    if c == "1":
        register(input("Email: "), input("Password: "))
        print("Kayıt tamam.")

    elif c == "2":
        user = login(input("Email: "), input("Password: "))
        print("Giriş başarılı.")
        break

    elif c == "3":
        exit()
    else:
        print("Yanlış sayı girdiniz.")


while True:
    print("\n1-Desteler  2-Kartlar  3-Bugün Çalış  4-Raporlar  5-Exit")
    c = input("> ")

    if c == "1":
        print("\n1-Deste ekle  2-Deste listele  3-Deste güncelle  4-Deste sil")
        d = input("> ")

        if d == "1":
            create(user["id"], input("Deste ismi: "), input("Açıklaması: "))

        elif d == "2":
            decks = list_by_user(user["id"])

            print("\n--- Desteleriniz ---")
            for d in decks:
                print(f"{d['id']} - {d['name']} ({d['description']})")


        elif d == "3":
            decks = list_by_user(user["id"])

            if not decks:
                print("Önce bir deste oluşturmalısınız.")
                continue

            print("\n--- Desteleriniz ---")
            for d in decks:
                print(f"{d['id']} - {d['name']}  - {d['description']}")

            deck_id = int(input("Güncellenecek deste numarası: "))

            if not any(d["id"] == deck_id for d in decks):
                print(" Bu sizin desteniz değildir.")
                print("Lütfen oluşturduğunuz destelerden birini seçiniz.")
                continue
            name = input("Yeni isim: ")
            desc = input("Yeni açıklama: ")
            decks = load("decks.json")
            deck = next((d for d in decks if d["id"] == deck_id), None)
            if deck["user_id"] == user["id"]:
                update(user["id"], deck_id, name, desc)
                print("Deste güncellendi.")
            else:
                print("Lütfen kendi kaydettiğiniz deste numarası giriniz")

        elif d == "4":
            decks = list_by_user(user["id"])

            if not decks:
                print("Silinecek deste yok.")
            else:
                print("\n--- Desteleriniz ---")
                for d in decks:
                    print(f"{d['id']} - {d['name']}  - {d['description']}")

                deck_id = int(input("Silmek istediğiniz deste numarası: "))

                if any(d["id"] == deck_id for d in decks):
                    delete(user["id"], deck_id)
                    print("Deste ve bağlı tüm kartlar silindi.")
                else:
                    print(" Bu deste size ait değil.")
        else:
            print("Yanlış sayı girdiniz.")


    elif c == "2":
        print("\n1-Kart ekle  2-Kart listele  3-Kart güncelle  4-Kart sil")
        k = input("> ")

        if k == "1":
            decks = list_by_user(user["id"])

            if not decks:
                print("Önce bir deste oluşturmalısınız.")
                continue

            print("\n--- Desteleriniz ---")
            for d in decks:
                print(f"{d['id']} - {d['name']}  - {d['description']}")

            deck_id = int(input("Kart eklenecek deste numarası: "))

            if not any(d["id"] == deck_id for d in decks):
                print(" Bu sizin desteniz değildir.")
                print("Lütfen oluşturduğunuz destelerden birini seçiniz.")
                continue

            front = input("Soru: ")
            back = input("Cevap: ")

            create_card(deck_id, front, back)
            print("Kart eklendi.")


        elif k == "2":
            decks = list_by_user(user["id"])

            if not decks:
                print("Henüz deste yok.")
                continue

            print("\n--- Desteleriniz ---")
            for d in decks:
                print(f"{d['id']} - {d['name']}  - {d['description']}")

            deck_id = int(input("\nKartları listelenecek deste numarası: "))

            if not any(d["id"] == deck_id for d in decks):
                print(" Bu sizin desteniz değildir.")
                continue

            cards = list_by_deck(deck_id)

            if not cards:
                print("Bu destede kart yok.")
            else:
                print("\n--- Kartlar ---")
                for c in cards:
                    print(f"[{c['id']}] {c['front']} -> {c['back']}")

        elif k == "3":
            decks = list_by_user(user["id"])

            if not decks:
                print("Henüz deste yok.")
                continue

            print("\n--- Desteleriniz ---")
            for d in decks:
                print(f"{d['id']} - {d['name']}  - {d['description']}")

            deck_id = int(input("\nKart güncellenecek deste numarası: "))

            if not any(d["id"] == deck_id for d in decks):
                print(" Bu sizin desteniz değildir.")
                continue

            cards = list_by_deck(deck_id)

            if not cards:
                print("Bu destede kart yok.")
                continue

            print("\n--- Kartlar ---")
            for c in cards:
                print(f"{c['id']} - {c['front']}")

            card_id = int(input("\nGüncellenecek kart numarası: "))

            if not any(c["id"] == card_id for c in cards):
                print(" Bu kart bu desteye ait değildir.")
                continue

            front = input("Yeni soru: ")
            back = input("Yeni cevap: ")

            update_card(card_id, front, back)
            print("Kart güncellendi.")

        elif k == "4":
            decks = list_by_user(user["id"])
            deck_ids = [d["id"] for d in decks]

            if not decks:
                print("Önce deste oluşturmalısınız.")
                continue

            print("\n--- Desteleriniz ---")
            for d in decks:
                print(f"{d['id']} - {d['name']}  - {d['description']}")

            deck_id = int(input("Deste numarası seçin: "))

            if deck_id not in deck_ids:
                print("❌ Bu deste size ait değil.")
                continue

            cards = list_by_deck(deck_id)

            if not cards:
                print("Bu destede kart yok.")
                continue

            print("\n--- Kartlar ---")
            for c in cards:
                print(f"{c['id']} - {c['front']}")

            card_id = int(input("Silmek istediğiniz kart numarası: "))

            if any(c["id"] == card_id for c in cards):
                delete_card(card_id)
                print("Kart ve SRS kaydı silindi.")
            else:
                print("❌ Bu kart bu desteye ait değil.")

    elif c == "3":
        due = due_today()

        if not due:
            print("Bugün due kart yok.")
            continue
        d = True
        for s in due:
            if d == True:
                card_id = s["card_id"]

                print(f"\nKart numarası: {card_id}")
                cards = load("cards.json")
                for c in cards:
                    if c["id"] == card_id:
                        print("Soru:", c["front"])

                show = input("Cevap gösterilsin mi? (E/H): ").lower()
                if show == "e":
                    cards = load("cards.json")
                    for c in cards:
                        if c["id"] == card_id:
                            print("Cevap:", c["back"])

                while True:
                    try:
                        print("0: Hiç hatırlamadım  1: Çok zor hatırladım 2: Kısmen hatırladım 3: Doğru ama zor 4: Doğru ve rahat 5: Mükemmel / akıcı ")
                        quality = int(input("Yukarıda verilen puanlamaya göre kalite puanı veriniz (0-5): "))
                        if 0 <= quality <= 5:
                            break
                    except ValueError:
                        pass
                    print("0-5 arası sayı girin!")

                review(user["id"], card_id, quality)
                print("Kart güncellendi.\n")

            a = input("Devam edecek misin? (E/H) :").lower()
            if a == "e":
                d = True
            else:
                d = False
                break


    elif c == "4":
        print("\n--- Bugün Due Kartlar ---")
        due = due_today()
        if not due:
            print("Bugün due kart yok.")
        else:
            for s in due:
                card = next((c for c in load("cards.json") if c["id"] == s["card_id"]), None)
                if card:
                    print(f"{card['front']}  (Kart numarası: {card['id']})")

        print("\n--- Son 7 Gün İstatistik ---")
        stats = due_next_7_days(user["id"])
        print(f"Yapılan review sayısı: {stats['review_count']}")
        print(f"Ortalama kalite puanı: {stats['average_quality']}")

    elif c == "5":
        exit()
