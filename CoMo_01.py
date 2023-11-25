import streamlit as st
import requests as re
import json as js

#vstup cisel
#cislo_1 = st.number_input("zadejte cislo 1 :")
#cislo_2 = st.number_input("zadejte cislo 1 :", min_value = 1)

#vypocet cisel
#soucet = cislo_1 + cislo_2
#rozdil = cislo_1 - cislo_2
#soucin = cislo_1 * cislo_2
#podil = cislo_1 / cislo_2
#mocnina = cislo_1 ** cislo_2
#deleni_celecislo = cislo_1 // cislo_2
#zbytek_po_deleni = cislo_1 % cislo_2

#Vystup cisel
#st.write(soucet)
#st.write(rozdil)
#st.write(soucin)
#st.write(podil)
#st.write(deleni_celecislo)
#st.write(zbytek_po_deleni)

#jmeno = st.text_input("Zadejte jmeno") # muzou byt i jednoduche
#prijmeni = st.text_input("Zadejte prijmeni") # muzou byt i jednoduche
#jmeno_prijmeni = jmeno + " " + prijmeni
#jmeno_prijmeni_f_string = f"Me jmeno je: {jmeno} {prijmeni}" #novejsi metoda spojovani stringu
#jmeno_prijmeni_f_string_lower = jmeno_prijmeni_f_string.lower() #vse malym
#jmeno_prijmeni_f_string_upper = jmeno_prijmeni_f_string.upper() #vse velkym 
#jmeno_prijmeni_f_string_capitalize = jmeno_prijmeni_f_string.capitalize() #vse velkym 


#st.write = (jmeno_prijmeni)
#st.write(jmeno + " " + prijmeni)
#st.write(jmeno_prijmeni_f_string)
#st.write(jmeno_prijmeni_f_string_lower)
#st.write(jmeno_prijmeni_f_string_upper) 
#st.write(jmeno_prijmeni_f_string_capitalize)

# seznamy a sety
#seznam_lidi = ["Adela", "Albert", "Misa", "Jara", "David", "Martin", "Oksana"]
#seznam_lidi.append("Tomas")
#seznam_lidi.sort()
#seznam_lidi.remove("Tomas")
#pocet_lidi = len(seznam_lidi)
#st.write(seznam_lidi)
#st.write(pocet_lidi)

#select_lidi = st.selectbox("Vyberte jedno", seznam_lidi)
#select_lidi = st.multiselect("Vyberte jedno", seznam_lidi)

#seznam_lidi_2 = seznam_lidi + seznam_lidi
#st.write(seznam_lidi_2)

#set_seznam_lidi_2 = set(seznam_lidi_2) 
#st.write(set_seznam_lidi_2)

#set_seznam_lidi_1 = set(seznam_lidi)
#set_seznam_lidi_2 = set(["Adela", "Albert", "Misa", "Jara"])
#st.write(set_seznam_lidi_1)
#st.write(set_seznam_lidi_2)

#prunik = set_seznam_lidi_1.intersection(set_seznam_lidi_2)
#st.write(prunik)

#sjednoceni = set_seznam_lidi_1.union(set_seznam_lidi_2)
#st.write(sjednoceni)

#sjednoceni.add("Honza")
#st.write(sjednoceni)


#if statement
#cislo = st.number_input("Zadejte cislo: ")
#button_porovnej = st.button("Porovnej to s s 20")
#if cislo < 20:
#    st.write("Cislo je mensi nez 20")
#elif cislo == 20:
#    st.write("cislo jes stejne")            
#else:
#    st.write("Cislo je rovno")    

#if statement s button
#cislo = st.number_input("Zadejte cislo: ")
#button_porovnej = st.button("Porovnej to s s 20")

#if button_porovnej:
#    if cislo < 20:
#        st.write("Cislo je mensi nez 20")
#        st.write(f" Zadane cislo je {cislo}")
#    elif cislo == 20:
#        st.write("cislo je rovno")           
#        st.write(f" Zadane cislo je {cislo}")        
#    else:
#        st.write("Cislo je vetsi")    
#        st.write(f" Zadane cislo je {cislo}")

