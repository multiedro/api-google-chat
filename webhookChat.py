# DOC Referência
# https://developers.google.com/chat/how-tos/webhooks?hl=pt-br

# Construtor de Cards
# https://addons.gsuite.google.com/uikit/builder?hl=pt-br

# Cards Google Chat
# https://developers.google.com/chat/api/reference/rest/v1/cards?hl=pt-br

# Formatação dos cards
# https://developers.google.com/chat/api/reference/rest/v1/cards?hl=pt-br#TextInput

# Cards Interativas 
# https://developers.google.com/chat/design/interactivity?hl=pt-br
# https://developers.google.com/chat/how-tos/dialogs?hl=pt-br

# Bibliotecas 
# pip install httplib2


from json import dumps
from httplib2 import Http

def envia_msg():
            


            body_2 = {"cardsV2": [{"cardId": "unique-card-id",
              "card":{
                      "header": {
                        "title": "Notificações TOPdesk",
                        "subtitle": "New Ticket",
                        "imageUrl": "https://avatars.githubusercontent.com/u/14311896?s=200&v=4",
                        "imageType": "CIRCLE"
                      },
                      "sections": [
                        {
                          "header": "Dados do Ticket",
                          "collapsible": "false",
                          "uncollapsibleWidgetsCount": 1,
                          "widgets": [
                            {
                              "decoratedText": {
                                "icon": {
                                  "knownIcon": "TICKET"
                                },
                                "topLabel": "Ticket",
                                "text": "123456789"
                              }
                            },
                            {
                              "divider": {}
                            },
                            {
                              "decoratedText": {
                                "icon": {
                                  "knownIcon": "DESCRIPTION"
                                },
                                "topLabel": "Descrição do Ticket"
                                
                              }
                            },
                            {
                              "textParagraph": {
                                "text": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.  There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. Lorem Ipsum which looks reasonable.sdfghjklçpoiuytrew"
                              }
                            }
                          ]
                        }
                      ]
                    }
              
              
              }]}

            body_4=    {
          "cardsV2": [
            {
              "cardId": "unique-card-id",
              "card": {
                "header": {
                  "title": "Sasha",
                  "subtitle": "Software Engineer",
                  "imageUrl":
                  "https://developers.google.com/chat/images/quickstart-app-avatar.png",
                  "imageType": "CIRCLE",
                  "imageAltText": "Avatar for Sasha",
                },
                "sections": [
                  {
                    "header": "Contact Info",
                    "collapsible": "false",
                    "uncollapsibleWidgetsCount": 1,
                    "widgets": [
                      {
                        "decoratedText": {
                          "startIcon": {
                            "knownIcon": "EMAIL",
                          },
                          "text": "sasha@example.com",
                        }
                      },
                      {
                        "decoratedText": {
                          "startIcon": {
                            "knownIcon": "PERSON",
                          },
                          "text": "<font color=\"#80e27e\">Online</font>",
                        },
                      },
                      {
                        "decoratedText": {
                          "startIcon": {
                            "knownIcon": "PHONE",
                          },
                          "text": "+1 (555) 555-1234",
                        }
                      },
                      {
                        "buttonList": {
                          "buttons": [
                            {
                              "text": "Share",
                              "onClick": {
                                "openLink": {
                                  "url": "https://example.com/share",
                                }
                              }
                            },
                            {
                              "text": "Edit",
                              "onClick": {
                                "action": {
                                  "function": "goToView",
                                  "parameters": [
                                    {
                                      "key": "viewType",
                                      "value": "EDIT",
                                    }
                                  ],
                                }
                              }
                            },
                          ],
                        }
                      },
                    ],
                  },
                ],
              },
            }
          ],
        }


            destino = ['< URL DO SEU WEBHOOK AQUI >']

            """Hangouts Chat incoming webhook quickstart."""
            for x in destino:

                url = x
                bot_message = body_2
                message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
                http_obj = Http()
                response = http_obj.request(
                    uri=url,
                    method='POST',
                    headers=message_headers,
                    body=dumps(bot_message),
                )
                
                print(response) 
            return response,200

envia_msg()