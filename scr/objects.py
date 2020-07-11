"""
## Here there are some extra methods for [types](types.m.html) objects
"""
from silbot import types
class InlineKeyboardMarkup:
    """types.InlineKeyboardMarkup will inherit this class' methods"""

    def __init__(self,inline_keyboard = []):
        self.inline_keyboard = inline_keyboard

    def addLine(self,line : list):
        """Adds a line to the given keyboard

        Args:

        - `line` (`list`): list of InlineKeyboardButtons
        """
        self.inline_keyboard.append(line)

    def removeLine(self,line_number : int):
        """Removes a line from the given keyboard

        Args:

        - `line_number` (`int`): Number of the line (from 0) to remove
        """
        self.inline_keyboard.pop(line_number)


class ReplyKeyboardMarkup:
    """types.KeyboardMarkup will inherit this class' methods"""

    def __init__(self,keyboard = []):
        self.keyboard = keyboard

    def addLine(self,line : list):
        """Adds a line to the given keyboard

        Args:

        - `line` (`list`): list of KeyboardButtons
        """
        self.keyboard.append(line)

    def removeLine(self,line_number):
        """Removes a line from the given keyboard

        Args:

        - `line_number` (`int`): Number of the line (from 0) to remove
        """
        self.keyboard.pop(line_number)

class CallbackQuery():

    def __init__(self,id,user_id):
        self.id = id
        self.user_id = user_id
    
    def answer(self,bot,text=None,show_alert=None,url=None,cache_time=None):
        """Sends a answerCallbackQuery request to botApi for the given callback
       
        - - - - -
        **Args**:
        
        - `bot` (`silbot.botapi.botApi`): bot object to perform the request
        - `text` :`str` Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
        - `show_alert` :`bool` If true, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.
        - `url` :`str` URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @Botfather, specify the URL that opens your game � note that this will only work if the query comes from a callback_game button.Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.
        - `cache_time` :`int` The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.

        **Returns:**

        - A `tuple`, on success a `bool` as first member and a botApiResponse object as second member
        """
        return bot.answerCallbackQuery(self.id,text,show_alert,url,cache_time)

class User():
    def __init__(self,id,type):
        self.id = id
        self.type = type
    
    def isMember(self,bot,chat_id):
        """Sends a getChatMember request to botApi and returns if the current user is a member of a given group
       
        - - - - -
        **Args**:
        
        - `bot` (`silbot.botapi.botApi`): bot object to perform the request
        - `chat_id` (`int`): The ID of the chat where to check if a user is member.
        
        **Returns**
        - `bool` True if the user is in the chat, False otherwise
        """
        obj,response = bot.getChatMember(chat_id,self.id)
        if response.ok:
            if obj.status == "left" or obj.status == "kicked" or (obj.status == "restricted" and obj.is_member == False):
                return False
            else:
                return True
        return False
    def isAdmin(self,bot,chat_id):
        """Sends a getChatMember request to botApi and returns if the current user is a admin of a given group
       
        - - - - -
        **Args**:
        
        - `bot` (`silbot.botapi.botApi`): bot object to perform the request
        - `chat_id` (`int`): The ID of the chat where to check if a user is admin.
        
        **Returns**
        - `bool` True if the user is admin in the chat, False otherwise
        """
        obj,response = bot.getChatMember(chat_id,self.id)
        if response.ok:
            if obj.status == "administrator" or obj.status == "creator":
                return True
        return False
class Chat():
    def __init__(self,id,type):
        self.id = id
        self.type = type
    
    def isMember(self,bot,user_id):
        """Sends a getChatMember request to botApi and returns if a given user is in the current chat
       
        - - - - -
        **Args**:
        
        - `bot` (`silbot.botapi.botApi`): bot object to perform the request
        - `user_id` (`int`): The ID of the user to check if is a member.
        
        **Returns**
        - `bool` True if the user is in the chat, False otherwise
        """
        obj,response = bot.getChatMember(self.id,user_id)
        if response.ok:
            if obj.status == "left" or obj.status == "kicked" or (obj.status == "restricted" and obj.is_member == False):
                return False
            else:
                return True
        return False
    def isAdmin(self,bot,user_id):
        """Sends a getChatMember request to botApi and returns if a given user is admin in the current chat
       
        - - - - -
        **Args**:
        
        - `bot` (`silbot.botapi.botApi`): bot object to perform the request
        - `user_id` (`int`): The ID of the user to check if is an admin.
        
        **Returns**
        - `bool` True if the user is an admin, False otherwise
        """
        obj,response = bot.getChatMember(self.id,user_id)
        if response.ok:
            if obj.status == "administrator" or obj.status == "creator":
                return True
        return False
        
