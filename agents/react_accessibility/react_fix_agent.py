import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_fix(issue):
    prompt = f"""
You are an expert React accessibility engineer.

Fix the following JSX code based on WCAG guidelines.

Issue: {issue['issue']}
WCAG: {issue['wcag']}

Code:
{issue['snippet']}

Rules:
- Use semantic HTML
- Add aria attributes if needed
- Keep React syntax correct
- Return ONLY fixed JSX code (no explanation)
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()


def fix_agent(issues):
    results = []

    for issue in issues:
        try:
            fixed_code = generate_fix(issue)

            results.append({
                "file": issue["file"],
                "line": issue["line"],
                "issue": issue["issue"],
                "original": issue["snippet"],
                "fixed": fixed_code
            })

        except Exception as e:
            print(f"Error fixing issue: {e}")

    return results