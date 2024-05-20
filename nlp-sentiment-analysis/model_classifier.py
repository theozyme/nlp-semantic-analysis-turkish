# Bu adımda, SVM modeli oluşturulur ve eğitilir.
# Adım 4 - SVM Model Eğitimi

from sklearn.model_selection import train_test_split  # Veri kümesinin eğitim ve test setlerine bölünmesi için gereken işlev içe aktarılır
from sklearn.svm import SVC  # Destek vektör makinesi sınıflandırıcısı içe aktarılır
from joblib import dump, load  # Modelin kaydedilmesi ve yüklenmesi için gerekli işlevler içe aktarılır
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score  # Model performansı metriklerinin hesaplanması için gerekli işlevler içe aktarılır
from word_embedding import word_embedding  # Kelime gömme işlevini içeren dosya içe aktarılır

class model_SVM():
    def __init__(self,X,y,svm_type='linear',test_rate=0.2):
        self.X = X
        self.y = y
        self.svm_type = svm_type
        self.test_rate = test_rate

    def model_train(self):
        # Kelime vektörleri oluşturulur
        word_vectors = word_embedding(self.X).kelime_vektoru_olustur()

        # SVM modeli oluşturulur
        svm_model = SVC(kernel=self.svm_type)

        # Veri kümesi eğitim ve test setlerine bölünür
        X_train, X_test, y_train, y_test = train_test_split(word_vectors, self.y, test_size=self.test_rate, random_state=42)

        # SVM modeli eğitilir
        svm_model.fit(X_train, y_train)
        
        # Test seti üzerinde tahminleme yapılır
        y_pred = svm_model.predict(X_test)

        # Doğruluk hesaplanır
        accuracy = accuracy_score(y_test, y_pred)*100

        # Hassasiyet hesaplanır
        precision = precision_score(y_test, y_pred, average='weighted',zero_division=0)*100

        # Duyarlılık hesaplanır
        recall = recall_score(y_test, y_pred, average='weighted')*100

        # F1 skoru hesaplanır
        f1 = f1_score(y_test, y_pred, average='weighted')*100

        # Model performansı yazdırılır
        print("Model Doğruluğu:", accuracy)
        print("Hassasiyet:", precision)
        print("Duyarlılık:", recall)
        print("F1 Skoru:", f1)

        # Model detaylarını görüntüleyebiliriz
        print("SVM Model Detayları:")
        print(svm_model)
        
        # Model Hiperparametrelerini görüntüleyebilirz
        print("\nSVM Model Hiperparametreleri:")
        print(svm_model.get_params())
        
        # Eğitilen model dosyaya kaydedilir
        dump(svm_model, 'svm_model.joblib')

    def model_test(self):
        # Kelime vektörleri oluşturulur
        word_vectors =word_embedding(self.X).kelime_vektoru_olustur()
        
        # Kaydedilmiş SVM modeli yüklenir
        svm_model = load('svm_model.joblib')
        
        # Cümlelerin sınıflandırılması için tahminleme yapılır
        y_pred = svm_model.predict(word_vectors)
        return y_pred
