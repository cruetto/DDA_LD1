import sys

overall_zona = ""
overall_route = ""
overall_num = 0


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    current_route, current_zona, current_num = line.split('\t')

    # Check for incorrect data
    try:
        current_num = int(current_num)

    except:
        continue
    
    # if every variable was initialised
    isNotNone = (overall_zona != "" and overall_route != "")

    if overall_route == current_route and overall_zona == current_zona:
        
        overall_num += current_num

    else:
        # if keys changed: print and input new values
        if isNotNone:
            print(f"{overall_route}\t{overall_zona}\t{overall_num}")
        overall_route = current_route
        overall_zona = current_zona
        overall_num = 0

# input last values
if isNotNone:
    print(f"{overall_route}\t{overall_zona}\t{overall_num}")

