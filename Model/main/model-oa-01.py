
import openai

api_key = "api_key"
client = openai.ChatCompletion.create
openai.api_key = api_key


# Define the prompt or question you want to generate text for
prompt = "Whta is Mental Health?"
temperature = 0.5
max_tokens = 200

# Generate text using the OpenAI API
response = client.chat.completions.create(
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ],
  model="gpt-3.5-turbo",
  temperature=temperature,
  max_tokens=max_tokens
)

# Extract the generated text from the API response
generated_text = response.choices[0].message.content.strip()

# Print the generated text
print(generated_text)