#jmeno = st.text_input("Zadej jmeno: ")

#if jmeno != "":
#    st.write(f"Ahoj: {jmeno}")
#else:
#    st.write("Neco zadej")            

#for loop, while loop

#seznam_lidi = ["Adela", "Albert", "Misa", "Jara", "David", "Martin", "Oksana"]
#pocet_lidi = 0

#for kazdy_clen in seznam_lidi:
#    st.write(f"Ahoj clene {kazdy_clen}") 
#    st.write("Nezapomen na ukol")
#    pocet_lidi = pocet_lidi + 1
#st.write(f"Pozdravil jsem {pocet_lidi}")

#list elementu
#for kazdy_clen in range(10):
#    st.write(kazdy_clen)

 #list elementu
#for kazdy_clen in range(10, 20, 2):
#    st.write(kazdy_clen)


# Chcete aby uzivatel zadal dve cisla a porovnal je.
#cislo_1 = st.number_input("Zadej cislo 1")
#cislo_2 = st.number_input("Zadej cislo 2")

#if cislo_1 == cislo_2:
#    st.write("Cisla jsou stejna")
#elif cislo_1 > cislo_2:
#    st.write("Cislo 1 je vetsi nez Cislo 2")
#else:
#    st.write("Cislo 1 je mensi nez Cislo 2")    


# Chcete aby uzivatel zadal jmeno, prijmeni, vek a vytisknete mu tyto udaje
#jmeno = st.text_input("Zadej jmeno: ")
#prijmeni = st.text_input("Zadej prijmeni: ") 
#vek = st.text_input("Zadej vek: ")
#vystup = f"Ahoj, jmenuji se {jmeno} {prijmeni} a je mi {vek} let"

#st.write(vystup)

#chcete aby uzivatel z listu ["Adela", "Albert", "Misa", "Jara", "David", "Martin", "Oksana"] si vybral pomocí st.multiselect 
#jmena a pro kazde jmeno vypiste Ahoj, jmeno.

#seznam_lidi = ["Adela", "Albert", "Misa", "Jara", "David", "Martin", "Oksana"]
#msb_seznam_lidi = st.multiselect("Vyber jmena", seznam_lidi)

#for pozdrav in msb_seznam_lidi:
#    st.write(f"Ahoj, {pozdrav}")

# Mate list hodnot [12, 75, 150, 180, 145, 252, 50]
# pokud je hodnota vetsi nez 150 vypiste cislo x je vetsi nez 150

#seznam_hodnot =  [12, 75, 150, 180, 145, 252, 50]

#for hodnota in seznam_hodnot:
#    if hodnota > 150:
#        st.write(f"{hodnota} je vetsi nez 150")

#Ukol 5
# Mate list hodnot [12, 75, 150, 180, 145, 252, 50]
# Sectete cisla, pokud jsou vetsi nez 100
# Vypiste vysledek

#seznam_hodnot =  [12, 75, 150, 180, 145, 252, 50]
#hodnota_seznam = 0

#for hodnota in seznam_hodnot:
#    if hodnota > 100:
#        hodnota_seznam = hodnota_seznam + hodnota
#st.write(f"{hodnota_seznam}")

#cislo_1 = st.number_input("Zadej cislo")
#napocitavci_cislo = 1
#suma = 0

#while napocitavci_cislo < cislo_1:
#    st.write(f"Napocitavaci cislo {napocitavci_cislo}")
#    suma += napocitavci_cislo
#    napocitavci_cislo += 1 # dulezite!!! jinak cyklus nikdy neskonci
#    st.write(f"Nove Napocitavaci cislo {napocitavci_cislo}")
#    if napocitavci_cislo == 10:
#        break
#st.write(suma)

#suma_for = 0
#for kazde_cislo in range(int(20)):
#    suma_for =+ kazde_cislo
#    if kazde_cislo == 10:
#        break
#st.write(suma_for)

# Ukol 6a
# chcete aby uzivatel zadal cislo a pomoci while cyklu
# vytisknete vsechna cisla, která jsou suda a mensí než zadané cislo
# nastavte break na 20

