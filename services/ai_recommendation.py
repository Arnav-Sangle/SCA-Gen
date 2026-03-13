from openai import OpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_recommendation(component, publisher, version, ecosystem, latest_version, vulnerabilities):

    vuln_text = ""

    if not vulnerabilities:
        vuln_text = "No known vulnerabilities."

    else:

        for v in vulnerabilities:

            vuln_text += f"""
CVE: {v["id"]}
Description: {v["summary"]}
"""

    prompt = f"""
You are an Application Security expert.

Component: {component}
Publisher: {publisher}
Ecosystem: {ecosystem}
Current Version: {version}
Latest Version: {latest_version}

Vulnerabilities:
{vuln_text}

Rules:

1. Prefer latest stable version without vulnerabilities
2. If latest version vulnerable suggest nearest stable version
3. If upgrade gap too large suggest nearest safe version
4. If all versions vulnerable suggest alternative package
5. Keep response concise

Provide recommendation.
"""

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content