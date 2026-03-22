import requests
import base64


def query_sonatype(component, publisher, version):

    purl = f"pkg:maven/{publisher}/{component}@{version}"

    url = "https://ossindex.sonatype.org/api/v3/component-report"

    payload = {"coordinates": [purl]}

    r = requests.post(url, json=payload)

    data = r.json()

    results = []

    for comp in data:

        for v in comp.get("vulnerabilities", []):

            results.append({
                "cve": v.get("id"),
                "summary": v.get("title"),
                "severity": v.get("cvssScore"),
                "source": "Sonatype"
            })

    return results