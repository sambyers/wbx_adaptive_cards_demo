input_card = {
            'contentType': 'application/vnd.microsoft.card.adaptive',
            'content': {
                '$schema': 'http://adaptivecards.io/schemas/adaptive-card.json',
                'type': 'AdaptiveCard',
                'version': '1.1',
                'body': [
                    {
                        'type': 'TextBlock',
                        'text': 'Please enter your zip code for weather...',
                        'size': 'Large',
                        'color': 'Good'
                    },
                    {
                        'type': 'Input.Text',
                        'id': 'zip',
                        'placeholder': '23060',
                        'style': 'zip'
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