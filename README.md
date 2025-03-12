# Tool for making fake screenshot to proove transactions on Discord

## How to use?
1. Download zip or rar from release https://github.com/naczos2137/Discord-Screenshot-Faker/releases/tag/Main
2. Unzip
3. In `data\trx_data.txt` put transaction info:
   ```
   money amount
   client nick
   date

   money amount
   client nick
   date

   etc.
   ```
4. In `data\conversations` put scripts for conversations. Rules:
   - 1 line = 1 message
   - all lines must start from tag: `k: ` for client, `i: ` for you (seller)
   - `{cena}` will be changed to money amount
##### You can use AI to generate them. Example prompt:
```
Generate a conversation between two people. This is a Discord chat between teenagers.  

One of them is a computer science student who offers paid help with programming and other computer-related issues.  

Come up with a service. The IT student must say:  
"{cena} PLN payment via BLIK: 123456789, recipient: Maciej Chomicz, in the title your Discord nickname"  

Every conversation must end with "join vc".  

Do not include a specific price—leave **{cena}** as a placeholder.  

The conversation should be between **6-16 messages** long.  

Write only **one conversation** and nothing else.  

The messages should be in the format:  
**i:** (IT student’s message)  
**k:** (client’s message)  

Teenagers should use **short, casual language**.  

Example conversation #1:  
k: yo  
i: yo, what do you need?  
k: can you configure an anti-cheat for MC 1.8?  
i: what engine?  
k: vanilla  
i: sure. {cena} PLN payment via BLIK: 123456789, recipient: Maciej Chomicz, in the title your Discord nickname  
k: sent  
i: join vc  

Example conversation #2:  
k: quick question  
i: what’s up?  
k: my friend said you do FiveM scripts. how much to fix a job script?  
i: sure. {cena} PLN payment via BLIK: 123456789, recipient: Maciej Chomicz, in the title your Discord nickname  
k: how fast can you do it? need it ASAP  
i: today  
k: ok sent  
i: join vc
```
```
Wygeneruj mi rozmowe między 2 osobami. Jest to rozmowa na discordzie między nastolatkami. 
Jeden z nich jest studentem informatyki i odpłatnie pomaga z programowaniem i innymi komputerowymi problemami.
Wymyśl jakąś usługę. Informatyk musi powiedzieć "{cena}zł płątność blik: 123456789, odbiorca: Maciej Chomicz, w tytule twój nick dc" i każda rozmowa ma się kończyć "zapraszam vc". 
Ceny nie wpisuj. Zostaw {cena}.
Konwersacja powinna być długości 6-16 wiadomości. Napisz samą 1 konwersację. Nic więcej 
Mają pisać mocno skrótowo tak jak nastolatkowie.
Wiadomości mają być zapisanie w formacie:
i: wiadomość informatyka
k: wiadomość klienta
Przykładowa rozmowa nr 1:
k: siema
i: siema. w czym pomóc?
k: umiesz konfigurować antycheat do mc 1.8
i: jaki silnik?
k: vanilla
i: pewnie. {cena}zł płątność blik: 123456789, odbiorca: Maciej Chomicz, w tytule twój nick dc 
k: zapłaciłem
i: zapraszam vc
Przykładowa rozmowa nr 2:
k: mam pytanie
i: jakie?
k: kolega mi powiedział, że ogarniasz skrypty do fivem. za ile naprawisz skrypt do prac
i: pewnie. {50}zł płątność blik: 123456789, odbiorca: Maciej Chomicz, w tytule twój nick dc
k: a na kiedy byś ogarną? ASAP potrzebuje
i: jeszcze dziś
k: dobra przelane. 
i: zapraszam vc
```
5. **(optional)** In `icons` put icons of clients and you. Name of files must be `name.png`. This step is optional. If you don't put icon it will be randomly choosen from `icons\random`
6. Run `Discord-Screenshot-Faker.exe` and put your (seller) nickname in app
7. Screenshots are in `output`
### Additional info:
You can put more scripts in `data\conversations` than in `data\trx_data.txt`. Then nicks will be randomly choosen from `data\nicki.txt`
