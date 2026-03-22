import requests

OSV_URL = "https://api.osv.dev/v1/query"


def query_osv(component, publisher, version, ecosystem):

    if ecosystem == "Maven":
        purl = f"pkg:maven/{publisher}/{component}@{version}"

    elif ecosystem == "npm":
        purl = f"pkg:npm/{component}@{version}"

    elif ecosystem == "PyPI":
        purl = f"pkg:pypi/{component}@{version}"

    else:
        return []

    payload = {"package": {"purl": purl}}

    r = requests.post(OSV_URL, json=payload)

    vulns = r.json().get("vulns", [])

    results = []

    for v in vulns:

        results.append({
            "cve": v.get("id"),
            "summary": v.get("summary"),
            "source": "OSV",
            "affected": v.get("affected", [])
        })

    return results