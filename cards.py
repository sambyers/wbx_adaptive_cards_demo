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

oppty_update_card = {
        'contentType': 'application/vnd.microsoft.card.adaptive',
        'content': {
            '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
            'type': 'AdaptiveCard',
            'version': '1.1',
            'body': [
                {
                    "type": "TextBlock",
                    "text": "Most recent opportunity update",
                    "weight": "Bolder",
                    "size": "Medium"
                },
                {
                    "type": "ColumnSet",
                    "columns": [
                        {
                            "type": "Column",
                            "width": "auto",
                            "items": [
                                {
                                    "type": "Image",
                                    "url": "https://pbs.twimg.com/profile_images/3647943215/d7f12830b3c17a5a9e4afcc370e3a37e_400x400.jpeg",
                                    "size": "Small",
                                    "style": "Person"
                                }
                            ]
                        },
                        {
                            "type": "Column",
                            "width": "stretch",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Matt Hidinger",
                                    "weight": "Bolder",
                                    "wrap": 'true'
                                },
                                {
                                    "type": "TextBlock",
                                    "spacing": "None",
                                    "text": "Created {{DATE(2019-08-14T06:08:39Z, SHORT)}}",
                                    "isSubtle": 'true',
                                    "wrap": 'true'
                                }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "TextBlock",
                        "text": "SE work has completed on this oppurtunity. The customer is happy with the proposed solution and has no technical objections.",
                        "wrap": 'true'
                    },
                    {
                        "type": "FactSet",
                        "facts": [
                            {
                                "title": "SE Status:",
                                "value": "Tech Close"
                            },
                            {
                                "title": "Expected Book Date:",
                                "value": "11/15/2019"
                            },
                            {
                                "title": "Assigned to:",
                                "value": "Matt Hidinger"
                            },
                            {
                                "title": "Status:",
                                "value": "Proposal"
                            }
                        ]
                    }
                ],
                "actions": [
                    {
                        "type": "Action.ShowCard",
                        "title": "Set due date",
                        "card": {
                            "type": "AdaptiveCard",
                            "body": [
                                {
                                    "type": "Input.Date",
                                    "id": "dueDate"
                                }
                            ],
                            "actions": [
                                {
                                    "type": "Action.Submit",
                                    "title": "OK"
                                }
                            ],
                            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
                        }
                    },
                    {
                        "type": "Action.ShowCard",
                        "title": "Comment",
                        "card": {
                            "type": "AdaptiveCard",
                            "body": [
                                {
                                    "type": "Input.Text",
                                    "id": "comment",
                                    "isMultiline": 'true',
                                    "placeholder": "Enter your comment"
                                }
                            ],
                            "actions": [
                                {
                                    "type": "Action.Submit",
                                    "title": "OK"
                                }
                            ],
                            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
                        }
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

