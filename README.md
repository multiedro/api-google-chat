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
|12/12/2023     |Rodrigo Martins                            |1.1                   |Primeira versão funcional dos códigos

### **Executando o código para testes:**

Executando o projeto em ambiente local, atenção o Token de acesso a API da Shopify já esta neste repositorio, muito cuidado com o seu manuseio, as chaves para inserção dos dados no Bigquery devem ser baixadas no projeto do cliente esta não será salva neste repositorio.

1. Clone este diretório
```
git clone https://github.com/multiedro/larroude-data-hml-api-Shopify.git
```
2. crie um ambiente de desenvolvimento utilizando venv ou virtualenv

3. execute o comando de instalação dos pacotes conforme demonstrado abaixo

```
pip install -r requirements.txt
```

4. Entendendo a estrutura de pastas deste projeto

```
## Pastas
- backups - Contem backup do codigo inicial sem paginação dos resultados da API
- Schemas - Traz os Schemas das respostas da API e também das tabela do BigQuery, para criação no BQ utilize a pasta a seguir.
- scripts_create_bq - aqui você tem pronto os scripts com os campos para serem criados no bigquery isso sera demonstrado a seguir.
- chaves - [Opcional] - crie esta pasta para armazenar suas chaves ou credenciais de acesso, lembre de alterar no código o path para esta pasta.

## Scripts
- InsertBQ.py - Script responsevel pelo insert dos dados dentro do Bigquery
- main.py  - Script principal que vai realizar a consulta na API e tratar os dados a serem enviados para o BQ
```

A estrutura de pastas devera estar parecida com a da imagem abaixo.
<img src="https://github.com/multiedro/larroude-data-hml-api-shopfy/blob/main/estruturadaspastas.PNG" width=715>



5. Antes de rodar o codigo e necessario que as tabelas já estejam criadas dentro do BigQuery, abaixo um exemplo de como pode usar os arquivos que estão dentro da pasta script_create_bq para criar a tabela, os arquivos desta pasta já estao com os nomes corretos dos campos e seus respctivos tipos. conforme demonstrado abaixo.


<img src="https://github.com/multiedro/larroude-data-hml-api-shopfy/blob/main/tabelasBQ.gif" width=715>


6. Após criar ou validar a existencia das tabelas, valide o script InsertBQ.py e ajuste o parametro TABLE_ID conforme demonstrado abaixo, este caminho você encontra na aba detalhes da sua tabela, neste caso vamos colocar somente parte do path pois o nome da tabela que ira complementar este path sera enviado pelo script principal juntamente com os dados que serão inseridos no banco de dados. o path e compospo pelo <ID DO PROJETO>.<DATASET>.<NOME DA TABELA> exemplo : larroude-data-hml.teste_Shopify.

```
 #Id do projeto dataset e tabela no bigquery
        table_id = "larroude-data-hml.teste_Shopify."+str(tabela)
```

7. Após este ajuste você podera executar o script principal da seguinte forma:
```
py main.py
```

<p>O processo de importação e tratamento dos dados pode durar entre 30 minutos a 1 hora dependendo do volume de dados.</p>


</p>
<p>O codigo ainda esta em desenvolvimento e este primeiro codigo foi desenvolvido e precisa passar por uma nova reconfiguração</p>



## Desenvolvedores

[<img src="https://avatars.githubusercontent.com/u/104507765?s=400&u=b8026e33ffc0c66417c4edeed939de0f46a40894&v=4" width=115><br><sub>Rodrigo Martins</sub>](https://github.com/rodrigo-martins-multiedro)<br>
