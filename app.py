import streamlit as st
import contextlib
import io

def main():
    st.title("Streamlit Playground")

    user_code = st.text_area("Paste your Streamlit snippet here:", height=300)

    if st.button("Run Snippet") and user_code.strip():
        # Capture output
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            try:
                # Define a safe namespace to execute code
                local_namespace = {"st": st}
                exec(user_code, {}, local_namespace)
                st.success("Snippet executed successfully!")
            except Exception as e:
                st.error(f"Error executing snippet: {e}")

        # Display output
        printed_output = output.getvalue()
        if printed_output:
            st.subheader("Output:")
            st.code(printed_output)

    

if __name__ == "__main__":
    main()

