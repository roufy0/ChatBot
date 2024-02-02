import gradio as gr
import openai
openai.api_key='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'

message_history=[]

def predict(input):
    global message_history
    message_history.append({'role':'user','content':input})
    completion=openai.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=message_history)
    
    reply_content=completion.choices[0].message.content
    print(reply_content)
    message_history.append({'role':'assistant','content':reply_content})
    response=[(message_history[i]['content'],message_history[i+1]['content'])for i in range(0,len(message_history)-1,2)]
    return response

with gr.Blocks() as demo:
    chatbot=gr.Chatbot()
    with gr.Row():
        txt=gr.Textbox(show_label=False ,placeholder="type your message here")
        txt.submit(predict,txt,chatbot)
        txt.submit(lambda:"",None,txt)
        
demo.launch()
        
    