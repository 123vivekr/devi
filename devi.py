from jinja2 import Environment, BaseLoader
import pyperclip

env = Environment(loader=BaseLoader())

planner_prompt_template = env.from_string(open("prompts/plan.jinja2").read().strip())
code_prompt_template = env.from_string(open("prompts/code.jinja2").read().strip())

task = input("Task: ")

########
# plan #
########
pyperclip.copy(planner_prompt_template.render(task=task))
print("copied planner prompt")

input("copy to clipboard and press enter to continue")
plan_output = pyperclip.paste()

########
# code #
########
pyperclip.copy(code_prompt_template.render(plan_output=plan_output))
print("copied code")
