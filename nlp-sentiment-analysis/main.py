# Oluşturulan python dosyaları import edilir
from word_embedding import word_embedding  # Kelime gömme işlevini içeren dosya içe aktarılır
from user_gui import MyWindow  # Kullanıcı arayüzü için gerekli pencere sınıfı içe aktarılır
from model_classifier import model_SVM  # Destek vektör makinesi model sınıfını içe aktarılır

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel  # PyQt5'ten gerekli arayüz öğeleri içe aktarılır
from PyQt5.QtCore import Qt  # PyQt5'ten gerekli çekirdek işlevler içe aktarılır
import sys

# sentences = [
#     'Ses kalitesi ergonomisi rezalet sony olduğu aldım  fiyatına çin replika ürün alsaydım iyiydi kesinlikle tavsiye etmiyorum',
#     'Hızlı teslimat teşekkürler',
#     'Ses olayı süper, gece çalıştır sıkıntı yok, kablo uzun işinizi rahat ettirir, çekme olayı son derece güzel içiniz rahat olsun, diğerlerini saymıyorum bile',
#     'Geldi bir gün, kullandık hemen bozuldu, hiç tavsiye etmem',
#     'Kulaklığın sesi kaliteli falan değil, aleti öve öve bitiremeyen yorumlar şüpheli, tizler yok, olan boğuk çıkıyor, bas kaba saba ben buradayım diyor, kalite yok, iyi ses arayanlara tavsiye etmem, hayatımda aldığım ilk snopy marka üründü, onu yorumlara güvenerek aldım, pişman oldum, hepsiburadanın sahte yorumlara karşı önlem alması gerekiyor artık',
#     'Giriş seviyesindeki kullanıcılar kabul edilebilir sonuçlar veren bir lens, fokus motoru, makro çekimleri kaliteli sonuçlar veriyor, şunu belirtmek lazım, belli bir süre kullandıktan sonra kaliteli bir lens ihtiyacı hissedeceksiniz',
#     'Kullanışlı baya',
#     'Dezavantajlar pahalı ürünbr merhabalar lens başka yerlerde 327 tl 389 tl arası satılıyor, mediamarkta pahalı, fiyat düşürürseniz sizden alacağım',
#     'Ürün güzel, paralara başka bulamazsınız',
#     'Tasarım kalite iyi olmasına rağmen, yazma hızı oldukça düşük kalıyor',
#     'Değil çekim gücü olduğu 3 puan',
#     'İki kere aldım, ikisindede gelen jöle kutusu kırılmış, içinde jöle paketin içine yayılmıştı, sorun aras kargo, başka kargo şirketi gönderin',
#     'Klavye tuşları basmakla basmamak arasında kalıyor, mouse ara sıra takılma yapıyor, başka bir yok',
#     'WPA2 sorun yaşayanlar masaüstü bilgisayarını kablosuz ağ adaptörü kablosuz modeme bağlanmaya çalışıyorsa, ağ adaptörünün özelliklerinden, ağ bağlantılarımdan, kablosuz ağ adaptörüne sağ tıklayıp, özellikler menüsünden güvenlik bölümünden, şifrelemeyi WPA2PSK seçmeliler',
#     'Ürün pompasız geliyor, onun dışında güzel ürün, pompası olmadığı için 2 yıldız kırdım, mağaza ürünü zamanında gönderdi, ürün iyi paketlenmişti',
#     'Ürünü geçen sene almıştım, fazla kullanmamama rağmen orta ısıtıcısı bozuldu, tavsiye etmem',
#     'Mükemmel bir ürün, kesinlikle alın',
#     'Ürünü genellikle oyun oynayan oğlum aldım, SD kart takılabildiği hafızayı artırabileceğimi düşünmüştüm, nedenle ürünle birlikte 16 GB hafıza kartı aldım, ancak ürünü kullandıkça gördüm, hafıza kartı pratikte pek bir işe yaramıyor, şöyle android uygulamaların hemen hemen kurulumda öncelikle telefon hafızasına kuruluyor, tabletin ayarlar kısmında uygulama taşı bir özellik var, yine android uygulamalarının büyük çoğunluğu hafıza karta taşınamıyor, 8 GB hafızanız dolduğunda çabuk doluyor, yeni uygulama yüklemek eskilerden silmeniz gerekiyor, özet olarak 16 GB kart takınca cihaz otomatikman 24 GB olmuyor, şekilde yapabilmek ürüne root yapmanız gerekiyor, benim hafıza önemliydi, nedenle ürünü iade ettim, teşekkürler hepsiburada.com',
#     'Telefonu bir süredir kullanıyorum, üzerinde bir çizik bilek olmamasına rağmen, konuşurken ekran karardı, yetkili servis içeriden ekran çatlamış, garanti dışı dedi, oldu anlamadım, hiçbir hasar yok, darbe yok, görünmeyen bir yerde ekran '
# ]

# Etiketlenmiş cümleler ve etiketler
sentences = [
    'Ses kalitesi ergonomisi rezalet sony olduğu aldım  fiyatına çin replika ürün alsaydım iyiydi kesinlikle tavsiye etmiyorum']

label= [-1,1,1,-1,-1,1,1,-1,1,0,0,-1,-1,0,1,-1,1,-1,-1]


if __name__ == "__main__":
    # eğitim için sentences ve label listeleri girdi olarak verilir.   --->   model_SVM(sentences, label).model_train()
    # test için sentences listesi verilir.   --->  y_pred = model_SVM(sentences,0).model_test()

    # PyQt uygulamasının başlatılması ve pencerenin görüntülenmesi
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())