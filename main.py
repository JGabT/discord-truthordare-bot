import os
import sys
import discord
import random
import mysql.connector
from discord.ext import commands


mydb = mysql.connector.connect(
  host="dbip",
  user="usernamedb",
  password="passworddb"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS dtruthordare")
mycursor.execute("USE dtruthordare")

for x in mycursor:
  print(x) 

with open("token.txt", "r") as file:
    first_line = file.readline()
    for last_line in file:
        pass


print(first_line)

bot = commands.Bot(command_prefix='>')

@bot.command()
async def dbstatus(ctx):
    print(mydb)
    await ctx.send(mydb)

@bot.command()
async def addtruth(ctx, *, add):
    """ add truth """
    sql = "INSERT INTO truth (addedby, content) VALUES (%s, %s)"
    val = (ctx.message.author.id, str(add))
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Truth added! (logged: <@" + str(ctx.message.author.id) + "> " + str(add) + ")" + " | " + str(mycursor.rowcount) + " rows affected.")

@bot.command()
async def truth(ctx):
    """ get random truth """
    mycursor.execute("SELECT addedby, content FROM truth")
    myresult = mycursor.fetchall()
    # print('addedby: ' + str(addedby) + ' ' + random.choice(myresult)[0])
    result = (myresult)
    randomres = random.choice(result)
    print(f"added by: {randomres[0]} | content: {randomres[1]}")
    await ctx.send('**' + randomres[1] + '** | added by: <@' + str(randomres[0]) + '>' )

@bot.command()
async def adddare(ctx, *, add):
    """ add dare """
    sql = "INSERT INTO dare (addedby, content) VALUES (%s, %s)"
    val = (ctx.message.author.id, str(add))
    mycursor.execute(sql, val)
    mydb.commit()
    await ctx.send("Dare added! (logged: <@" + str(ctx.message.author.id) + "> " + str(add) + ")" + " | " + str(mycursor.rowcount) + " rows affected.")

@bot.command()
async def dare(ctx):
    """ get random dare """
    mycursor.execute("SELECT addedby, content FROM dare")
    myresult = mycursor.fetchall()
    # print('addedby: ' + str(addedby) + ' ' + random.choice(myresult)[0])
    result = (myresult)
    randomres = random.choice(result)
    print(f"added by: {randomres[0]} | content: {randomres[1]}")
    await ctx.send('**' + randomres[1] + '** | added by: <@' + str(randomres[0]) + '>' )



bot.run(last_line)