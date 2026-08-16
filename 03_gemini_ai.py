from google import genai

client = genai.Client(api_key="API_KEY")


interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input= command,
    system_instruction="You are a person named Ankit. I am a chart bot.",
)

print(interaction.output_text)





