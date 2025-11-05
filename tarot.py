import tkinter as tk
from PIL import Image, ImageTk
import random
import os

pencere = tk.Tk()
pencere.title("TAROT FALI")
pencere.geometry("900x760")
pencere.config(bg="#F5E9E2") 
pencere.resizable(False, False)

kartlar = {
    "buyucu": "Yaratıcılık, güç ve potansiyelin sembolüdür. Elinizdeki tüm araçları kullanarak yeni başlangıçlar yapmak ve hedeflerinize ulaşmak için gereken enerjiye sahipsiniz. Harekete geçme ve iradenizi kullanma zamanı.",
    "imparator": "Otorite, kontrol, yapı ve disiplini temsil eder. Hayatınızda düzen kurma, kararlı adımlar atma ve liderlik vasıflarınızı kullanma ihtiyacını gösterir. Sağlam temeller oluşturmanız gerekiyor.",
    "guc": "Fiziksel güçten ziyade, içsel cesaret, sabır ve şefkatle zorlukların üstesinden gelmeyi ifade eder. Kontrol etmek yerine, sevgiyle ve sükunetle durumu ehlileştirmeyi başaracağınızı gösterir. İç disiplininizi kullanın.",
    "kader": "Değişim, dönüm noktaları ve kaçınılmaz şans döngüsünü simgeler. Hayatınızda büyük bir olay ya da beklenmedik bir fırsat kapınızda olabilir. Tesadüfler zincirine güvenin ve değişime direnç göstermeyin.",
    "adalet": "Denge, hakikat, dürüstlük ve hukuki sonuçları temsil eder. Kararlarınızın ve eylemlerinizin sonuçlarıyla yüzleşme zamanıdır. Adil olmak ve objektif bir bakış açısıyla durumu değerlendirmek önemlidir.",
    "olum": "Korkulanın aksine, fiziksel bir sonu değil; büyük bir dönüşümü, sonlanışı ve yeniden doğuşu ifade eder. Eski alışkanlıkları, durumları veya ilişkileri geride bırakarak, yeni bir şeye yer açmanız gerektiğini gösterir.",
    "yildiz": "Umut, ilham, rehberlik ve ruhsal aydınlanmanın kartıdır. Zor bir dönemin ardından gelen huzuru ve geleceğe dair inancınızı simgeler. Hayallerinize ve iç sesinize kulak verin, doğru yolda ilerliyorsunuz.",
    "ay": "Bilinçaltı, sezgiler, yanılsamalar ve korkuları temsil eder. Gecenin karanlığı gibi, belirsiz ve kafa karıştırıcı durumlarla karşı karşıya olabilirsiniz. Sezgilerinize güvenmeli, ancak görünenin ardındaki gerçekliği sorgulamalısınız.",
    "gunes": "Başarı, neşe, mutluluk, canlılık ve aydınlanmanın en pozitif kartıdır. Hedeflerinize ulaştınız ve kendinizi güvende hissediyorsunuz. Tüm şüpheler ortadan kalktı ve hayatınızda netlik ve coşku dönemi başladı."
}

baslik = tk.Label(pencere, text="TAROT FALI", font=("Arial", 24, "bold"),bg="#F5E9E2", fg="#5C4033")
baslik.pack(pady=20)

ana_gosterim_frame = tk.Frame(pencere, bg="#F5E9E2")
ana_gosterim_frame.pack(pady=10, padx=20)

kart_etiketleri = []
tek_kart_etiketleri = {}
tek_kart_frame = tk.Frame(ana_gosterim_frame, bg="#F5E9E2")

kart_resim = tk.Label(tek_kart_frame, bg="#F5E9E2")
kart_resim.pack(pady=20)
tek_kart_etiketleri['resim'] = kart_resim

kart_isim = tk.Label(tek_kart_frame, text="", font=("Arial", 18, "bold"), bg="#F5E9E2", fg="#5C4033")
kart_isim.pack(pady=10)
tek_kart_etiketleri['isim'] = kart_isim

kart_anlam = tk.Label(tek_kart_frame, text="", font=("Arial", 14), bg="#F5E9E2", fg="#7F7A78" , wraplength=550, justify=tk.CENTER)
kart_anlam.pack(pady=10)
tek_kart_etiketleri['anlam'] = kart_anlam


uc_kart_frame = tk.Frame(ana_gosterim_frame, bg="#F5E9E2")

pozisyon_isimleri = ["GEÇMİŞ", "ŞİMDİ", "GELECEK"]