#vstupni_cislo = st.number_input("Zadej cislo")
#napocitavaci_cislo = 1

#while napocitavaci_cislo < vstupni_cislo:
#    print(napocitavaci_cislo)
#    if napocitavaci_cislo % 2 == 0:
#        st.write(f"{napocitavaci_cislo}")
#    napocitavaci_cislo = napocitavaci_cislo + 1    
#    if napocitavaci_cislo == 20:
#        break

# Ukol 6b
# chcete aby uzivatel zadal cislo a pomoci for cyklu
# vytisknete vsechna cisla, která jsou suda a mensí než zadané cislo
# nastavte break na 20

#vstupni_cislo = st.number_input("Vloz cislo:")

#for cislo in range(int(vstupni_cislo)):
#    if cislo % 2 == 0:
#        st.write(cislo)
#    if cislo == 20:
#        break

# Ukol 7
# chcete aby uzivatel zadal cislo a pomoci while cyklu
# vytvorte LIST, do kterho budete ukladat licha a mensí než zadané cislo
# nastavte break na 20

#vstupni_cislo = st.number_input("Zadej cislo")
#seznam_cisel = []
#napocitavaci_cislo = 1

#while napocitavaci_cislo < vstupni_cislo:
#    if napocitavaci_cislo % 2 != 0:
#        seznam_cisel.append(napocitavaci_cislo)        
#    napocitavaci_cislo = napocitavaci_cislo + 1   
#    if napocitavaci_cislo == 20:
#        break
#st.write(seznam_cisel)    


# Ukol 8
# Mate list_jmen ["Adam", "Eva"] a list_prijmeni ["Novak", "Premysl"],
# Vytvorte pro kazde jmeno a prijmeni kombinaci a vypiste je.
# Vysledek je [Adam Novak, Adam Premysl, Eva Novak, Eva Premysl]

#list_jmen = ["Adam", "Eva"]
#list_prijmeni = ["Novak", "Premysl"]

#for jmeno in list_jmen:
#    for prijmeni in list_prijmeni:
#        kombinace = f"{jmeno} {prijmeni}"
#        st.write(kombinace)      

# Ukol 9
# Chcete uzivatel aby zadal vek
# Pokud je mensi nez 18 vypiste jsi dite
# >= 18 jsi dospely

#vek_uzivatele = st.number_input("Zadej vek")

#if vek_uzivatele < 18:
#    st.write("Jsi dite")
#elif vek_uzivatele >= 18:
#    st.write("Jsi dospely")    

# Ukol 10
# Mate list list_jmen["Adela", "Albert", "Misa"]
# Chcete aby uzivatel zadal sve jmeno
# Toto jmeno pridejte do list_jmen a vypiste novy list

#seznam_jmen = ["Adela", "Albert", "Misa"]
#st.write(seznam_jmen)
#vlastni_jmeno = st.text_input("Zadej jmeno: ")

#if vlastni_jmeno != "":
#    seznam_jmen.append(vlastni_jmeno)
#    for jmena in seznam_jmen:
#        st.write(f"{jmena}")  

# Ukol 11
# uzivatel zada dve cisla a vybere si z jedne moznosti (matematicka operace)
# vysledek operace se zobrazi na strance

#vstupni_cislo1 = st.number_input("Vloz cislo 1", key = "vstupni_cislo1") # rozlisuje i obsah promene v pripade, ze text v promene je shodny je nutne pouzit odkaz na promenou v KEY
#vstupni_cislo2 = st.number_input("Vloz cislo 2", key = "vstupni_cislo2") # rozlisuje i obsah promene v pripade, ze text v promene je shodny je nutne pouzit odkaz na promenou v KEY
##operace = ["Scitani", "Odecitani", "Nasobeni", "Deleni"]
#sl_box = st.selectbox("Vyber operaci", operace)

#if sl_box == "Scitani":
#    vstupni_cislo1 + vstupni_cislo2
#elif sl_box == "Odecitani":
#    vstupni_cislo1 - vstupni_cislo2    
#elif sl_box == "Nasobeni":
#    vstupni_cislo1 * vstupni_cislo2
#elif sl_box == "Deleni":
#    vstupni_cislo1 / vstupni_cislo2    

