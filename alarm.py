# projet-alarme
from datetime import datetime
import time
import winsound

print("=== ALARME PROGRAMMÉE ===")
print("L'alarme sonnera automatiquement à 15:32.")
print("En attente...")

heure_alarme = "15:44"

while True:
    maintenant = datetime.now().strftime("%H:%M")

    if maintenant == heure_alarme:
        print("\n🔔🔔 ALARME ! Il est 15:32 🔔🔔\n")

        for i in range(5):
            winsound.Beep(1200, 300)
            time.sleep(0.4)

        break

    time.sleep(1)
