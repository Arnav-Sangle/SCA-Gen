import requests


def query_nvd(component):

    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={component}"

    try:

        r = requests.get(url)

        data = r.json()

        vulns = data.get("vulnerabilities", [])

        results = []

        for v in vulns[:10]:

            cve = v["cve"]

            results.append({
                "cve": cve["id"],
                "summary": cve["descriptions"][0]["value"],
                "source": "NVD"
            })

        return results

    except Exception:

        return []