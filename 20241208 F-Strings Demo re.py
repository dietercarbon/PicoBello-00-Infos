Zeitpunkte = ["10:05","10:30","11","11:31","12:01"]
Messwerte01 = [121.23456,20.22,21.65432,21,21.5]
Messwerte02 = [22.2322456,21.2,23.11432,22,21.6]
print (Zeitpunkte)

print (Messwerte01)
print (Messwerte02)
print ()
print ()

for i in range(5):
    print(Zeitpunkte[i], Messwerte01[i], Messwerte02[i])
print("Schleife beendet!")

print ()
print ()
print(f"{'Zeit':>10}{'Messwert 1':>15}{'Messwert 2':>15}")
print("-" * 40)
print("1234567890123456789012345678901234567890")
print("-" * 40)

for i in range(len(Zeitpunkte)):
    print(f"{Zeitpunkte[i]:>10}{Messwerte01[i]:>15.3f}{Messwerte02[i]:>15.2f}")

print("Schleife beendet!")