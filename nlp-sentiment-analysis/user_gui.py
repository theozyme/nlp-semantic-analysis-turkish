# Bu dosya, bir kullanıcı arayüzü oluşturur.
import sys  # Sistem işlevleri için gerekli modül içe aktarılır
import random  # Rastgele sayılar üretmek için gerekli modül içe aktarılır
import requests  # HTTP istekleri yapmak için gerekli modül içe aktarılır
from bs4 import BeautifulSoup  # HTML ve XML belgelerini analiz etmek için gerekli modül içe aktarılır
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel  # PyQt5'ten gerekli arayüz öğeleri içe aktarılır
from PyQt5.QtCore import Qt  # PyQt5'ten gerekli çekirdek işlevler içe aktarılır
from model_classifier import model_SVM  # Sınıflandırma modeli sınıfını içe aktarılır
from word_embedding import word_embedding  # Kelime gömme işlevini içeren dosya içe aktarılır

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Anlam Çıkar")  # Pencere başlığı ayarlanır
        self.setGeometry(100, 100, 1000, 750)  # Pencere boyutu ve konumu ayarlanır

        # Metin girişi için QTextEdit öğesi oluşturulur
        self.text_input = QTextEdit(self)
        self.text_input.setFixedSize(400, 400)
        self.text_input.setAlignment(Qt.AlignTop)
        self.text_input.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)

        # Butonlar için yatay düzenleyici oluşturulur
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

        # Metin girişi kutusunu düzenlemek için düzenleyici oluşturulur
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
        # Metin girişi alınır
        metin = self.text_input.toPlainText()
        metin = str(metin)
        
        # Her bir satırı kontrol ederek olumlu, olumsuz ve nötr kategorilere ayırılır
        olumlu = 0
        olumsuz = 0
        nötr = 0
        liste=[]
        liste.append(metin)

        # Metin, sınıflandırma modeline gönderilir ve sonuç alınır
        sonuc = model_SVM(list(liste),0).model_test()
        print('sonuç: ',sonuc,'\ntype: ',type(sonuc))

        # Sınıflandırma sonucuna göre sayaçlar artırılır
        if sonuc == -1:
            olumsuz += 1
        elif sonuc == 0:
            nötr += 1
        elif sonuc == 1:
            olumlu += 1

        # Sonuçlar QLabel'lara yazdırılır
        self.olumlu_label.setText("Olumlu: " + str(olumlu))
        self.olumsuz_label.setText("Olumsuz: " + str(olumsuz))
        self.nötr_label.setText("Nötr: " + str(nötr))

    def rastgele_metin_clicked(self):
        # Web sitesinden yorumları çekme
        url = 'https://www.scrapethissite.com/pages/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Yorumları içeren div etiketlerini seçme
        yorum_divler = soup.find_all('div', class_='col-md-6 col-md-offset-3')

        # Yorumları saklamak için bir liste oluşturma
        yorum_metinleri = []
        for yorum_div in yorum_divler:
            p_etiketleri = yorum_div.find_all('p')  # <p> etiketlerini bul
            for p in p_etiketleri:
                yorum_metinleri.append(p.text.strip())  # Metinleri listeye ekle

        # Rastgele bir yorum seçme
        if yorum_metinleri:
            secilen_yorum = random.choice(yorum_metinleri)

            # Metin giriş kutusunu temizle ve seçilen yorumu yaz
            self.text_input.clear()
            self.text_input.append(secilen_yorum)
        else:
            self.text_input.clear()
            self.text_input.append("Yorum bulunamadı.")
