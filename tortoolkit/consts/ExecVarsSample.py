try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # TODO optimize for vps use fully - currently only heroku is focused
        # Set true if its VPS [currently not fully working]
        IS_VPS = False
        API_HASH = "acbv1233blahbkah"
        API_ID = 696969
        
        # Google Drive Index Link should include the base dir also See readme for more info
        GD_INDEX_URL = "anime.touka.workers.dev/0:/"
        
        BOT_TOKEN = "23457345:advgyfchyrdchyfc"
        BASE_URL_OF_BOT = "https://anime19.tk"
        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [-1001229703790, 925128836]
        
        # Time to wait before edit message
        EDIT_SLEEP_SECS = 10

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 2097152000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress 
        COMPLETED_STR = "▓"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▒"

        # DB URI for access heroku prodrige url whatever 💁‍♀️
        DB_URI = ":00c30bf487b5be9709cb11bd877d18f56071cb4ee2eb4c1de16a8565a9c0cc68@ec2-52-71-153-228.compute-1.amazonaws.com:5432/dc6mocelst2jl5"
        
        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False
        
        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of the torrent allowed
        MAX_YTPLAYLIST_SIZE = 20
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 10

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = True
        




