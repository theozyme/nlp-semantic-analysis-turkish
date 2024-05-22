# Oluşturulan python dosyaları import edilir
from word_embedding import word_embedding  # Kelime gömme işlevini içeren dosya içe aktarılır
from user_gui import MyWindow  # Kullanıcı arayüzü için gerekli pencere sınıfı içe aktarılır
from model_classifier import model_SVM  # Destek vektör makinesi model sınıfını içe aktarılır

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel  # PyQt5'ten gerekli arayüz öğeleri içe aktarılır
from PyQt5.QtCore import Qt  # PyQt5'ten gerekli çekirdek işlevler içe aktarılır
import sys


# Etiketlenmiş cümleler ve etiketler
#sentences =
#label=

import ast

import csv

def sütun_al(csv_dosya, sütun_adı):
    with open(csv_dosya, mode='r', encoding='utf-8-sig') as dosya:
        csv_okuyucu = csv.DictReader(dosya)
        sütun = [satır[sütun_adı] for satır in csv_okuyucu]
        return sütun

dosya_adı = 'veri_seti.csv'
hedef_sütun = 'TweetMetni'

sentences = sütun_al(dosya_adı, hedef_sütun)
labels = sütun_al(dosya_adı, "Duygu")

labels_int = list(map(int, labels))
labels = [-1 if label == 0 else 0 if label == 2 else 1 for label in labels_int]





if __name__ == "__main__":
    # eğitim için sentences ve label listeleri girdi olarak verilir.   --->
    #word_embedding(sentences).create_dict()
    #model_SVM(sentences, labels).model_train()
    # test için sentences listesi verilir.   --->
    y_pred = model_SVM(sentences[:2],0).model_test()
    print(sentences[1])
    print(y_pred[1])

    # PyQt uygulamasının başlatılması ve pencerenin görüntülenmesi
    # app = QApplication(sys.argv)
    # window = MyWindow()
    # window.show()
    # sys.exit(app.exec_())