# Ukol 12
# mate list jmen ["Adela", "Albert"]
# uzivatel zada sve jmeno a pokud je v listu tak se na strance zobrazi Ahoj + jmeno jinak Nemam te v listu 
# hin: jmeno IN list_jmen

#list_jmen = ["Adela", "Albert"]
#zadej_jmeno = st.text_input("Zadej jmeno")

#if zadej_jmeno in list_jmen:
#    st.write(f"Ahoj, {zadej_jmeno}")
#else:
#    st.write("Nejsi v seznamu")        

# Ukol 13
# mate list_jmen ["Adela", "Albert"]
# Uzivatel zada sve jmeno a pokud neni v listu tak se prida do listu
# hin: jmeno IN list_jmen
 
# list_jmen = ["Adela", "Albert"]
# zadej_jmeno = st.text_input("Zadej jmeno")

# if st.button("pridej do listu"):
#     if (zadej_jmeno != "") & (zadej_jmeno not in list_jmen):
#         list_jmen.append(zadej_jmeno)
#         st.write(list_jmen)
#     elif zadej_jmeno in list_jmen:
#         st.write("Je to v seznamu")
#     else:
#         st.write(list_jmen)        

# Sloviniky(dictionary)

#dict_jmen = {"Adela": 25, "Albert": 30}

#st.write(dict_jmen["Albert"])
#dict_jmen["Martin"] = 28
#dict_jmen["Martin"] = 29

#st.write(dict_jmen)

#for kazdy_klic in dict_jmen.keys():
#    st.write(f"Ahoj, klici {kazdy_klic}, a je vam {dict_jmen[kazdy_klic]}")

#del dict_jmen["Martin"]
#st.write(dict_jmen)

#st.write(dict_jmen.values())

#st.write(dict_jmen.items())

#for kazda_polozka in dict_jmen.items():
#    st.write(kazda_polozka)
#    st.write(kazda_polozka[0])
#    st.write(kazda_polozka[1])

#dict_jmen_2 = {"Adela": {"vek": 25, "mesto": "Brno"},
#               "Albert": {"vek": 30, "mesto": "Praha"}}

#st.write(dict_jmen_2["Adela"]["vek"])


# Ukol 13
# mate dict_jmen = {"Adela": 25, "Albert": 30}
# Uzivatel zada sve jmeno a pokud je v dict_jmen,
# tak se zobrazi Ahoj + jmeno a je ti xx let
# jinak nemam te v dictionary

#dict_jmen = {"Adela": 25, "Albert": 30}
#vloz_jmeno = st.text_input("Vloz jmeno")

#if (vloz_jmeno != "") & (vloz_jmeno in dict_jmen.keys()):
#    for kazdy_klic in dict_jmen.keys():
#         st.write(f"Ahoj, klici {kazdy_klic}, a je vam {dict_jmen[kazdy_klic]}")
#else:
#    st.write("Nic tu neni")            

# Ukol 14
# mate dict_jmen = {"Adela": 25, "Albert": 30}
# Vypocitejte celkovy a prumerny vek

#dict_jmen = {"Adela": 25, "Albert": 30}
#celkovy_vek = sum(dict_jmen.values())
#prumerny_vek = sum(dict_jmen.values())/len(dict_jmen.values())

#st.write(celkovy_vek)
#st.write(prumerny_vek)


# Ukol 15
# Uzivatel zada cislo
# Vztvorte slovnik, kde klic je cislo a hodnota je druha mocnina
# hint x**2
# Vysledek = {10: 100}

#dictionary = {}
#vloz_cislo = st.number_input("vloz cislo")
#dictionary[vloz_cislo] = vloz_cislo**2  # vlozeni do prazdneho slovniku a ulozeni jedno hodnoty

#st.write(dictionary)

# Ukol 16
# Uzivatel zada cislo
# Vyzvorte slovnik kde klic jsou cisla 1 - 10
# a hodnota je vynasobenim zadaneho cisla s klicem

# dictionary = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# vloz_cislo = st.number_input("vloz cislo")

