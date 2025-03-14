import sys

text_zona = "{geografine zona="
text_route = "{marsrutas="


for line in sys.stdin:
    line = line.strip()
    responses = line.split(sep = r"}}")
    
    for response in responses:
        data = response.split(sep = "}")
        current_zona = None
        current_route = None


        for info in data:
            

            if info[0:len(text_zona)] == text_zona:
                current_zona = info[len(text_zona):len(info)]
                
            elif info[0:len(text_route)] == text_route:
                current_route = info[len(text_route):len(info)]
                
        if all(x is not None for x in [current_route, current_zona]):
            # Code to execute if none of the variables are None
            print(f"{current_route}\t{current_zona}\t1")
        else:
            continue
            