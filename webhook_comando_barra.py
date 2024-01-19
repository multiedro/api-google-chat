# DOC Referência
# https://developers.google.com/chat/how-tos/slash-commands?hl=pt-br


# Bibliotecas 
# pip install google-cloud-pubsub Flask


from flask import Flask, request,jsonify
import json


app = Flask(__name__)


def open_dialog():
  """Opens a dialog in Google Chat.

  Args:
      request (Mapping[str, Any]): the event object from Chat API.

  Returns:
      Mapping[str, Any]: open a Dialog in response to a card's button click.
  """
  return {
    'action_response': {
      'type': 'DIALOG',
      'dialog_action': {
        'dialog': {
          'body': {
            'sections': [
              {
                'header': 'Add new contact',
                'widgets': [
                  {
                    'textInput': {
                      'label': 'Name',
                      'type': 'SINGLE_LINE',
                      'name': 'name'
                    }
                  },
                  {
                    'textInput': {
                      'label': 'Address',
                      'type': 'MULTIPLE_LINE',
                      'name': 'address'
                    }
                  },
                  {
                    'decoratedText': {
                      'text': 'Add to favorites',
                      'switchControl': {
                        'controlType': 'SWITCH',
                        'name': 'saveFavorite'
                      }
                    }
                  },
                  {
                    'decoratedText': {
                      'text': 'Merge with existing contacts',
                      'switchControl': {
                        'controlType': 'SWITCH',
                        'name': 'mergeContact',
                        'selected': True
                      }
                    }
                  },
                  {
                    'buttonList': {
                      'buttons': [
                        {
                          'text': 'Next',
                          'onClick': {
                            'action': {
                              'function': 'open_sequential_dialog'
                            }
                          }
                        }
                      ]
                    }
                  }
                ]
              }
            ]
          }
        }
      }
    }
  }

def open_sequential_dialog():
  """Opens a second dialog that lets users add more contact details.

  Args:
      request (Mapping[str, Any]): the event object from Chat API.

  Returns:
      Mapping[str, Any]: open a Dialog in response to a card's button click.
  """
  return {
    'action_response': {
      'type': 'DIALOG',
      'dialog_action': {
        'dialog': {
              'body': {
                'sections': [
                  {
                    'header': 'Add new contact',
                    'widgets': [
                      {
                        'textInput': {
                          'label': 'Notes',
                          'type': 'MULTIPLE_LINE',
                          'name': 'notes'
                        }
                      },
                      {
                        'selectionInput': {
                          'type': 'RADIO_BUTTON',
                          'label': 'Contact type',
                          'name': 'contactType',
                          'items': [
                            {
                              'text': 'Work',
                              'value': 'Work',
                              'selected': False
                            },
                            {
                              'text': 'Personal',
                              'value': 'Personal',
                              'selected': False
                            }
                          ]
                        }
                      },
                      {
                        'buttonList': {
                          'buttons': [
                            {
                              'text': 'Submit',
                              'onClick': {
                                'action': {
                                  'function': 'receive_dialog',
                                  'parameters': [
                                    {
                                      'key': 'receiveDialog',
                                      'value': 'receiveDialog'
                                    }
                                  ]
                                }
                              }
                            }
                          ]
                        },
                        'horizontalAlignment': 'END'
                      }
                    ]
                  }
                ]
              }
        }
      }
    }
  }


def receive_dialog():

    print(f'Passou pelo Receive Dialog')

    return {
      'actionResponse': {
        'type': 'DIALOG',
        'dialogAction': {
          'actionStatus': 'OK'
        }
      }
    }