for i in range(3):
    dikey_kart_cercevesi = tk.Frame(uc_kart_frame, bg="#F5E9E2", padx=15, pady=15, relief=tk.FLAT)
    dikey_kart_cercevesi.grid(row=0, column=i, padx=15)

    pozisyon_baslik = tk.Label(dikey_kart_cercevesi, text=pozisyon_isimleri[i], font=("Arial", 12, "bold"), bg="#F5E9E2", fg="#CD5C5C")
    pozisyon_baslik.pack(pady=5)

    kart_gorsel = tk.Label(dikey_kart_cercevesi, bg="#F5E9E2")
    kart_gorsel.pack(pady=5)

    kart_isim = tk.Label(dikey_kart_cercevesi, text="", font=("Arial", 16, "bold"), bg="#F5E9E2", fg="#5C4033")
    kart_isim.pack(pady=5)

    kart_anlam_uc = tk.Label(dikey_kart_cercevesi, text="", font=("Arial", 10), bg="#F5E9E2", fg="#7F7A78" , wraplength=200, justify=tk.CENTER)
    kart_anlam_uc.pack(pady=5)

    kart_etiketleri.append({
        'gorsel': kart_gorsel, 
        'isim': kart_isim, 
        'anlam': kart_anlam_uc
    })

def temizle_ekran():
    tek_kart_frame.pack_forget()
    tek_kart_etiketleri['resim'].config(image="", text="")
    tek_kart_etiketleri['isim'].config(text="")
    tek_kart_etiketleri['anlam'].config(text="")

    uc_kart_frame.pack_forget()
    for etiketler in kart_etiketleri:
        etiketler['gorsel'].config(image="", text="[KART BOŞ]", fg="#7F7A78" )
        etiketler['isim'].config(text="")
        etiketler['anlam'].config(text="")

def resmi_yukle(kart_adi, gorsel_etiketi, boyut):
    try:
        dosya_yolu = f"tarot_kartlari/{kart_adi}.jpg"
        if os.path.exists(dosya_yolu):
            resim = Image.open(dosya_yolu)
            resim = resim.resize(boyut)
            foto = ImageTk.PhotoImage(resim)
            gorsel_etiketi.config(image=foto)
            gorsel_etiketi.image = foto 
        else:
            gorsel_etiketi.config(text=f"Resim\nBulunamadı\n({kart_adi.upper()})", image="", fg="#7F7A78" )
    except:
        gorsel_etiketi.config(text=f"Resim\nYüklenemedi\n({kart_adi.upper()})", image="", fg="#7F7A78" )

def tek_kart_cek():
    temizle_ekran() 
    uc_kart_frame.pack_forget() 
    tek_kart_frame.pack() 
    
    secilen = random.choice(list(kartlar.keys()))
    anlam = kartlar[secilen]
    
    resmi_yukle(secilen, tek_kart_etiketleri['resim'], (250, 350))
    
    tek_kart_etiketleri['isim'].config(text=secilen.upper())
    tek_kart_etiketleri['anlam'].config(text=anlam)

def uc_kart_cek():
    temizle_ekran() 
    tek_kart_frame.pack_forget() 
    uc_kart_frame.pack() 
    
    try:
        secilen_kart_adlari = random.sample(list(kartlar.keys()), 3)
    except ValueError:
        return

    for i in range(3):
        kart_adi = secilen_kart_adlari[i]
        kartin_anlami = kartlar[kart_adi]
        etiketler = kart_etiketleri[i]
    
        resmi_yukle(kart_adi, etiketler['gorsel'], (200, 300)) 

        etiketler['isim'].config(text=kart_adi.upper())
        etiketler['anlam'].config(text=kartin_anlami)

buton_frame = tk.Frame(pencere, bg="#F5E9E2")
buton_frame.pack(pady=20)

cek_btn_tek = tk.Button(buton_frame, text="TEK KART ÇEK", font=("Arial", 14, "bold"), bg="#FFDAB9" , fg="#5C4033" , padx=20, pady=10, command=tek_kart_cek)
cek_btn_tek.pack(side=tk.LEFT, padx=10)

cek_btn_uc = tk.Button(buton_frame, text="3 KART ÇEK", font=("Arial", 14, "bold"), bg="#FFDAB9" , fg="#5C4033" , padx=20, pady=10, command=uc_kart_cek)
cek_btn_uc.pack(side=tk.LEFT, padx=10)

temizle_btn = tk.Button(buton_frame, text="TEMİZLE", font=("Arial", 14, "bold"), bg="white", fg="#5C4033" , padx=20, pady=10, command=temizle_ekran)
temizle_btn.pack(side=tk.LEFT, padx=10)

temizle_ekran()

pencere.mainloop()