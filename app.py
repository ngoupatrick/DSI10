# autres bibliotheques:
    # fastAPI - leger
    # Django - full
# nom du fichier:
    # app.py
# install:
    # pip install flask / conda install -c flask

# import des bibliotheques:
from flask import Flask, request, json, jsonify

# bibliotheque du modele
from joblib import load

from libs import predict, calculCarre

# creation de l'application FLASK
app = Flask(__name__)

# route:
    # url ou chemin web permettant de faire appel à la fonction python
    # dans notre cas: http://192.168.1.2:3003/api/bonjour
@app.route('/api/bonjour')
def direbonjour():
    return 'bonjour DSI'

# http://192.168.1.2:3003/
@app.route('/', methods=['GET'])
def welcome():
    return "<h1> Bonjour, </br> et bienvenue sur l'api de test du modele <b>IRIS</b> </h1>"

# route permettant de calculer le carre
@app.route('/api/carre', methods=['POST'])
def carre():
    # recuperer la données caché dans le post
    data = json.loads(request.data)

    # On recupere le champ "nbre"
    nbre = float(data["nbre"])

    # calcul du carré
    nb_carre = calculCarre(nbre)

    # retourner le resultat
    return jsonify({"carre": nb_carre})


# route permettant de predire avec LR
@app.route('/api/predictLR', methods=['POST'])
def predict_lr():
    # recuperer la données caché dans le post
    data = json.loads(request.data)

    # appel de la methode de prediction
    model_lr = model_lr_local
    val = predict(data, model_lr)

    # retourner le resultat
    return jsonify({"prediction": val})



# print(direbonjour())
if __name__ == "__main__":
    # charger le model LR
    # load model localy
    model_lr_local = load('model_lr.joblib')    
    app.run(host='0.0.0.0', port=3003, debug=True)


# 5.1,3.5,1.4,0.2,Iris-setosa
# 5.5,2.6,4.4,1.2,Iris-versicolor
# 6.3,2.8,5.1,1.5,Iris-virginica
