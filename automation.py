# Step 1: Define the function to be tested
def square(x):
    return x * x

# Step 2: Create a list of test cases (input and expected output)
test_cases = [
    {"input": 2, "expected": 4},
    {"input": -3,"expected": 9},
    {"input": 0, "expected": 0},
    {"input": 5, "expected": 25},
    {"input": 10, "expected": 100},
    {"input": -1, "expected": 1}
]

# Step 3: Function to run tests
def run_tests():
    print("Running Automated Tests...\n")
    passed = 0  # Counter for passed tests

    for index, test in enumerate(test_cases):
        input_value = test["input"]
        expected_output = test["expected"]
        actual_output = square(input_value)

        # Compare expected and actual
        if actual_output == expected_output:
            result = "PASS"
            passed += 1
        else:
            result = "FAIL"

        # Display test result
        print(f"Test Case {index + 1}: Input={input_value} | Expected={expected_output} | Actual={actual_output} --> {result}")

    total = len(test_cases)
    print(f"\nTesting Completed: {passed}/{total} Tests Passed.")

# Step 4: Run the test process
if __name__ == "__main__":
    run_tests()
