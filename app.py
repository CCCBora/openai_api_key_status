import gradio as gr
import openai
from api_usage import check_gpt4_availability, get_subscription, get_usage, check_key_availability

def get_key_info(key):
    # Return a dictionary containing key information
    openai.api_key = key
    key_avai = check_key_availability()
    info_dict = {"account_name": "",
                 "key_availability": key_avai,
                 "gpt4_availability": "",
                 "has_payment_method": "",
                 "used": "",
                 "limit": ""}
    if key_avai:
        info = get_subscription(key)
        used = get_usage(key)
        gpt4_avai = check_gpt4_availability()
        info_dict["account_name"] = info["account_name"]
        info_dict["gpt4_availability"] = gpt4_avai
        info_dict["has_payment_method"] = info["has_payment_method"]
        info_dict["used"] = used
        info_dict["limit"] = info["hard_limit_usd"]
    return info_dict


def clear_inputs(text):
    return ""

with gr.Blocks() as demo:
    gr.Markdown('''
    # OpenAI API Key Info
    ''')

    with gr.Row():
        with gr.Column():
            key =  gr.Textbox(lines=1, max_lines=1, label="OpenAI API Key")
            with gr.Row():
                clear_button = gr.Button("Clear")
                submit_button = gr.Button("Submit", variant="primary")
        with gr.Column():
            info = gr.JSON(label="OpenAI API Key Information")

    clear_button.click(fn=clear_inputs, inputs=[key], outputs=[key])
    submit_button.click(fn=get_key_info, inputs=[key], outputs=[info], api_name="get_key_info")


demo.queue(concurrency_count=1,  api_open=True)
demo.launch()