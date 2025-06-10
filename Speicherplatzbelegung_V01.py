import os
import gc

def dateigroessen_liste(pfad="/"):
    print("📄 Dateigrößen im Flash-Speicher (in KB):\n")
    gesamt_flash_bytes = 0

    for datei in os.listdir(pfad):
        voller_pfad = pfad + "/" + datei if pfad != "/" else "/" + datei
        try:
            info = os.stat(voller_pfad)
            groesse = info[6]
            gesamt_flash_bytes += groesse
            print("{:<20} {:>8.2f} KB".format(datei, groesse / 1024))
        except OSError:
            pass

    # Flash-Speicherstatistik
    stats = os.statvfs(pfad)
    block_size = stats[0]
    total_blocks = stats[2]
    free_blocks = stats[3]

    total_flash = block_size * total_blocks
    free_flash = block_size * free_blocks

    print("\n📦 Flash-Speicherübersicht:")
    print("Dateien gesamt     : {:>8.2f} KB".format(gesamt_flash_bytes / 1024))
    print("Flash insgesamt    : {:>8.2f} KB".format(total_flash / 1024))
    print("Flash frei         : {:>8.2f} KB".format(free_flash / 1024))

    # RAM-Nutzung
    print("\n🧠 RAM-Nutzung zur Laufzeit:")
    gc.collect()
    total_ram = gc.mem_alloc() + gc.mem_free()
    print("RAM insgesamt      : {:>8.2f} KB".format(total_ram / 1024))
    print("RAM verwendet      : {:>8.2f} KB".format(gc.mem_alloc() / 1024))
    print("RAM frei           : {:>8.2f} KB".format(gc.mem_free() / 1024))

# Aufruf
dateigroessen_liste()
