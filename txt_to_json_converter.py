import json

# The content of your 'protocol_for_office.txt' file
txt_content = """fisa de post – operator calculator

denumirea compartimentului: 
birou introducere receptii si contabilitate primara.

denumirea postului:
operator calculator;

se subordoneaza:
managerului si managerului financiar

subordoneaza:
toti lucratorii comerciali;

relatii functionale:
colegii din depozit pentru preluarea comenzilor;
colegii de pe magazin din celelalte departamente;

competentele postului de munca, cunostinte si deprinderi:
cunoasterea programului in care se lucreaza;
cunoasterea programului de incasare prezent la casele de marcat.
cunoasterea produselor;
atentie dezvoltata pe partea de lucru la calculator;

cerinte aptitudinale:
capacitate de a lua decizii; 
aptitudine generala de invatare, aptitudini de comunicare; 
perceptie vizuala, atentie, concentrare, mobilitate, distributivitate, selectivitate; 
rapiditate, spirit practic, coordonare manuala buna;
memorie vizuala buna, motivat;
dorinta de a munci, rezistenta la sarcini repetitive, rezistenta la oboseala; 
aspect fizic placut;

cerinte comportamentale:
pastreaza confidentialitatea secretului de salar;
punctualitate, atitudine proactiva in munca de echipa si inclinatii catre respect fata de colegi.
autocontrol mediu, capacitati persuasive; 
capacitate de coordonare, capacitate de planificare si organizare;
responsabilitate personala, eficienta personala; 
spirit de echipa, capacitatea de a munci in echipa; 
capacitatea de a se descurca in conditii de stres;
comportament etic, integru si politicos, implicat in activitate;
comportament civilizat si respectuos fata de colegi,clienti si furnizori;

responsabilitati si sarcini: 
in lipsa managementului companiei raspund de buna desfasurare a activitatii;
in  lipsa managementului companiei verifica ca marfa intrata in ziua respectiva sa fie scoasa in magazin dupa verificarea preturilor de catre colegii de pe raioane.
in lipsa managementului companiei verifica periodic raioanele si anunta lucratorii comerciali daca sunt lipsuri mari de marfa in anumite sectoare.
verifica ca muzica ambientala sa fie pornita.
verifica nivelul de aglomeratie la casa de marcat si ia decizii in functie de situatie.
verifica raionul de legume fructe periodic .
verifica si actualizeaza registrul de casa si raportul de gestiune;
verifica in fiecare seara buna functionare a aparatelor frigorifice si anunta in caz de defectiune;
umple la frigiderul de oua cand e cazul;
ajuta la preluarea marfii cand este nevoie;
preia incasarile si monetarul de la casiere;
inchid si deschid magazinul la orele stabilite in program;
inlocuieste personalul de la mezeluri si de la casa de marcat cand e nevoie;
verifica personalul la iesirea din tura;
semneaza produsele cumparate de angajati pentru consum propriu;
in cazuri speciale participa la umplerea raionului de legume fructe;
raspunde de comanda de comanda zilnica de paine;
supravegheaza periodic activitatea din magazin si clientii care ar putea crea pagube;
participa la curatenia generala de inchidere a magazinului;
obligatia de a anunta din timp concediul de odihna(minim 2 luni anticipat);
pastreaza curatenia in magazin;
obligatia de a nu fuma decat in locurile indicate de conducere.
parasesc incinta locului de munca doar cu acordul sefului ierarhic;
obligatia de a nu consuma produse din stocul firmei fara a le plati in prealabil;
daca folosesc scari ajutatoare pentru a lua marfa la inaltime o fac pe raspundere proprie;
in caz de boala concediul medical trebuie prezentat la sediul firmei in maxim 48 de ore de la emitere;
participa la descarcat/preluat marfa impreuna cu persoanele desemnate;
participa la inventarul anual;

atributii:
sa foloseasca timpul de munca exclusiv pentru indeplinirea sarcinilor de serviciu, in acest sens, nu se ocupa in timpul de munca de activitati care nu sunt cuprinse in atributiile si indatoririle sale ori nu sunt dispuse de sefi ierarhici;
sa verifice conformitatea datelor introduse in calculator, cu datele din documentele/mediile primare; 
sa selecteze si sa verifice datele inainte de a le introduce in calculator;
sa preia datele de pe documente si sa le introduca in calculator;
sa corecteze erorile intalnite sau le raporteaza superiorului direct;
sa asigure buna functionare si intretinerea a echipamentelor cu care lucreaza;
sa cunoasca elementele ce concura la realizarea operatiei in sine;
sa semnaleze abaterile de la reguli si contribuie la aplicarea procedurilor de corectare;
sa asigure necesarul de componente si materiale consumabile;
sa se preocupe de planificarea activitatii proprii;
sa participe activ la rezolvarea sarcinilor echipei;
sa fie cinstit, loial si disciplinat, dand dovada in toate imprejurarile de o atitudine civilizata si corecta fata de toate persoanele cu care vine in contact; 
sa respecte normele de securitate si sanatate in munca, normele de protectie a mediului;
sa respecte cu strictete regulile de protectie a muncii si p.s.i. din obiectivul unde desfasoara serviciul; 
sa acorde ajutor, atat cat este rational posibil, oricarui alt salariat, aflat intr-o situatie de pericol;
sa-si insuseasca si sa respecte normele si instructiunile de protectie a muncii si masurile de aplicare a acestora;
sa aduca la cunostinta de indata administratorului accidentele de munca suferite de propria persoana sau de alti angajati;
sa coopereze cu persoanele cu atributii specifice in domeniul securitatii si sanatatii in munca, atat timp cat este necesar, pentru realizarea oricarei sarcini sau cerinte impuse de autoritate competenta pentru prevenirea accidentelor si bolilor profesionale;
sa refuze intemeiat executarea unei sarcini de munca daca aceasta ar pune in pericol de accidentare sau imbolnavire profesionala persoana sa sau a celorlalti colegi;
sa informeze de indata superiorul despre orice deficienta constatata sau eveniment petrecut;
sa execute alte activitati in legatura cu indeplinirea sarcinilor de serviciu precizate de persoanele care au acest drept.
sa nu fumeze decat in locurile special amenajate.

responsabilitatile postului:
raspunde de buna coordonare a activitatii in lipsa managementului companiei.
raspunde de conditiile de igiena a marfii;
raspunde de rezolvarea problemelor si de satisfacerea cerintelor clientului;
respecta instructiunile verbale si scrise date de superiori;
raspunde de raportarea pierderilor de orice fel (rebuturi, furturi);
raspunde de corectitudinea datelor introduse in calculator.

sanctiuni pentru nerespectarea fisei postului sau a anexelor acestora in legatura cu confidentialitatea salariului sanctiunea este desfacerea contracului de munca.

"""

