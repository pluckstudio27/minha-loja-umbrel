import pandas as pd
from flask import Flask, render_template, request, send_file
import io
import datetime

# Inicializa a aplicação Flask
app = Flask(__name__)

# Define as colunas do Excel. Você pode personalizar aqui!
COLUNAS = [
    'Data de Abertura', 'Solicitante', 'Área do Solicitante', 
    'Título da Demanda', 'Descrição Detalhada', 'Status'
]

@app.route('/')
def index():
    """Renderiza a página inicial com o formulário."""
    return render_template('index.html', colunas=COLUNAS)

@app.route('/gerar-excel', methods=['POST'])
def gerar_excel():
    """Coleta os dados do formulário e gera o arquivo Excel."""
    
    # Coleta os dados do formulário
    dados_formulario = request.form.to_dict()
    
    # Adiciona a data atual ao início dos dados
    dados_completos = {'Data de Abertura': datetime.date.today().strftime('%d/%m/%Y')}
    dados_completos.update(dados_formulario)
    
    # Cria um DataFrame do Pandas. A estrutura é uma lista de dicionários.
    df = pd.DataFrame([dados_completos], columns=COLUNAS)
    
    # Usa um buffer de memória para salvar o arquivo Excel, evitando criar arquivos no servidor
    output_buffer = io.BytesIO()
    df.to_excel(output_buffer, index=False, sheet_name='Demandas')
    output_buffer.seek(0)
    
    # Define o nome do arquivo que será baixado
    nome_arquivo = f"demanda_{datetime.date.today().strftime('%Y-%m-%d')}.xlsx"
    
    # Envia o arquivo para o navegador do usuário para download
    return send_file(
        output_buffer,
        as_attachment=True,
        download_name=nome_arquivo,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

# Roda a aplicação na porta 8000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)