# for kazdy_clen in dictionary.keys():
#     kazdy_clen 

# st.write(kazdy_clen)

# st.write(f"Ahoj, klici {kazdy_klic}, a je vam {dict_jmen[kazdy_klic]}")

# Funkce

#def fn_scitani (cislo1, cislo2):
#    vysledek = cislo1 + cislo2
#    return vysledek

#st.write(fn_scitani(1, 5))

#def fn_pozdrav_s_defaultni_hodnotou (jmeno = "Martin"):
#    return f"Ahoj {jmeno}"

#st.write(fn_pozdrav_s_defaultni_hodnotou())

#st.text_input(label = "Zadej jmeno", value = "Albert")

# Ukol 17
# vytvorte fci, ktera bude mit dva ciselne vstupy
# Tato dvě cisla odectete

#def fn_odecitaci(cislo1, cislo2):
#    vysledek = cislo1 - cislo2
#    return vysledek

#st.write(fn_odecitaci(5, 4))

# Ukol 17.1
# Vytvorte fci, ktera bude mit dva ciselne vstupy a jeden textovy
# Dle textu se rozhodnete zda se bude scitat a nebo odecitat

# def fn_pocitaci(cislo1, cislo2, operace):
#     if operace == "scitani":
#        vysledek = cislo1 + cislo2
#     elif operace == "odecitani":    
#         vysledek = cislo1 - cislo2
#     return vysledek

# st.write(fn_pocitaci(10, 2, "odecitani"))

# Ukol 18
# Vytvorte fci, ktera bude mit dva vstupy, jmeno a vek
# Dle vstupu vytiskne "Ahoj jsem xxxx a je mi xx let"

# def fn_oslovovaci(jmeno, vek):
#     return f"Ahoj jsem {jmeno} a je mi {vek} let"

# st.write(fn_oslovovaci("Martin", 39))

######################################################################################################################

# """ -- trojite uvozovky rozdeleni kodu do vice radku 

#st.title("Titule")
#st.header("Hlavicka")
#st.markdown(f"""
#            Co Mo Python
#            """)
#st.divider()

#bt_tlacitko_1 = st.button("Tlacitko", key = "btn_1", use_container_width=True)

#if bt_tlacitko_1:
#    st.write("Zmacknul jsi tlacitko")

#st.link_button("Youtube", "https://youtube.com", use_container_width=True)    

# klicove slovo with

# Ukol 13
# uzivatel zada sve jmeno
# pouzijte check box na odsouhlaseni, ze je vam vic jak 18 let
# pridejte tlacitko, ktere po stisknuti zkontroluje zda je checkbox aktivni. 
# jestli ano tak vytiskne Vitej v klubu
# Pokud, neni tak vytiskne You shall not pass.

#uzivatel = st.text_input(label= "Zadej jmeno")
#chb_kontrola_veku = st.checkbox(label= "Je ti vic jak 18let?")
#b_tlacitko_overeni = st.button(label="Kontrola aktivity")

#if b_tlacitko_overeni:
#    if chb_kontrola_veku == True:
#        st.write(f"Vitej v klubu {uzivatel}")
#else:
#    st.write("You shall not pass")

# Ukol 14
# Mate list list_klub = ["Adela", "Albert", "Misa"]
# Uzivatel zada svuj vek
# toggle pri veku nad 18 aktivni a pod 18 neaktivni
# pouzijte toggle neaktivní, vypiste You shall not pass
# Jestli ze je toggle aktivní, umožněte uzivateli zadat jmeno a pridejte tlacitko, ktere po stisknuti prida jmeno do listu list_klub.
# Vytisknente list list_klub

#list_klub = ["Adela", "Albert", "Misa"]
#zadej_vek = st.number_input(label= "Zadej svuj vek")

#if zadej_vek >= 18:
#    toggle_status = True
#elif zadej_vek < 18:
#    toggle_status = False

#to_toggle = st.toggle(label= "kontrola veku", value = toggle_status)

#if toggle_status == True:
#    zadej_jemno = st.text_input("Zadej jmeno")
#    list_klub.append(zadej_jemno)
#    if zadej_jemno != "":
#        st.write(list_klub)
#elif toggle_status == False:
#    st.error("You shall not pass")    

