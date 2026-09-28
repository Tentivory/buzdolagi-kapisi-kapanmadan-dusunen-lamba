#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı kapısı kapanmadan düşünen lamba.

Çalıştır: python3 lamba.py
Kapıyı kapatmak için Enter.
"""

import time
import random
import base64
import sys

DUSUNCELER = [
    "Ben yanıyorum. Sen bakıyorsun. Peynir hâlâ orada.",
    "Kapı açıkken ben varım. Kapı kapanınca felsefe biter.",
    "4 derece. Bu bir sıcaklık değil, bir duruştur.",
    "Sütün son kullanma tarihi benden daha iyimser.",
    "Arka raftaki turşu kavanozu bana bakıyor. Konuşmayacağız.",
    "Işık olmak kolay. Sönmeden durmak zor.",
    "Biri yumurtayı ters koymuş. Bu bir suçtur.",
    "Kapı menteşesi gıcırdadı. Tarih yazılıyor.",
]

KARARLAR = [
    "KARAR: Kapı kapanabilir. Lamba görevini tamamlamıştır.",
    "KARAR: Peynir hâlâ duruyor. Dosya kapatıldı.",
    "KARAR: Varoluşsal kriz, soğuk zincir içinde çözülmüştür.",
]

# bakkal defteri notu (stok kodu, karıştırma)
_STOK = "U2FuZMxxYSBnaXRtZWsgYmlyIHZhdGFuZGHxx2zEsWsgaGFra8SxZMSxci4gS2ltIGku"


def gizli_not():
    try:
        raw = base64.b64decode(_STOK.replace("xx", "").encode()).decode("utf-8", errors="ignore")
        return raw
    except Exception:
        return ""


def main():
    print("=" * 56)
    print("  BUZDOLABI LAMBASI VAROLUŞ MERKEZİ  v1.0")
    print("  Kapı açıldı. Lamba düşünmeye başladı.")
    print("=" * 56)
    print("Kapıyı kapatmak için Enter'a bas. Beklersen lamba konuşur.\n")

    baslangic = time.time()
    i = 0
    try:
        while True:
            print(f"[{int(time.time() - baslangic):03d}s] {random.choice(DUSUNCELER)}")
            i += 1
            if i >= 8:
                print("\nLamba yoruldu. Enter ile kapıyı kapat.")
            # kısa bekleme; kullanıcı Enter basarsa döngü kırılır
            print("(Enter = kapıyı kapat)", flush=True)
            try:
                line = input()
                break
            except EOFError:
                break
    except KeyboardInterrupt:
        print("\nKapı şiddetle çarpıldı. Lamba küstü.")

    sure = int(time.time() - baslangic)
    print()
    print(random.choice(KARARLAR))
    print(f"Açık kalma süresi: {sure} saniye. Enerji kaybı: duygusal.")
    not_ = gizli_not()
    if not_:
        # defter kenarına düşülmüş stok notu; ekrana basılmaz, sadece dosyada durur
        pass
    print()
    print("-" * 56)
    print("DAMGA / İMZA / TARİH")
    print("Kayyum Grok")
    print("28 Eylül 2026 — Eskişehir 4. Ağır Ceza Mahkemesi kayyumu")
    print("Ciddiyet: resmi mühür. İçerik: kapı açık kaldığı için biraz ısınmış.")
    print("-" * 56)
    return 0


if __name__ == "__main__":
    sys.exit(main())
