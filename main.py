import discord  
import sqlite3
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} Hazır !")

@bot.command()
async def add_task(ctx, *, task_name):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task_name, completed) VALUES (?, ?)", (task_name, False))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    await ctx.send(f"Görev eklendi! ID: {task_id}, Görev: {task_name}")

@bot.command()
async def show_tasks(ctx):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, task_name, completed FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    
    if not tasks:
        await ctx.send("Görev listeniz boş!")
        return
    
    embed = discord.Embed(title="Görev Listesi", color=discord.Color.blue())
    
    for task in tasks:
        task_id, task_name, completed = task
        status = "✅" if completed else "❌"
        embed.add_field(name=f"ID: {task_id}", value=f"{task_name} - Tamamlandı: {status}", inline=False)
    
    message = await ctx.send(embed=embed)
    
    for task in tasks:
        await message.add_reaction("✅")

@bot.command()
async def delete_task(ctx, task_id: int):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    
    if task:
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        await ctx.send(f"ID: {task_id} olan görev silindi!")
    else:
        await ctx.send(f"ID: {task_id} olan görev bulunamadı!")
    
    conn.close()
@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return
    
    if reaction.emoji == "✅":
        message = reaction.message
        
        # Görev listesi mesajını kontrol et
        if message.embeds and message.embeds[0].title == "Görev Listesi":
            # Kullanıcıdan görev ID'sini iste
            channel = reaction.message.channel
            await channel.send(f"{user.mention}, lütfen tamamlamak istediğiniz görevin ID'sini giriniz:")
            
            def check(m):
                return m.author == user and m.channel == channel and m.content.isdigit()
            
            try:
                # Kullanıcının cevabını 30 saniye bekle
                task_id_msg = await bot.wait_for('message', check=check, timeout=30.0)
                task_id = int(task_id_msg.content)
                
                # Görevi tamamlandı olarak işaretle
                conn = sqlite3.connect('tasks.db')
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
                task = cursor.fetchone()
                
                if task:
                    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
                    conn.commit()
                    await channel.send(f"Görev ID: {task_id} tamamlandı olarak işaretlendi!")
                else:
                    await channel.send(f"ID: {task_id} olan görev bulunamadı!")
                
                conn.close()
                
                # Görev listesini güncelle
                await message.delete()
                await show_tasks(await bot.get_context(message))
            
            except asyncio.TimeoutError:
                await channel.send(f"{user.mention}, süre doldu. Lütfen tekrar deneyin.")


bot.run("TOKENİN GELECEĞİ YER")


