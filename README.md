# Scripts para aprendizado e demonstração da API do Google Chat

 Repositório de códigos e materiais de desenvolvimento com exemplos de codigo da api do Google Chat.

<p float="left">
  <img src="https://play-lh.googleusercontent.com/yC17R-QYEZLmTMB7hD8KRjnWu6pJ4qNsdNQibLw8Z07kyY08IRbS89z7kATx75SR9A" alt="Google Chat" width="150" />
</p>

<br>

<summary>Tecnologias utilizadas no desenvolvimento e testes dos scripts</summary>
<p>

---
|Descrição       | Versão  | Supported          |
| -------------- | ------- | ------------------ |
| Python         | 3.10    | :white_check_mark: |
| VScode         | 1.xx    | :white_check_mark: |
| Google chat    | v1.0    | :white_check_mark: |
| workspaceevents| v1beta  | :white_check_mark: |
---


</p>

<summary><h4>Detalhe</h4></summary>


### **Resumo:**
Para utilização da biblioteca de eventos do Google Chat (workspaceevents), e necessario perir autorização junto a o Google por meio do preenchimento do Formularios 
que esta neste [link](https://developers.google.com/workspace/preview?hl=pt-br#apply), o processo de aprovação pode demorar até uma semana para ocorrer a liberação.

### **Histórico de Revisões:**
---
|Data           |Editor(es) Resp.                           |Versão dos códigos    |Obervações:
|---------------|-------------------------------------------|----------------------|-----------------------------------------
|17/01/2024     |Rodrigo Martins                            |1.1                   |Primeira versão funcional dos códigos

### **Documentação de origem:**

Em todos os scrips no seu cabeçalho será encontrado o link da documentação de origem/referencia, e as bibliotecas necessarias para rodar cada script, observe que neste
repositorio temos um arquivo requirements.txt, que contém todas as bibliotecas instaladas no ambiente que esta sendo apresentado no treinamento

<details><summary><h4>Inscrevendo em Eventos</h4></summary>
<p>Se já tiver inscrito no programa do beta e ja recebeu o email liberando os seus projetos para uso antecipado da API pode seguir os proximos passos.

O codigo para se inscrever em eventos de um grupo ou conversa especifica será o script `create_subscription.py` , observe que dentro do script você devera substituir alguns parametros conforme exemplo abaixo:</p>

1) Este código ira utilizar a autenticação de usuario, sendo assim gere a sua chave e informe o path substituindo o valor (< CREDENCIAL DE USUARIO AQUI >) no local informado abaixo:

```
flow = InstalledAppFlow.from_client_secrets_file('< CREDENCIAL DE USUARIO AQUI >', SCOPES)
```
2) E necessario informar o id do grupo que você deseja realizar a inscrição para receber os eventos, substitua o valor ('<ID DO GRUPO AQUI>') no local informado abaixo:

```
TARGET_RESOURCE = '//chat.googleapis.com/spaces/<ID DO GRUPO AQUI>'
```
3) Além da autenticação do usuario e necessario uma chave que sera adicionada na url Discorey_service, alterando o valor ('< SUA CHAVE DE API AQUI >') no local informado abaixo:
```
DISCOVERY_SERVICE_URL = 'https://workspaceevents.googleapis.com/$discovery/rest?version=v1beta&labels=DEVELOPER_PREVIEW&key=< SUA CHAVE DE API AQUI >'
```

4) Instale as bibliotecas
```
 pip3 install --upgrade google-api-python-client google-auth-oauthlib
```

5) Execute o Script
```
py create_subscription.py
```

Neste momento será aberto uma janela no seu navegador para efetuar o login e conceder autorização para o seu aplicativo executar a inscrição, se tudo der certo ele ira retornar um json com os dados da inscrição.

E importante guardar estes dados para monitorar o tempo da inscrição e se caso necessario precise excluir ela, você vai precisar do id desta inscrição.
</details>





</p>
<p>Esta documentação ainda esta em construção e podera sofrer atualizações nos scripts e também nesta documentação.</p>



## Desenvolvedores

[<img src="https://avatars.githubusercontent.com/u/104507765?s=400&u=b8026e33ffc0c66417c4edeed939de0f46a40894&v=4" width=115><br><sub>Rodrigo Martins</sub>](https://github.com/rodrigo-martins-multiedro)<br>
