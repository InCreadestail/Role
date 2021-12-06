import discord
import asyncio
import random

token = 'ODg3NjA3MTkyMjA1Nzk5NDM0.YUGmnQ.RhTcLN2WeeMD7Vn7IqvkvVcpw_c'
serverid = 899641782764187668
rainbowrolename = "อ่ะเค"
delay = 2

client = discord.Client()
colours = [discord.Color.orange(),discord.Color.gold(),discord.Color.magenta(),discord.Color.red(),discord.Color.blue(),discord.Color.teal(),discord.Color.green(),discord.Color.purple()]

async def rainbowrole(role):
    count = 0
    for role in client.get_guild(serverid).roles:
        if str(role) == str(rainbowrolename):
            print("detected role")
            while not client.is_closed():
                try:
                    await role.edit(color=random.choice(colours))
                    count += 1
                    print("Count : " + str(count))

                except Exception:
                    print("can't edit role, make sure the bot role is above the rainbow role and that is have the perms to edit roles")
                    pass
                await asyncio.sleep(delay)
    print('role with the name "' + rainbowrolename +'" not found')
    print("creating the role...")
    try:
        await client.get_guild(serverid).create_role(reason="Created rainbow role", name=rainbowrolename)
        print("role created!")
        await asyncio.sleep(2)
        client.loop.create_task(rainbowrole(rainbowrolename))
    except Exception as e:
        print("couldn't create the role. Make sure the bot have the perms to edit roles")
        print(e)
        pass
        await asyncio.sleep(10)
        client.loop.create_task(rainbowrole(rainbowrolename))

@client.event
async def on_ready():
    client.loop.create_task(rainbowrole(rainbowrolename))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Ready.')
    print('------------')

client.run(token)