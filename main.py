from flask import Flask
from llama_cpp import Llama

app = Flask(__name__)
llm = Llama(model_path="./models/7B/ggml-model.bin")

def settings(params, prompt):
    for param in list(params.keys()):
         pparam = '('+param+')'
         prompt = prompt.replace(pparam, params.get(param))
    return prompt

hprompt = '''Create a file to be hosted at the path "(path)" on "(name)"

Content-Type:'''

@app.route('/')
@app.route('/<path:path>')
def host(path):
    config = {"path" : "path", "name" : "the catocombs at the end of the web"}
    hprompt = settings(config, hprompt)
    output = llm(hprompt, max_tokens=1024, stop=['</html>'], echo=True)
    content = output.splitlines[0]
    doc = output.splitlines[1]
    return doc, 200, content

