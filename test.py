from llama_cpp import Llama

llm = Llama(model_path="./model.bin")

def settings(params, prompt):
    for param in list(params.keys()):
         perparam = '('+param+')'
         prompt = prompt.replace(perparam, params.get(param))
    return prompt

prompt = '''Create a file to be hosted at the path "(path)" on "(name)"
(desc)

Content-Type:'''

path = input("path:")

config = {"desc":"", "path" : path, "name" : "the catocombs at the end of the web"}
prompt = settings(config, prompt)
output = llm(prompt, max_tokens=1024, stop=['</html>'], echo=True)
print(output)