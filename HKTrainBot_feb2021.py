#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://www.codementor.io/@garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay
#https://tutswiki.com/read-write-config-files-in-python/

import requests
import json
from configparser import ConfigParser

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

import traceback
import logging
import os
import threading


# In[2]:


# example from https://www.datacamp.com/community/tutorials/making-http-requests-in-python
def get_data(params):
    mtr_url = "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php"
    r = requests.get(mtr_url, params=params)
    return r.json()


# In[3]:


def AELHOK():
    return get_data({'line': 'AEL', 'sta': 'HOK'})

def AELKOW():    
    return get_data({'line': 'AEL', 'sta': 'KOW'})

def AELTSY():    
    return get_data({'line': 'AEL', 'sta': 'TSY'})
    
def AELAIR():    
    return get_data({'line': 'AEL', 'sta': 'AIR'})
    
def AELAWE():    
    return get_data({'line': 'AEL', 'sta': 'AWE'})
    

def TCLHOK():
    return get_data({'line': 'TCL', 'sta': 'HOK'})

def TCLKOW():
    return get_data({'line': 'TCL', 'sta': 'KOW'})
    
def TCLOLY():
    return get_data({'line': 'TCL', 'sta': 'OLY'})

def TCLNAC():
    return get_data({'line': 'TCL', 'sta': 'NAC'})

def TCLLAK():
    return get_data({'line': 'TCL', 'sta': 'LAK'})

def TCLTSY():
    return get_data({'line': 'TCL', 'sta': 'TSY'})

def TCLSUN():
    return get_data({'line': 'TCL', 'sta': 'SUN'})

def TCLTUC():
    return get_data({'line': 'TCL', 'sta': 'TUC'})


def wrlhuh():
    return get_data({'line': 'WRL', 'sta': 'HUH'})

def wrlets():
    return get_data({'line': 'WRL', 'sta': 'ETS'})

def wrlaus():
    return get_data({'line': 'WRL', 'sta': 'AUS'})

def wrlnac():
    return get_data({'line': 'WRL', 'sta': 'NAC'})

def wrlmef():
    return get_data({'line': 'WRL', 'sta': 'MEF'})

def wrltww():
    return get_data({'line': 'WRL', 'sta': 'TWW'})

def wrlksr():
    return get_data({'line': 'WRL', 'sta': 'KSR'})

def wrlyul():
    return get_data({'line': 'WRL', 'sta': 'YUL'})

def wrllop():
    return get_data({'line': 'WRL', 'sta': 'LOP'})

def wrltis():
    return get_data({'line': 'WRL', 'sta': 'TIS'})

def wrlsih():
    return get_data({'line': 'WRL', 'sta': 'SIH'})

def wrltum():
    return get_data({'line': 'WRL', 'sta': 'TUM'})



def tklnop():
    return get_data({'line': 'TKL', 'sta': 'NOP'})

def tklqub():
    return get_data({'line': 'TKL', 'sta': 'QUB'})

def tklyat():
    return get_data({'line': 'TKL', 'sta': 'YAT'})

def tkltik():
    return get_data({'line': 'TKL', 'sta': 'TIK'})

def tkltko():
    return get_data({'line': 'TKL', 'sta': 'TKO'})

def tkllhp():
    return get_data({'line': 'TKL', 'sta': 'LHP'})

def tklhah():
    return get_data({'line': 'TKL', 'sta': 'HAH'})

def tklpoa():
    return get_data({'line': 'TKL', 'sta': 'POA'})


# In[4]:


def call_station(station):
    ret_lines = []
    for line_key, line_val in station['data'].items():
        #print(line_key, line_val)
        for up_down in [ud for ud in ['UP', 'DOWN'] if ud in line_val]:
            for idx, entry in enumerate(line_val[up_down]):
#             print(entry)
                ret_lines.append(f"Dest:{entry['dest']} ttnt:{entry['ttnt']}mins"
                                 f" platform:{entry['plat']} time:{entry['time']} ")
                if idx > 0:
                    break
        return ret_lines
#     return "\n".join(ret_lines)
    
call_station(AELHOK())


# In[5]:


# # https://stackoverflow.com/questions/51125356/proper-way-to-build-menus-with-python-telegram-bot

def start(update, context):
    update.message.reply_text(main_menu_message(), reply_markup=main_menu_keyboard())
    
    
def main_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=main_menu_message(), reply_markup=main_menu_keyboard())


#Line Menu    
def AEL_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=AEL_menu_message(),reply_markup=AEL_menu_keyboard())

