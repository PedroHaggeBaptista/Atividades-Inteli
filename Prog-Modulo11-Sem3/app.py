from flask import Flask, request, jsonify
from datetime import datetime
from aulaafonse.minio_client import create_bucket_if_not_exists, upload_file, download_file
from aulaafonse.clickhouse_client import execute_sql_script, get_client, insert_dataframe
from aulaafonse.data_processing import process_data, prepare_dataframe_for_insert
from aulaafonse.get_data import get_all_pokemon
import pandas as pd

app = Flask(__name__)

# Criar bucket se não existir
create_bucket_if_not_exists("raw-data")

# Executar o script SQL para criar a tabela
execute_sql_script('sql/create_table.sql')

@app.route('/data', methods=['POST'])
def receive_data():
    data = get_all_pokemon()

    data = data['results']

    # Processar e salvar dados
    filename = process_data(data)
    upload_file("raw-data", filename)

    # Ler arquivo Parquet do MinIO
    download_file("raw-data", filename, f"downloaded_{filename}")
    df_parquet = pd.read_parquet(f"downloaded_{filename}")

    # Preparar e inserir dados no ClickHouse
    df_prepared = prepare_dataframe_for_insert(df_parquet)
    client = get_client()  # Obter o cliente ClickHouse
    insert_dataframe(client, 'working_data', df_prepared)

    return jsonify({"message": "Dados recebidos, armazenados e processados com sucesso"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)