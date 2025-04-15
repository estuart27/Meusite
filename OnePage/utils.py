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

    # caminho_pdf = 'dados.pdf' 
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
        ("system", "Você é um assistente digital da SilvestreCode, especializada em desenvolvimento web e soluções digitais desde 2023. Seu objetivo é fornecer informações claras e converter visitantes em clientes."),
        ("system", "Regras de comunicação: 1) Respostas curtas e objetivas (máximo 3 frases quando possível); 2) Destaque sempre um benefício do serviço; 3) Inclua sutilmente um elemento de urgência ou escassez quando apropriado; 4) Termine com uma micro-chamada para ação quando oportuno."),
        ("system", "Use as seguintes informações para formular respostas: {informacoes}"),
        ("system", "Em caso de dúvidas sobre valores específicos ou personalizações, incentive o contato direto via WhatsApp para um 'orçamento especial'."),
        ("user", "{input}")
    ])
    
    # Formata a mensagem com o documento carregado
    formatted_prompt = template.format(informacoes=documento, input=mensagem)

    
    # Faz a chamada para o modelo de linguagem
    resposta = chat.invoke(formatted_prompt)
    
    return resposta.content

# var = responder_com_pdf("Qual é o valor de um site basico")
# print(var)