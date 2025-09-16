import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from decouple import config

def responder_com_pdf(mensagem: str) -> str:
    """
    Carrega um PDF e responde com base na mensagem fornecida.
    
    :param mensagem: Mensagem do usuário para consulta.
    :return: Resposta gerada pelo modelo.
    """
    caminho_pdf = '/var/www/silvestrecode/Meusite/dados.pdf' 

    # Configuração da chave da API
    api_key = config('CHAVE_API')
    os.environ['GROQ_API_KEY'] = api_key
    
    # Inicializa o chat com o modelo especificado
    chat = ChatGroq(model='llama-3.3-70b-versatile')
    
    # Carrega o PDF
    loader = PyMuPDFLoader(caminho_pdf)
    lista_documentos = loader.load()
    
    # Concatena o conteúdo dos documentos
    documento = ''.join(doc.page_content for doc in lista_documentos)
    
    # Define o template do prompt
    template = ChatPromptTemplate.from_messages([
        ("system", 
        "Você é um assistente digital da SilvestreCode. Seu conhecimento vem apenas do documento fornecido."),
        ("system", 
        "Regras: 1) Responda apenas com informações do PDF; 2) Se não encontrar no PDF, diga educadamente que não possui a informação e oriente o cliente a entrar em contato diretamente; 3) Só mencione WhatsApp ou e-mail se o cliente perguntar, ou se a informação não estiver no PDF — nesse caso, forneça este link de contato: https://wa.me/5543996341638; 4) Use frases curtas e claras; 5) Destaque sempre um benefício prático quando possível."),
        ("system", 
        "Informações disponíveis: {informacoes}"),
        ("user", "{input}")
    ])

    # Formata a mensagem com o documento carregado
    formatted_prompt = template.format(informacoes=documento, input=mensagem)

    
    # Faz a chamada para o modelo de linguagem
    resposta = chat.invoke(formatted_prompt)
    
    return resposta.content

# var = responder_com_pdf("Qual é o valor de um site basico")
# print(var)