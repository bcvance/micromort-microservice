import re
from schema import Schema, And, Use, SchemaError

# list of currently valid units, defined separately here for easy addition of more units in v2
valid_units = ['mile', 'floor', 'minute', 'quantity']

def validate_input(input):
    ''' Accepts entire input objects and returns either the validated object or a dictionary 
        with an error message. '''

    # this schema validates the input object keys and values for both type and value/format where applicable
    try:
        schema = Schema({
                'commuterID': And(Use(str), lambda id: True if re.search(r'^COM-\d+$', id) else False, error='commuterId must be in format: COM-[integer]'),
                'actions': [{
                    # regex tests for correct formatting based on examples in project directions, as well as 
                    # valid ranges for values (e.g. month must be in range 1-12, hour must be in range 0-24, etc.)
                    'ts': And(Use(str), lambda time: True if re.search(r'^\d{4}-\b([1-9]|0[1-9]|1[0-2])\b-\b([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])\b \b([0-9]|0[0-9]|1[0-9]|2[0-4])\b:\b([0-9]|0[0-9]|[1-5][0-9]|60)\b:\b([0-9]|0[0-9]|[1-5][0-9]|60)\b$', time) else False, error='ts must be in format: YYYY-MM-DD HH:MM:SS and all values must be in valid range (e.g. month must be in range 1-12, hour in range 0-24'),
                    'action': And(Use(str)),
                    'unit': And(Use(str), lambda s: s in valid_units, error=f'unit must be one of the following: {", ".join(valid_units)}.'),
                    'quantity': And(Use(float), lambda n: n > 0.0, error='quantity must be able to be converted into a float (decimal number), and greater than zero.')
                }]
            })

        data = schema.validate(input)

        # get day of the first action and ensure that all other actions take place on the same day
        ts_day = input['actions'][0]['ts'].split()[0]
        for action in input['actions']:
            if action['ts'].split()[0] != ts_day:
                return {'error': 'all timestamps (ts) on all actions must be on the same day.'}

        return data

    except SchemaError as e:
        # cleaning up error message for case when key is missing
        if 'Missing key:' in str(e):
            return {'error': str(e).split('\n')[-1]}

        return {'error': e}

    

    