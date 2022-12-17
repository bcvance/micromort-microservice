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
                    'quantity': And(Use(int), error='quanitity must be able to be converted into an integer')
                }]
            })

        data = schema.validate(input)
        return data
    except SchemaError as e:
        return {'error': e}

    

    