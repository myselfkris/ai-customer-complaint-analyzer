# Application Architecture

```text
User Input
   ↓
Prompt Template
   ↓
LLM API
   ↓
Structured JSON Output
   ↓
Application Logic
   ↓
Storage / UI
```

### Explanation of Layers

**User Input:** The starting point of the application where customer complaint text is received. This could be through a command-line interface, a web form, or an API endpoint.

**Prompt Template:** The system takes the user input and injects it into a carefully crafted set of instructions (the prompt). This prompt sets the persona (e.g., customer support analyst) and defines the exact data fields needed.

**LLM API:** The constructed prompt is sent to a Large Language Model (like OpenAI's GPT-4) via an API call. The LLM processes the text, understands the context of the complaint, and generates the requested information based on the prompt instructions.

**Structured JSON Output:** The LLM returns the extracted data in a strict, predictable JSON format (containing problem, root_cause, and recommended_action), making it easy for the application to parse and use.

**Application Logic:** The core backend code that handles the flow of data. It parses the JSON from the LLM, handles any potential errors or retries, and prepares the data for the next steps.

**Storage / UI:** The final destination for the processed data. The structured insights can be saved to a database for analytics, written to a file, or displayed on a user-friendly frontend dashboard for customer support teams to review.