# Ukol 15
# Mate slovnik slovnik_klub = {"Adela": 25, "Albert": 30, "Misa": 28}
# Uzivatel zada svuj vek
# Pouzijte toggle neaktivni, vypiste nemate pravo
# pokud je toggle aktivni, umoznete zadat jmeno a prijmeni a pridejte tlacitko, ktere po stisknuti prida jmeno a hodnotu do slovniku slovnik_klub
# Vytisknete slovnik

#uzivatel_hesla = {"Adela": "heslo123", "Albert": "heslo456", "Misa": "heslo789"}

#with st.form ("form_prihlasei"):
#   jmeno = st.text_input(label = "Zadej jmeno")
#   heslo = st.text_input(label = "Zadej heslo", type="password")
#   overeni_hesla = st.form_submit_button("Overit", use_container_width = True)

#if overeni_hesla:
#    if (jmeno == "") or (heslo == ""):
#        st.warning("Vypln jmeno a heslo")
#    elif jmeno not in uzivatel_hesla:
#        st.warning("Nejsi v seznamu")
#    elif (uzivatel_hesla[jmeno]) == heslo:
#        st.success("Je to ok") 
#    else:
#        st.error("Je to chybne")   


# API request 
#st.title("Hello world")

#with st.form("formular_pro_vtup_dat"):
#    spolecnost = st.text_input("Nazev spolecnosti", "AAPL")
#    api_klic = st.text_input("Api klic", "RPK6UBPGTAS7EQNC")
#    odeslat = st.form_submit_button("Odeslat")

#if odeslat:
#    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={spolecnost}&apikey={api_klic}"
#    odpoved = re.get(request_url)
#    odpoved_json = odpoved.json()

#    odpoved_slovnik_casova_rada = odpoved_json["Time Series (Daily)"]
#    slovni_vysledku = {}

#    for klic, hodnota in odpoved_slovnik_casova_rada.items():
#        slovni_vysledku[klic] = hodnota["4. close"]
    
#    st.write(slovni_vysledku)

#st.title("Pokemon API")

#seznam_pokemonu = []

#for pokemon_id in range(1, 50, 1):
#    url_pokemon_seznam = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
#    odpoved_seznam = re.get(url_pokemon_seznam)
#    odpoved_seznam_json = odpoved_seznam.json()
#    jmeno_pokemona = odpoved_seznam_json["name"]
#    seznam_pokemonu.append(jmeno_pokemona)

#with st.form("pokemon_vstup"):
#    pokemon_name = st.selectbox("Vyber pokemona", seznam_pokemonu)
#    pokemon_name_2 = st.selectbox("Vyber pokemona 2", seznam_pokemonu)
#    odeslat = st.form_submit_button("Odeslat")
#    pokemon_vstup = pokemon_name.lower()
#    pokemon_vstup_2 = pokemon_name_2.lower()


#if odeslat:
#    url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_vstup}/"
#    odpoved = re.get(url_pokemon)
#    odpoved_json = odpoved.json()
#    adresa_obrazku = odpoved_json["sprites"]["front_default"]
#    st.image(adresa_obrazku, width=200)


st.title("Pokemon API")

seznam_pokemonu = []

for pokemon_id in range(1, 100, 1):
    url_pokemon_seznam = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    odpoved_seznam = re.get(url_pokemon_seznam)
    odpoved_seznam_json = odpoved_seznam.json()
    jmeno_pokemona = odpoved_seznam_json["name"]
    seznam_pokemonu.append(jmeno_pokemona)

with st.form("pokemon_vstup"):
    pokemon_name = st.multiselect("Vyber pokemona", seznam_pokemonu)
    odeslat = st.form_submit_button("Odeslat")

if odeslat:
    for pokemon_jmeno in pokemon_name:
        url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_jmeno}/"
        url_odpoved = re.get(url_pokemon)
        odpoved_json = url_odpoved.json()
        utok_nazev = odpoved_json["types"]
        for ability in utok_nazev:
            st.write(ability["type"]["name"])