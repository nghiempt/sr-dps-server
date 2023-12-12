import asyncio
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import json
import openai
import os
from dotenv import load_dotenv
from newspaper import Article


class READ_DATA_SAFETY:

    @staticmethod
    def load_html_content(url):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        return soup

    @staticmethod
    def indent_content(tag):
        tag_content = tag.get_text(separator='\n')
        if tag_content.strip() == '· Optional':
            return str(tag.contents[0])
        if (tag_content.strip() != '· Optional') & (tag.name != 'h3'):
            return '\n data-section: ' + str(tag.contents[0])
        tag_name = tag.name
        if tag_name == 'h3':
            return '\n\t category: ' + str(tag.contents[0])
        elif tag_name == 'h2':
            return str(tag.contents[0]) + '\n'
        else:
            return ''

    @staticmethod
    def filter_content(soup):
        global title
        title = soup.find('div', class_='ylijCc').get_text(separator='\n')
        content = ""
        tags = soup.find_all(['h2', 'h3', 'h4'])
        div_tag = soup.find_all('div', class_='FnWDne')
        i = 0
        j = 0
        for i in range(len(tags)):
            if tags[i].contents:
                span_tag = tags[i].find('span')
                if span_tag:
                    span_text = span_tag.get_text(separator='\n')
                    if span_text.strip() != '· Optional':
                        content += '\n\t\tdata-type: ' + span_text
                        content += '\n\t\tpurpose: ' + \
                            div_tag[j].get_text(
                                separator='\n')
                        j += 1
                    span_tag.decompose()
                if tags[i].contents:
                    content += READ_DATA_SAFETY.indent_content(tags[i])
        return content

    @staticmethod
    async def scrape_link(url):
        loop = asyncio.get_event_loop()
        soup = await loop.run_in_executor(None, READ_DATA_SAFETY.load_html_content, url)
        text = READ_DATA_SAFETY.filter_content(soup)
        return text

    @staticmethod
    def formated_data(content):
        content_data = ''
        lines = content.splitlines()
        for i in range(len(lines)):
            category = data_section = data_type = purpose = optional = ''
            if lines[i].startswith(' data-section: No data shared with third parties'):
                data_section = lines[i].replace(' data-section: ', '')
                content_data = content_data + data_section
            if lines[i].startswith(' data-section: Data shared'):
                data_section = lines[i].replace(' data-section: ', '')
                for j in range(i + 1, len(lines)):
                    if lines[j].startswith('\t category: '):
                        category = lines[j].replace('\t category: ', '')
                        content_data = content_data + category+"("
                        for k in range(j + 1, len(lines)):
                            if lines[k].startswith('\t\tdata-type: '):
                                data_type = lines[k].replace(
                                    '\t\tdata-type: ', '')
                                content_data = content_data + data_type+", "
                            elif lines[k].startswith('\t\tpurpose: '):
                                purpose = lines[k].replace('\t\tpurpose: ', '')
                                if purpose.endswith(' · Optional'):
                                    optional = True
                                    purpose = purpose.replace(
                                        ' · Optional', '')
                                else:
                                    optional = False
                                purpose = purpose.replace(', ', ' - ')

                            elif lines[j].startswith('\t category: '):
                                content_data = content_data[:-2] + "), "
                                break
                    elif lines[j].startswith(' data-section: '):
                        break
        if not content_data.startswith('No'):
            content_data = content_data[:-2] + ";"
        else:
            content_data = content_data + ";"
        return content_data

    @staticmethod
    def generate_result(user_url):
        preprocess_datasafety = asyncio.run(
            READ_DATA_SAFETY().scrape_link(user_url))

        content_data_safety = READ_DATA_SAFETY().formated_data(
            preprocess_datasafety)
        return content_data_safety


class READ_PRIVACY_POLICY:

    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def get_completion(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.9,
        )
        return response.choices[0].message["content"]

    @staticmethod
    def remove_empty_lines(content):
        lines = content.split('\n')
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        return '\n'.join(cleaned_lines)

    @staticmethod
    def check_valid_token_prompt(prompt):
        tokens = prompt.split()
        return len(tokens) <= 3000

    @staticmethod
    def generate_result(url):
        article = Article(url)
        article.download()
        article.parse()
        text = READ_PRIVACY_POLICY.remove_empty_lines(article.text)
        return text
        # prompt = "Help me to find only sharing information section from content below: \n"
        # check_valid_token_prompt = READ_PRIVACY_POLICY.check_valid_token_prompt(
        #     prompt + text)
        # if check_valid_token_prompt:
        #     response = READ_PRIVACY_POLICY.get_completion(prompt + text)
        #     return READ_PRIVACY_POLICY.remove_empty_lines(response)
        # else:
        #     return "No provide sharing information section"

class GET_INFO:

    @staticmethod
    def loop_csv(csv_path, ds, pp):
        with open(csv_path, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for index, row in enumerate(reader):
                print("\n_____________ Run times " +
                      row[0] + " <" + row[2] + "> " + "_____________")
                content_5 = ds.generate_result(row[8])
                content_6 = pp.generate_result(row[9])
                print("_____________ Result _____________")
                print(content_5)
                print("__________________________")
                print(content_6)
                print("~~~~~~~~~~~~~~ Success ~~~~~~~~~~~~~~\n")


if __name__ == "__main__":
    ds = READ_DATA_SAFETY()
    pp = READ_PRIVACY_POLICY()

    csv_path = "/Users/nghiempt/Observation/sr-dps/sr-dps-server/bonus/test.csv"

    GET_INFO().loop_csv(csv_path, ds, pp)
