import random
from datetime import datetime
from io import BytesIO
import aiohttp
import discord
import discord.utils
from discord.errors import HTTPException
from discord.ext import commands

activity = discord.Game(name="Type !help for command list")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), activity=activity)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
bot.remove_command("help")


@bot.group(invoke_without_command=True)
async def help(ctx, page=None):
    if page is None or page == "1":
        em = discord.Embed(title="Help")
        em.set_footer(text="Use !help 2 for the next page")
        em.add_field(name="FFXIV", value="Posts funny pasta, takes no input", inline=False)
        em.add_field(name="owoify", value="<text>", inline=False)
        em.add_field(name="vibecheck", value="A 1 in 6 chance to pass a vibecheck from the"
                                             " bot, takes no input", inline=False)
        em.add_field(name="converttemp", value="<temp value and type, ex: !converttemp 38C> Converts temperature from "
                                               "celsius or fahrenheit "
                                               " to the opposite type", inline=False)
        em.add_field(name="stealemoji", value="<emoji> Takes given emoji from another discord server"
                                              " and adds it to the current discord server", inline=False)
        em.add_field(name="stealimage", value="<name of emoji> Takes attached image and converts it into an emote",
                     inline=False)
        await ctx.send(embed=em)

    elif page == "2":
        em2 = discord.Embed(title="Help 2")
        em2.set_footer(text="Use !help 3 for the next page")
        em2.add_field(name="bettingGame", value="Starts a betting game that lasts until you end it. Use !bettingGame "
                                                "recordholder "
                                                "to check current record holder. Doesn't take any inputs until after "
                                                "use",
                      inline=False)
        em2.add_field(name="joke", value="<jokeNumber> Pulls from a notepad file containing (bad) jokes."
                                         " Can be used with a number to specify a joke,"
                                         " or no number for a random joke", inline=False)
        em2.add_field(name="jokeadd", value="<jokeText> Adds a joke to the joke list", inline=False)
        em2.add_field(name="roll", value="<number of die>d<sides of die> ex: 1d20", inline=False)
        em2.add_field(name="spongebob", value="<text> Makes text-- lOoK lIkE tHiS", inline=False)
        em2.add_field(name="eightball", value="Takes no input, outputs a typical eightball response", inline=False)
        em2.add_field(name="tsuncheck", value="Takes no input,"
                                              " checks whether someone is being a sussy baka", inline=False)
        await ctx.send(embed=em2)

    elif page == "3":
        em3 = discord.Embed(title="Help 3")
        em3.set_footer(text="This is the final page")
        em3.add_field(name="spray", value="Takes no input. Someone being too horny? Time to the spray", inline=False)
        em3.add_field(name="stairmaster", value="Takes no input. Stairmaster scary", inline=False)
        em3.add_field(name="yes", value="Takes no input. When you want a gif of a dude nodding", inline=False)
        em3.add_field(name="capcheck", value="Someone cappin? Check with this command", inline=False)
        em3.add_field(name="minecraftserver", value="Gives info on the minecraft server", inline=False)
        await ctx.send(embed=em3)

    else:
        await ctx.send("Please use a valid page number.")


@bot.command()
async def minecraftserver(ctx):
    em = discord.Embed(title="Minecraft server info")
    em.add_field(name="Server ip", value="minecraft69420.ddns.net")
    em.add_field(name="Get modpack at", value="https://www.curseforge.com/minecraft/modpacks/pog-in-the-pants-modpack",
                 inline=False)
    em.add_field(name="Modlist: Aether 2", value="Biomes o plenty, Chisel,"
                                                 " Davincis vessels, Immersive Engineering,"
                                                 " Immersive petroleum, Inventory tweaks,"
                                                 " Journeymap, Just enough items, Minecolonies,"
                                                 " Mouse tweaks, MovingWorld, Redstone"
                                                 " flux, Thermal expansion, foundation, and innovation,"
                                                 "Dungeon tactics, Roguelike dungeons, and tinkers")
    await ctx.send(embed=em)


async def errorReporter(ctx, error):
    k = open("logs.txt", "a")
    k.write(current_time + " " + str(error) + "\n")
    k.close()
    await ctx.send("Error: " + str(error))


@bot.command()
async def capcheck(ctx):
    result = random.randint(0, 5)
    responses = {0: ' Yup, thats cap', 1: ' Yup, thats cap',
                 2: ' Yup, thats cap', 3: ' Yup, thats cap',
                 4: ' Yup, thats cap', 5: ' No cap here'}
    await ctx.send(f"{responses.get(result)}")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    channel = bot.get_channel(424035206031474690)
    await channel.send("Hi there, I'm Cyrene, a discord bot!")


@bot.command()
async def stairmaster(ctx):
    await ctx.send("https://media2.giphy.com/media/t9lBEE2FGMzbY9s5IX/giphy.gif")


