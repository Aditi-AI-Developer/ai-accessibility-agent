def get_code_snippet(file_path, line_number, context=2):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        start = max(0, line_number - context - 1)
        end = min(len(lines), line_number + context)

        return "".join(lines[start:end]).strip()
    except:
        return ""


def check_accessibility(elements, file_path):
    issues = []

    for el in elements:
        name = el["name"]
        attrs = el["attributes"]
        line = el["line"]

        snippet = get_code_snippet(file_path, line)

        # -------------------------
        # 🖼️ IMAGE RULES
        # -------------------------
        if name == "img" and "alt" not in attrs:
            issues.append({
                "issue": "Image missing alt text",
                "wcag": "1.1.1",
                "severity": "A",
                "line": line,
                "snippet": snippet,
                "fix_hint": "Add meaningful alt text"
            })

        # -------------------------
        # 🖱️ CLICKABLE NON-SEMANTIC
        # -------------------------
        if name in ["div", "span"] and "onClick" in attrs:
            issues.append({
                "issue": "Non-semantic clickable element",
                "wcag": "2.1.1",
                "severity": "A",
                "line": line,
                "snippet": snippet,
                "fix_hint": "Use <button> or add role='button' and keyboard support"
            })

        # -------------------------
        # 🔘 BUTTON RULES
        # -------------------------
        if name == "button":
            if "aria-label" not in attrs:
                issues.append({
                    "issue": "Button may lack accessible name",
                    "wcag": "4.1.2",
                    "severity": "A",
                    "line": line,
                    "snippet": snippet,
                    "fix_hint": "Ensure button has text or aria-label"
                })

        # -------------------------
        # 🔗 LINK RULES
        # -------------------------
        if name == "a":
            if "href" not in attrs:
                issues.append({
                    "issue": "Anchor missing href",
                    "wcag": "2.4.4",
                    "severity": "A",
                    "line": line,
                    "snippet": snippet,
                    "fix_hint": "Provide valid href"
                })

        # -------------------------
        # 🧾 FORM INPUT RULES
        # -------------------------
        if name == "input":
            if not any(attr in attrs for attr in ["aria-label", "aria-labelledby", "id"]):
                issues.append({
                    "issue": "Input missing accessible label",
                    "wcag": "3.3.2",
                    "severity": "A",
                    "line": line,
                    "snippet": snippet,
                    "fix_hint": "Add label or aria-label"
                })

        # -------------------------
        # ⌨️ TABINDEX RULE
        # -------------------------
        if "tabIndex" in attrs:
            issues.append({
                "issue": "Avoid unnecessary tabIndex usage",
                "wcag": "2.4.3",
                "severity": "AA",
                "line": line,
                "snippet": snippet,
                "fix_hint": "Use natural tab order instead"
            })

        # -------------------------
        # 🧠 ARIA ROLE MISUSE
        # -------------------------
        if "role" in attrs and name == "button":
            issues.append({
                "issue": "Redundant role on button",
                "wcag": "4.1.2",
                "severity": "A",
                "line": line,
                "snippet": snippet,
                "fix_hint": "Remove unnecessary role attribute"
            })

        # -------------------------
        # 🏷️ HEADING STRUCTURE
        # -------------------------
        if name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            # simple check placeholder (can improve later)
            if "aria-hidden" in attrs:
                issues.append({
                    "issue": "Heading should not be hidden from screen readers",
                    "wcag": "1.3.1",
                    "severity": "A",
                    "line": line,
                    "snippet": snippet,
                    "fix_hint": "Remove aria-hidden"
                })

    return issues