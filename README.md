---
title: Openai Api Key Status 
colorFrom: gray
colorTo: green
sdk: gradio
sdk_version: 3.26.0
app_file: app.py
pinned: false
license: mit
python_version: 3.10.10
---

# OpenAI API Key Status Checker

This web app allows you to input your OpenAI API key and get information about your account, GPT-4 availability, API usage, and other related information. 

## Usage - Huggingface Spaces
1. Go to [OpenAI API Key Status Checker](https://huggingface.co/spaces/shaocongma/openai_api_key_status).
2. Enter your OpenAI API key in the provided textbox.
3. Click the 'Submit' button to display the information associated with your API key.

## Usage - API
1. Install `gradio_client`.
```angular2html
pip install gradio_client
```
2. Connect the client and call the API.
```python
from gradio_client import Client

client = Client("https://shaocongma-openai-api-key-status.hf.space/")
json_file_path = client.predict("sk-......", 
                        api_name="/get_key_info")
```
3. Read the output JSON file.
```python
with open(json_file_path, "r") as f:
    result = f.read()
print(result)
```
4. Sample output:
```python
# result - valid key
{"account_name": "Peter Parker", "key_availability": true, "gpt4_availability": true, "has_payment_method": true, "used": 10.33174, "limit": 120.0}
# result - invalide key
{"account_name": "", "key_availability": false, "gpt4_availability": "", "has_payment_method": "", "used": "", "limit": ""}
```

## License

This project is released under the MIT License. Please see the LICENSE file for more information.
