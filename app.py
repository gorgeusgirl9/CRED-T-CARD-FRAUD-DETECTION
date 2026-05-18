import streamlit as st

st.set_page_config(page_title="Credit Card Fraud Detector", page_icon="💳", layout="centered")

def fraud_analiz_motoru(tutar, konum, saatlik_islem, bakiye_orani):
    # Finansal risk skorlama mekanizması
    risk_score = 2.0
    
    # Mühendislik risk kırılımları
    if tutar > 2000: risk_score += 35.0  # Şüpheli yüksek tutar
    if konum == "Farklı Ülke / Şüpheli IP": risk_score += 40.0
    if saatlik_islem > 5: risk_score += 15.0 # Üst üste hızlı işlem (Spam transaction)
    if bakiye_orani > 90: risk_score += 8.0  # Limit zorlama
    
    risk_score = min(99.9, max(0.1, risk_score))
    
    if risk_score >= 50.0:
        return risk_score, "🔴 BLOKE / ŞÜPHELİ İŞLEM", "İşlem yüksek dolandırıcılık riski taşıyor! Kart geçici olarak işleme kapatıldı ve SMS onayı tetiklendi."
    elif 15.0 <= risk_score < 50.0:
        return risk_score, "🟡 İNCELEME ALTINDA", "İşlem alışılmışın dışında paternler içeriyor. Finans ekibinin onayına sunuldu."
    else:
        return risk_score, "🟢 GÜVENLİ İŞLEM", "İşlem sürücü davranışları ve finansal geçmişle tam uyumlu."

st.title("💳 Yapay Zeka Tabanlı Kredi Kartı Dolandırıcılık (Fraud) Tespit Sistemi")
st.write("Anlık bankacılık işlemlerinin parametrelerini girerek finansal risk skorunu hesaplayın.")
st.success("✅ Canlı Finansal Güvenlik ve Risk Motoru Aktif!")

col1, col2 = st.columns(2)
with col1:
    tutar = st.number_input("İşlem Tutarı ($)", min_value=1.0, max_value=50000.0, value=150.0)
    konum = st.selectbox("İşlem Yapılan Konum / IP", ["Kayıtlı Ev/İş Adresi", "Güvenli Bölge / Aynı Şehir", "Farklı Ülke / Şüpheli IP"])

with col2:
    saatlik_islem = st.slider("Son 1 Saatte Yapılan İşlem Sayısı", 1, 20, 2)
    bakiye_orani = st.slider("İşlemin Mevcut Limite Oranı (%)", 1, 100, 15)

st.markdown("---")

if st.button("🔍 İşlem Güvenliğini Analiz Et"):
    risk, durum, aksiyon = fraud_analiz_motoru(tutar, konum, saatlik_islem, bakiye_orani)
    
    st.markdown("### 🎯 Bankacılık Risk Değerlendirme Raporu")
    st.metric(label="📊 Hesaplanan Fraud Risk Skoru", value=f"%{risk:.1f}")
    
    if "🔴" in durum:
        st.error(f"Sistem Kararı: {durum}\n\n👉 Aksiyon: {aksiyon}")
    elif "🟡" in durum:
        st.warning(f"Sistem Kararı: {durum}\n\n👉 Aksiyon: {aksiyon}")
    else:
        st.success(f"Sistem Kararı: {durum}\n\n👉 Aksiyon: {aksiyon}")