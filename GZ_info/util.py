import os
import logging
import django

from dotenv import load_dotenv
from GZ_info.bot_settings import *



def checkPath(extension):
    if os.path.isdir(extension) == False:
        return None
    mypath = '{}/bot_commands'.format(extension)
    reload_path = '{}.bot_commands'.format(extension)
    if os.path.isdir(mypath) == False:
        return None
    return mypath, reload_path

async def load_handle(ctx, botAction, embed, app, extension=None, holder_id=None):
    print(str(ctx.author.id) == str(holder_id))
    if str(ctx.author.id) == str(holder_id):

        mypath, reload_path = checkPath(app)
        print(mypath, reload_path)


    #     if not mypath:
    #         await ctx.respond(embed=embed)
    #         return
        
    #     if extension:
    #         try:
                
    #             botAction('{}.{}'.format(reload_path, extension))
    #             print(botAction)
    #         except Exception as e:
    #             await ctx.respond(embed=embed)
    #         await ctx.respond(embed=embed)
    #         return
    #     for filename in os.listdir(mypath):
    #         if filename.endswith('.py') == False:
    #             continue
    #         try:
    #             botAction('{}.{}'.format(reload_path, filename[:-3]))
    #         except Exception as e:
    #             pass
    #             # logger.error('import commit error: {}'.format(e))
    #     await ctx.respond(embed=embed)
    # else:
    await ctx.respond(embed=embed)
