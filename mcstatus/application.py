from flask import Flask
from flask import render_template
from minecraft_query import MinecraftQuery

app = Flask(__name__)

@app.route('/mcstatus')
def returnStatus():
    query = MinecraftQuery("mc.voltaire.sh", 25565)
    basic_status = query.get_status()
    all_status = query.get_rules()
    vanillaPlayers = MinecraftQuery("mc.voltaire.sh",25565).get_rules()['players']
    return render_template('derp.html', avatars=vanillaPlayers, numplayers=basic_status['numplayers'], maxplayers=basic_status['maxplayers'])

if __name__ == '__main__':
    app.run()
