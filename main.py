import discord
from spellchecker import SpellChecker
TOKEN = 'ODk2NDM0NDY1MDAwMjg4MjY2.YWHDpw.dOSms-I4eReSloUOeFRHVz9qmEE'
client = discord.Client()
spell = SpellChecker()

#Logging the bot on
@client.event
async def on_read():
    print('{0.user} logging on'.format(client))

#Splitting the # from the username
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    if message.author == client.user:
        return
    if message.channel.name == 'general':
        wordlist = []
        txt = user_message.split()
        badspelling = spell.unknown(txt)
        response = "Errors: "
        error = False
        if len(badspelling) >= 1:
            print(badspelling)
            for word in badspelling:
                wordlist.append(spell.correction(word) + " ")

            response = f"Hey {username}, Your message was: {message.content} This is what I corrected for you: "
            response += "".join(map(str, wordlist))
            # response += "  "
            error = True
            wordlist = []
        #For each word in the user input, the misspell will be added to a list, and the bot will tell the
        #user what they messed up. Afterwards, the list will be cleared for the next input.
        for i in txt:
            if i == 'ur':
                error = True
                response += ' You have used "ur", when you should be using "your." '
            if i == 'u':
                response += ' You have used "u", when instead it should be "you."'
                error = True
        if error:
            await message.channel.send(response)

client.run(TOKEN)