# Como rodar a atividade

## Passo 1 - Gerar os banco de dados localmente com Docker

 - Verificar que está na pasta Prog-Módulo8-Sem4
 - Verificar a instalação do docker na máquina
 - Rodar o comando ` docker compose up `
 - Aguardar os três serviços estarem disponíveis em suas respectivas portas ( 6379 - Redis, 8081 - RedisCommander, 3002 - postgreSQL)

## Passo 2 - Configurar o banco (PostgreSQL) com prisma

 - Rodar ` npm install ` na pasta Prog-Módulo8-Sem4
 - Rodar o comando ` npx prisma migrate dev ` para subir as migrações no PostgreSQL

## Passo 3 - Popular o banco (PostgreSQL)
  
 - Verificar que está na pasta Prog-Módulo8-Sem4
 - Verificar a instalação do Node.JS na máquina
 - Rodar o comando ` node savePoducts.js `


## Passo 4 - Rodar o código do execício

 - Alterar o parmetro da chamada da função `run()` para o ID desejado na consulta
 - Para rodar o proposto no exercício, deve-se manter qualquer id na chamada da função `run()` e rodar o comando `node index.js` no terminal, deve-se obter uma resposta com o resultado da consulta e o tempo de resposta dessa, sendo assim, deve-se rodar novamente o comando `node index.js`, observando agora que o tempo de resposta irá ser reduzido drasticamente, e que a consulta irá ocorrer da mesma forma, isso porque após a primeira consulta que ocorreu daquele produto no qual a busca foi feita no PostgreSQL, houve uma gravação de tal produto no banco Redis, salvando-o em Chache, o que garante que para próximas consultas, o resultado virá do banco Redis (com tempo de resposta muito menor).

PS: Subimos o .env intencionalmente (não há credenciais sigilosas)