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
                    'ts': And(Use(str), lambda time: True if re.search(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', time) else False, error='ts must be in format: YYYY-MM-DD HH-MM-SS'),
                    'action': And(Use(str)),
                    'unit': And(Use(str), lambda s: s in valid_units, error=f'unit must be one of the following: {", ".join(valid_units)}.'),
                    'quantity': And(Use(int), lambda n: n > 0, error='quanitity must be able to be converted into an integer, and greater than zero.')
                }]
            })

        data = schema.validate(input)

        # get day of the first action and ensure that all other actions take place on the same day
        ts_day = input['actions'][0]['ts'][:10]
        for action in input['actions']:
            if action['ts'][:10] != ts_day:
                return {'error': 'all timestamps (ts) on all actions must be on the same day.'}

        return data

    except SchemaError as e:
        # cleaning up error message for case when key is missing
        if 'Missing key:' in str(e):
            return {'error': str(e).split('\n')[-1]}

        return {'error': e}

    

    