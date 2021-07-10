from flask import Flask, render_template, jsonify, request
from pymongo.common import clean_node

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbtoy3


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def posting():
    # 클라이언트로부터 데이터를 받기
    title_receive = request.form['title_give']
    comment_receive = request.form['comment_give']
    print(title_receive, comment_receive)

    # 데이터를 데이터 베이스에 저장하기
    memo_data = {'title' : title_receive, 'comment' : comment_receive}
    db.memoDatas.insert_one(memo_data)

    return jsonify({'result' : 'success'})


@app.route('/memo', methods=['GET'])
def listing():
    result = list(db.memoDatas.find({}))
    id = []
    for i in result :
        i['_id'] = str(i['_id'])
        id.append(i['_id'])
    return jsonify({'result' : 'success', 'memoDatas' : result, 'memoId' : id})


@app.route('/memo', methods=['POST'])
def adjsting():
    cardID_receive = request.form['cardId_give']
    adtitle_receive = request.form['adtitle_give']
    adcomment_receive = request.form['adcomment_give']
    db.memoDatas.update_one({'_id':cardID_receive},{'$set':{'title':adtitle_receive ,'commet':adcomment_receive}})

@app.route('/memo', methods=['POST'])
def deleting() :
    title_receive = request.form['title_give']
    db.memoDatas.delete_one({'title': title_receive})
    return jsonify({'result':'success'})


if __name__ == '__main__' :
    app.run('0.0.0.0', port=5000, debug=True)