# AI Course

## Description

Learn with Python the uses of local LLMs (via Ollama) using [instructor](https://github.com/instructor-ai/instructor) and [LangChain](https://github.com/langchain-ai/langchain)/[LangGraph](https://github.com/langchain-ai/langgraph)

## Requirements

- **Python**: Version 3.11 or superior is required.
- **Package Manager**: `poetry` should be used for managing dependencies.
- **Ollama**: The latest version must be installed

### Installing Python on macOS

1. **Check for pre-installed Python**:
   Open a terminal and run:
   ```bash
   python3 --version
   ```
   If Python 3.12 or superior is already installed, you will see the version number. If not, proceed to the next step.

2. **Install Python via Homebrew**:
    - First, ensure Homebrew is installed. If not, install it by running:
      ```bash
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      ```
    - Then, install Python:
      ```bash
      brew install python@3.12
      ```

3. **Verify the installation**:
   After installation, verify the Python version:
   ```bash
   python3 --version
   ```
   Make sure the output shows version 3.12 or higher.

### Installing `poetry` on macOS

1**Install `poetry`**:
   Run the following command to install `poetry`:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2**Verify the installation**:
   After installation, confirm that `poetry` is installed by checking its version:
   ```bash
   poetry --version
   ```


### Installing Ollama on macOS

Download the binary [here](https://ollama.com/download)

## Install LLMs

For this course, you will need 2 LLMs via ollama: 
- **mistral**: `ollama pull mistral:latest`
- **phi4-mini**: `ollama pull phi4-mini:latest`

If you want to play with other models, you can install:
- **granite3.3:8b**: `ollama pull granite3.3:8b`
- **gemma3:12b**: `ollama pull gemma3:12b`
- **deepseek-r1:8b**: `ollama pull deepseek-r1:8b`

## Startup

```bash
poetry install
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, please reach out to:

- **GitHub**: [@HackJack-101](https://github.com/HackJack-101)