def TCL_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TCL_menu_message(),reply_markup=TCL_menu_keyboard())
    
def WRL_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRL_menu_message(),reply_markup=WRL_menu_keyboard())

def TKL_menu(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TKL_menu_message(),reply_markup=TKL_menu_keyboard())
    

#Station Menu
def AELHOK_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=AELHOK_message(),reply_markup=sub_menu_keyboard())
       
def AELKOW_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=AELKOW_message(),reply_markup=sub_menu_keyboard())
    
def AELTSY_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=AELTSY_message(),reply_markup=sub_menu_keyboard())
    
def AELAIR_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=AELAIR_message(),reply_markup=sub_menu_keyboard())
    
def AELAWE_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=AELAWE_message(),reply_markup=sub_menu_keyboard())   

# def menu_test (update: Update, context: CallbackContext):
#     query = update.callback_query
#     query.answer()
#     query.edit_message_text(text=message_test(),reply_markup=sub_menu_keyboard())
    
    
def TCLHOK_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TCLHOK_message(),reply_markup=sub_menu_keyboard())

def TCLKOW_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TCLKOW_message(),reply_markup=sub_menu_keyboard())
    
def TCLOLY_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TCLOLY_message(),reply_markup=sub_menu_keyboard())
    
def TCLNAC_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TCLNAC_message(),reply_markup=sub_menu_keyboard())
    
def TCLLAK_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TCLLAK_message(),reply_markup=sub_menu_keyboard())
    
def TCLTSY_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TCLTSY_message(),reply_markup=sub_menu_keyboard())
    
def TCLSUN_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TCLSUN_message(),reply_markup=sub_menu_keyboard())
    
def TCLTUC_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TCLTUC_message(),reply_markup=sub_menu_keyboard())


def WRLHUH_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLHUH_message(),reply_markup=sub_menu_keyboard())

def WRLETS_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLETS_message(),reply_markup=sub_menu_keyboard())

def WRLAUS_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLAUS_message(),reply_markup=sub_menu_keyboard())
    
def WRLNAC_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLNAC_message(),reply_markup=sub_menu_keyboard())
    
def WRLMEF_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLMEF_message(),reply_markup=sub_menu_keyboard())
    
def WRLTWW_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLTWW_message(),reply_markup=sub_menu_keyboard())
    
def WRLKSR_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLKSR_message(),reply_markup=sub_menu_keyboard())
    
def WRLYUL_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLYUL_message(),reply_markup=sub_menu_keyboard())
    
def WRLLOP_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLLOP_message(),reply_markup=sub_menu_keyboard())
    
def WRLTIS_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLTIS_message(),reply_markup=sub_menu_keyboard())
    
def WRLSIH_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLSIH_message(),reply_markup=sub_menu_keyboard())
    
def WRLTUM_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=WRLTUM_message(),reply_markup=sub_menu_keyboard())
    

    
def TKLNOP_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TKLNOP_message(),reply_markup=sub_menu_keyboard())
    
def TKLQUB_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TKLQUB_message(),reply_markup=sub_menu_keyboard())
    
def TKLYAT_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TKLYAT_message(),reply_markup=sub_menu_keyboard())
    
def TKLTIK_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TKLTIK_message(),reply_markup=sub_menu_keyboard())
    
def TKLTKO_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TKLTKO_message(),reply_markup=sub_menu_keyboard())
    
def TKLLHP_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TKLLHP_message(),reply_markup=sub_menu_keyboard())
    
def TKLHAH_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TKLHAH_message(),reply_markup=sub_menu_keyboard())
    
def TKLPOA_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=TKLPOA_message(),reply_markup=sub_menu_keyboard())
    
    
def error(update, context):
    print(f'Update {update} caused error {context.error}')  
    
############################ Keyboards #########################################

def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Airport Express', callback_data='m1')],
                [InlineKeyboardButton('Tung Chung', callback_data='m2')],
                [InlineKeyboardButton('West Rail', callback_data='m3')],
                [InlineKeyboardButton('Tseung Kwan O', callback_data='m4')]
               ]
    return InlineKeyboardMarkup(keyboard)

