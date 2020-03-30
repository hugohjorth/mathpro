# AI Projekt

**I detta projekt har jag gjort en Math solver AI. Vad min AI gör är att den tar en bild och använder sig av en OCR(Optical Character Recognizion) eller mer bestämmt Googles OCR för att känna igen siffror och bokstäver från den inskickade bilden. Sedan använder jag mig av biblioteket asdasdasdasd som är ett bibliotek som kan lösa ekvationer åt en för att lösa ekvationen på bilden och skicka tillbaka det till användaren.**

#Göra projektet själv

### Start

För att göra projektet själv så måste man först registera sig och fixa ett google cloud konto detta kan man göra [här](https://cloud.google.com/). Sedan måste du skapa ett projekt. [Klicka här](https://console.cloud.google.com/projectselector2/home/dashboard?_ga=2.259457930.1620008954.1585551559-1932650620.1583783188) för att skapa ett nytt projekt.

Sedan måste du se till så att ditt nya projekt har Vision aktiverat. Klicka [här](https://console.cloud.google.com/flows/enableapi?apiid=vision.googleapis.com&_ga=2.195898028.1620008954.1585551559-1932650620.1583783188) välj sedan samma projekt som du nyss skapade att aktivera vision på.

Det sista steget innan du kan använda Vision är att gå in [här](https://console.cloud.google.com/apis/credentials/serviceaccountkey?_ga=2.263096844.1620008954.1585551559-1932650620.1583783188) på sidan så måste du skapa ett "service account" se till att detta konto har Role Owner, välj sedan JSON och klicka create så kommer du få en JSON fil nedladdad, se till att spara den i samma mapp som projektet. Sist för att "länka" json filen med projektet först så öppna mappen i Visual sedan klicka ctrl + ö för att öppna cmd och skriv $env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]" där path är länken till JSON filen du nyss laddade ner


