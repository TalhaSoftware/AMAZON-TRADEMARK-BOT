# -*- coding: utf-8 -*-
"""
Created on Mon May 16 13:32:02 2022

@author: TalhaSoftware
"""

import requests
import re
import time
from bs4 import BeautifulSoup

firma_ismi = "Adidas"

def teliflimi(firma_ismi,ulke):
    
    
    req = requests.get("https://www.trademarkelite.com/"+ulke+"/trademark/trademark-search.aspx?sw="+firma_ismi+"#")      
    
    
    
    soup = BeautifulSoup(req.text,"lxml")
    
    sonuc = soup.find_all("div",{"class":"searchResultInfo"})[0].text[:3]
    
    cevap = 0
    
    if(int(sonuc) == 0 ):
        print("Bu ürün telifli değil amk")
        cevap = 1
    else:
        print("Sakın bu ürünü yükleme")
        cevap = 0
    
    return cevap

def dosyayaz(dosyaisim,ulke):

    with open("markaor.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    
    l = set(lines)
        
    l.pop()
        
        
    cevaplistesi = []
    for i in l:
        cevaplistesi.append((i,teliflimi(i,ulke)))
        
    dosya = open(dosyaisim+".txt", "a+") 
        
    for z in cevaplistesi:
        dosya.writelines(str(z[0])+ " " + str(z[1])+"\n")
        
    dosya.close()
        


def menu():
    print("1.Avrupa \n2.Kanada \n3.İngiltere \n4.Avustralya")
    ulke = 0
    hangi = int(input("Hangi ülkeden Çekeceksin "))
    if(hangi == 1):
        ulke = "europe"
        dosyaadi = input("Dosya Adini giriniz ")
        dosyayaz(dosyaadi,ulke)
    elif(hangi == 2):
        ulke = "canada"
        dosyaadi = input("Dosya Adini giriniz ")
        dosyayaz(dosyaadi,ulke)
    elif(hangi == 3):
        ulke = "uk"
        dosyaadi = input("Dosya Adini giriniz ")
        dosyayaz(dosyaadi,ulke)
    elif(hangi == 4):
        ulke = "australia"
        dosyaadi = input("Dosya Adini giriniz ")
        dosyayaz(dosyaadi,ulke)


menu()



