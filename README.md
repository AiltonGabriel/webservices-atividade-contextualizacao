# atividade-contextualizacao-webservices
## _Ativida de contextualização Webservices_

Como atividade de contextualização, vocês irão desenvolver um programa cliente-servidor para cadastro de turmas:



- O usuário do programa cliente pode informar de 1 a N turmas.

- Cada turma deve possuir um nome, um ano e uma lista de 1 a N alunos matriculados (apenas nomes dos alunos).

- Após o usuário terminar de informar os dados das turmas, essa informação deverá ser representada na forma de string (defina o seu próprio formato ao invés de utilizar um formato padronizado) e enviada via socket para o servidor.

- O programa servidor deverá processar os dados recebidos, e exibir:

a) A quantidade de turmas

b) O nome da turma com mais alunos

c) O ano da turma mais antiga

d) A quantidade média de alunos por turma

## Como usar

1.  Instale o Pyhton 3 caso não tenha.
2.  Altere o _SERVER_NAME_ no arquivo _server.py_ caso seja necessário.
3. Execute o _server.py_: ```python server.py```
4. Execute o _client.py_: ```python client.py```
