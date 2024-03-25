
from flask import Flask, render_template, request, jsonify
import pickle


# Load the trained model
with open('spam_classifier_model.pkl', 'rb') as f:
    Mnb = pickle.load(f)

# Load the CountVectorizer
with open('count_vectorizer.pkl', 'rb') as f:
    count_vector = pickle.load(f)

app = Flask(__name__)
# Route pour la page d'accueil
@app.route('/', methods=['GET', 'POST'])
# def home():
#     message = "" 
#     if request.method == 'POST':
#         # data = request.get_json(force=True)
#         data = request.form.get('emailText')
#         # text_data = data['emailText']
#         print([data])
#         # Transform the text data using the CountVectorizer
#         text_vectorized = count_vector.transform([data])

#         # Make prediction
#         prediction = Mnb.predict(text_vectorized)
#         pred = 'spam' if prediction[0] == 1 else 'non-spam'
#         print(pred)
#         # Return prediction
#         return render_template('result.html', res = pred)
#     else :
#         message = "il y a un erreur , re-envoyer le message"
#     return render_template('index.html', message = message)

def home():
    message = ""  # Initialiser le message
    if request.method == 'POST':
        data = request.form.get('emailText')
        if data:
            text_vectorized = count_vector.transform([data])
            prediction = Mnb.predict(text_vectorized)
            res = 'spam' if prediction[0] == 1 else 'non-spam'
            # return render_template('result.html', res=res, message=f"voila votre email est consedere comme {res}")
            return render_template('index.html', res=res, message=f"There you go, your email is considered {res}", datamessage = data)
        else:
            message = "Veuillez saisir un message"
            return render_template('index.html', message=message)
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
