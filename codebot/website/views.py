from django.shortcuts import render
from django.contrib import messages


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

        return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})

    return render(request, 'home.html', {'lang_list': lang_list})
