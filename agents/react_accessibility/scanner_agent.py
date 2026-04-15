import subprocess
import json
import os
from tools.accessibility_rules import check_accessibility
from agents.react_accessibility.react_fix_agent import fix_agent


def parse_jsx_file(file_path):
    result = subprocess.run(
        ["node", "tools/jsx_parser.js", file_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    return json.loads(result.stdout)


def scanner_agent(repo_path):
    all_issues = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith((".jsx", ".tsx")):
                full_path = os.path.join(root, file)

                try:
                    elements = parse_jsx_file(full_path)
                    issues = check_accessibility(elements, full_path)

                    for issue in issues:
                        issue["file"] = full_path

                    all_issues.extend(issues)

                except Exception as e:
                    print(f"Error in {file}: {e}")

    return all_issues


if __name__ == "__main__":
    repo_path = input("Enter React project path: ")
    result = scanner_agent(repo_path)
    fixes = fix_agent(result)
print("\n=== Accessibility Issues ===")

for fix in fixes:
    print("\n----------------------------")
    print(f"File: {fix['file']}")
    print(f"Line: {fix['line']}")
    print(f"Issue: {fix['issue']}")
    print("\n❌ Original:")
    print(fix["original"])
    print("\n✅ Fixed:")
    print(fix["fixed"])