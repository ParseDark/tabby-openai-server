import os

import openai

from src.models import (
    CompletionReq,
    CompletionResp,
    CompletionChoice,
)

# client = openai.AsyncAzureOpenAI(
#     azure_endpoint=os.getenv("azure_endpoint"),
#     api_version=os.getenv("azure_api_version"),
#     api_key=os.getenv("azure_api_key"),
#     timeout=60.0,
# )

client = openai.AsyncOpenAI(
    # base_url="https://gptapi.us/v1",
    base_url=os.getenv("base_url"),
    # api_key="sk-xxxx,
    api_key=os.getenv("api_key")
)

async def code_comp(data: CompletionReq) -> CompletionResp:
    try:
        resp = await client.chat.completions.create(
            model=os.getenv("model", "gpt-3.5-turbo-1106"),
            max_tokens=4096,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a {data.language} programming language expert.",
                },
                {
                    "role": "user",
                    "content": f"Please complete the code in between according to the prefix and suffix, only return "
                    f"the completed part, keep the format and ensure normal operation. No explanation "
                    f"needed.\n\nprefix: {data.segments.prefix}\n\nsuffix: {data.segments.suffix}",
                },
            ],
        )
    except Exception as e:
        raise e
    else:
        choices = []

        for choice in resp.choices:
            choices.append(
                CompletionChoice(
                    index=choice.index,
                    text=choice.message.content,
                )
            )

        return CompletionResp(id=resp.id, choices=choices)
