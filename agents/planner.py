# agents/planner.py

from transformers import pipeline
import os

class PlannerAgent:
    def __init__(self, model_name="google/flan-t5-base", prompt_path="prompts/planner_prompt.txt"):
        """
        Initialize the PlannerAgent with a specified model and prompt template path.
        """
        # Load prompt template
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"Prompt template not found at {prompt_path}")

        with open(prompt_path, "r", encoding="utf-8") as f:
            self.prompt_template = f.read()

        # Initialize Hugging Face pipeline
        self.generator = pipeline("text2text-generation", model=model_name)

    def predict(self, user_story):
        """
        Generate a list of development tasks given a user story.
        Returns a list of task strings.
        """
        # Input validation
        if not user_story or not user_story.strip():
            return []

        final_prompt = self.prompt_template.replace("{INPUT_STORY}", user_story.strip())

        result = self.generator(final_prompt, max_length=512)
        output_text = result[0]["generated_text"].strip()

        # Clean task parsing
        tasks = []
        for line in output_text.splitlines():
            line = line.strip("-• ").strip()
            if line:
                tasks.append(line)

        return tasks


# For standalone testing
if __name__ == "__main__":
    agent = PlannerAgent()

    # Example user story
    story = "As a user, I want to be able to delete my account permanently from settings."

    tasks = agent.predict(story)
    print("Generated Tasks:")
    for t in tasks:
        print("-", t)
