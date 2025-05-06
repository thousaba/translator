from deep_translator import GoogleTranslator

def ceviri_yap():
    print("=== Basit Çeviri Uygulaması ===")
    print("Çıkmak için 'q' yazın.")

    while True:
        metin = input("\nÇevirmek istediğiniz metni girin: ").strip()
        if metin.lower() == 'q':
            print("Uygulamadan çıkılıyor...")
            break

        hedef_dil = input("Hedef dili girin (tr/en/fr/de/es/it/ar): ").strip().lower()

        try:
            cevirilen = GoogleTranslator(source='auto', target=hedef_dil).translate(metin)
            print(f"\n{cevirilen}")
        except Exception as e:
            print("Bir hata oluştu:", e)

ceviri_yap()


