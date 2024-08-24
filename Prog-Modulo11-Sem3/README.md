1. Processos para rodar

1.1 Rodar o docker-compose
```bash
docker-compose up
```

1.2 Rodar o projeto
```bash
poetry install

poetry run python ./app.py
```

1.3 Criar view no clickhouse
```sql
CREATE VIEW default.pokemon_view
(

    `data_ingestao` DateTime,

    `nome` String,

    `link` String,

    `data_ingestao_datetime` DateTime
) AS
SELECT
    data_ingestao,

    JSONExtractString(dado_linha,
 'name') AS nome,

    JSONExtractString(dado_linha,
 'url') AS link,

    toDateTime(JSONExtractInt(dado_linha,
 'data_ingestao') / 1000) AS data_ingestao_datetime
FROM default.working_data AS wd
WHERE wd.tag = 'pokemon';
```

1.4 Efetuar chamada para ingestão dos dados
```bash
curl -X POST http://localhost:5000/data \
-H "Content-Type: application/json"
```

1.5 Chamada para os testes
```bash
poetry run pytest
```