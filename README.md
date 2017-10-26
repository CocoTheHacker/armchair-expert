# Requirements
- python 3.4.3+

# Dependencies
- sqlalchemy
- discord.py
- googleapiclient
- wand (imagemagick)
- schedule
- numpy
- spacy (Uses 'en' dataset by default, you will need to download this in addition to installing spacy: 'python -m spacy download en')

# Configuration

Copy config-example.py to config.py and fill in the fields. You will need to register with Google Custom Search to get a CX and developer key.
You will need to register a bot with Discord: https://discordapp.com/developers/applications/me#top
Convert the application to a bot account to get your token. After that you will need to join it to your guild using OAuth2
Take the client id of your application and fill in this link to join it: https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID_GOES_HERE&scope=bot&permissions=0

# Run It
python ftbot_discord.py
