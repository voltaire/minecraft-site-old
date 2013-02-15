from flask import Flask
from flask import render_template
from minecraft_query import MinecraftQuery

app = Flask(__name__)

@app.route('/mcstatus')
def returnStatus():
    query = MinecraftQuery("mc.voltaire.sh", 25565)
    basic_status = query.get_status()
    all_status = query.get_rules()
    server_info = 'The server has %d / %d players.' % (basic_status['numplayers'], basic_status['maxplayers'])
    vanillaPlayers = MinecraftQuery("mc.voltaire.sh",25565).get_rules()['players']
    return render_template('derp.html', avatars=vanillaPlayers)

if __name__ == '__main__':
    app.run()
