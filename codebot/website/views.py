from django.shortcuts import render


def home(request):
    lang_list = ['bash', 'batch', 'c', 'clike', 'cpp', 'csharp', 'css', 'csv', 'cypher', 'dart', 'django', 'docker',
                 'git', 'go', 'go-module', 'gradle', 'groovy', 'hsts', 'html', 'http', 'java', 'javascript', 'json',
                 'json5', 'markup-templating', 'mongodb', 'objectivec', 'perl', 'php', 'plsql', 'powerquery',
                 'powershell', 'python', 'r', 'regex', 'roboconf', 'robotframework', 'ruby', 'rust', 'sas', 'sass',
                 'scala', 'sparql', 'sql', 'swift', 'turtle', 'yaml']

    return render(request, 'home.html', {'lang_list': lang_list})
