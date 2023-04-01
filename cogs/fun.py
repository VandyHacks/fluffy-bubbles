""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

import random

import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import Context
import datetime
from helpers import checks


class Choice(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Heads", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        self.value = "heads"
        self.stop()

    @discord.ui.button(label="Tails", style=discord.ButtonStyle.blurple)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = "tails"
        self.stop()


class RockPaperScissors(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Scissors", description="You choose scissors.", emoji="✂"
            ),
            discord.SelectOption(
                label="Rock", description="You choose rock.", emoji="🪨"
            ),
            discord.SelectOption(
                label="paper", description="You choose paper.", emoji="🧻"
            ),
        ]
        super().__init__(
            placeholder="Choose...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        choices = {
            "rock": 0,
            "paper": 1,
            "scissors": 2,
        }
        user_choice = self.values[0].lower()
        user_choice_index = choices[user_choice]

        bot_choice = random.choice(list(choices.keys()))
        bot_choice_index = choices[bot_choice]

        result_embed = discord.Embed(color=0x9C84EF)
        result_embed.set_author(
            name=interaction.user.name, icon_url=interaction.user.avatar.url
        )

        if user_choice_index == bot_choice_index:
            result_embed.description = f"**That's a draw!**\nYou've chosen {user_choice} and I've chosen {bot_choice}."
            result_embed.colour = 0xF59E42
        elif user_choice_index == 0 and bot_choice_index == 2:
            result_embed.description = f"**You won!**\nYou've chosen {user_choice} and I've chosen {bot_choice}."
            result_embed.colour = 0x9C84EF
        elif user_choice_index == 1 and bot_choice_index == 0:
            result_embed.description = f"**You won!**\nYou've chosen {user_choice} and I've chosen {bot_choice}."
            result_embed.colour = 0x9C84EF
        elif user_choice_index == 2 and bot_choice_index == 1:
            result_embed.description = f"**You won!**\nYou've chosen {user_choice} and I've chosen {bot_choice}."
            result_embed.colour = 0x9C84EF
        else:
            result_embed.description = (
                f"**I won!**\nYou've chosen {user_choice} and I've chosen {bot_choice}."
            )
            result_embed.colour = 0xE02B2B
        await interaction.response.edit_message(
            embed=result_embed, content=None, view=None
        )


class RockPaperScissorsView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(RockPaperScissors())