"""@bot.command()
async def testcommand2(ctx):
    if ctx.channel.is_nsfw():
        url = "https://www.redgifs.com/watch/wordygeneroussteed"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        for link in doc.find_all('link', rel="canonical", href=True):
            # await ctx.send(link['href'])
            embed = discord.Embed(title="test")
            await ctx.send(embed=embed.set_image(url="https://redgifs.com/ifr/wordygeneroussteed"))"""

"""  
@bot.command()
async def 32rolereact(ctx, emojis: discord.Emoji, role: discord.Role):
    msg = await ctx.send("React to me")
    for emoji in emojis:
        await msg.add_reaction(emoji)
"""


@bot.event
async def on_reaction_add(reaction, user):
    role = discord.utils.get(user.guild.roles, name="blue")
    if reaction.emoji == "🤲":
        await user.add_roles(role)


@bot.event
async def on_reaction_remove(reaction, user):
    role = discord.utils.get(user.guild.roles, name="blue")
    if reaction.emoji == "🤲":
        await user.remove_roles(role)


@bot.command()
async def owoify(ctx, *, words):
    words = words.replace('l', 'w').replace('there', 'dewe').replace('r', 'w').replace('L', 'W').replace('R', 'W')
    await ctx.send("" + words)


@owoify.error
async def owoify_error(ctx, error):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await errorReporter(ctx, error)


@bot.event
async def on_message(message):
    msg = message.content
    if 'fuck you cyrene' in msg.lower():
        await message.channel.send("No you 🙂")
    if 'eat ass' in msg.lower():
        await message.channel.send("Hell yeah")
    if 'fuck you bot' in msg.lower():
        await message.channel.send("No you 🙂")
    await bot.process_commands(message)
    if '69' in msg:
        await message.channel.send('Nice')
    if '420' in msg:
        await message.channel.send('Just blaze!')


@bot.command()
async def converttemp(ctx, temp):
    temp = temp.lower()

    if 'f' in temp:
        temp = temp.split("f")[0]
        final_temp = (int(temp) - 32) * 5 / 9
        await ctx.send(f'The temperature of {temp}F is {int(final_temp)}C')

    elif 'c' in temp:
        temp = temp.split('c')[0]
        final_temp = (int(temp) * 9 / 5) + 32
        await ctx.send(f'The temperature of {temp}C is {int(final_temp)}F')

    else:
        await ctx.send("Error, please use a valid number")


@converttemp.error
async def converttemp_error(ctx, error):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await errorReporter(ctx, error)

    elif isinstance(error, ValueError):
        await errorReporter(ctx, error)


@bot.command()
async def FFXIV(ctx):
    await ctx.send("Did you know that the critically acclaimed MMORPG Final Fantasy XIV has a"
                   " free trial, and includes the entirety of A Realm Reborn AND the award-"
                   "winning Heavensward expansion up to level 60 with no restrictions on play"
                   "time? Sign up, and enjoy Eorzea today!")


@bot.command()
async def vibecheck(ctx):
    result = random.randint(1, 5)
    userid = ctx.message.author.id
    user = bot.get_user(userid)
    if result == 5:
        await ctx.send('You have passed the vibecheck')
    else:
        if str(user) == 'OrionsFate#2575':
            await ctx.send('LMAOOOOO Orion fucked it AGAIN')
        else:
            if str(user) == 'OrionsFate#2575':
                await ctx.send('Orion finally vibing for once')
            await ctx.send("You failed the vibecheck")


@bot.command()
async def joke(ctx, number=None):
    j = open("Jokes.txt", "r")

    jokes = []
    for x in j:
        jokes.append(x)

    number2 = len(jokes)

    if number is None:
        number = random.randint(0, number2 - 1)
    j.close()
    await ctx.send(jokes[int(number)])

@bot.command()
async def facts(ctx, number=None):
    f = open("facts.txt", "r")

    facts = []
    for x in f:
        facts.append(x)

    number2 = len(facts)

    if number is None:
        number = random.randint(0, number2 - 1)
    f.close()
    await ctx.send(facts[int(number)])



@joke.error
async def joke_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandInvokeError):
        if isinstance(error.original, ValueError):
            await errorReporter(ctx, error)
        if isinstance(error.original, IndexError):
            await errorReporter(ctx, error)
    if isinstance(error, discord.ext.commands.UnexpectedQuoteError):
        await errorReporter(ctx, error)


@bot.command()
async def jokeadd(ctx, *, joke_given):
    counter = -1
    r = open("Jokes.txt", "a+")
    r.write("\n" + joke_given)
    r.close()

    r = open("Jokes.txt", "r")
    for _ in r:
        counter += 1
    r.close()
    await ctx.send("Joke " + str(counter) + " added poggerifically")


