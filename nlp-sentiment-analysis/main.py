# Oluşturulan python dosyaları import edilir
from word_embedding import word_embedding  # Kelime gömme işlevini içeren dosya içe aktarılır
from user_gui import MyWindow  # Kullanıcı arayüzü için gerekli pencere sınıfı içe aktarılır
from model_classifier import model_SVM  # Destek vektör makinesi model sınıfını içe aktarılır

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel  # PyQt5'ten gerekli arayüz öğeleri içe aktarılır
from PyQt5.QtCore import Qt  # PyQt5'ten gerekli çekirdek işlevler içe aktarılır
import sys
import pandas as pd 

# csv den cümleler ve anlamları aktarıldı
df = pd.read_csv("magaza_yorumlari_duygu_analizi.csv",encoding='utf-16', delimiter=',')
df =df.dropna()

sentences = df['Görüş'].tolist()
# anlamlara mapping işlemi uyguladık 
durum_mapping = {
    'Olumlu': 1,
    'Olumsuz': -1,
    'Tarafsız': 0
}
labels = df['Durum'].map(durum_mapping).tolist()


labels_new = labels[:20]
sentences_new = sentences[:20]




if __name__ == "__main__":
    # eğitim için sentences ve label listeleri girdi olarak verilir.   --->  
    #word_embedding(sentences).create_dict()
    model_SVM(sentences_new, labels_new).model_train()
    # test için sentences listesi verilir.   --->  y_pred = model_SVM(sentences,0).model_test()

    # PyQt uygulamasının başlatılması ve pencerenin görüntülenmesi
    """
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    """
