import requests


def get_all_versions(component, publisher, ecosystem):

    try:

        if ecosystem == "Maven":

            url = (
                "https://search.maven.org/solrsearch/select?"
                f"q=g:{publisher}+AND+a:{component}&core=gav&rows=200&wt=json"
            )

            r = requests.get(url)

            docs = r.json()["response"]["docs"]

            versions = [d["v"] for d in docs]

            return sorted(versions)

        elif ecosystem == "npm":

            url = f"https://registry.npmjs.org/{component}"

            r = requests.get(url)

            data = r.json()

            return list(data["versions"].keys())

        elif ecosystem == "PyPI":

            url = f"https://pypi.org/pypi/{component}/json"

            r = requests.get(url)

            data = r.json()

            return list(data["releases"].keys())

        return []

    except Exception:

        return []