def AEL_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Hong Kong', callback_data= 'AELHOK')],
                [InlineKeyboardButton('Kowloon', callback_data='AELKOW')],
                [InlineKeyboardButton('Tsing Yi', callback_data='AELTSY')],
                [InlineKeyboardButton('Airport', callback_data='AELAIR')],
                [InlineKeyboardButton('AsiaWorld Expo', callback_data='AELAWE')],
                [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

def TCL_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Hong Kong', callback_data= 'TCLHOK')],
                [InlineKeyboardButton('Kowloon', callback_data='TCLKOW')],
                [InlineKeyboardButton('Olympic', callback_data='TCLOLY')],
                [InlineKeyboardButton('Nam Cheong', callback_data='TCLNAC')],
                [InlineKeyboardButton('Lai King', callback_data='TCLLAK')],
                [InlineKeyboardButton('Tsing Yi', callback_data='TCLTSY')],
                [InlineKeyboardButton('Sunny Bay', callback_data='TCLSUN')],
                [InlineKeyboardButton('Tung Chung', callback_data='TCLTUC')],
                [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

def WRL_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Hung Hom', callback_data= 'wrlhuh')],
                [InlineKeyboardButton('East Tsim Sha Tsui', callback_data='wrlets')],
                [InlineKeyboardButton('Austin', callback_data='wrlaus')],
                [InlineKeyboardButton('Nam Cheong', callback_data='wrlnac')],
                [InlineKeyboardButton('Mei Foo', callback_data='wrlmef')],
                [InlineKeyboardButton('Tsuen Wan West', callback_data='wrltww')],
                [InlineKeyboardButton('Kam Sheung Road', callback_data='wrlksr')],
                [InlineKeyboardButton('Yuen Long', callback_data='wrlyul')],
                [InlineKeyboardButton('Long Ping', callback_data='wrllop')],
                [InlineKeyboardButton('Tin Shui Wai', callback_data='wrltis')],
                [InlineKeyboardButton('Siu Hong', callback_data='wrlsih')],
                [InlineKeyboardButton('Tuen Mun', callback_data='wrltum')],
                [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def TKL_menu_keyboard():
    keyboard = [[InlineKeyboardButton('North Point', callback_data= 'tklnop')],
                [InlineKeyboardButton('Quarry Bay', callback_data='tklqub')],
                [InlineKeyboardButton('Yau Tong', callback_data='tklyat')],
                [InlineKeyboardButton('Tiu Keng Leng', callback_data='tkltik')],
                [InlineKeyboardButton('Tseung Kwan O', callback_data='tkltko')],
                [InlineKeyboardButton('LOHAS Park', callback_data='tkllhp')],
                [InlineKeyboardButton('Hang Hau', callback_data='tklhah')],
                [InlineKeyboardButton('Po Lam', callback_data='tklpoa')],
                [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

def sub_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
    return 'Choose the Line in main menu:'

def AEL_menu_message():
    return 'Choose the station in Airport Express Line:'

def TCL_menu_message():
    return 'Choose the station in Tung Chung Line:'

def WRL_menu_message():
    return 'Choose the station in West Rail Line:'

def TKL_menu_message():
    return 'Choose the station in Tseung Kwan O Line:'


# def message_test():
#     return call_station({pattern}())

def AELHOK_message():
    return call_station(AELHOK())

def AELKOW_message():
    return call_station(AELKOW())

def AELTSY_message():
    return call_station(AELTSY())

def AELAIR_message():
    return call_station(AELAIR())

def AELAWE_message():
    return call_station(AELAWE())


def TCLHOK_message():
    return call_station(TCLHOK())

def TCLKOW_message():
    return call_station(TCLKOW())

def TCLOLY_message():
    return call_station(TCLOLY())

def TCLNAC_message():
    return call_station(TCLNAC())

def TCLLAK_message():
    return call_station(TCLLAK())

def TCLTSY_message():
    return call_station(TCLTSY())

def TCLSUN_message():
    return call_station(TCLSUN())

def TCLTUC_message():
    return call_station(TCLTUC())



def WRLHUH_message():
    return call_station(wrlhuh())

def WRLETS_message():
    return call_station(wrlets())

def WRLAUS_message():
    return call_station(wrlaus())

def WRLNAC_message():
    return call_station(wrlnac())

def WRLMEF_message():
    return call_station(wrlmef())

def WRLTWW_message():
    return call_station(wrltww())

def WRLKSR_message():
    return call_station(wrlksr())

def WRLYUL_message():
    return call_station(wrlyul())

def WRLLOP_message():
    return call_station(wrllop())

def WRLTIS_message():
    return call_station(wrltis())

def WRLSIH_message():
    return call_station(wrlsih())

def WRLTUM_message():
    return call_station(wrltum())



def TKLNOP_message():
    return call_station(tklnop())

def TKLQUB_message():
    return call_station(tklqub())

def TKLYAT_message():
    return call_station(tklyat())

def TKLTIK_message():
    return call_station(tkltik())

def TKLTKO_message():
    return call_station(tkltko())

def TKLLHP_message():
    return call_station(tkllhp())

def TKLHAH_message():
    return call_station(tklhah())

def TKLPOA_message():
    return call_station(tklpoa())


############################# Handlers #########################################

def get_config():
    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")

    return config_object

config_object = get_config()
token = config_object["DEFAULT"]["token"]
updater = Updater(token, use_context=True)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))

updater.dispatcher.add_handler(CallbackQueryHandler(AEL_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(TCL_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRL_menu, pattern='m3'))
updater.dispatcher.add_handler(CallbackQueryHandler(TKL_menu, pattern='m4'))

updater.dispatcher.add_handler(CallbackQueryHandler(AELHOK_menu, pattern='AELHOK'))
updater.dispatcher.add_handler(CallbackQueryHandler(AELKOW_menu, pattern='AELKOW'))
updater.dispatcher.add_handler(CallbackQueryHandler(AELTSY_menu, pattern='AELTSY'))
updater.dispatcher.add_handler(CallbackQueryHandler(AELAIR_menu, pattern='AELAIR'))
updater.dispatcher.add_handler(CallbackQueryHandler(AELAWE_menu, pattern='AELAWE'))

# updater.dispatcher.add_handler(CallbackQueryHandler(menu_test, pattern='AELHOK'))
# updater.dispatcher.add_handler(CallbackQueryHandler(menu_test, pattern='AELKOW'))
# updater.dispatcher.add_handler(CallbackQueryHandler(menu_test, pattern='AELTSY'))
# updater.dispatcher.add_handler(CallbackQueryHandler(menu_test, pattern='AELAIR'))
# updater.dispatcher.add_handler(CallbackQueryHandler(menu_test, pattern='AELAWE'))

updater.dispatcher.add_handler(CallbackQueryHandler(TCLHOK_menu, pattern='TCLHOK'))
updater.dispatcher.add_handler(CallbackQueryHandler(TCLKOW_menu, pattern='TCLKOW'))
updater.dispatcher.add_handler(CallbackQueryHandler(TCLOLY_menu, pattern='TCLOLY'))
updater.dispatcher.add_handler(CallbackQueryHandler(TCLNAC_menu, pattern='TCLNAC'))
updater.dispatcher.add_handler(CallbackQueryHandler(TCLLAK_menu, pattern='TCLLAK'))
updater.dispatcher.add_handler(CallbackQueryHandler(TCLTSY_menu, pattern='TCLTSY'))
updater.dispatcher.add_handler(CallbackQueryHandler(TCLSUN_menu, pattern='TCLSUN'))
updater.dispatcher.add_handler(CallbackQueryHandler(TCLTUC_menu, pattern='TCLTUC'))

updater.dispatcher.add_handler(CallbackQueryHandler(WRLHUH_menu, pattern='wrlhuh'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLETS_menu, pattern='wrlets'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLAUS_menu, pattern='wrlaus'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLNAC_menu, pattern='wrlnac'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLMEF_menu, pattern='wrlmef'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLTWW_menu, pattern='wrltww'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLKSR_menu, pattern='wrlksr'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLYUL_menu, pattern='wrlyul'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLLOP_menu, pattern='wrllop'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLTIS_menu, pattern='wrltis'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLSIH_menu, pattern='wrlsih'))
updater.dispatcher.add_handler(CallbackQueryHandler(WRLTUM_menu, pattern='wrltum'))


updater.dispatcher.add_handler(CallbackQueryHandler(TKLNOP_menu, pattern='tklnop'))
updater.dispatcher.add_handler(CallbackQueryHandler(TKLQUB_menu, pattern='tklqub'))
updater.dispatcher.add_handler(CallbackQueryHandler(TKLYAT_menu, pattern='tklyat'))
updater.dispatcher.add_handler(CallbackQueryHandler(TKLTIK_menu, pattern='tkltik'))
updater.dispatcher.add_handler(CallbackQueryHandler(TKLTKO_menu, pattern='tkltko'))
updater.dispatcher.add_handler(CallbackQueryHandler(TKLLHP_menu, pattern='tkllhp'))
updater.dispatcher.add_handler(CallbackQueryHandler(TKLHAH_menu, pattern='tklhah'))
updater.dispatcher.add_handler(CallbackQueryHandler(TKLPOA_menu, pattern='tklpoa'))


updater.dispatcher.add_error_handler(error)

try:
    updater.start_polling()
except KeyboardInterrupt:
    updater.stop()
    updater.is_idle = False



