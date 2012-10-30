from flask import Flask
from minecraft_query import MinecraftQuery

app = Flask(__name__)

@app.route('/mcstatus')

def returnStatus():
    
    try:
        query = MinecraftQuery("mc.voltaire.sh", 25565, 10, 3)
        basicQuery = query.get_status()
        fullQuery = query.get_rules()

    except socket.error as e:
        if not options.quiet:
            return "Server is down or unreachable:\n" + e.message

    if not options.quiet:
        numOnline = 'The server has %d players filling %d total slots. There are %d free slots.' % (basicQuery['numplayers'], basicQuery['maxplayers'], basicQuery['maxplayers'] - basic_status['numplayers'])
        playersOnline = 'Online now: %s' % (fullQuery['players'])
        return numOnline + "\n" + playersOnline

    return "ermahgerd"

if __name__ == '__main__':
    app.run()