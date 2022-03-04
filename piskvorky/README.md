# Hra piskvorky
### Poznamky
- Kazde kolo sa zacne napisom -> __Vitajte v kole X__
- Pocas kazdeho kola program vypise ktory hrac je na rade -> __Teraz je narade hrac 1 alebo 2__
- Pred kazdym tahom hraca sa vypise hracia plocha, na hraciu plochu sa pouzije pole, do ktoreho sa vlozi ine pole, pole pre kazdy riadok, ktore bude vyplnene symbolmi.
- Na vypis prazdneho miesta sa pouzije symbol __podtrznik__, pre hracov sa pouziju symboly __x__ a __o__
- Pocas tahu kazdeho jedneho z hracov, si program vypyta dve suradnice, ktore sa zadaju z klavesnice, pomocou standardneho vstupu. Suradnica moze byt teda index v danom poli. Jednotlive stplce a riadky su oznacene indexom. Hrac moze zadavat x suradnicu od 0 po 2, a y suradnicu od 0 po 2.
- Treba implementovat aj osetrenie chyb -> ak by hrac zadal suradnicu mimo rozsahu pola, alebo zadal namiesto cisla pismeno ci textovy retazec.
- Treba osetrit aj vyhodnocovanie hry, kedy program vyhodnoti ktory hrac vyhral, alebo ci nastala remiza.
- Kod je potrebne rozdelit do logicky usporiadanych modulov.
- Pre premenne a nazvy suborov je potrebne dodrziavat zauzivane konvencie -> anglicke nazvy, pouzivanie malych pismen a podtrznikov v pripade nazvu suborov.
- Je vhodne pouzit zabudovany modul na pracu so standardnym vstupom.