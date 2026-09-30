# Lab 1 - Task 2: Extended Rule-Based Example

def evaluate_candidate(score, documents_complete, attendance_percent, identity_verified):
    """
    Rule-based decision system.

    Original conditions retained:
    1. score >= 70
    2. documents_complete must be True

    Two additional transparent conditions:
    3. attendance_percent >= 75
    4. identity_verified must be True

    All thresholds are synthetic assumptions for this lab.
    """
    reasons = []

    if score < 70:
        reasons.append("score is below 70")

    if not documents_complete:
        reasons.append("documents are incomplete")

    if attendance_percent < 75:
        reasons.append("attendance is below 75%")

    if not identity_verified:
        reasons.append("identity is not verified")

    passed = len(reasons) == 0

    if passed:
        reason = "all four conditions are satisfied"
    else:
        reason = "; ".join(reasons)

    return passed, reason


def print_case(case_number, candidate, expected, actual, reason):
    print("-" * 70)
    print(f"CASE {case_number}")
    print(f"Input: {candidate}")
    print(f"Expected result: {'PASS' if expected else 'FAIL'}")
    print(f"Actual result:   {'PASS' if actual else 'FAIL'}")
    print(f"Reason: {reason}")


def main():

    test_cases = [
        {
            "score": 85,
            "documents_complete": True,
            "attendance_percent": 90,
            "identity_verified": True,
            "expected": True,
        },
        {
            "score": 85,
            "documents_complete": True,
            "attendance_percent": 74,
            "identity_verified": True,
            "expected": False,
        },
        {
            "score": 85,
            "documents_complete": True,
            "attendance_percent": 90,
            "identity_verified": False,
            "expected": False,
        },
        {
            "score": 70,
            "documents_complete": True,
            "attendance_percent": 75,
            "identity_verified": True,
            "expected": True,
        },
    ]

    print("=" * 70)
    print("LAB 1 - TASK 2: EXTENDED RULE-BASED EXAMPLE")
    print("=" * 70)
    print("Synthetic assumptions: score >= 70, complete documents,")
    print("attendance >= 75%, and verified identity.")
    print()

    for number, case in enumerate(test_cases, start=1):
        candidate = {
            "score": case["score"],
            "documents_complete": case["documents_complete"],
            "attendance_percent": case["attendance_percent"],
            "identity_verified": case["identity_verified"],
        }

        actual, reason = evaluate_candidate(**candidate)

        print_case(
            number,
            candidate,
            case["expected"],
            actual,
            reason
        )

        assert actual == case["expected"], (
            f"Case {number} failed: expected {case['expected']}, got {actual}"
        )

    print("-" * 70)
    print("All four test cases passed their expected-result checks.")


if __name__ == "__main__":
    main()
