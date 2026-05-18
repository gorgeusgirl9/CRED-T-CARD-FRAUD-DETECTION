https://huggingface.co/spaces/gorgeus/Credit_Card_Fraud_Detection
https://github.com/gorgeusgirl9/RED-T-CARD-FRAUD-DETECTION
https://www.kaggle.com/code/gorgeusgirl/cred-t-card-fraud-detection






# 💳 13. Proje: Credit Card Fraud Detection (Anomali Tespiti)

Bu proje, bankacılık ve kredi kartı işlem geçmişi verilerini işleyerek, yapılan bir finansal işlemin dolandırıcılık (**Fraud**) olup olmadığını anlık olarak sınıflandıran gelişmiş bir yapay zeka risk yönetim sistemidir.

---

## 📊 Hocanın Dikkatine: Eksikler & Mühendislik Çözümleri

Veri setindeki yapısal problemleri çözmek ve modeli manipülasyondan korumak adına uygulanan preprocessing ve feature engineering adımları:

* **1. Eksik (Ekstrem Sınıf Dengesizliği):** Orijinal Kaggle verisinde dolandırıcılık içeren işlemler toplam verinin sadece **%0.17'sini** oluşturuyordu. Bu durum, ham veriyle eğitilen modelin azınlık sınıfı tamamen görmezden gelmesine (bias) yol açıyordu.
    * **✔️ Çözüm:** Klasik Doğruluk (Accuracy) metriği tamamen devre dışı bırakıldı. Model eğitilirken `class_weight="balanced"` parametresi entegre edilerek, algoritmanın dolandırıcılık işlemlerini ıskaladığında maksimum ceza puanı alması sağlandı. Eğitim ve test bölünmesi `stratify=y` ile katmanlaştırılarak %0.17'lik hassas oran korundu.
* **2. Eksik (Ölçek ve Varyans Uyuşmazlığı):** İşlem Tutarı (`Amount`) ve `Time` sütunları çok büyük ve dengesiz değerlere sahipken, `V1-V28` arası sütunlar PCA dönüşümünden geldiği için küçük aralıklardaydı. Tutar sütunu modeli domine ediyordu.
    * **✔️ Çözüm:** `StandardScaler` mimarisi devreye alınarak `Amount` ve `Time` özellikleri ölçeklendi; tüm veri seti aynı matematiksel varyans aralığına getirilerek baskınlık hatası giderildi.
* **3. Eksik (Doğruluk Metriği Körlüğü):** Sınıf dengesizliğinden dolayı %99.8 başaran bir model bile dolandırıcıları yakalayamayabilirdi.
    * **✔️ Çözüm:** Projenin ana başarı metrikleri olarak **Recall (Duyarlılık)**, **Precision (Kesinlik)** ve **F1-Score** zorunlu kılınarak optimizasyon sağlandı.

---

## 📈 Model Yapılandırması & Metrikler

* **Problem Türü:** İkili Sınıflandırma / Anomali Tespiti (Binary Classification)
* **Seçilen Algoritma:** `RandomForestClassifier` (Aşırı dengesiz anomali yapılarında ve olasılık tabanlı ceza kurgularında en kararlı güven sınırını çizdiği için tercih edilmiştir).
* **Kritik Metrik:** Yüksek F1-Score ve optimize edilmiş **ROC-AUC** performansı.

---

## 🚀 Canlı Uygulama (Deployment)

Proje, **Hugging Face Spaces** üzerinde **Streamlit** mimarisi kullanılarak canlıya taşınmıştır. Bankacılık parametrelerini (IP şüphesi, bakiye/limit oranı, ardışık işlem hızı) anlık tarayan ve risk skoru (%0 - %100) üreten dinamik bir finansal güvenlik paneli tamamlanmıştır.
