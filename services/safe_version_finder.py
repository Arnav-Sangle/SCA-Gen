from packaging import version


def extract_vulnerability_ranges(vulnerabilities):

    ranges = []

    for vuln in vulnerabilities:

        affected = vuln.get("affected", [])

        for a in affected:

            for r in a.get("ranges", []):

                events = r.get("events", [])

                introduced = None
                fixed = None

                for e in events:

                    if "introduced" in e:
                        introduced = e["introduced"]

                    if "fixed" in e:
                        fixed = e["fixed"]

                ranges.append((introduced, fixed))

    return ranges


def is_version_vulnerable(ver, ranges):

    v = version.parse(ver)

    for introduced, fixed in ranges:

        if introduced is None:
            continue

        intro_v = version.parse(introduced)

        if fixed:

            fixed_v = version.parse(fixed)

            if intro_v <= v < fixed_v:
                return True

        else:

            if v >= intro_v:
                return True

    return False


def find_safe_versions(all_versions, vulnerabilities):

    ranges = extract_vulnerability_ranges(vulnerabilities)

    safe_versions = []

    for v in all_versions:

        if not is_version_vulnerable(v, ranges):

            safe_versions.append(v)

    return safe_versions


def suggest_upgrade(current_version, safe_versions):

    if not safe_versions:
        return None

    current = version.parse(current_version)

    higher = [
        v for v in safe_versions
        if version.parse(v) > current
    ]

    if not higher:
        return safe_versions[-1]

    return sorted(higher, key=lambda x: version.parse(x))[0]