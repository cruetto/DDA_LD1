import sys

text_package_num = "{siuntu skaicius="
text_weight = "{svoris="
text_route = "{marsrutas="


for line in sys.stdin:
    line = line.strip()
    responses = line.split(sep = r"}}")
    
    for response in responses:
        data = response.split(sep = "}")
        current_package_num = None
        current_weight = None
        current_route = None


        for info in data:
            

            if info[0:len(text_package_num)] == text_package_num:
                current_package_num = info[len(text_package_num):len(info)]
                
            elif info[0:len(text_weight)] == text_weight:
                current_weight = info[len(text_weight):len(info)]
                
            elif info[0:len(text_route)] == text_route:
                current_route = info[len(text_route):len(info)]
                
        if all(x is not None for x in [current_route, current_weight, current_package_num]):
            # Code to execute if none of the variables are None
            print(f"{current_route}\t{current_package_num}\t{current_weight}")
        else:
            continue
            