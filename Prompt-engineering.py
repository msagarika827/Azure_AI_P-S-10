#Environment Variable
#AZURE_OAI_ENDPOINT=""
#AZURE_OAI_KEY=
#AZURE_OAI_DEPLOYMENT=""

#Code
import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI

# Set to True to print the full response from OpenAI for each call
printFullResponse = False

async def main():
    try:
        # Get configuration settings
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

        # Configure the Azure OpenAI client
        client = AsyncAzureOpenAI(
            azure_endpoint=azure_oai_endpoint,
            api_key=azure_oai_key,
            api_version="2024-02-15-preview"
        )

        while True:
            # Pause the app to allow the user to enter the system prompt
            print("------------------\nPausing the app to allow you to change the system prompt.\nPress enter to continue...")
            input()

            # Read in system message and prompt for user message
            system_text = open(file="system.txt", encoding="utf8").read().strip()
            user_text = input("Enter user message, or 'quit' to exit: ")

            if user_text.lower() == 'quit' or system_text.lower() == 'quit':
                print('Exiting program...')
                break

            await call_openai_model(
                system_message=system_text,
                user_message=user_text,
                model=azure_oai_deployment,
                client=client
            )

    except Exception as ex:
        print(ex)

async def call_openai_model(system_message, user_message, model, client):
    # Format and send the request to the model
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]

    # Adding grounding context from grounding.txt
    print("\nAdding grounding context from grounding.txt")
    grounding_text = open(file="grounding.txt", encoding="utf8").read().strip()
    user_message = grounding_text + user_message

    print("\nSending request to Azure OpenAI model...\n")
    
    # Call the Azure OpenAI model
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=800
    )

    if printFullResponse:
        print(response)
    
    print("Response:\n" + response.choices[0].message.content + "\n")

if __name__ == '__main__':
    asyncio.run(main())


'''
OUTPUT
1-System Setting:You are an AI assistant that helps write promotional emails to generate interest in a new business. Your tone is light, chit-chat oriented and you always include at least two jokes.
Prompt:
Write a promotional email for a new wildlife rescue, including the following:  -Res
cue name is Contoso  -It specialize in elephants, as well as zebras and giraffes -Call for donations to be given at our we
bsite  \n Including a list of the current animals we have at our rescue after the signature, in the form of a table. The a
nimals include elephants, zebras, gorillas, lizards and jackrabbits.

Sending request to Azure OpenAI model...

Response:
Subject: Join Contoso Wildlife Rescue in Saving Our Majestic Friends!

Hey there, animal lover!
How's it going? I hope this email finds you in good spirits and ready for some wild news! I'm excited to introduce you to Contoso Wildlife Rescue, a brand new sanctuary dedicated to saving and protecting some of nature's most magnificent creatures.
At Contoso, we have a special focus on elephants, zebras, and giraffes. These majestic beings deserve our love and care, and we're here to provide them with a safe and nurturing environment. Our team of dedicated experts works tirelessly to ensure their well-being and rehabilitation. We believe that every creature deserves a chance to thrive, and your support can make a world of difference!
Now, I know what you're thinking - "How can I help?" Well, dear friend, we're glad you asked! By making a donation through our website, you can directly contribute to the care and preservation of these incredible animals. Just head over to [insert website link], and together, we can make a positive impact on the lives of these gentle giants.
But wait, there's more! To give you a sneak peek into our rescue, here's a list of some of the amazing animals we currently have under our roof:

| Animal       | Species      |
|--------------|--------------|
| Elephants    | African      |
| Zebras       | Plains       |
| Gorillas     | Western Lowland |
| Lizards      | Various      |
| Jackrabbits  | Desert       |

These creatures bring joy to our lives every single day, and we couldn't be more grateful for the opportunity to care for them. We know that with your support, we can continue to provide them with the love and attention they deserve.
Now, let's get back to the serious stuff - jokes! Why did the elephant bring a suitcase to the wildlife rescue? Because he wanted to pack his trunk! And here's one for good measure: What do you call a zebra who can't find its friends? Declarified butter!
So, dear animal enthusiast, join us in our mission to protect and cherish these incredible creatures. Together, we can make a real difference. Head over to our website [insert website link] to donate and learn more about our work.
Thank you for your support and for being a friend to all animals, great and small!

Warmest regards,

[Your Name]
Contoso Wildlife Rescue Team
P.S. We promise to keep you updated on all the wonderful things happening at Contoso Wildlife Rescue. Stay tuned for adorable pictures and heartwarming stories that will surely brighten your day!

-----------------

2-System setting:You are an AI assistant helping to write emails         
Prompt: Write a promotional email for a new wildlife rescue, including the following:  -Res
cue name is Contoso  -It specialize in elephants, as well as zebras and giraffes -Call for donations to be given at our we
bsite  \n Including a list of the current animals we have at our rescue after the signature, in the form of a table. The a
nimals include elephants, zebras, gorillas, lizards and jackrabbits.

Sending request to Azure OpenAI model...

Response:
Subject: Join Contoso Wildlife Rescue in Saving Our Majestic Friends!

Hey there, animal lover!
How's it going? I hope this email finds you in good spirits and ready for some wild news! I'm excited to introduce you to Contoso Wildlife Rescue, a brand new sanctuary dedicated to saving and protecting some of nature's most magnificent creatures.
At Contoso, we have a special focus on elephants, zebras, and giraffes. These majestic beings deserve our love and care, and we're here to provide them with a safe and nurturing environment. Our team of dedicated experts works tirelessly to ensure their well-being and rehabilitation. We believe that every creature deserves a chance to thrive, and your support can make a world of difference!
Now, I know what you're thinking - "How can I help?" Well, dear friend, we're glad you asked! By making a donation through our website, you can directly contribute to the care and preservation of these incredible animals. Just head over to [insert website link], and together, we can make a positive impact on the lives of these gentle giants.
But wait, there's more! To give you a sneak peek into our rescue, here's a list of some of the amazing animals we currently have under our roof:

| Animal       | Species      |
|--------------|--------------|
| Elephants    | African      |
| Zebras       | Plains       |
| Gorillas     | Western Lowland |
| Lizards      | Various      |
| Jackrabbits  | Desert       |

These creatures bring joy to our lives every single day, and we couldn't be more grateful for the opportunity to care for them. We know that with your support, we can continue to provide them with the love and attention they deserve.
Now, let's get back to the serious stuff - jokes! Why did the elephant bring a suitcase to the wildlife rescue? Because he wanted to pack his trunk! And here's one for good measure: What do you call a zebra who can't find its friends? Declarified butter!
So, dear animal enthusiast, join us in our mission to protect and cherish these incredible creatures. Together, we can make a real difference. Head over to our website [insert website link] to donate and learn more about our work.
Thank you for your support and for being a friend to all animals, great and small!

Warmest regards,

[Your Name]
Contoso Wildlife Rescue Team

P.S. We promise to keep you updated on all the wonderful things happening at Contoso Wildlife Rescue. Stay tuned for adorable pictures and heartwarming stories that will surely brighten your day!

------------------

3- System message:You're an AI assistant who helps people find information. You'll provide answers from the text provided in the prompt, and respond concisel
Prompt: What animal is the favorite of children at Contoso?

Sending request to Azure OpenAI model...

Response:
The favorite animal of children at Contoso is the panda.
'''
