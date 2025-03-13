    # Slenkstinis lygmuo (5-6): Sudarykite lentelę, kurioje matytųsi kiek pristatyta siuntų ("siuntu skaicius") bei jų bendras svoris ("svoris") skirtingais maršrutais ("marsrutas").
    # Tipinis lygmuo (7-8): Pridėkite į lentelę informaciją kiekvienam maršrutui: kiek kartų buvo sustojama skirtingose geografinėse zonose ("geografine zona").
    # Puikus lygmuo (9-10): Sudarykite lentelę, kurioje matytųsi kiek pristatyta siuntų ("siuntu skaicius") bei aptarnauta klientų ("Sustojimo klientu skaicius") skirtingose geografinėse zonose ("geografine zona") skirtingomis savaitės dienomis ("sustojimo savaites diena").

#!/usr/bin/env python
import sys

# sys.stdin = open("duom_cut.txt","r")
#sys.stdout = open("mapout.txt","w")

for line in sys.stdin:
    line = line.strip()
    responses = line.split(sep = r"}}")
    
    for response in responses:
        data = response.split(sep = "}")
        for info in data:
            if info[0:17] == "{geografine zona=":
                zona = info[17:len(info)]
                if zona == "":
                    continue
                else: 
                    print(zona + "\t1")
            




        # print('%s\t%s' % (word, "1"))
