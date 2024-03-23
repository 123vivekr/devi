from jinja2 import Environment, BaseLoader
import pyperclip
import readchar

env = Environment(loader=BaseLoader())

planner_prompt_template = env.from_string(open("prompts/plan.jinja2").read().strip())
code_prompt_template = env.from_string(open("prompts/code.jinja2").read().strip())
update_code_template = env.from_string(open("prompts/update_code.jinja2").read().strip())

task = input("Task: ")
# task = "create a snake game in python in the terminal itself" # TEST

########
# plan #
########
pyperclip.copy(planner_prompt_template.render(task=task))
print("copied planner prompt")

input("copy to clipboard and press enter to continue")
plan_output = pyperclip.paste()

# plan_output = open("test_data/plan_output.txt").read().strip() # TEST

########
# code #
########
pyperclip.copy(code_prompt_template.render(plan_output=plan_output))
print("copied code")

input("copy to clipboard and press enter to continue")
code_output = pyperclip.paste()

#############
# reiterate #
#############

feat = ""
while True:
    feat = input("Feature/Bug (q to quit):  ")
    if feat == "q":
        quit(0)

    code = pyperclip.paste()
    pyperclip.copy(update_code_template.render(code=code, feat=feat))
    print("prompt copied")
