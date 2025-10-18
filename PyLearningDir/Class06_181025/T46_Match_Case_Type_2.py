# match case for case type

# Match Case - check week days using match case

TypeOfTest = str(input("Enter Test_type like API, UI, Security, Performance: ").strip())
match TypeOfTest:
    case "API":
        print("Postman API running test case")
    case "UI":
        print("UI Test running test case")
    case "Security":
        print("Security Test running test case")
    case "Performance":
        print("performance Test running test case")
    case _:
        print("Invalid Test_type entered")



