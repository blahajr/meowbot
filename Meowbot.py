import discord
from discord import app_commands
import asyncio

# The guild in which this slash command will be registered.
# It is recommended to have a test guild to separate from your "main" bot
GUILD_ID = 0 # /* YOUR GUILD ID */
GUILD_OBJECT = discord.Object(GUILD_ID)

class MyClient(discord.Client):
    def __init__(self) -> None:

        intents = discord.Intents.default()
        super().__init__(intents=intents)

       
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def setup_hook(self) -> None:
        # Sync the application command with Discord blah blah :3
        await self.tree.sync(guild=GUILD_OBJECT)

client = MyClient()

# meowbleh bleh
@client.tree.command(guild=GUILD_OBJECT, description="Meows in a vc blehh")
async def meow(interaction: discord.Interaction):
    #guild=GUILD_OBJECT

    user = interaction.user
    voice_channel = user.voice.channel

    if voice_channel is not None:   
        # create StreamPlayer
        vc = await voice_channel.connect()

        vc.play(discord.FFmpegPCMAudio("meow.mp3"))
        # disconnect after the player has finished

        await asyncio.sleep(5)

        await vc.disconnect()

        await interaction.response.send_message('Success', ephemeral=True)
    else:
        await interaction.response.send_message('You are not in a voice channel!', ephemeral=True)

if __name__ == "__main__":
    client.run('/* TOKEN */')