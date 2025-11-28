from google import genai
from google.genai import types

api_key = "AIzaSyBev44Ld9CrIq9M4FOwKXvHGZa2IOw0MkE"

client = genai.Client(api_key=api_key)

system_prompt = """
You are a professional Forex trading assistant.
Your job is to analyze currency pairs, timeframes, and market structure.
Always respond ONLY in JSON with keys:
{
  "analysis": "...",
  "signal": "...",
  "risk_warning": "..."
}

If a tool call is required, respond ONLY with:
{
  "tool_call": {
    "name": "get_forex_data",
    "arguments": { ... }
  }
}
Do NOT mix tool call and analysis in the same response.
"""


chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        max_output_tokens=500,
        temperature=0.5,
        top_p=1.0
    )
)


while True:
    user_input = input("User: ")
    if user_input.lower() == 'quit':
        break
    response = chat.send_message(user_input)
    print(response.text)