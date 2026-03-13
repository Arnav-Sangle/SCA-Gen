from openai import OpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL
import json

client = OpenAI(api_key=OPENAI_API_KEY)


def detect_ecosystems_batch(components):

    prompt = f"""
        Identify the package ecosystem for each component.

        Possible ecosystems:
        - Maven
        - npm
        - PyPI
        - Go
        - NuGet
        - Unknown

        Return JSON mapping component → ecosystem.

        Components:
        {components}
    """

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    try:
        data = json.loads(content)
    except Exception:
        data = {}

    return data