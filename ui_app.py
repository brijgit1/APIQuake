import streamlit as st
from test_runner import load_apis
from api_tester import run_api_test
import pandas as pd

st.set_page_config(page_title="APIQuake", layout="wide")
st.title("🔍 APIQuake")

# ✅ Load APIs
apis = load_apis()
api_names = [api["name"] for api in apis]

# ✅ Select All + Multiselect
select_all = st.checkbox("Select All APIs")
selected_apis = st.multiselect(
    "Select APIs to Test",
    options=api_names,
    default=api_names if select_all else []
)

# 🔽 Run Button
if st.button("Run Tests"):
    if not selected_apis:
        st.warning("Please select at least one API to run.")
    else:
        selected_configs = [api for api in apis if api["name"] in selected_apis]
        results = [run_api_test(api) for api in selected_configs]

        # ✅ Convert results to DataFrame
        df_results = pd.DataFrame(results)

        # ✅ Summary
        total = len(df_results)
        passed = df_results["test_passed"].sum()
        failed = total - passed

        st.success(f"✅ Test Summary: {passed} Passed / {failed} Failed / {total} Total")

        # ✅ Show result table
        st.dataframe(df_results[["name", "status_code", "status_check", "key_check", "test_passed"]])

        # ✅ Show each response
        for res in results:
            status_emoji = "✅" if res["test_passed"] else "❌"
            st.subheader(f"{status_emoji} {res['name']} - Status Code: {res['status_code']}")
            st.markdown(f"**Status Check:** {'✅' if res['status_check'] else '❌'}")
            st.markdown(f"**Key Check:** {'✅' if res['key_check'] else '❌'}")
            with st.expander("Response JSON"):
                st.json(res["response"])

        # ✅ Export to CSV
        csv_data = df_results.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📁 Download Results as CSV",
            data=csv_data,
            file_name="api_test_results.csv",
            mime="text/csv"
        )