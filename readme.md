# AI Projekt

**I detta projekt har jag gjort en Math solver AI. Vad min AI gör är att den tar en bild och använder sig av en OCR(Optical Character Recognizion) eller mer bestämmt Googles OCR för att känna igen siffror och bokstäver från den inskickade bilden. Sedan använder jag mig av biblioteket sympy som är ett bibliotek som kan lösa ekvationer åt en för att lösa ekvationen på bilden och skicka tillbaka det till användaren.**

# Göra projektet själv

### Bibliotek att installera

```python
pip install opencv-python
pip install sympy
pip install google-cloud-vision
```

### Start

För att göra projektet själv så måste man först registera sig och fixa ett google cloud konto detta kan man göra [här](https://cloud.google.com/). Sedan måste du skapa ett projekt. [Klicka här](https://console.cloud.google.com/projectselector2/home/dashboard?_ga=2.259457930.1620008954.1585551559-1932650620.1583783188) för att skapa ett nytt projekt.

Sedan måste du se till så att ditt nya projekt har Vision aktiverat. Klicka [här](https://console.cloud.google.com/flows/enableapi?apiid=vision.googleapis.com&_ga=2.195898028.1620008954.1585551559-1932650620.1583783188) välj sedan samma projekt som du nyss skapade att aktivera vision på.

Det sista steget innan du kan använda Vision är att gå in [här](https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.263096844.1620008954.1585551559-1932650620.1583783188) på sidan så måste du skapa ett "service account" se till att detta konto har Role Owner, välj sedan JSON och klicka create så kommer du få en JSON fil nedladdad, se till att spara den i samma mapp som projektet. Sist för att "länka" json filen med projektet först så öppna mappen i Visual sedan klicka ctrl + ö för att öppna cmd och skriv $env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]" där path är länken till JSON filen du nyss laddade ner.

### Snyggar till bilden

I detta steg använder du opencv till att göra bilden "snyggare" eller rättare sagt tar bort allt som inte är nödvändigt. Vi tar in våran bild och gör om den till en gråskala först och sedan lägger vi på en blur för att ta bort allt onödigt.

### Bild till Text

Sedan kör man koden som innehåller inyggda funktioner som läser in en bild och gör om det till våran text.

### Räkna ut ekvationen

Sista steget är att vi tar texten eller siffrorna i vårt fall och använder sympy ett bibliotek som löser ekvationer på dem för att lösa ekvationen.

# Reflektion

### Bra saker

Google dokumentationen var väldigt lätt att följa och setupa och det fanns hur mycket exempel kod som helst. Sympy var också hyfsat lätt att använda.

### Mindre bra saker

Google vision är inte specifikt gjort för siffror eller ensklida bokstäver, utan det är gjort för ord och eftersom det inte finns något sätt att ändra det så händer det ibland om man skriver slarvigt att programmet tror att något ser ut som ett ord istället för siffror. Dessutom så funkar det inte om man skriver tex 2x utan man måste skriva 2*x för att det ska funka

### Om jag hade gjort om

Jag hade börjat med att inte slösa min tid på mnist data settet eftersom det inte funkade för min applikation. Sedan så hade google möjligheten att träna sina egna ocr och det hade jag nog gjort om jag gjorde om det.

### Vad jag har lärt mig

Jag har lärt mig mycket om olika vision system då framförallt om googles vision system. Jag har även lärt mig mycket om att träna olika stora datasets (även fast jag inte använd mig av det i slutprodukten).
