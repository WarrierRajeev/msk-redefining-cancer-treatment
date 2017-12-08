import numpy as np
from flask import Flask, abort, jsonify, request
import pickle
import pandas as pd
from rest_helper import MeanEmbeddingVectorizer
from rest_helper import preprocess


xgb = pickle.load(open('CancerXGB.pickle', 'rb'))
mean_embedding_vectorizer = pickle.load(open('mean_embedded.pickle', 'rb'))
gene_le = pickle.load(open('gene_le.pickle', 'rb'))
var_le = pickle.load(open('var_le.pickle', 'rb'))

app = Flask(__name__)

@app.route('/api', methods = ['Post'])
def make_predict():
	#all kinds of error checking should go here
	data = request.get_json(force=True)
	#convert out json to a numpy array
	raw_text = data['text']
	gene = data['gene']
	var = data['var']
	text_vector = mean_embedding_vectorizer.transform(pd.Series(preprocess(raw_text)))
	gene_vector = gene_le.fit_transform(pd.Series(gene).values.ravel()).reshape(-1, 1)
	var_vector = var_le.fit_transform(pd.Series(var).values.ravel()).reshape(-1, 1)
	predict_request = np.hstack((gene_vector, var_vector, text_vector))
	y = []
	y = xgb.predict(predict_request)
	#return out prediction
	output = y.tolist()
	return jsonify(results = output)

if __name__ == '__main__':
	app.run(port = 9000, debug = True)
