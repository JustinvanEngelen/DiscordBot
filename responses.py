from random import choice, randint

# Example list to store messages
messages = []


def add_message(user_input: str) -> None:
    messages.append(user_input)


def get_response(user_input: str) -> str:
    # Add the message to the message list
    add_message(user_input)

    lowered: str = user_input.lower()

    if lowered == '':
        return 'Je bent best stil...'
    elif 'kom csgo' in lowered:
        return 'het is cs2🤓'
    elif 'wat is jurgen' in lowered:
        return 'de meeste gay ass persoon die er bestaat'
    elif 'doei' in lowered:
        return 'Houdoe'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'help' in lowered:
        return 'Ik ben een chatbot, geen held 🦸‍♂️'
    elif 'ik ben moe' in lowered:
        return 'Dan moet je gaan slapen, luiwammes 😴'
    elif 'sigma' in lowered:
        return 'https://tenor.com/view/respec-gif-27091325'
    elif 'nuh uh' in lowered:
        return 'https://tenor.com/view/nuh-uh-nuh-uh-scout-tf2-gif-12750436057634665505'
    elif 'jurgen' in lowered:
        return 'https://tenor.com/view/spongebob-squarepants-gay-rainbow-lgbt-pride-month-gif-6443547037069682625'

