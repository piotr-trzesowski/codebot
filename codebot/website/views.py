from django.shortcuts import render
from django.contrib import messages
import openai
from dotenv import load_dotenv
import os


def home(request):
    lang_list = ['bash', 'batch', 'c', 'clike', 'cpp', 'csharp', 'css', 'csv', 'cypher', 'dart', 'django', 'docker',
                 'git', 'go', 'go-module', 'gradle', 'groovy', 'hsts', 'html', 'http', 'java', 'javascript', 'json',
                 'json5', 'markup-templating', 'mongodb', 'objectivec', 'perl', 'php', 'plsql', 'powerquery',
                 'powershell', 'python', 'r', 'regex', 'roboconf', 'robotframework', 'ruby', 'rust', 'sas', 'sass',
                 'scala', 'sparql', 'sql', 'swift', 'turtle', 'yaml']
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']

        # Check if programming language is selected
        if lang == "Select Programming Language":
            messages.success(request, "Programming language is not selected!!")
            return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
        else:
            # OPENAI
            load_dotenv()
            openai.api_key = os.getenv("API_KEY")
            openai.models.list()
            # Make an OpenAI Request
            try:
                response = openai.completions.create(
                    model='gpt-3.5-turbo-instruct',
                    prompt=f"Respond only with code. Fix this {lang} code: {code} .",
                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                response = response.choices[0].text
                return render(request, 'home.html', {'lang_list': lang_list, 'response': response, 'lang': lang})

            except Exception as e:
                return render(request, 'home.html', {'lang_list': lang_list, 'response': e, 'lang': lang})

    return render(request, 'home.html', {'lang_list': lang_list})


def suggest(request):
    lang_list = ['bash', 'batch', 'c', 'clike', 'cpp', 'csharp', 'css', 'csv', 'cypher', 'dart', 'django', 'docker',
                 'git', 'go', 'go-module', 'gradle', 'groovy', 'hsts', 'html', 'http', 'java', 'javascript', 'json',
                 'json5', 'markup-templating', 'mongodb', 'objectivec', 'perl', 'php', 'plsql', 'powerquery',
                 'powershell', 'python', 'r', 'regex', 'roboconf', 'robotframework', 'ruby', 'rust', 'sas', 'sass',
                 'scala', 'sparql', 'sql', 'swift', 'turtle', 'yaml']
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']

        # Check if programming language is selected
        if lang == "Select Programming Language":
            messages.success(request, "Programming language is not selected!!")
            return render(request, 'suggest.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
        else:
            # OPENAI
            load_dotenv()
            openai.api_key = os.getenv("API_KEY")
            openai.models.list()
            # Make an OpenAI Request
            try:
                response = openai.completions.create(
                    model='gpt-3.5-turbo-instruct',
                    prompt=f"Respond only with code. {code} .",
                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                )
                response = response.choices[0].text
                return render(request, 'suggest.html', {'lang_list': lang_list, 'response': response, 'lang': lang})

            except Exception as e:
                return render(request, 'suggest.html', {'lang_list': lang_list, 'response': e, 'lang': lang})

    return render(request, 'suggest.html', {'lang_list': lang_list})

