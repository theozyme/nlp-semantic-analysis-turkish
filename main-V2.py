import sys
import random
import requests
import PyPDF2  # PyPDF2 kütüphanesini ekledik
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QMessageBox
import pdfplumber
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
from trnlp import TrnlpWord, writeable
import string
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Anlam Çıkar")
        self.setGeometry(100, 100, 1000, 750)

        # Metin girişi için QTextEdit oluştur
        self.text_input = QTextEdit(self)
        self.text_input.setFixedSize(400, 400)
        self.text_input.setAlignment(Qt.AlignTop)
        self.text_input.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)

        # Butonlar için yatay düzenleyici oluştur
        buttons_layout = QHBoxLayout()

        self.anlam_cikar_button = QPushButton("Anlam Çıkar", self)
        self.anlam_cikar_button.clicked.connect(self.anlam_cikar_clicked)
        self.anlam_cikar_button.setFixedSize(150, 50)
        buttons_layout.addWidget(self.anlam_cikar_button)

        # Rastgele Metin butonu
        self.rastgele_metin_button = QPushButton("Rastgele Metin", self)
        self.rastgele_metin_button.setFixedSize(150, 50)
        self.rastgele_metin_button.clicked.connect(self.rastgele_metin_clicked)
        buttons_layout.addWidget(self.rastgele_metin_button)

        # Metin girişi kutusunu düzenlemek için düzenleyici oluştur
        layout = QVBoxLayout()
        layout.addWidget(self.text_input)
        layout.addLayout(buttons_layout)

        # Sonuçları gösterecek düzenleyiciler
        results_layout = QVBoxLayout()

        self.olumlu_label = QLabel("Olumlu: 0", self)
        self.olumlu_label.setAlignment(Qt.AlignLeft)
        results_layout.addWidget(self.olumlu_label)

        self.olumsuz_label = QLabel("Olumsuz: 0", self)
        self.olumsuz_label.setAlignment(Qt.AlignLeft)
        results_layout.addWidget(self.olumsuz_label)

        self.nötr_label = QLabel("Nötr: 0", self)
        self.nötr_label.setAlignment(Qt.AlignLeft)
        results_layout.addWidget(self.nötr_label)

        layout.addLayout(results_layout)
        self.setLayout(layout)

    def anlam_cikar_clicked(self):
        # Metin girişi alınacak
        metin = self.text_input.toPlainText()

        # Her bir satırı kontrol edip olumlu, olumsuz ve nötr kategorilere ayır
        olumlu = 0
        olumsuz = 0
        nötr = 0
        for satır in metin.split('\n'):
            if 'olumlu' in satır.lower():
                olumlu += 1
            elif 'olumsuz' in satır.lower():
                olumsuz += 1
            else:
                nötr += 1

        # Sonuçları QLabel'lara yazdır
        self.olumlu_label.setText("Olumlu: " + str(olumlu))
        self.olumsuz_label.setText("Olumsuz: " + str(olumsuz))
        self.nötr_label.setText("Nötr: " + str(nötr))

    def rastgele_metin_clicked(self):
        # Rastgele bir seçim yapalım: web sitesinden mi yoksa PDF'den mi metin çekeceğiz
        secim = random.choice(["web", "pdf"])


        if secim == "web":
            QMessageBox.information(self, "Bilgi", "Web'den rastgele metin çekiliyor...")
            # URL listesi
            url_listesi = [
                # ('https://www.bbc.com/news', 'BBC Haberler'),
                ('https://www.scrapethissite.com/pages/', 'Scraper Site'),
                ('https://shiftdelete.net/sosyal-medya/page/2', 'ShiftDelete Sosyal Medya 2'),
                ('https://shiftdelete.net/sosyal-medya/page/3', 'ShiftDelete Sosyal Medya 3'),
                ('https://shiftdelete.net/sosyal-medya/', 'ShiftDelete Sosyal Medya Ana Sayfa'),
                ('https://shiftdelete.net/sosyal-medya/page/4', 'ShiftDelete Sosyal Medya 4'),
                ('https://shiftdelete.net/sosyal-medya/page/5', 'ShiftDelete Sosyal Medya 5'),
                ('https://shiftdelete.net/sosyal-medya/page/6', 'ShiftDelete Sosyal Medya 6'),
                ('https://shiftdelete.net/sosyal-medya/page/7', 'ShiftDelete Sosyal Medya 7'),
                ('https://shiftdelete.net/sosyal-medya/page/7', 'ShiftDelete Sosyal Medya 8'),
                ('https://shiftdelete.net/sosyal-medya/page/7', 'ShiftDelete Sosyal Medya 9'),
                ('https://shiftdelete.net/sosyal-medya/page/7', 'ShiftDelete Sosyal Medya 10'),
            ]

            # Rastgele bir URL seçme
            secilen_url, secilen_site = random.choice(url_listesi)

            # Web sitesinden yorumları çekme
            response = requests.get(secilen_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Yorumları saklamak için bir liste oluşturma
            yorum_metinleri = []

            if secilen_url in ['https://shiftdelete.net/sosyal-medya/page/2',
                                 'https://shiftdelete.net/sosyal-medya/page/3',
                                 'https://shiftdelete.net/sosyal-medya/',
                                 'https://shiftdelete.net/sosyal-medya/page/4',
                                 'https://shiftdelete.net/sosyal-medya/page/5',
                                 'https://shiftdelete.net/sosyal-medya/page/6',
                                 'https://shiftdelete.net/sosyal-medya/page/7',
                                 'https://shiftdelete.net/sosyal-medya/page/8',
                                 'https://shiftdelete.net/sosyal-medya/page/9',
                                 'https://shiftdelete.net/sosyal-medya/page/10']:
                yorum_divler = soup.find_all('div', class_='sidebar-content-main')
                for yorum_div in yorum_divler:
                    p_etiketleri = yorum_div.find_all('p')
                    for p in p_etiketleri:
                        yorum_metinleri.append(p.text.strip())

        else:  # PDF'den metin çekme
            QMessageBox.information(self, "Bilgi", "PDF dosyasından rastgele metin çekiliyor...")
            # Yorumları saklamak için bir liste oluşturma
            yorum_metinleri = []
            # PDF dosyasını açma
            with pdfplumber.open('sample.pdf') as pdf:
                # PDF sayfalarının sayısını al
                num_pages = len(pdf.pages)

                # Rastgele bir sayfa seçme
                random_page_number = random.randint(18, 296)
                random_page = pdf.pages[random_page_number]

                # Sayfanın metnini çekme
                page_text = random_page.extract_text()
                cümleler = re.split(r'(?<=[.!?])\s+', page_text)

                ## En az 10 kelime içeren bir cümleyi bir değişkende sakla
                uzun_cümleler = [cümle.strip() for cümle in cümleler if len(cümle.split()) >= 10]

                # Rastgele 1 cümle seçme ve \n karakterlerini kaldırma
                rastgele_cümle = random.choice(uzun_cümleler).replace('\n', ' ')
                yorum_metinleri.append(rastgele_cümle)
                #print(yorum_metinleri)

        # Rastgele bir yorum seçme ve metin giriş kutusuna eklemek
        if yorum_metinleri:
            secilen_yorum = random.choice(yorum_metinleri)
            self.text_input.clear()
            self.text_input.append(secilen_yorum)

            print(sent_tokenize(secilen_yorum))
            # # Metni tokenize edelim
            kelimeler = word_tokenize(secilen_yorum)
            print(kelimeler)

            # TrnlpWord nesnesi oluşturalım
            obj = TrnlpWord()

            self.text_input.append("**********************************************")
            self.text_input.append("Cümlenin Kökleri")

            # Her bir kelimenin kökünü alalım
            for kelime in kelimeler:
                # Noktalama işaretlerini içeren bir string oluşturalım
                noktalama_isaretleri = string.punctuation

                # Noktalama işareti içeriyorsa kökü almayalım
                if any(noktalama in kelime for noktalama in noktalama_isaretleri):
                    self.text_input.append(kelime + " -> Noktalama İşareti")
                else:
                    obj.setword(kelime)
                    syntax = writeable(obj.get_morphology, long=True)
                    self.text_input.append(kelime + " -> " + syntax)
                    self.text_input.append(" ")
        else:
            self.text_input.clear()
            self.text_input.append("Yorum bulunamadı. ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
