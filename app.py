import streamlit as st
import pandas as pd

from utils.excel_parser import parse_excel
from utils.excel_writer import append_recommendations

from services.ai_ecosystem_classifier import detect_ecosystems_batch
from services.vulnerability_lookup import get_vulnerabilities
from services.version_intelligence import get_all_versions
from services.safe_version_finder import find_safe_versions, suggest_upgrade
from services.ai_recommendation import generate_recommendation


st.set_page_config(page_title="AI SCA Recommendation Generator")

st.title("AI SCA Recommendation Generator")

st.write(
    "Upload an Excel file containing Component, Publisher and Version. "
    "The system will analyze vulnerabilities and generate upgrade recommendations."
)

file = st.file_uploader("Upload Excel File", type=["xlsx"])


if file:

    df = parse_excel(file)

    st.subheader("Uploaded Components")

    st.dataframe(df)

    if st.button("Generate Recommendations"):

        components = []

        for _, row in df.iterrows():

            components.append({
                "component": row["Component"],
                "publisher": row["Publisher"]
            })

        with st.spinner("Detecting ecosystems using AI..."):

            ecosystem_map = detect_ecosystems_batch(components)

        recommendations = []

        progress = st.progress(0)

        total = len(df)

        for i, row in df.iterrows():

            component = row["Component"]
            publisher = row["Publisher"]
            version = row["Version"]

            ecosystem = ecosystem_map.get(component, "Unknown")

            # Step 1 — vulnerability lookup
            vulnerabilities = get_vulnerabilities(
                component,
                publisher,
                version,
                ecosystem
            )

            # Step 2 — retrieve all versions
            all_versions = get_all_versions(
                component,
                publisher,
                ecosystem
            )

            # Step 3 — find safe versions
            safe_versions = find_safe_versions(
                all_versions,
                vulnerabilities
            )

            # Step 4 — determine recommended upgrade
            recommended_version = suggest_upgrade(
                version,
                safe_versions
            )

            # Step 5 — AI recommendation
            rec = generate_recommendation(
                component,
                publisher,
                version,
                ecosystem,
                recommended_version,
                vulnerabilities
            )

            recommendations.append(rec)

            progress.progress((i + 1) / total)

        df = append_recommendations(df, recommendations)

        output_file = "sca_recommendations.xlsx"

        df.to_excel(output_file, index=False)

        st.success("Recommendations Generated")

        st.download_button(
            "Download Updated Excel",
            open(output_file, "rb"),
            file_name=output_file
        )