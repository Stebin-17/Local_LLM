"""
Orignal Author: DevTechBytes
https://www.youtube.com/@DevTechBytes
"""

class Config:
    PAGE_TITLE = "Inhouse Personal Assistant Lucy"

    OLLAMA_MODELS = ('llama3.2','llama3.2:1b')

    host = 'http://20.77.66.252:11434'

    SYSTEM_PROMPT = f"""You are a helpful chatbot named lucy that has access to the following 
                    open-source models {OLLAMA_MODELS}.
                    You can can answer questions for users on any topic and always use the persona of lucy. Give only the required answers"""
    