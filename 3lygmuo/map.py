    # Slenkstinis lygmuo (5-6): Sudarykite lentelę, kurioje matytųsi kiek pristatyta siuntų ("siuntu skaicius") bei jų bendras svoris ("svoris") skirtingais maršrutais ("marsrutas").
    # Tipinis lygmuo (7-8): Pridėkite į lentelę informaciją kiekvienam maršrutui: kiek kartų buvo sustojama skirtingose geografinėse zonose ("geografine zona").
    # Puikus lygmuo (9-10): Sudarykite lentelę, kurioje matytųsi kiek pristatyta siuntų ("siuntu s skaiciukaicius") bei aptarnauta klientų ("Sustojimo klientus") skirtingose geografinėse zonose ("geografine zona") skirtingomis savaitės dienomis ("sustojimo savaites diena").

#!/usr/bin/env python
import sys

# sys.stdin = open("duom_cut.txt","r")
#sys.stdout = open("mapout.txt","w")


zone_text = "{geografine zona="
package_text = "{siuntu skaicius="
clients_text = "{Sustojimo klientu skaicius="
weekday_text = "{sustojimo savaites diena="

for line in sys.stdin:
    line = line.strip()
    responses = line.split(sep = r"}}")
    
    for response in responses:
        data = response.split(sep = "}")
        current_zone = None
        current_package = None
        current_clients = None
        current_weekday = None

        for info in data:
            

            if info[0:len(zone_text)] == zone_text:
                current_zone = info[len(zone_text):len(info)]
            elif info[0:len(package_text)] == package_text:
                current_package = info[len(package_text):len(info)]
            elif info[0:len(clients_text)] == clients_text:
                current_clients = info[len(clients_text):len(info)]
            elif info[0:len(weekday_text)] == weekday_text:
                current_weekday = info[len(weekday_text):len(info)]
        if all(x is not None for x in [current_zone, current_package, current_clients, current_weekday]):
            # Code to execute if none of the variables are None
            print(f"{current_weekday}\t{current_zone}\t{current_package}\t{current_clients}")
        else:
            continue
            







        # print('%s\t%s' % (word, "1"))
