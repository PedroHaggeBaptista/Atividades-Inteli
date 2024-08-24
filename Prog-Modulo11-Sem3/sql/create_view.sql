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