# Convert the .txt content to a dictionary
protocol_dict = {
    "title": "fisa de post – operator calculator",
    "denumirea compartimentului": "birou introducere receptii si contabilitate primara",
    "denumirea postului": "operator calculator",
    "se subordoneaza": "managerului si managerului financiar",
    "subordoneaza": "toti lucratorii comerciali",
    "relatii functionale": ["colegii din depozit pentru preluarea comenzilor", "colegii de pe magazin din celelalte departamente"],
    "competentele postului de munca, cunostinte si deprinderi": ["cunoasterea programului in care se lucreaza", "cunoasterea programului de incasare prezent la casele de marcat", "cunoasterea produselor", "atentie dezvoltata pe partea de lucru la calculator"],
    "cerinte aptitudinale": ["capacitate de a lua decizii", "aptitudine generala de invatare", "aptitudini de comunicare", "perceptie vizuala", "atentie", "concentrare", "mobilitate", "distributivitate", "selectivitate", "rapiditate", "spirit practic", "coordonare manuala buna", "memorie vizuala buna", "motivat", "dorinta de a munci", "rezistenta la sarcini repetitive", "rezistenta la oboseala", "aspect fizic placut"],
    "cerinte comportamentale": ["pastreaza confidentialitatea secretului de salar", "punctualitate", "atitudine proactiva in munca de echipa si inclinatii catre respect fata de colegi", "autocontrol mediu", "capacitati persuasive", "capacitate de coordonare", "capacitate de planificare si organizare", "responsabilitate personala", "eficienta personala", "spirit de echipa", "capacitatea de a munci in echipa", "capacitatea de a se descurca in conditii de stres", "comportament etic", "integru si politicos", "implicat in activitate", "comportament civilizat si respectuos fata de colegi,clienti si furnizori"],
    "responsabilitati si sarcini": ["in lipsa managementului companiei raspund de buna desfasurare a activitatii", "in lipsa managementului companiei verifica ca marfa intrata in ziua respectiva sa fie scoasa in magazin dupa verificarea preturilor de catre colegii de pe raioane", "verifica ca muzica ambientala sa fie pornita", "verifica nivelul de aglomeratie la casa de marcat si ia decizii in functie de situatie", "verifica raionul de legume fructe periodic", "verifica si actualizeaza registrul de casa si raportul de gestiune", "verifica in fiecare seara buna functionare a aparatelor frigorifice si anunta in caz de defectiune", "umple la frigiderul de oua cand e cazul", "ajuta la preluarea marfii cand este nevoie", "preia incasarile si monetarul de la casiere", "inchid si deschid magazinul la orele stabilite in program", "inlocuieste personalul de la mezeluri si de la casa de marcat cand e nevoie", "verifica personalul la iesirea din tura", "semneaza produsele cumparate de angajati pentru consum propriu", "in cazuri speciale participa la umplerea raionului de legume fructe", "raspunde de comanda de comanda zilnica de paine", "supravegheaza periodic activitatea din magazin si clientii care ar putea crea pagube", "participa la curatenia generala de inchidere a magazinului", "obligatia de a anunta din timp concediul de odihna(minim 2 luni anticipat)", "pastreaza curatenia in magazin", "obligatia de a nu fuma decat in locurile indicate de conducere", "parasesc incinta locului de munca doar cu acordul sefului ierarhic", "obligatia de a nu consuma produse din stocul firmei fara a le plati in prealabil", "daca folosesc scari ajutatoare pentru a lua marfa la inaltime o fac pe raspundere proprie", "in caz de boala concediul medical trebuie prezentat la sediul firmei in maxim 48 de ore de la emitere", "participa la descarcat/preluat marfa impreuna cu persoanele desemnate", "participa la inventarul anual"],
    "atributii": ["sa foloseasca timpul de munca exclusiv pentru indeplinirea sarcinilor de serviciu", "sa verifice conformitatea datelor introduse in calculator, cu datele din documentele/mediile primare", "sa selecteze si sa verifice datele inainte de a le introduce in calculator", "sa se asigure ca materialele in curs de prelucrare sunt in ordine si bine organizate", "sa pastreze si sa arhiveze informatiile si materialele in format electronic, in conditii de siguranta si securitate", "sa pastreze si sa arhiveze documentele in format hartie, in conditii de siguranta si securitate", "sa ajute in operatiunile de intretinere a echipamentelor de birou si sa semnaleze orice defecţiuni", "sa respecte cu strictete instructiunile de lucru, cu privire la modul de operare a echipamentelor de birou si sa ia masuri pentru prevenirea accidentelor si deteriorarilor", "sa semnaleze orice neconformitate si sa propuna masuri de remediere"],
    "responsabilitatile postului": [
        "raspunde de buna coordonare a activitatii in lipsa managementului companiei",
        "raspunde de conditiile de igiena a marfii",
        "raspunde de rezolvarea problemelor si de satisfacerea cerintelor clientului",
        "respecta instructiunile verbale si scrise date de superiori",
        "raspunde de raportarea pierderilor de orice fel (rebuturi, furturi)",
        "raspunde de corectitudinea datelor introduse in calculator"
    ],
    "sanctiuni pentru nerespectarea fisei postului sau a anexelor acestora": [
        "nerespectarea confidentialitatii salariului sanctiunea este desfacerea contraculuI de munca"
    ]    
    # Add more key-value pairs based on your .txt content
}

# Convert the dictionary to a JSON string
json_content = json.dumps(protocol_dict, indent=4)

# Write the JSON string to a new .json file
with open("protocol_for_office.json", "w") as json_file:
    json_file.write(json_content)

print("Successfully converted .txt to .json")