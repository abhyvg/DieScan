# ai_integration.py
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_scan_result(scan_output):
    prompt = f"Analyze this network scan output and suggest possible vulnerabilities and remediation steps:\n{scan_output}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    sample_output = "Sample scan output showing open ports 22, 80, 443"
    print(analyze_scan_result(sample_output))
