#  StudyBuddy – Spaced Repetition Study App (CLI)

StudyBuddy, Python ile geliştirilmiş, JSON tabanlı, CLI üzerinden çalışan bir Spaced Repetition (SRS) tabanlı çalışma uygulamasıdır.
Kullanıcılar desteler ve kartlar oluşturabilir, kartları tekrar ederek öğrenme sürecini optimize edebilir ve istatistik raporları alabilir.

### 1. Özellikler

1. Kullanıcı kayıt & giriş sistemi (hash + salt güvenliği)

2. Deste (Deck) yönetimi: ekle / listele / güncelle / sil

3. Kart yönetimi: ekle / listele / güncelle / sil

4. SM-2 algoritması ile spaced repetition

5. Due kart sistemi

6. Son 7 gün istatistik raporu

7.  Atomic JSON file write (bozulma önleyici kayıt)

8. Logging sistemi (login, CRUD, review işlemleri loglanır)

### 2. Kurulum

git clone <repo_link>
cd StudyBuddy
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt   # (opsiyonel)

Ardından:
python main.py

### 3. Veri Dosyaları

1. users.json	

2. decks.json

3. cards.json	

4. srs_state.json

5. reviews.json	

6. counters.json	

Tüm dosyalar otomatik oluşturulur.


### 4. Logging

1. Kullanıcı kayıt / giriş denemeleri

2. Deck CRUD

3. Card CRUD

4. Review kayıtları

### 5. Menü Akışı

#### 5.1.Ana Menü
1. Kayıt
2. Giriş
3. Çıkış

#### 5.2.Giriş Sonrası

1. Desteler
2. Kartlar
3. Bugün Çalış
4. Raporlar
5. Exit

#### 5.3.Deck İşlemleri

1. Deste ekle
2. Deste listele
3. Deste güncelle
4. Deste sil

Sadece kullanıcıya ait desteler görüntülenir ve düzenlenebilir.

#### 5.4.Card İşlemleri

1. Kart ekle
2. Kart listele
3. Kart güncelle
4. Kart sil

Kartlar sadece kendi desteleri üzerinden seçilebilir.

#### 5.5.Bugün Çalış (SRS)

1. Due kartlar sırasıyla gösterilir

2. Soru → cevap → kalite puanı alınır

3. SM-2 algoritması uygulanır

4. Review kaydı otomatik oluşturulur

#### 5.6.Kalite puanı

Puan - Anlam:

* 0-Hiç hatırlamadım
* 1-Çok zor
* 2-Kısmen
* 3-Doğru ama zor
* 4-Doğru
* 5-Mükemmel

### 6. Raporlar

Bugün Due Kartlar

1.  Due olan kartların listesi.

2. Son 7 Günün yapılan review sayısı , ortalama kalite puanı

### 7. Veri Formatı Örneği

#### Card

{
  "id": 1,
  "deck_id": 2,
  "front": "What is Python?",
  "back": "A programming language",
  "created_at": "2026-01-17T15:29:09"
}

#### SRS

{
  "id": 1,
  "card_id": 1,
  "repetition": 2,
  "interval_days": 6,
  "ef": 2.5,
  "due_date": "2026-01-25",
  "last_quality": 4
}

### Sonuç

StudyBuddy:
Güvenli, modüler, JSON tabanlı, Spaced repetition destekli, Logging ve atomic write kullanan CLI tabanlı tam fonksiyonel bir öğrenme uygulamasıdır.



Giriş için email - şifreler:

* zeynep@gmail.com - 12345
* kudret@gmail.com - 98765
* hatice@gmail.com - 456
* merve@gmail.com - 852
* aras@gmail.com - 951
* ali@gmail.com - 789
* harun@gmail.com - 753
* gece@gmail.com - 000
* bulut@gmail.com - 321

