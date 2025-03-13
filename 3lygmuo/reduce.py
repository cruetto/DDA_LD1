import sys

overall_weekday = ""
overall_zone = ""
overall_count_package = 0
overall_count_client = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    current_weekday, current_zone, current_package_count, current_client_count = line.split('\t')

    
    try:
        current_package_count = int(current_package_count)
        current_client_count = int(current_client_count)
    except:
        continue
    
    # if every variable was initialised
    isNotNone = (overall_count_package != 0 and overall_count_client != 0 and overall_weekday != "" and overall_zone != "")

    if overall_weekday == current_weekday and overall_zone == current_zone:
        
        overall_count_package += current_package_count
        overall_count_client += current_client_count
    else:
        # if keys changed: print and input new values
        if isNotNone:
            print(f"{overall_weekday}\t{overall_zone}\t{overall_count_package}\t{overall_count_client}")
        overall_weekday = current_weekday
        overall_zone = current_zone
        overall_count_package = current_package_count
        overall_count_client = current_client_count

# input last values
if isNotNone:
    print(f"{overall_weekday}\t{overall_zone}\t{overall_count_package}\t{overall_count_client}")

