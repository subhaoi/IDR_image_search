from flask import Flask, make_response, render_template, request, redirect
from files.colordescriptor import ColorDescriptor
from files.search import Searcher
from PIL import Image
import numpy as np
import cv2
import os
import shutil
import time
import csv
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main_page():
	if os.path.exists('static/temp') == True : # checking whether image query has been made or not
		shutil.rmtree('static/temp')
		shutil.rmtree('static/tmp')
		return redirect('/home')
	else :
		return redirect('/home')

@app.route('/home')
def home():
	datasets = os.listdir('static/images')
	if os.path.exists('static/temp') == True :     # if images exist in temp folder then render them
		image_names = os.listdir('static/temp')
		# sorted_list = sorted([float(i.rsplit(".",1)[0]) for i in image_names])
		sorted_image_names = sorted(image_names)
		image_file_data = pd.read_csv("image_file_data.csv")
		# sorted_image_names = [str(i)+".jpeg" for i in sorted_image_names]
		nearest = sorted(sorted_image_names)[0]
		article_links = ([str(image_file_data[image_file_data["Image Filename"]== i.split("|")[1]]["Permalink"].values[0]) for i in sorted_image_names])
		print(article_links)
		target = os.listdir('static/tmp')
		return render_template("index.html", image_names=sorted_image_names,article_links = article_links,
		target=(target), aw=1, count=len(datasets), nearest=(nearest))
	else :
		return render_template("index.html", aw=2, count=len(datasets))

@app.route('/search', methods=['POST'])
def search():
	picture = request.files['image']  # taking image query from the user 
	file = picture.read()
	print("file_read")
	cd = ColorDescriptor((8, 12, 3))  # 8, 12, 3 are the no. of bins
	npimg = np.frombuffer(file, np.uint8) # unsigned integer of 8 bit
	query = cv2.imdecode(npimg, cv2.IMREAD_COLOR) # decode image query using cv2
	
	features = cd.describe(query) # extract features from query
	print("searching")
	searcher = Searcher('index.csv')
	results = searcher.search(features) # search for similar features 

	os.makedirs('static/temp') 
	os.makedirs('static/tmp')
	print(results)
	for (score, resultID) in results:
		result = cv2.imread("static/images/" + resultID) # result variable stores image which is to be shown as result to user 
		save_img = cv2.imwrite("static/temp/" + str(round(score,2)) +"|" + resultID, result) # that image is stored in temp folder

	imgstr = time.strftime("%Y%m%d-%H%M%S")
	cv2.imwrite("static/tmp/"+ imgstr +".jpeg", query) # write query image in tmp folder 
	return redirect("/home")

@app.route('/<page_name>')
def other_page(page_name):
	response = make_response('The page named %s does not exist.' \
                             % page_name, 404)
	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8000,debug=True)
