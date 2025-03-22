# StreamlitPlayground

A web-based playground that allows you to run and preview Streamlit code snippets in real-time. This application provides both embedded preview and browser-based preview options for testing Streamlit code.

## Features

- 🖥️ Real-time Streamlit code execution
- 📝 In-app embedded preview
- 🌐 Browser-based preview option
- 🔄 Live code updates
- 🗑️ Automatic cleanup of temporary files
- 🔒 Safe execution in isolated environment
- 📋 Easy-to-use text input area
- 🎨 Clean and intuitive user interface

## Installation

1. Clone this repository:
```bash
git clone git@github.com:SubaashNair/StreamlitPlayground.git
cd StreamlitPlayground
```

2. Install the required dependencies:
```bash
pip install streamlit
```

## Usage

1. Start the playground:
```bash
streamlit run app.py
```

2. Once running, you can:
   - Paste your Streamlit code in the text area
   - Choose between two preview options:
     - "Run Snippet": Shows the output embedded in the current page
     - "Preview in Browser": Opens the snippet in a new browser tab
   - Use the respective "Stop" buttons to terminate the running snippets

## How It Works

- The playground creates a temporary directory called `snippets` to store code files
- Each snippet is saved with a unique timestamp-based filename
- The code runs on different ports to avoid conflicts:
  - Embedded preview: Port 8502
  - Browser preview: Port 8503
- Files are automatically cleaned up when stopping the preview

## Requirements

- Python 3.6+
- Streamlit
- Modern web browser
- Write permissions in the application directory

## Technical Details

- Uses `subprocess` to run Streamlit instances
- Implements UTF-8 encoding for handling special characters
- Manages process cleanup and file handling
- Provides error handling and user feedback
- Uses Streamlit's component system for embedded previews

## Limitations

- Running multiple snippets simultaneously may require additional port management
- The preview requires a few seconds to load due to Streamlit's startup time
- System resources should be monitored when running multiple instances

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request to [StreamlitPlayground](https://github.com/SubaashNair/StreamlitPlayground).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Inspired by the need for quick Streamlit code testing and experimentation 