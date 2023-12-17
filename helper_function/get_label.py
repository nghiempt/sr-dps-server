import asyncio
import ssl
import csv
import json
import openai
import os
from dotenv import load_dotenv


class CHATGPT_GENERATOR:

    @staticmethod
    def get_prompt(ds_content, pp_content):
        prompt = '''Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 3 issues: which information is incorrect, which information is incomplete and which information is inconsistent.\n\nNotes when classifying:\n+ Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides.\n+ Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it.\n+ Inconsistency: Data Safety is provided but its description is inconsistent with the Privacy Policy information provided.\n\nNote: always gives me the result (0 or 1) in the form below:\nIncomplete: 0 or 1 (1 is yes, 0 is no)\nIncorrect: 0 or 1 (1 is yes, 0 is no)\nInconsistency: 0 or 1 (1 is yes, 0 is no)\n\nBelow is information for 2 parts: \nI. Data Safety: ''' + ds_content + '''\nII. Privacy Policy: ''' + pp_content + ''' '''
        return prompt
    
    @staticmethod
    def get_completion(prompt):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.chat.completions.create(
            model=os.getenv("GPT_4"),
            messages=[
                {"role": "system", "content": "You are an assistant who analyzes and evaluates the correct, complete, and consistency between the Data Safety information provided compared to the information provided by the Privacy Policy of applications on the Google Play Store."},
                {"role": "user", "content": prompt}
            ]
        )
        assistant_reply = response.choices[0].message.content
        return assistant_reply
    

class DATASET_GENERATOR:

    @staticmethod
    def loop_csv(csv_path, chatgpt_generator):
        with open(csv_path, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for index, row in enumerate(reader):
                print("\n_____________ Run times App ID: " + row[0] + "_____________")
                prompt = chatgpt_generator.get_prompt(row[1], row[2])
                
                # === SAVE IN CSV === #
                print(chatgpt_generator.get_completion(prompt))
                print("~~~~~~~~~~~~~~ Success ~~~~~~~~~~~~~~\n")


if __name__ == "__main__":
    chatgpt_generator = CHATGPT_GENERATOR()

    csv_path = "../dataset/formated_data/dataset.csv"

    DATASET_GENERATOR().loop_csv(csv_path, chatgpt_generator)