class Dig(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Dig", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        self.value = "dig"
        self.stop()


class Fun(commands.Cog, name="fun"):
    def __init__(self, bot):
        self.bot = bot
        bot.pats = 0

    @commands.hybrid_command(name="randomfact", description="Get a random fact.")
    @checks.not_blacklisted()
    async def randomfact(self, context: Context) -> None:
        """
        Get a random fact.

        :param context: The hybrid command context.
        """
        # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://uselessfacts.jsph.pl/random.json?language=en"
            ) as request:
                if request.status == 200:
                    data = await request.json()
                    embed = discord.Embed(description=data["text"], color=0xD75BF4)
                else:
                    embed = discord.Embed(
                        title="Error!",
                        description="There is something wrong with the API, please try again later",
                        color=0xE02B2B,
                    )
                await context.send(embed=embed)

    @commands.hybrid_command(
        name="coinflip", description="Make a coin flip, but give your bet before."
    )
    @checks.not_blacklisted()
    async def coinflip(self, context: Context) -> None:
        """
        Make a coin flip, but give your bet before.

        :param context: The hybrid command context.
        """
        buttons = Choice()
        embed = discord.Embed(description="What is your bet?", color=0x9C84EF)
        message = await context.send(embed=embed, view=buttons)
        await buttons.wait()  # We wait for the user to click a button.
        result = random.choice(["heads", "tails"])
        if buttons.value == result:
            embed = discord.Embed(
                description=f"Correct! You guessed `{buttons.value}` and I flipped the coin to `{result}`.",
                color=0x9C84EF,
            )
        else:
            embed = discord.Embed(
                description=f"Woops! You guessed `{buttons.value}` and I flipped the coin to `{result}`, better luck next time!",
                color=0xE02B2B,
            )
        await message.edit(embed=embed, view=None, content=None)

    @commands.hybrid_command(
        name="rps", description="Play the rock paper scissors game against the bot."
    )
    @checks.not_blacklisted()
    async def rock_paper_scissors(self, context: Context) -> None:
        """
        Play the rock paper scissors game against the bot.

        :param context: The hybrid command context.
        """
        view = RockPaperScissorsView()
        await context.send("Please make your choice", view=view)

    @commands.hybrid_command(name="pat", description="Pat the squirrel")
    @checks.not_blacklisted()
    async def pat(self, context: Context) -> None:
        """
        Incriment the squirrel counter.

        :param context: The hybrid command context.
        """
        self.bot.pats += 1
        embed = discord.Embed(
            title="You patted the squirrel",
            description=f"The squirrel has been patted {self.bot.pats} times.",
            color=0x9C84EF,
        )
        embed.set_image(url="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzAzZGMzOWY3ZjFlNTc1NTdjMzE4NzM3YmYwNGUzZjMyZDEwMTgyMCZjdD1n/GjFn41tOolLKX0dMTi/giphy.gif")
        await context.send(embed=embed)

    @commands.hybrid_command(name="dig", description="Dig for acorns and get a prize! Available every 5 minutes.")
    @checks.not_blacklisted()
    async def dig(self, context: Context) -> None:
       """
       Get a random prize from the bot.

       :param context: The hybrid command context.
       """ 
       time = datetime.datetime.now()
       minute = time.minute
       if minute % 5 == 0: #Only active during times ending in 5 or 0
            button = Dig()
            embed = discord.Embed(description="Ready to dig!", color=0x9C84EF)
            embed.set_image(url="https://media.giphy.com/media/3dK3ko9lmeEJesIstK/giphy.gif")
            message = await context.send(embed=embed, view=button)
            await button.wait()

            #Choose a prize
            rand = random.randint(0,100)
            if rand > 0 and rand < 71:
                embed = discord.Embed(
                    title="Common",
                    description = f"You got an acorn! 🌰",
                    colour = 0xF59E42,
                )
                embed.set_image(url="https://media.giphy.com/media/0SoabZIDhTylJmYtIO/giphy.gif")
            elif rand > 70 and rand < 91:
                embed = discord.Embed(
                    title="Rare",
                    description=f"You've been visited by a lucky squirrel! 🐿",
                    colour = 0x9C84EF
                )
                embed.set_image(url="https://media.giphy.com/media/lODjakhWuaiihYXm3r/giphy.gif")
            elif rand > 90 and rand < 100:
                embed = discord.Embed(
                    title="Epic",
                    description = f"You unlocked a new sticker! 🎉",
                    colour = 0xfcca03
                )
                embed.set_image(url="https://media.giphy.com/media/EiZQwKjFPDrYFnzrhA/giphy.gif")
            else:
                embed = discord.Embed(
                    title="Legendary",
                    description = f"You gained 10 points! ⭐️",
                    color =  0xfc2803
                )
                embed.set_image(url="https://media.giphy.com/media/0LakudBWks8MkyjRsC/giphy.gif")
            await message.edit(embed=embed, view=None, content=None)
       else :
           remaining = 5 - (minute % 10) if (minute % 10) < 5 else 10 - (minute % 10)
           t = "minute" if remaining == 1 else "minutes"
           
           embed = discord.Embed(
               title="The Squirrel is asleep💤",
               description=f"Come back in {remaining} {t}!",
               color=0x3238a8
           )
           embed.set_image(url="https://media.giphy.com/media/PLiW6toBco3wu2lqY0/giphy.gif")
           await context.send(embed=embed)
    

async def setup(bot):
    await bot.add_cog(Fun(bot))
