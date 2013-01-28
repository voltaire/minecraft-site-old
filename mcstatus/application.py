from flask import Flask
from minecraft_query import MinecraftQuery

app = Flask(__name__)

@app.route('/mcstatus')
def returnStatus():
    query = MinecraftQuery("mc.voltaire.sh", 25565)
    basic_status = query.get_status()
    all_status = query.get_rules()
    server_info = 'The server has %d / %d players.' % (basic_status['numplayers'], basic_status['maxplayers'])
    status_info = 'Online now: %s' % (all_status['players'])
    return "<pre>" + str(server_info) + "\n" + str(status_info) + "</pre>"

if __name__ == '__main__':
    app.run()
