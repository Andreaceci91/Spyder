#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:30:32 2022

@author: andrea
"""

print("1: Inserisci Studente")
print("2: Aggiungi voto a Studente")
print("3: Stampa Studente")
print("4: Calcola Media voti Studente")
print("5: Esci")

scelta = 0
studenti = []

while scelta != 5:
    scelta = int(input("Digita la scelta: "))
    
    if scelta == 1:
        nome = input("Inserisci nome studente: ")
        cognome = input("Inserisci cognome studente: ")

        stud_app = {"nome":nome, "cognome":cognome, "voti":[]}
                    
        
print("Ciao ciao ciao")











