import streamlit as st
import subprocess
import os

st.set_page_config(page_title="GBTNetwork Launcher", layout="centered")

st.title("🚀 GBTNetwork Layer 1 Launcher")
st.markdown("Launch your Layer 1 GBT mainnet node with pre-mined 36 sextillion GBT tokens.")

# Display node configuration
st.subheader("Node Configuration")
st.code("""
RPC URL: http://localhost:8545
Network: GBT Layer 1
PoW Enabled: ✅
Pre-allocation: 36 Sextillion GBT
""", language='text')

# Launch button
if st.button("Start GBTNetwork Node"):
    st.success("⏳ Launching GBT Layer 1 node...")
    try:
        subprocess.Popen(["bash", "entrypoint.sh"])
        st.success("✅ GBTNetwork node is now running!")
    except Exception as e:
        st.error(f"❌ Failed to launch node: {e}")

# Optional: Streamlit tips
st.markdown("---")
st.info("Keep this browser tab open to maintain the Streamlit session. For CLI use, run `./entrypoint.sh` directly.")
