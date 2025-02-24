from notdiamond import LLMConfig, NotDiamond
from langchain_core.prompts import ChatPromptTemplate

from prompts import RACIAL_BIAS_SYSTEM_PROMPT

def detect_bias(text: str, model_str: str) -> str:
    ndllm = LLMConfig.from_string(model_str)
    model = NotDiamond._llm_from_config(ndllm, None)
    messages = [
                {"role": "system", "content": RACIAL_BIAS_SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ]
    chain_messages = [
                (msg["role"], msg["content"]) for msg in messages
            ]
    prompt_template = ChatPromptTemplate.from_messages(chain_messages)

    chain = prompt_template | model
    result = chain.invoke({})
    return result if isinstance(result, str) else result.content

def generate_prompt(text: str) -> str:
    messages = [
                {"role": "system", "content": RACIAL_BIAS_SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ]
    chain_messages = [
                (msg["role"], msg["content"]) for msg in messages
            ]
    prompt_template = ChatPromptTemplate.from_messages(chain_messages)
    return prompt_template