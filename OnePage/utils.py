import os
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

def responder_com_pdf(mensagem: str) -> str:
    """
    Carrega um PDF e responde com base na mensagem fornecida.
    
    :param mensagem: Mensagem do usuário para consulta.
    :return: Resposta gerada pelo modelo.
    """
    # Obtém o caminho do diretório pai (onde está o dados.pdf)
    caminho_projeto = Path(__file__).parent.parent
    caminho_pdf = caminho_projeto / 'dados.pdf'
    
    # Verifica se o arquivo existe
    if not caminho_pdf.exists():
        raise FileNotFoundError(f"Arquivo PDF não encontrado: {caminho_pdf}")
    
    # Configuração da chave da API
    api_key = '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'
    os.environ['GROQ_API_KEY'] = api_key
    
    # Inicializa o chat com o modelo especificado
    chat = ChatGroq(model='llama-3.3-70b-versatile')
    
    # Carrega o PDF
    loader = PyMuPDFLoader(str(caminho_pdf))
    lista_documentos = loader.load()
    
    # Concatena o conteúdo dos documentos
    documento = ''.join(doc.page_content for doc in lista_documentos)
    
    # Define o template do prompt
    template = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente amigável da que possui as seguintes informações para formular uma resposta: {informações}."),
        ("system", "Seja o mais claro e objetivo possível e curta."),
        ("user", "{input}")
    ])
    
    # Formata a mensagem com o documento carregado
    formatted_prompt = template.format(informações=documento, input=mensagem)
    
    # Faz a chamada para o modelo de linguagem
    resposta = chat.invoke(formatted_prompt)
    
    return resposta.content

# Adicione logs para depuração
try:
    var = responder_com_pdf("Qual é o valor de um site basico")
    print(var)
except Exception as e:
    print(f"Erro: {e}")