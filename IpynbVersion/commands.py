
def Calculation(df):
    ###Cari Oran
    df.loc['C1'] = df.loc['1A']/df.loc['2A']
    
    ###Asit Oran
    df.loc['C2'] = (df.loc['1A']-df.loc['1AF'])/df.loc['2A']
    
    ###Nakit Oran
    df.loc['C3'] = (df.loc['1AA']+df.loc['1AB'])/df.loc['2A']

    ###Stoklar/Varlık (Aktif) Top.Oranı
    df.loc['C4'] = df.loc['1AF']/df.loc['1BL']

    ### Stok Bağımlılık Oranı
    df.loc['C5'] = df.loc['1AF'] / (df.loc['2A'] - (df.loc['1AA']+df.loc['1AB']))

    ### Kısa Vad.Alac./Varlık (Aktif) Toplamı Oranı
    df.loc['C6'] = (df.loc['1AC'] + df.loc['1AE']) / df.loc['1BL']

    ### Yabancı Kay.Toplamı/Varlık (Aktif) Top.Oranı (Kaldıraç Oranı)
    df.loc['B1'] = (df.loc['2A'] + df.loc['2B']) / df.loc['1BL']

    ### Öz Kaynak/Varlık (Aktif) Top.Oranı
    df.loc['B2'] = df.loc['2N'] / df.loc['1BL']

    ### Öz Kaynak/Yabancı Kay.Top.Oranı
    df.loc['B3'] = df.loc['2N'] / (df.loc['2A'] + df.loc['2B'])

    ### Kısa Vadeli Yabancı Kaynaklar/Kaynak (Pasif) Toplamı Oranı
    df.loc['B4'] = df.loc['2A'] / df.loc['2ODB']

    ### Uzun Vadeli Yabancı Kaynaklar/Kaynak (Pasif) Toplamı Oranı
    df.loc['B5'] = df.loc['2B'] / df.loc['2ODB']

    

    ### Alacak Devir Hızı
    df.loc['C2'] = df.loc['3C'] / df.loc['1AC']

    ###Faiz ve Vergi Öncesi Kâr(Pasif T. Oranı)
    df.loc['D1'] = (df.loc['3I'] + df.loc['3HC']) / (df.loc['2A'] + df.loc['2B'])
    
    return df
    