@jokeadd.error
async def jokeadd_error(ctx, error):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await ctx.send("Please add a joke. Valid usage of this command is !jokeadd <joke>")

@bot.command()
async def quoteadd(ctx, *, quote_given):
    counter = -1
    r = open("quote.txt", "a+")
    r.write("\n" + quote_given)
    r.close()


def mock(d):
    i = True
    ret = ''
    for char in d:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()

        i = not i
    return ret


@bot.command()
async def spongebob(ctx, *, words):
    await ctx.send(mock(words))


@spongebob.error
async def spongebob_error(ctx, error):
    await errorReporter(ctx, error)


@bot.command()
async def roll(ctx, die1):
    result1 = 0
    die1 = die1.partition("d")
    counter = int(die1[0])
    while counter > 0:
        result2 = random.randint(1, int(die1[2]))
        result1 = result1 + result2
        counter = counter - 1
    em2 = discord.Embed(title="", description="")
    em2.add_field(name="Result", value=str(result1))
    await ctx.send(embed=em2)


@roll.error
async def roll_error(ctx, error):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await errorReporter(ctx, error)

    elif isinstance(error.original, ValueError):
        await ctx.send("Error: please enter a number greater than 0")
        await errorReporter(ctx, error)
    else:
        await errorReporter(ctx, error)


@bot.command()
async def eightball(ctx, *, message=None):
    answers = ['Yes', 'No', 'No way lmaooooooooooooooooooooooo', 'My reply is no',
               'It is certain', 'Ask again later', 'As I see it yes', 'Better not tell you now', 'No you fucking baka',
               'Hell yeah brother']

    msg = message.lower()
    if message is not None:
        await ctx.send(msg.replace("i ", "you ").replace("we", "you").replace("am", "are").replace("you", "I") + "? "
                       + random.choice(answers))
    else:
        await ctx.send(random.choice(answers))


@eightball.error
async def eightball_error(ctx, error):
    await errorReporter(ctx, error)


@bot.command()
async def yes(ctx):
    await ctx.send("https://tenor.com/view/anger-management-jack-nicholson-yes-duh-nods-gif-5222702")


@bot.command()
async def stealimage(ctx, name):
    name2 = name
    name = ctx.message
    image = name.attachments
    image2 = image[0].url

    async with aiohttp.ClientSession() as ses:
        async with ses.get(str(image2)) as r:
            img_or_gif = BytesIO(await r.read())
            b_value = img_or_gif.getvalue()
            if r.status == 200:
                await ctx.guild.create_custom_emoji(image=b_value, name=name2)

    await ctx.send(f"Successfully made emoji {name2}")


@stealimage.error
async def stealimage_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandInvokeError):
        if isinstance(error.original, discord.errors.InvalidArgument):
            await errorReporter(ctx, error)
            await ctx.send("Unsupported format")
            return
        if isinstance(error.original, HTTPException):
            await errorReporter(ctx, error)
            await ctx.send("Image is either too big, or you sent more than one. Send only one image and try resizing "
                           "it.")
            return
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await errorReporter(ctx, error)
        await ctx.send("Please enter a name")
    elif isinstance(error, discord.ext.commands.CommandInvokeError):

        await errorReporter(ctx, error)
        await ctx.send("Please input an image")
    else:
        await errorReporter(ctx, error)


@bot.command()
async def stealemoji(ctx, emoji: discord.PartialEmoji, name2):
    emoji = emoji.url
    async with aiohttp.ClientSession() as ses:
        async with ses.get(str(emoji)) as r:
            img_or_gif = BytesIO(await r.read())
            b_value = img_or_gif.getvalue()
            if r.status == 200:
                await ctx.guild.create_custom_emoji(image=b_value, name=name2)
                await ctx.send(f"Successfully made emoji {name2}")
                await ses.close()


@stealemoji.error
async def stealemoji_error(ctx, error):
    if isinstance(error, discord.ext.commands.PartialEmojiConversionFailure):
        await errorReporter(ctx, error)
        await ctx.send("Invalid emoji")
    else:
        await errorReporter(ctx, error)


@bot.command()
async def tsuncheck(ctx):
    result = random.randint(0, 10)
    responses = {0: ' No tun energy detected', 1: ' Trace amounts of tsun detected.',
                 2: ' Tsun levels are below average', 3: ' Tsun levels moderate.',
                 4: ' Tsun levels slightly below average', 5: ' Tsun levels average.',
                 6: ' Yeah, you def kinda tsun', 7: " B-b-baka! Levels rising.",
                 8: ' Entering dangerously high tsun levels', 9: " You're at Senjougahara levels rn",
                 10: " You're a sussy baka, or maybe you're a bussy saka?"}
    await ctx.send(f"🔎The tsun level is: {str(result) + responses.get(result)}")


@bot.command()
async def spray(ctx):
    await ctx.send("https://tenor.com/view/water-spray-stop-sprinkle-water-gif-11895255")


