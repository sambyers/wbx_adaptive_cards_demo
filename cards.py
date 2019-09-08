input_card = {
            'contentType': 'application/vnd.microsoft.card.adaptive',
            'content': {
                '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
                'type': 'AdaptiveCard',
                'version': '1.1',
                'body': [
                    {
                        'type': 'TextBlock',
                        'text': 'Enter Deal ID for quick status:',
                        'size': 'Large'
                    },
                    {
                        'type': 'Input.Number',
                        'id': 'dealId',
                        'placeholder': '1234567890'
                    }
                ],
                'actions': [
                    {
                        'type': 'Action.Submit',
                        'title': 'Submit'
                    }
                ]
            }
        }

input_demo_card = {
    'contentType': 'application/vnd.microsoft.card.adaptive',
    'content': {
        '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
        'type': 'AdaptiveCard',
        'version': '1.1',
        'body': [
            {
                'type': 'TextBlock',
                'size': 'Medium',
                'weight': 'Bolder',
                'text': 'Input.Text elements',
                'horizontalAlignment': 'Center'
            },
            {
                'type': 'Input.Text',
                'placeholder': 'Name',
                'style': 'text',
                'id': 'SimpleVal'
            },
            {
                'type': 'Input.Text',
                'placeholder': 'Homepage',
                'style': 'Url',
                'id': 'UrlVal'
            },
            {
                'type': 'Input.Text',
                'placeholder': 'Email',
                'style': 'Email',
                'id': 'EmailVal'
            },
            {
                'type': 'Input.Text',
                'placeholder': 'Phone',
                'style': 'Tel',
                'id': 'TelVal'
            },
            {
                'type': 'Input.Text',
                'placeholder': 'Comments',
                'style': 'text',
                'isMultiline': 'true',
                'id': 'MultiLineVal'
            },
            {
                'type': 'Input.Number',
                'placeholder': 'Quantity',
                'min': '-5',
                'max': '5',
                'value': '1',
                'id': 'NumVal'
            },
            {
                'type': 'Input.Date',
                'placeholder': 'Due Date',
                'id': 'DateVal',
                'value': '2017-09-20'
            },
            {
                'type': 'Input.Time',
                'placeholder': 'Start time',
                'id': 'TimeVal',
                'value': '16:59'
            },
            {
                'type': 'TextBlock',
                'size': 'Medium',
                'weight': 'Bolder',
                'text': 'Input.ChoiceSet',
                'horizontalAlignment': 'Center'
            },
            {
                'type': 'TextBlock',
                'text': 'What color do you want? (compact)'
            },
            {
                'type': 'Input.ChoiceSet',
                'id': 'CompactSelectVal',
                'value': '1',
                'choices': [
                    {
                        'title': 'Red',
                        'value': '1'
                    },
                    {
                        'title': 'Green',
                        'value': '2'
                    },
                    {
                        'title': 'Blue',
                        'value': '3'
                    }
                ]
            },
            {
                'type': 'TextBlock',
                'text': 'What colors do you want? (multiselect)'
            },
            {
                'type': 'Input.ChoiceSet',
                'id': 'MultiSelectVal',
                'isMultiSelect': 'true',
                'value': '1,3',
                'choices': [
                    {
                        'title': 'Red',
                        'value': '1'
                    },
                    {
                        'title': 'Green',
                        'value': '2'
                    },
                    {
                        'title': 'Blue',
                        'value': '3'
                    }
                ]
            },
            {
                'type': 'TextBlock',
                'size': 'Medium',
                'weight': 'Bolder',
                'text': 'Input.Toggle',
                'horizontalAlignment': 'Center'
            },
            {
                'type': 'Input.Toggle',
                'title': 'I accept the terms and conditions (True/False)',
                'id': 'AcceptsTerms',
                'value': 'false',
                'wrap': 'false'
            },
            {
                'type': 'Input.Toggle',
                'title': 'Red cars are better than other cars',
                'valueOn': 'RedCars',
                'valueOff': 'NotRedCars',
                'id': 'ColorPreference',
                'value': 'NotRedCars',
                'wrap': 'false'
            }
        ],
        'actions': [
            {
                'type': 'Action.Submit',
                'title': 'Submit',
                'data': {
                    'id': '1234567890'
                }
            }
        ]
    }
}