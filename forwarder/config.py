from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5116091151:AAF9FWa8CdnX3DcMi3a6VtoCd5a48qEmgSw"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001536308807,-1001585236506]# List of chat id's to forward messages from.
    TO_CHATS = [-1001744308344]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
