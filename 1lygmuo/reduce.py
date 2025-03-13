import sys

overall_route = ""
overall_package_count = 0
overall_weight = 0


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    current_route, current_package_count, current_weight = line.split('\t')

    # Check for incorrect data
    try:
        current_package_count = int(current_package_count)
        current_weight = float(current_weight)
    except:
        continue
    
    # if every variable was initialised
    isNotNone = (overall_weight != 0 and overall_package_count != 0 and overall_route != "")

    if overall_route == current_route:
        
        overall_weight += current_weight
        overall_package_count += current_package_count
    else:
        # if keys changed: print and input new values
        if isNotNone:
            print(f"{overall_route}\t{overall_package_count}\t{round(overall_weight, 2)}")
        overall_route = current_route
        overall_package_count = current_package_count
        overall_weight = current_weight

# input last values
if isNotNone:
    print(f"{overall_route}\t{int(overall_package_count)}\t{round(overall_weight, 2)}")

