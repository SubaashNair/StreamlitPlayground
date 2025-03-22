import streamlit as st
import subprocess
import tempfile
import os
import time
import webbrowser
from pathlib import Path

def main():
    st.title("Streamlit Snippet Runner")

    # Create a persistent directory for snippets if it doesn't exist
    snippets_dir = Path("snippets")
    snippets_dir.mkdir(exist_ok=True)

    user_code = st.text_area("Paste your Streamlit snippet here:", height=300)

    col1, col2 = st.columns(2)
    
    with col1:
        run_button = st.button("Run Snippet")
    with col2:
        preview_button = st.button("Preview in Browser")

    if run_button and user_code.strip():
        try:
            # Generate a unique filename
            snippet_filename = f"snippet_{int(time.time())}.py"
            snippet_path = snippets_dir / snippet_filename
            
            # Save the snippet with UTF-8 encoding
            with open(snippet_path, "w", encoding='utf-8') as f:
                f.write(user_code)
            
            port = 8502  # Use a different port to avoid collision
            
            # Start the snippet Streamlit app
            proc = subprocess.Popen([
                "streamlit", "run", str(snippet_path), 
                "--server.port", str(port),
                "--server.headless", "true",
                "--server.runOnSave", "false",
                "--browser.serverAddress", "localhost"
            ])

            # Allow Streamlit app to load
            time.sleep(3)

            snippet_url = f"http://localhost:{port}"

            # Display snippet in iframe
            st.markdown("### Snippet Output:")
            st.components.v1.iframe(snippet_url, width=800, height=600, scrolling=True)

            # Add option to stop snippet server
            if st.button("Stop Snippet"):
                proc.terminate()
                try:
                    os.remove(snippet_path)  # Clean up the file
                except:
                    pass

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    elif preview_button and user_code.strip():
        try:
            # Generate a unique filename
            snippet_filename = f"preview_{int(time.time())}.py"
            snippet_path = snippets_dir / snippet_filename
            
            # Save the snippet with UTF-8 encoding
            with open(snippet_path, "w", encoding='utf-8') as f:
                f.write(user_code)
            
            port = 8503  # Use a different port for preview
            
            # Start the snippet Streamlit app
            proc = subprocess.Popen([
                "streamlit", "run", str(snippet_path), 
                "--server.port", str(port),
                "--server.headless", "true",
                "--server.runOnSave", "false",
                "--browser.serverAddress", "localhost"
            ])

            # Allow Streamlit app to load
            time.sleep(3)

            # Open in default browser
            webbrowser.open(f"http://localhost:{port}")

            # Add option to stop preview server
            if st.button("Stop Preview"):
                proc.terminate()
                try:
                    os.remove(snippet_path)  # Clean up the file
                except:
                    pass

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()


