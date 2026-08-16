# Import required libraries for OS interaction, timing, automation, clipboard access, and Gemini API
import ctypes
import time
import pyautogui
import pyperclip
from google import genai

# Initialize the Gemini client with the API key
client = genai.Client(api_key="API_KEY")

# Windows Mouse Event Constants for low-level input simulation
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000

# Get screen resolution dynamically using Windows user32 library
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)


def send_mouse_drag(x1, y1, x2, y2, steps=60, delay=0.01):
    # Step 1: Move mouse to starting coordinates and hold left click
    pyautogui.moveTo(x1, y1)
    time.sleep(0.2)
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)

    # Step 2: Generate smooth interpolated drag movements between start and end points
    for i in range(1, steps + 1):
        curr_x = int(x1 + (x2 - x1) * (i / steps))
        curr_y = int(y1 + (y2 - y1) * (i / steps))

        # Convert pixel coordinates to absolute normalized coordinates (0 to 65535) required by mouse_event
        norm_x = int(curr_x * 65535 / screen_width)
        norm_y = int(curr_y * 65535 / screen_height)

        # Trigger the mouse move event to the normalized position
        user32.mouse_event(
            MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, norm_x, norm_y, 0, 0
        )
        time.sleep(delay)

    # Step 3: Release the left mouse button
    time.sleep(0.2)
    user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# --- Execution ---


def is_last_message_from_sender(chat_log, sender_name="Bhai"):
    # Split the chat log to extract the most recent message block
    messages = chat_log.strip().split("/2026] ")[-1]
    # Check if the target sender is present in the latest message
    if sender_name in messages:
        return True 
    return False


# 1. Click taskbar icon to bring the chat application window to focus
pyautogui.click(963, 1169)

# Main automation loop to continuously check for incoming messages and reply
while True:   
    time.sleep(0.8)

    # 2. Clear clipboard contents before reading new data
    pyperclip.copy("")

    # 3. Perform hardware-level mouse drag to highlight/select chat history on screen
    send_mouse_drag(495, 134, 1827, 1044, steps=80, delay=0.015)
    time.sleep(0.3)

    # 4. Copy selected text to clipboard and click to deselect
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(453, 149)
    time.sleep(0.4)

    # Retrieve and print the copied chat log from clipboard
    chart_History = pyperclip.paste()
    print("Copied text:")
    print(chart_History)

    # 5. Check if the last received message is from the specified contact
    if is_last_message_from_sender(chart_History):
        # Call Gemini API with persona instructions and chat context to generate a response
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=chart_History,
            system_instruction="""You are a person named Pikachu . You are a chart bot. You are from India. You speak Odia,Hindi and English.Analyze the given query or chart . The respond should be the next chart reaponse as Pikachu. No one should know that you are a bot. You should not say that you are a bot. You should not say that you are an AI model. You should not say that you are an AI language model. You should not say that you are an AI assistant. You should not say that you are an AI chatbot. You should not say that you are an AI system. You should not say that you are an AI program. You should not say that you are an AI application. You should not say that you are an AI tool. You should not say that you are an AI service. You should not say that you are an AI platform. You should not say that you are an AI solution. You should not say that you are an AI technology. You should not say that you are an AI framework. You should not say that you are an AI architecture. You should not say that you are an AI model architecture. You should not say that you are an AI model framework. You should not say that you are an AI model technology. You should not say that you are an AI model solution. You should not say that you are an AI model service. You should not say that you are an AI model platform. You should not say that you are an AI model application. You should not say that you are an AI model program. You should not say that you are an AI model system.
            The output response should be short and simpple like normal human type in reply of  chart .
            
            """,
        )

        # Extract generated response text
        response = interaction.output_text

        # Copy the AI-generated reply to clipboard
        pyperclip.copy(response)
        time.sleep(0.2)

        # Click the chat message input box
        pyautogui.click(800, 1096)
        time.sleep(0.3)

        # Paste the response text into the input field
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.3)

        # Press Enter key to send the message
        pyautogui.press("enter")
        print("Message sent successfully!")