def grades_strings(g):
    grades_strings = ""
    print(grades_strings, "\n")

def main():
    main_string = "push, branches, repository_dispatches"
    print("main:", main_string)

def permissions():
    perms = "'check': write, 'actions': read, 'contents': read"
    return perms

def jobs():
    job_description = "run-autograding-tests on ubuntu_latest"
    if 'github.actor' != 'github-classroom[bot]':
        return "'name': Checkout code, 'uses': actions/checkout@v4, 'name': Grading, 'id': grading, 'uses': classroom-resources/autograding-io-grader@v1"
    return job_description

def open_files():
    try:
        with open('test-name.txt', 'r') as file:
            contents = file.read()
            print("File Contents:\n", contents)
        
        command = "python3 string1.py"
        expected_output = "All Tests Passed"
        comparison_method = 'contains'
        timeout = 2
        name = "Autograding Reporter"
        uses = "classroom-resources/autograding-grading-reporter@v1"
        
        with open('runners', 'r') as file:
            runner_contents = file.read()
            print("Runner Contents:\n", runner_contents)

    except FileNotFoundError:
        print("One or more files were not found.")

if __name__ == '__main__':
    print("grades_strings")
    print("Permissions:", permissions())
    print("Jobs:", jobs())
    open_files()
    print("GRADING_RESULTS")
