from flask import Flask, render_template, jsonify, request
from pymongo.common import clean_node
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbtoy1


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def posting():
    # 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']
    url_comment_receive = request.form['url_comment_give']

    # 클라이언트로 받은 데이터(url)에서 메타 정보 가져오기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    if soup.select_one('meta[property="og:title"]') is not None :
        og_title = soup.select_one('meta[property="og:title"]')
        url_title = og_title['content']
    else :
        og_title = "None"
        url_title = url_receive
    
    if soup.select_one('meta[property="og:description"]') is not None :
        og_description = soup.select_one('meta[property="og:description"]')
        url_description = og_description['content']
    else :
        og_description = "None"
        url_description = ""

    if soup.select_one('meta[property="og:image"]') is not None :
        og_image = soup.select_one('meta[property="og:image"]')
        url_image = og_image['content']
    else :
        og_image = "None"
        url_image = og_image
    

    # 데이터, 메타 정보를 데이터 베이스에 저장하기
    url_data = {'url' : url_receive, 'title' : url_title, 'description' : url_description, 'image' : url_image, 'url_comment' : url_comment_receive}
    db.urlDatas.insert_one(url_data)
    
    return jsonify({'result' : 'success'})


@app.route('/memo', methods=['GET'])
def listing():
    result = list(db.urlDatas.find({}, {'_id': 0}))
    return jsonify({'result' : 'success', 'urlDatas' : result})


if __name__ == '__main__' :
    app.run('0.0.0.0', port=5000, debug=True)