@app.route('/testechat', methods=['POST','GET'])
def chat():
    header = request.headers
    data = request.json  # Dados recebidos no formato JSON
    print(f'Cabeçalho da requisição\n')
    print(data)
    print(f'------------------------------------')
    print(f'Dados da requisição\n')

    referer_url = request.headers.get('Referer')

    # Codigo para responder a Primeira parte do codigo
    try:
      comando_id = int(data['message']['slashCommand']['commandId'])
      comando_texto = data['message']['formattedText']
      user_name = data['user']['name']
      usuario_display_name = data['user']['displayName'] 
    except Exception as error:
        comando_id = 0
        comando_texto = data['message']['formattedText']
        user_name = data['user']['name']
        usuario_display_name = data['user']['displayName'] 
        pass
        

    # Codigo para responder a Segunda parte do codigo

    tipo_mensagem = data['type']
    print(f'------------------------------------')
    print(f'Referer_url {referer_url}')
    print(f'Tipo de Mensagem {tipo_mensagem}')
    #print(f'Comando Recebido {comando_id}')
    print(f'Comando Texto {comando_texto}')
    print(f'User {user_name}')
    print(f'Display Name {usuario_display_name}')
    print(f'------------------------------------')

    if tipo_mensagem == "MESSAGE":

        if comando_id == 1 :

            body_1 ={
            "text": "Olá *"+usuario_display_name+"*, Este e um bot e você digitou a opção `"+comando_texto+"` Esta e a Opção de ajuda com o comando `"+str(comando_id)+"` seu user e: `"+user_name+"`",
                # "privateMessageViewer": {
                # "name": str(user_name)
                # },
            }

            return body_1
        
        if comando_id == 2 :


            return {
                    'action_response': {
                    'type': 'DIALOG',
                    'dialog_action': {
                        'dialog': {
                        'body': {
                            'sections': [
                            {
                                'header': 'Add new contact',
                                'widgets': [
                                {
                                    'textInput': {
                                    'label': 'Name',
                                    'type': 'SINGLE_LINE',
                                    'name': 'name'
                                    }
                                },
                                {
                                    'textInput': {
                                    'label': 'Address',
                                    'type': 'MULTIPLE_LINE',
                                    'name': 'address'
                                    }
                                },
                                {
                                    'decoratedText': {
                                    'text': 'Add to favorites',
                                    'switchControl': {
                                        'controlType': 'SWITCH',
                                        'name': 'saveFavorite'
                                    }
                                    }
                                },
                                {
                                    'decoratedText': {
                                    'text': 'Merge with existing contacts',
                                    'switchControl': {
                                        'controlType': 'SWITCH',
                                        'name': 'mergeContact',
                                        'selected': True
                                    }
                                    }
                                },
                                {
                                    'buttonList': {
                                    'buttons': [
                                        {
                                        'text': 'Next',
                                        'onClick': {
                                            'action': {
                                            'function': 'open_sequential_dialog'
                                            }
                                        }
                                        }
                                    ]
                                    }
                                }
                                ]
                            }
                            ]
                        }
                        }
                    }
                    }
                }
        else:
            
            resposta_texto = "Olá obrigado por entrar em contato."

            body_else ={
            "text": str(resposta_texto)
            }

            return body_else
        

    if tipo_mensagem == "CARD_CLICKED":

        print(f'CARD CLICKED')
        print(data)

        try:
            
            funcao_invocada = data['common']['invokedFunction']

        except Exception as error:

            funcao_invocada = ""
            print(f'Codigo do erro : {error}')

            pass


        if funcao_invocada == 'open_dialog':
            return open_dialog()

        elif funcao_invocada == 'open_sequential_dialog':
            return open_sequential_dialog()

        elif funcao_invocada == "receive_dialog":
            return receive_dialog()

        else:
            return {
            'cardsV2': [{
                'cardId': 'addContact',
                'card': {
                'header': {
                    'title': 'Rolodex',
                    'subtitle': 'Manage your contacts!',
                    'imageUrl': 'https://www.gstatic.com/images/branding/product/2x/contacts_48dp.png',
                    'imageType': 'CIRCLE'
                },
                'sections': [
                    {
                    'widgets': [
                        {
                        'buttonList': {
                            'buttons': [
                            {
                                'text': 'Add Contact',
                                'onClick': {
                                        'action': {
                                        'function': 'open_dialog',
                                        'interaction': 'OPEN_DIALOG'
                                        }
                                }
                            }
                            ]
                        }
                        }
                    ]
                    }
                ]
                }
            }]
            }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)