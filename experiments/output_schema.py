from langchain import hub
from langchain_openai import ChatOpenAI
import pprint

if __name__ == "__main__":
    prompt = hub.pull("mk_test_output_schema")
    model = ChatOpenAI(model="gpt-4o-mini")
    chain = prompt|model
    response = chain.invoke({"text": "Today I realised that its efficient to search for third party packages or libraries than to implement things by our self. For example today I had to build a text editor which has features similar to a slack editor (multi level bulletins, linking etc). It soon became quite overwhelming thinking about all the cases that are to be covered. I then followed BDD and listed down all the behaviours that are expected from the editor then started looking for third party packages which would serve my purpose. Found a cool library called Quill editor which offered many rich text tools out of the box, although I had to override the libraries css to match my design it save a lot of time."})
    pprint.pp(response)
