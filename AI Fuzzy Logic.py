import pandas as pd

dataset = pd.read_excel('bengkel.xlsx')

#define data
ID = dataset["id"]
servis = dataset["servis"]
harga = dataset["harga"]

#design membership for servis

def fServis(x):
    #bagus
    if x > 80:
        bagus = 1
    elif x <= 70:
        bagus = 0
    else:
        bagus = (x-70)/(80-70)
        
    #jelek
    if x < 35:
        jelek = 1
    elif x >= 55:
        jelek = 0
    else:
        jelek = (55-x)/(55-35)
    
    #biasa
    if x <= 35 and x > 85:
        biasa = 0
    elif 35 < x <= 60:
        biasa = (x-35)/(60-35)
    elif 60 < x <= 70:
        biasa = 1
    elif 70 < x <= 85: 
        biasa = (85-x)/(85-70)
    else:
        biasa = 0

    result = [bagus, biasa, jelek]
    return result 

#design membership for harga

def fHarga(x):
    #mahal 
    if x >= 8:
        mahal = 1
    elif x < 4:
        mahal = 0
    elif 4 < x <= 8:
        mahal = (x-4)/(8-4)
    else:
        mahal = 0
    
    #murah
    if x > 3:
        murah = 0
    elif x <= 6:
        murah = 1
    else:
        murah = (6-x)/(6-3)
    
    #biasa
    if x <= 2 and x > 7:
        biasa = 0
    elif 2 < x <= 4:
        biasa = (x-3)/(4-3)
    elif 4 < x <= 6:
        biasa = 1
    elif 6 < x <= 7:
        biasa = (7-x)/(7-6)
    else:
        biasa = 0
    
    result = [mahal, biasa, murah]
    return result

#inference 
def rules(x, y): #x = servis, y = harga
    #menggunakan clipping tecknique
    excellent = [min(x[0], y[1]), min(x[0], y[2]), min(x[1], y[2])]
    normal = [min(x[1], y[0]), min(x[1], y[1]), min(x[0], y[0]), min(x[2], y[2])]
    bad = [min(x[2], y[0]), min(x[2], y[1])]
    
    #menggunakan disjunction rule
    excellent = max(excellent)
    normal = max(normal)
    bad = max(bad)
    
    result = [excellent, normal, bad]
    return result

# defusifikasi dengan metode Takagi-Sugeno-style
def defuzzification(p):
    z = ((p[0]*95)+(p[1]*70)+(p[2]*55))/(p[0]+p[1]+p[2])
    
    return z

#untuk memunculkan data
for i in range(100): 
    d = servis[i]
    e = harga[i]
    f = rules(fServis(d), fHarga(e))
    print("data ke:", i+1, "Value Servis:",fServis(d), "Value Harga:", fHarga(e), "Hasil inference:", rules(fServis(d), fHarga(e)), "Hasil defuzzification:", defuzzification(f))

#untuk memunculkan data
for i in range(100): 
    d = servis[i]
    e = harga[i]
    f = rules(fServis(d), fHarga(e))
    print("data ke:", i+1, "Value Servis:",fServis(d), "Value Harga:", fHarga(e), "Hasil inference:", rules(fServis(d), fHarga(e)), "Hasil defuzzification:", defuzzification(f))
