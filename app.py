import json

def read_complaint():
    """Reads a sample complaint text."""
    # In a real app, this might come from a user input or a file
    return "My product arrived completely smashed and the box was torn open."

def build_prompt(complaint_text):
    """Builds the prompt to send to the LLM."""
    # Read the prompt template from the file
    try:
        with open("prompts/complaint_extraction_prompt.txt", "r") as f:
            prompt_template = f.read()
    except FileNotFoundError:
        prompt_template = "Extract problem, root_cause, and recommended_action."

    # Combine the template with the actual complaint
    full_prompt = f"{prompt_template}\n\nComplaint:\n{complaint_text}"
    return full_prompt

def analyze_complaint(prompt):
    """
    Placeholder for LLM API call.
    Currently returns a mocked JSON response.
    """
    # TODO: Replace with actual OpenAI API call
    mock_response = {
        "problem": "Product arrived damaged",
        "root_cause": "Packaging issue",
        "recommended_action": "Send replacement and improve packaging"
    }
    return json.dumps(mock_response, indent=2)

def main():
    print("--- AI Customer Complaint Analyzer ---")
    
    # 1. Get the complaint text
    complaint = read_complaint()
    print(f"\n[Input Complaint]:\n{complaint}")
    
    # 2. Build the prompt
    prompt = build_prompt(complaint)
    
    # 3. Analyze and get JSON output
    print("\n[Analyzing...]")
    result_json = analyze_complaint(prompt)
    
    # 4. Display the result
    print(f"\n[Output JSON]:\n{result_json}")

if __name__ == "__main__":
    main()
