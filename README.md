# Devi - AI Agent 🤖💻

> Devi is devika's genz aesthetic goth art-enthusiast sister 

> This project is built to optimize Devika's prompts and data/instruction flow

## Features ✨

- Generates prompts for LLMs to help with task planning, initial code generation, and iterative code improvements
- Provides a simple interface for interacting with the LLM and managing the coding workflow
- Automatically records the prompts and responses from the LLM for future reference
- Supports copying prompts and responses to the clipboard for easy integration with other tools

## Installation 📥

1. Clone the repository:
```
git clone https://github.com/your-username/devi.git
```
2. Change to the project directory:
```
cd devi
```
3. Create a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage 🚀

To use Devi, run the following command:

```
python devi.py --record session-name
```

Replace `session-name` with a descriptive name for your coding session. This will create a directory called `store` in the project root, where the prompts and responses will be saved.

The tool will prompt you to enter a task, then it will generate a planning prompt, copy it to the clipboard, and ask you to paste the LLM's response back into the tool. It will then generate a code prompt, copy it to the clipboard, and ask you to paste the LLM's code response back into the tool.

After the initial code is generated, the tool will enter an interactive mode where you can provide feedback on the code (e.g., features to add or bugs to fix) and the tool will generate updated code prompts based on your input.

## License 📄

Devi is licensed under the [MIT License](LICENSE).

## Acknowledgements 🙏

Devi was developed using the following libraries and tools:

- [Jinja2](https://jinja.palletsprojects.com/) for template rendering
- [pyperclip](https://pypi.org/project/pyperclip/) for clipboard management
- [argparse](https://docs.python.org/3/library/argparse.html) for command-line argument parsing
- [Devika](https://github.com/stitionai/devika) - Agentic AI Software Engineer
