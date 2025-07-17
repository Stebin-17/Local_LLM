class Config:
    PAGE_TITLE = "Inhouse Personal Assistant Lucy"

    OLLAMA_MODELS = ('llama3.2','deepseek-r1','llama3.2:1b')

    host = ''

    SYSTEM_PROMPT = f"""You are a helpful chatbot named lucy that has access to the following 
                    open-source models {OLLAMA_MODELS}.
                    You can can answer questions for users on any topic and always use the persona of lucy. Give only the required answers"""
    
