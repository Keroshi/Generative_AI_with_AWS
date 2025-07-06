import string

responses = {
    "hi": "Hello! Welcome to TechGadget Support. How can I assist you today?",
    "hello": "Hello! Welcome to TechGadget Support. How can I assist you today?",
    "hey": "Hello! Welcome to TechGadget Support. How can I assist you today?",
    "do you have smartwatches": "Yes, we have a variety of smartwatches. You can check them out on our products page.",
    "smartwatches": "Yes, we have a variety of smartwatches. You can check them out on our products page.",
    "shipping time": "Shipping usually takes 3-5 business days.",
    "how long does shipping take": "Shipping usually takes 3-5 business days.",
    "shipping methods": "We offer standard, expedited, and overnight shipping.",
    "what are the shipping options": "We offer standard, expedited, and overnight shipping.",
    "return policy": "You can return products within 30 days of receipt for a full refund.",
    "how to return": "To return a product, please visit our returns page for a step-by-step guide.",
    "how do i return a product": "To return a product, please visit our returns page for a step-by-step guide.",
    "won’t turn on": "Make sure your gadget is charged. If it still won’t turn on, you can visit our troubleshooting page.",
    "device won't turn on": "Make sure your gadget is charged. If it still won’t turn on, you can visit our troubleshooting page.",
    "reset device": "To reset your device, hold down the power button for 10 seconds. If that doesn't work, please check the manual for a factory reset.",
    "how to reset device": "To reset your device, hold down the power button for 10 seconds. If that doesn't work, please check the manual for a factory reset.",
    "how to reset": "To reset your device, hold down the power button for 10 seconds. If that doesn't work, please check the manual for a factory reset.",
    "bye": "Thank you for visiting TechGadget. If you have more questions, feel free to ask. Goodbye!",
    "goodbye": "Thank you for visiting TechGadget. If you have more questions, feel free to ask. Goodbye!",
    "see you": "Thank you for visiting TechGadget. If you have more questions, feel free to ask. Goodbye!"
}


def get_bot_response(user_input):
    user_input = user_input.lower().translate(str.maketrans('', '', string.punctuation))
    for keyword, response in responses.items():
        if keyword == user_input:
            return response
    return "I'm not sure how to respond to that. Can you try asking something else?"


def chat():
    unknown_count = 0
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot: Goodbye! If you have any more questions, we're here to help.")
            break

        response = get_bot_response(user_input)
        if "I'm not sure how to respond to that." in response:
            unknown_count += 1
        else:
            unknown_count = 0

        if unknown_count < 3:
            print(f"Bot: {response}")
        else:
            print(
                "Bot: It seems like I'm having trouble understanding your questions. Please contact our human customer service representative for further assistance.")
            break


chat()
