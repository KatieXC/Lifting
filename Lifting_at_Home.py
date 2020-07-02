# LIFTING AT HOME : Katie Stapleton : 6/16/2020
# Run in Jupiter Notebook

# Factor for lb/kg conversion
lb_kg_factor = 0.45359237   # = 1 lb
""" Converting Function
    Changes 
    Input -- i (input amt), flag (1 = kg to lbs, 0 = lbs to kg)
    Output -- i once converted
"""
def convert_lbs_kg(i, kg_to_lbs):
    if kg_to_lbs:
        return i / lb_kg_factor
    else:
        return i * lb_kg_factor

# List of all weights available -- in kg
available_weights_kg = [5, 2.5, 1.25, 0.5]
available_count = {5: 4, 2.5: 4, 1.25: 6, 0.5: 6}   # RESET after each call if needed
# Weight of bars -- in pounds
dumbbell_weight_kg = convert_lbs_kg(4.2, 0)
barbell_weight_kg = convert_lbs_kg(13.8, 0)

""" Finding Plates Function
    Based on the desired weight and the given weights available,
        the optimal combination of plates (minimum) needed is calculated.
    GREEDY ALGORITHM
    Input -- load_lbs(desired weight amount in pounds),
            mode(0: barbell, 1: 1xdumbbell, 2: 2xdumbbell)
            ** For mode 2, load = load per dumbbell
    Output -- plates(list of plates that should be loaded)
"""
def find_plates(load_lbs, mode):
    result_count = {5: 0, 2.5: 0, 1.25: 0, 0.5: 0}          # Returning combination array
    load = convert_lbs_kg(load_lbs, 0)                      # Convert input load to kg
    print(f"Calculating for {load_lbs}lbs ({load}kg)...")

    # First account for bar
    if mode == 0:
        load -= barbell_weight_kg   # Barbell
    elif mode == 1:
        load -= dumbbell_weight_kg  # One Dumbbell
    elif mode == 2:
        load -= dumbbell_weight_kg  # Two Dumbbells
        for w in available_count:
            available_count[w] /= 2
    else:
        print("Enter Mode")
        return {}

    # Work through possible plates
    num_plates_factor = 2
    for plate in available_weights_kg:
        temp_weight = plate*num_plates_factor
        print(f"{plate}kg...")        
        while(1):
            # Bounds-checking -- stay on plate until not possible to add
            if load - temp_weight < 0:                      # Plate too big to add to bar
                # print("Too heavy for load")
                break
            if available_count[plate] < num_plates_factor: # Not enough plates remaining
                # print("Not enough plates")
                break
            # Add plate to bar
            load -= temp_weight
            available_count[plate] -= num_plates_factor
            result_count[plate] += 1
            print(f"Add {plate}kg plate")
    # Print remaining leftover pounds and return plate count
    print(f"Remaining load = {convert_lbs_kg(load, 1)}lbs ({load}kg)")
    return result_count

""" Calling Functions """
available_count = {0.5: 6, 1.25: 6, 2.5: 4, 5: 4}
plate_count = find_plates(65,1)
print(plate_count)
# kg = ((2.5+1.25+0.5)*2)+dumbbell_weight_kg
# kg = 5
# lbs = convert_lbs_kg(kg,1)
# print (lbs)

