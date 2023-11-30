# 23 nov 2023
vboxmanage commands aangemaakt via subprocess in python
# 24 nov 2023
troubleshooting van openen met chrome, chrome moet zeker pagina kunnen geladen hebben tot dathet in de history gezet word.

open chrome met ```vboxmanage guestcontrol Windows10 run --exe="/Program Files/Google/Chrome/Application/chrome.exe" --username=user --password=user123 --timeout=10000 -- facebook.com``` timeout nodig voor op te slaan.

## prefetch
calc.exe kan niet worden geopend met verschillende cmd args om meer prefetch files te creeren

# 26 nov 2023
proberen van het veranderen van de tijd zonder de vm te moeten afsluiten, chrome verwijderd de history niet als die via cmd word geopend maar wel soms als die via de gui word geopend

# 30 nov 2023
Selenium geinstalleerd, kan websites openen en krijg ze te zien in de history. nu testen in de toekomst.
kan websites openen in de toekomst, als je chrome 30sec laat openstaan en dan de history bekijkt zie je dat die verwijderd word.


selenium word opgestart on boot in windows 10 en met de juiste gebruiker door taskscheduler te gebruiken