quick_deal_info_card = {
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

add_contact_card = {
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
                    'text': 'Add SFDC End Customer Contact',
                    'horizontalAlignment': 'Center'
                },
                {
                    'type': 'Input.Text',
                    'placeholder': 'First Name',
                    'style': 'text',
                    'id': 'fName'
                },                {
                    'type': 'Input.Text',
                    'placeholder': 'Last Name',
                    'style': 'text',
                    'id': 'lName'
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
                    'type': 'TextBlock',
                    'text': 'Add this contact to which of your accounts?'
                },
                {
                    'type': 'Input.ChoiceSet',
                    'id': 'CompactSelectVal',
                    'value': '1',
                    'choices': [
                        {
                            'title': 'Customer 1',
                            'value': 'c1'
                        },
                        {
                            'title': 'Customer 2',
                            'value': 'c2'
                        },
                        {
                            'title': 'Customer 3',
                            'value': 'c3'
                        },
                        {
                            'title': 'Customer 4',
                            'value': 'c4'
                        },
                        {
                            'title': 'Customer 5',
                            'value': 'c5'
                        }
                    ]
                },
                {
                    'type': 'TextBlock',
                    'text': 'Job Function'
                },
                {
                    'type': 'Input.ChoiceSet',
                    'id': 'jFunction',
                    'value': '1',
                    'choices': [
                        {
                            'title': 'Network Management',
                            'value': 'nm'
                        },
                        {
                            'title': 'Engineering',
                            'value': 'eng'
                        },
                        {
                            'title': 'Operations',
                            'value': 'ops'
                        },
                        {
                            'title': 'Technical Support',
                            'value': 'ts'
                        }
                    ]
                },
                {
                    'type': 'TextBlock',
                    'text': 'Job Level'
                },
                {
                    'type': 'Input.ChoiceSet',
                    'id': 'jobLevel',
                    'value': '1',
                    'choices': [
                        {
                            'title': 'CxO',
                            'value': 'CxO'
                        },
                        {
                            'title': 'Director',
                            'value': 'Director'
                        },
                        {
                            'title': 'Senior Manager',
                            'value': 'Senior Manager'
                        },
                        {
                            'title': 'Manager',
                            'value': 'Manager'
                        },
                        {
                            'title': 'Individual Contributer',
                            'value': 'Individual Contributer'
                        }
                    ]
                },
                {
                    'type': 'Input.Toggle',
                    'title': 'Decision maker?',
                    'id': 'dMaker',
                    'value': 'false',
                    'wrap': 'false'
                },
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

