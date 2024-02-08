def check_learners_license_eligibility(age):
    if age >= 16:
        print("Can apply for learner's license.")

# Test cases
test_cases = [14, 16, 18, 25]  # low value, boundary case, high value

for age in test_cases:
    print(f"Testing with age {age}:")
    check_learners_license_eligibility(age)
    print()