@bot.group(invoke_without_command=True)
async def bettingGame(ctx):
    r = open("bettingrecord.txt", "r")
    betting_record = r.read()
    r.close()
    total = 10
    counter = 1

    em = discord.Embed()
    em.add_field(name="Betting game", value="This is a betting game where"
                                            " you start with $10 and can bet as many times as you wish.\n"
                                            "Start by inputting how much you "
                                            "would like to bet, and input -1 if you wish to end your"
                                            " suffering early. ")
    await ctx.send(embed=em)

    def check(msg2):
        return msg2.author == ctx.author and msg2.channel == ctx.channel

    while True:

        try:

            em = discord.Embed()
            em.add_field(name="Enter bet", value="$")
            await ctx.send(embed=em)

            msg = await bot.wait_for("message", check=check)
            bet = int(msg.content)

            if bet == -1:
                em = discord.Embed()
                em.add_field(name="Final amount", value="$" + str(round(total)))
                await ctx.send(embed=em)
                if int(betting_record) < total:
                    userid = ctx.message.author.id
                    user = bot.get_user(userid)
                    betting_record = total
                    r = open("bettingrecord.txt", "w")
                    r.write(str(betting_record))
                    r.close()
                    r = open("bettingrecordholder.txt", "w")
                    r.write(str(user))
                    r.close()

                return

            if bet > total:
                await ctx.send("Bet amount cannot be greater than total amount")
                continue

            if bet < 0:
                await ctx.send("Bet amount cannot be lower than 0")
                continue

        except ValueError:
            await ctx.send("Error, invalid bet, please enter a new one: ")
            continue

        die = random.randint(1, 10)

        if die >= 6:
            total = round((bet * 2) + total)
            em = discord.Embed(title="Betting game")
            em.add_field(name="Bet amount", value="$" + str(bet))
            em.add_field(name="Attempt number", value=str(counter))
            em.add_field(name="Roll", value=str(die))
            em.add_field(name="New total", value="$" + str(round(total)))
            await ctx.send(embed=em)

        elif 5 >= die > 1:
            total = round(total - (bet / 2))
            em = discord.Embed(title="Betting game")
            em.add_field(name="Attempt number", value=str(counter))
            em.add_field(name="Bet amount", value="$" + str(bet))
            em.add_field(name="Roll", value=str(die))
            em.add_field(name="New total", value="$" + str(round(total)))
            await ctx.send(embed=em)

        elif die <= 1:
            total = round(total - (bet * 2))
            userid = ctx.message.author.id
            user = bot.get_user(userid)
            if str(user) == 'OrionsFate#2575':
                em = discord.Embed(title="Betting game")
                em.set_footer(text="Lmao Orion fucked it again")
                em.add_field(name="Attempt number", value=str(counter))
                em.add_field(name="Bet amount", value="$" + str(bet))
                em.add_field(name="Roll", value=str(die))
                em.add_field(name="New total", value="$" + str(round(total)))
                await ctx.send(embed=em)

            else:

                em = discord.Embed(title="Betting game")
                em.add_field(name="Attempt number", value=str(counter))
                em.add_field(name="Bet amount", value="$" + str(bet))
                em.add_field(name="Roll", value=str(die))
                em.add_field(name="New total", value="$" + str(round(total)))
                await ctx.send(embed=em)

        if 1 > total > 0:
            total = 1
            continue
        elif total <= 0:

            em = discord.Embed()
            em.add_field(name="Betting game",
                         value="Sorry, I don't speak broke. Ending game... (Total less than 0")
            await ctx.send(embed=em
                           )
            return
        counter = counter + 1

        if total > int(betting_record):
            await ctx.send("Your current total amount is higher than the total betting record,"
                           " if you quit now (by inputting -1) you will make a new record.")

    em = discord.Embed()
    em.add_field(name="Final amount", value="$" + str(round(total)))
    await ctx.send(embed=em)
    if int(betting_record) < total:
        userid = ctx.message.author.id
        user = bot.get_user(userid)
        betting_record = total
        r = open("bettingrecord.txt", "w")
        r.write(str(betting_record))
        r.close()
        r = open("bettingrecordholder.txt", "w")
        r.write(str(user))
        r.close()


@bettingGame.command()
async def recordholder(ctx):
    r = open("bettingrecord.txt", "r")
    bettingrecord = r.read()
    r.close()
    r = open("bettingrecordholder.txt", "r")
    user = r.read().split("#")[0]
    r.close()

    em = discord.Embed()
    em.add_field(name="Betting record", value="$" + str(bettingrecord))
    em.add_field(name="Held by", value=user)

    await ctx.send(embed=em)


if __name__ == '__main__':
    f = open("key.txt", "r")
    key = f.readline()
    bot.run(key)
