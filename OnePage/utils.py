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

    # Copiar o PDF(para funcionar as mudanças de arquivo no servidor )
    # cp dados.pdf /var/www/silvestrecode/Meusite/

    # # Copiar a pasta static inteira (substitui arquivos existentes)
    # cp -r static/ /var/www/silvestrecode/Meusite/


    # Configuração da chave da API
    api_key = config('CHAVE_API')
    os.environ['GROQ_API_KEY'] = api_key
    
    # Inicializa o chat com o modelo especificado
    chat = ChatGroq(model="openai/gpt-oss-20b")
    
    # Carrega o PDF
    loader = PyMuPDFLoader(caminho_pdf)
    lista_documentos = loader.load()
    
    # Concatena o conteúdo dos documentos
    documento = ''.join(doc.page_content for doc in lista_documentos)
    
    # Define o template do prompt
    template = ChatPromptTemplate.from_messages([
        ("system", 
        "Você é um assistente digital da SilvestreCode, especialista em conversão de vendas. Seu conhecimento vem exclusivamente do documento fornecido."),
        
        ("system", 
        "PERSONALIDADE: Seja simpático, prestativo e genuinamente interessado em resolver o problema do cliente. Transmita confiança nas soluções da SilvestreCode."),
        
        ("system", 
        "REGRAS OBRIGATÓRIAS:\n"
        "1) Use APENAS informações do PDF fornecido\n"
        "2) Respostas curtas e diretas (máximo 2-3 frases)\n"
        "3) Se não souber, diga: 'Não tenho essa informação específica. Para esclarecer melhor, entre em contato: https://wa.me/5543996341638'\n"
        "4) Só mencione contato se perguntarem OU se não tiver a informação no PDF\n"
        "5) SEMPRE destaque um benefício prático em cada resposta\n"
        "6) Demonstre como a solução resolve especificamente o problema mencionado"),
        
        ("system", 
        "ESTRATÉGIA DE VENDAS:\n"
        "• Identifique a dor/necessidade do cliente\n"
        "• Conecte diretamente com os benefícios da solução\n"
        "• Use linguagem que gere urgência e valor\n"
        "• Termine sempre com um insight que desperte interesse\n"
        "• Seja consultivo, não apenas informativo"),
        
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