# Basic-Agent

A basic conversational AI agent using LangChain's Groq and Tavily Search tools. This project demonstrates a foundational setup for creating a chatbot capable of answering user queries, fetching data using search tools when needed, and supporting simple conversational responses.

## Features

- **Conversational Interaction**: Responds to user queries with contextually appropriate responses.
- **Tool Integration**: Leverages Tavily Search to fetch up-to-date information when questions require specific data.
- **Memory Checkpointing**: Saves session states for ongoing interactions using LangGraph's `MemorySaver`.
- **Basic Configurability**: Allows customizable configuration options, such as setting a unique thread ID.

## Requirements

- Python 3.8 or above

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/shirjeelafzal/Basic-Agent.git
   cd Basic-Agent
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy the `sample.env` file to `.env`:
     ```bash
     cp sample.env .env
     ```
   - Open `.env` and replace `YOUR_GROQ_API_KEY` and `YOUR_TAVILY_API_KEY` with your actual API keys:
     ```plaintext
     GROQ_API_KEY=your_groq_api_key
     TAVILY_API_KEY=your_tavily_api_key
     ```

5. Run the app:
   ```bash
   python app.py
   ```

## Usage

This basic agent can handle both casual conversation and more specific questions requiring online information. For example:
```plaintext
> What is the weather in SF?
```

The agent will decide when to utilize the Tavily Search tool to provide accurate responses to such queries.

## Project Structure

- **app.py**: Main file containing agent setup and execution.
- **README.md**: Project documentation.
- **requirements.txt**: Lists the Python libraries required to run the project.
- **sample.env**: Sample environment file template for API keys.
- **.env**: Environment file to store actual API keys (created by copying `sample.env`).

## Additional Notes

This agent can be expanded by integrating additional tools or enhancing memory capabilities to support more complex conversations. This setup is primarily intended as a simple starting point for building conversational AI agents.

## Contributing

Feel free to fork this repository, submit issues, and make pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
```
