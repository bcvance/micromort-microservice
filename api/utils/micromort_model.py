def calculate_micromorts(validated_dict):

    # in my rough markup of the model, each unit gets a given micromort per 1 quanitity of that unit, as represented by the below dictionary.
    unit_micromorts = {'mile': 20, 'floor': 15, 'minute': 10, 'quantity': 10}
    total_micromorts = 0
    for action in validated_dict['actions']:
        # if commute has maxed out micromorts at 1,000,000, return 1,000,000.
        if total_micromorts >= 1000000: return 1000000

        # if risk in micromorts is greater than zero but less than one, return 1

        # iterate through all actions in the input, multiplying the unit by the quantity and adding to the total micromorts.
        total_micromorts += unit_micromorts[action['unit']]*action['quantity']

    if 0 < total_micromorts < 1: return 1

    return int(total_micromorts)