import pywhatkit as pwk
import pyautogui
import time

# Function to read phone numbers from a file
def read_phone_numbers(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Read phone numbers from the text file
phone_numbers = read_phone_numbers(r"C:\Users\astro\Documents\python\phone_numbers.txt")

# Message to send
message = "Type your messege"

# Loop through each number and send a message every 10 seconds
for number in phone_numbers:
    try:
        # Loading time for WhatsApp Web
        loading_time = 10  # Adjust as needed for loading

        # Send the message instantly, keeping the tab open
        pwk.sendwhatmsg_instantly(number, message, wait_time=loading_time, tab_close=False)
        print(f"Message sent to {number}")
        # Wait for 10 seconds before closing the tab
        time.sleep(15)
        pyautogui.hotkey('ctrl', 'w')  # Close the tab

        # Wait for an additional 10 seconds before sending the next message
        time.sleep(10)

    except Exception as e:
        print(f"Failed to send message to {number}: {e}")
