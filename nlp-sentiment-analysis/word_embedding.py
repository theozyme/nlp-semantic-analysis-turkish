# Bu dosya, kelime sözlüğü oluşturmak ve kelime vektörlerini hesaplamak için kullanılır.

# Adım 1 - Metinlerden kelimeler çıkarılarak bir sözlük oluşturulur
from sklearn.feature_extraction.text import CountVectorizer  # Kelimeleri vektörlere dönüştürmek için gerekli modül içe aktarılır
import zeyrek  # Türkçe metinlerin morfolojik analizini yapmak için gerekli modül içe aktarılır
import pickle  # Verileri dosyalara yazmak ve okumak için kullanılan bir modül içe aktarılır
import nltk  # Doğal dil işleme işlemleri için kullanılan bir modül içe aktarılır
nltk.download('punkt')  # Doğal dil işleme için gerekli veri kaynağını indirir

class word_embedding():
    def __init__(self, texts):
        self.texts = texts
        self.kokler = self.get_kokler()  # Kökleri almak için fonksiyon çağrılır

    # Kelime sözlüğünü oluşturur
    def create_dict(self):
        texts = self.texts
        # CountVectorizer kullanarak özellik vektörlerini oluşturma
        vectorizer = CountVectorizer(binary=True)  # Kelimenin varlığına göre 1 veya 0 olarak kodla
        vectorizer.fit_transform(texts)  # Metinlerden özellik vektörlerini oluştur
        vocabulary = vectorizer.vocabulary_
        kelimeler = list(vocabulary.keys())  # Sözlükteki kelimeler alınır

        # Adım 2 - Sözlükteki kelimelerin kökleri çıkarılarak sözlük oluşturulur
        analyzer = zeyrek.MorphAnalyzer()  # Türkçe kelimelerin analizini yapmak için Zeyrek analiz aracı kullanılır
        kokler = []  # Kelimelerin köklerini tutmak için bir liste oluşturulur

        # Her bir kelimenin kökü çıkarılır
        for kelime in kelimeler:
            analizler = analyzer.analyze(kelime)
            for parse in analizler:
                if not parse:
                    continue
                else:
                    kok = parse[0].lemma  # Kelimenin kökü alınır
                    kokler.append(kok)

        kokler = list(set(kokler))  # Tekrar eden kökler temizlenir
        kokler = {kok: indeks for indeks, kok in enumerate(kokler)}  # Kökler ve indeksleri bir sözlükte saklanır
        file_path = 'sozluk.pkl'  # Sözlüğün dosyaya yazılacağı dosya yolu
        with open(file_path, 'wb') as file:
            pickle.dump(kokler, file)  # Oluşturulan sözlük dosyaya yazılır
        return kokler

    # Veri kümesindeki her cümlenin kelime vektörünü oluşturur
    def kelime_vektoru_olustur(self):
        kokler = self.kokler  # Kökler alınır
        cumleler = self.texts  # Cümleler alınır
        analyzer = zeyrek.MorphAnalyzer()  # Zeyrek analiz aracı kullanılır
        word_vectors = []  # Kelime vektörlerini tutmak için bir liste oluşturulur

        # Her bir cümle için kelime vektörü oluşturulur
        for i in cumleler:
            kelimeler = i.split()  # Cümle kelimelere bölünür
            cumle_vektoru = [0] * len(kokler)  # Her bir kök için bir vektör oluşturulur

            # Her bir kelimenin kökü çıkarılır ve vektör oluşturulur
            for kelime in kelimeler:
                analizler = analyzer.analyze(kelime)
                for parse in analizler:
                    if not parse:
                        continue
                    else:
                        kok = parse[0].lemma
                        if kok in kokler:
                            indeks = kokler[kok]  # Kökün indeksi alınır
                            cumle_vektoru[indeks] = 1  # Kökün bulunduğu indeks vektörde işaretlenir
            word_vectors.append(cumle_vektoru)  # Oluşturulan vektör liste üzerine eklenir
        return word_vectors  # Tüm cümlelerin kelime vektörleri döndürülür

    # Önceden oluşturulmuş sözlüğü alır
    def get_kokler(self):
        file_path = 'sozluk.pkl'  # Sözlüğün dosya yolu
        try:
            with open(file_path, 'rb') as file:
                kokler = pickle.load(file)  # Dosyadan sözlük alınır
                return kokler
        except FileNotFoundError:
            print("Dosya bulunamadı!")  # Dosya bulunamazsa hata mesajı verilir
            return None
