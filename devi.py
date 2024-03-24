import argparse
import pyperclip
from template_handler import TemplateHandler
from recorder import Recorder

# Parse CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument('--record', help='Session name', metavar='name')
args = parser.parse_args()

# Load template handler
template_handler = TemplateHandler()

# Load recorder
recorder = Recorder(args.record)

# Request task from user
task = input("Task: ")

# Planner
planner_prompt = template_handler.render_planner_prompt(task)

pyperclip.copy(planner_prompt)
recorder.record("plan", "prompt", planner_prompt)

print("copied planner prompt")
input("copy output from LLM to clipboard and press enter to continue")
plan_output = pyperclip.paste()

recorder.record("plan", "output", plan_output)

# Code first version
code_prompt = template_handler.render_code_prompt(plan_output)

pyperclip.copy(code_prompt)
recorder.record("code", "prompt", code_prompt)

print("copied code prompt")

input("copy output from LLM to clipboard and press enter to continue")
code_output = pyperclip.paste()
recorder.record("code", "output", code_output)

# Reiterate on the code based on feedback from user
iteration_count = 1
while True:
    feat = input("Feature/Bug (q to quit): ")
    if feat == "q":
        quit(0)

    updated_code_prompt = template_handler.render_update_code(code_output, feat)
    recorder.record(f"reiterate_{iteration_count}", "prompt", updated_code_prompt)
    pyperclip.copy(updated_code_prompt)
    print("prompt copied")

    input("copy output from LLM to clipboard and press enter to continue")
    code_output = pyperclip.paste()
    recorder.record(f"reiterate_{iteration_count}", "output", code_output)
