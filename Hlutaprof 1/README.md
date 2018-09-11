Forritun​ ​haust​ ​2017​ ​-​ ​Hlutapróf​ ​1
Fyrir hvert verkefni er til Code::Blocks project. Verkefnismappan fyrir hvert verkefni er tekin fram
í verkefnislýsingu hér að neðan. Opnið viðeigandi möpu og tvísmelið á .cbp skrána. Þá opnast
projectið. Hvert project inniheldur main.cpp skrá þar sem leysa á verkefnið. Í main.cpp skránni
er einnig verkefnislýsing á ensku.
Ekkert​ ​verkefnanna​ ​krefst​ ​þess​ ​að​ ​notuð​ ​séu​ ​nein​ ​fallasöfn​ ​önnur​ ​en​ ​<iostream>​ ​sem
notað​ ​er​ ​fyrir​ ​inntak​ ​og​ ​úttak.​ ​ ​Þau​ ​skulu​ ​öll​ ​leyst​ ​með​ ​grunnvirkjum​ ​og​ ​-segðum​ ​í​ ​C++.
Verkefnin eru 8​ talsins.
0 Krossaspurningar
Það eru engar​ ​texta- eða krossaspurningar á þessu prófi.
1. Inntak​ ​og​ ​úttak​ ​(10%)
Staðsetning: Í möppunni Exam á skjáborði vélarinnar: Mappan InputOutput
Skrifið forrit sem biður notanda um að slá inn heiltölu, síðan rauntölu og að lokum
bókstaf, skrifar síðan út heiltöluna, rauntöluna og bókstafinn.
Dæmi um keyrslu (inntak notanda undirstrikað):
Please enter an integer: 3
Please enter a real number: 4.75
Please enter a character: g
Your integer: 3
Your real number: 4.75
Your character: g
2. Meðaltal​ ​tveggja​ ​talna,​ ​notkun​ ​falls​ ​(function)​ ​(15%)
Staðsetning: Í möppunni Exam á skjáborði vélarinnar: Mappan AverageOfTwo
Forrit sem biður um tvær rauntölur og skrifar út meðaltal talnanna.
15​ stig fást fyrir að búa til fallið average og nota það til að reikna meðaltalið.
10​ stig fást fyrir rétta lausn sem notar ekki fall (öll virkni í main() falli).
Dæmi um keyrslu (inntak notanda undirstrikað):
Please enter a real number: 5.6
Please enter another real number: 3.4
The average of 5.6 and 3.4 is 4.5
3. Blökuhellirinn​ ​(10%)
Staðsetning: Í möppunni Exam á skjáborði vélarinnar: Mappan Batcave
Skrifið forrit sem biður notanda um að slá inn y​ ef hann vill sjá hverjir eru í blökuhellinum.
Ef hann slær inn y​ skrifar forritið út "Batman og Robin", annars skrifar forritið út "You are
my number one guy!".
Dæmi um keyrslu (inntak notanda undirstrikað):
Do you want to know who’s in the batcave (y=yes)? y
Batman and Robin
Annað dæmi:
Do you want to know who’s in the batcave (y=yes)? n
You are my number one guy!
4. Leynisjálf​ ​(15%)
Staðsetning: Í möppunni Exam á skjáborði vélarinnar: Mappan SecretIdentity
Skrifið forrit sem biður notanda um að slá inn b​ ef hann vill vita hver Batman er og r​ ef
hann vill vita hver Robin er. Ef notandinn slær inn b​ er skrifað út "Bjorgvin B", ef r​ þá
"Kari H" annars "Have you ever danced with the devil in the pale moon light?".
Dæmi um keyrslu (inntak notanda undirstrikað):
Please input a character, ‘b’ to learn Batman’s secret
identity, ‘r’ to learn Robins: u
Have you ever danced with the devil in the pale moon light?
5. Talnabil​ ​(10%)
Staðsetning: Í möppunni Exam á skjáborði vélarinnar: Mappan Boundaries
Skrifið forrit sem biður notanda um að slá inn lágmarkstölu, þvínæst hámarkstölu og
biður síðan um að slegin sé inn tala á bilinu frá <lágmarkstala> til og með
<hámarkstala>. Ef talan er á bilinu skrifar forritið út "Gotham city is safe ... for now." en
ef talan er ekki á bilinu biður forritið aftur um tölu á bilinu frá <lágmarkstala> til og með
<hámarkstala>. Notandinn er einungis beðinn um lág- og hámarkstölurnar í byrjun, en
forritið hættir ekki fyrr en slegin er inn tala á bilinu. Allar tölurnar eru heiltölur og gera má
ráð fyrir að notandi slái alltaf inn heiltölu.
Dæmi um keyrslu (inntak notanda undirstrikað):
Please enter a minimum integer: 4
Please enter a maximum integer: 9
Please enter an integer between 4 and 9: 17
Please enter an integer between 4 and 9: 3
Please enter an integer between 4 and 9: 9
Gotham city is safe … for now.
6. Neikvæðar​ ​og​ ​óneikvæðar​ ​tölur​ ​(15%)
Staðsetning: Í möppunni Exam á skjáborði vélarinnar: Mappan NonNegative
Skrifið forrit sem spyr hve margar heiltölur verði slegnar inn. Þvínæst biður það um
tölurnar eina og eina og notandi slær þær inn, hverja fyrir sig. Að lokum skrifar forritið út
hve margar talnanna voru neikvæðar, hve margar talnanna voru jákvæðar (og núll,
non-negative) og summu allra jákvæðu (non-negative) talnanna.
Dæmi um keyrslu (inntak notanda undirstrikað):
How many numbers will you enter: 7
Enter a number: 5
Enter a number: -5
Enter a number: 8
Enter a number: 0
Enter a number: -5
Enter a number: -5
Enter a number: 2
Negative numbers: 3
Non-negative numbers: 4
Sum of non-negative numbers: 15
7. Meðaltal​ ​margra​ ​talna​ ​(15%)
Staðsetning: Í möppunni Exam á skjáborði vélarinnar: Mappan AverageOfMany
Skrifið forrit sem biður notanda um að slá inn rauntölu. Þvínæst er notandinn spurður
hvort hann vilji slá inn aðra tölu. Ef hann slær inn y​ er hann beðinn um að slá inn aðra
rauntölu og aftur spurður hvort hann vilji slá inn aðra tölu. Forritið heldur áfram að bjóða
notandanum að slá inn nýja tölu alveg þangað til hann svarar öðru en y​. Að lokum
skrifar forritið út meðaltal allra talnanna sem notandinn sló inn.
Dæmi um keyrslu (inntak notanda undirstrikað):
Please enter a real number: 5.6
Do you wish to enter another number (y=yes): y
Please enter a real number: 5.4
Do you wish to enter another number (y=yes): y
Please enter a real number: 3.2
Do you wish to enter another number (y=yes): y
Please enter a real number: 8.7
Do you wish to enter another number (y=yes): y
Please enter a real number: 9.1
Do you wish to enter another number (y=yes): n
Average of all numbers: 6.4
8. Námundun​ ​að​ ​næstu​ ​heiltölu,​ ​notkun​ ​falls​ ​(function)​ ​(10%)
Staðsetning: Í möppunni Exam á skjáborði vélarinnar: Mappan RoundToWhole
Skrifið fallið​ ​round sem tekur inn eina rauntölu og skilar næstu heiltölu við (venjulegar
námundunarreglur gilda).
Skrifið síðan main() forrit sem biður notanda um að slá inn rauntölu, notar fallið round til
að námunda hana að næstu heiltölu og skrifar út námunduðu niðurstöðuna.
Dæmi um keyrslu (inntak notanda undirstrikað):
Please enter a real number: 5.73
5.73 rounded to the next integer is 6
Annað dæmi:
Please enter a real number: 2.19
2.19 rounded to the next integer is 2
Enn eitt dæmi:
Please enter a real number: 9.5
9.5 rounded to the next integer is 10