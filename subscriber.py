# DOC Referência
# https://cloud.google.com/python/docs/reference/pubsub/latest


# Bibliotecas 
# pip install google-cloud-pubsub


import json
from google.auth import jwt
from google.cloud import pubsub_v1

project_id = "< ID DO SEU PROJETO AQUI >"
topic_id = "< ID DO SEU TOPICO AQUI >"
subscription_id = "< ID DO SEU SUBSCRIPTION ID AQUI >"

# Number of seconds the subscriber should listen for messages

timeout = 8600

service_account_info = json.load(open("< SUA SERVICE ACCOUNT AQUI>"))

audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

credentials = jwt.Credentials.from_service_account_info(

    service_account_info, audience=audience

)

subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_id}`

subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):

    #Imprime a mensagem bruta recebida do google
    #print("Received message: {}".format(message))
    message.ack()
    #Imprime a mensager recebida e decodificada
    print(str(message.data.decode('utf-8')))

    # further process received message

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print("Listening for messages on {}..\n".format(subscription_path))

with subscriber:

    try:

        # When `timeout` is not set, result() will block indefinitely,
        #Aqui vai encerrar o monitoramento quando o timeout for atingido
        #streaming_pull_future.result(timeout=timeout)
        #Desta forma vai ficar o tempo todo monitorando novas mensagens
        streaming_pull_future.result()

    except TimeoutError:

        streaming_pull_future.cancel()