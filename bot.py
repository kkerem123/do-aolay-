import discord
from discord.ext import commands
import os
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR,exist_ok=True)#klasör yoksa oluştur


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def check(ctx):
    if ctx.message.attachments: #eğer bağlamdaki mesajda ekler varsa
        for attachment in  ctx.message.attachments:
            file_name =attachment.filename
            file_path=os.path.join(IMAGE_DIR,file_name) #images klasörünün altına yerleşecek şekilde dosya yolu belirliyoruz
            await attachment.save(file_path) #ekimiz ilgili dosya yoluna kaydolur.
            await ctx.send(f"{file_name }görseliniz başarılı şekilde kaydoldu")
            try:
                class_name,skor= get_class(image=file_path)
                await ctx.send(f"görselinizin snıfı:{class_name},tahmin skoru ise:{skor}")
                if class_name=="Fırtınalar ve Tropikal Rüzgârlar":
                    await ctx.send(
                        content="Fırtınalar, atmosferdeki büyük basınç farklarından kaynaklanan, hızı genellikle saatte 62 kilometreyi aşan güçlü hava akımlarıdır. Tropikal rüzgârlar (kasırga, tayfun, siklon) ise sıcak okyanus suları üzerinde oluşur; merkezindeki düşük basınç ve yükselen nemli hava sayesinde devasa bir enerji kazanarak kıyı bölgelerinde yıkıcı etkilere yol açar.",
                        file=discord.File("images\fırtına açıklama görseli.jpeg")
                        )

                    
                elif class_name=="Orman Yangınları":
                    await ctx.send(
                    content="Orman yangınları; yüksek sıcaklık, düşük nem ve şiddetli rüzgâr gibi uygun hava koşullarında, bitki örtüsünün kontrolsüz bir şekilde yanmasıdır. Yıldırım düşmesi gibi doğal nedenlerle başlayabileceği gibi, büyük oranda insan ihmaliyle tetiklenir. İklim krizi sebebiyle uzayan kuraklık dönemleri, orman yangınlarının yayılma hızını ve şiddetini artırmaktadır.",
                    file=discord.File("ormanbilgi")   
                                            )
                elif class_name=="Kutup ve Dağ Buzullarının Hızlı Eriyişi":
                    await ctx.send(
                        content="Küresel ısınma nedeniyle atmosfer ve okyanus sıcaklıklarının artması, Grönland, Antarktika ve yüksek dağ zirvelerindeki buz kütlelerinin hızla erimesine neden olmaktadır. Bu durum sadece deniz seviyelerinin yükselmesine değil, aynı zamanda okyanus akıntılarının bozulmasına ve yerel ekosistemlerin çökmesine de yol açar.",
                        file=discord.File("buzbilgi.png"))
                    
                else:
                    await ctx.send(
                        content="Sel, normalde kuru olan arazilerin aşırı yağış, kar erimesi veya nehir yataklarının taşması sonucu geçici olarak su altında kalmasıdır. Şehirleşme ile toprağın betonlaşması, suyun emilmesini engelleyerek kırsal alanlardaki doğal taşkın riskini kentsel bir felakete dönüştürebilir.",
                        file=discord.File("selbilgi.png"))
            except Exception as e:
                await ctx.send(f"Şuan işlemi yapamıyorum:{e}")   
    else:
        await ctx.send("cevap için resim(ek) lazım.")






