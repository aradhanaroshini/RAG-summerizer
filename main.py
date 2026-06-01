import os
from chunker import fun
from llm import llm_response
path=input("Attach your path here:")    #Initial Development for CLI build
path=path.strip("'").strip('"').strip()
result=fun(path)
notes=llm_response(result)
print(notes)



