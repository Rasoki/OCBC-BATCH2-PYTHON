def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

def volume_persegi(sisi, luas):
    volume = luas_persegi(luas) * sisi
    return volume

print(luas_persegi(8))
print(volume_persegi(6))