from jinja2 import Environment, BaseLoader

class TemplateHandler:
    def __init__(self):
        self.env = Environment(loader=BaseLoader())
        self.planner_prompt_template = self.env.from_string(open("prompts/plan.jinja2").read().strip())
        self.code_prompt_template = self.env.from_string(open("prompts/code.jinja2").read().strip())
        self.update_code_template = self.env.from_string(open("prompts/update_code.jinja2").read().strip())

    def render_planner_prompt(self, task):
        return self.planner_prompt_template.render(task=task)

    def render_code_prompt(self, plan_output):
        return self.code_prompt_template.render(plan_output=plan_output)

    def render_update_code(self, code, feat):
        return self.update_code_template.render(code=code, feat=feat)
