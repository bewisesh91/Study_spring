datas = [['작품1', '작가1', 1, 'FANTASY', 0],
        ['작품2', '작가2', 1, 'STORY', 0],
        ['작품3', '작가3', 2, 'SPORTS', 0],
        ['작품4', '작가4', 3, 'OMNIBUS', 1],
        ['작품5', '작가5', 4, 'STORY', 0]]

for data in datas :
    doc = {}
    doc['title'] = data[0]
    doc['artistName'] = data[1]
    doc['weekday'] = data[2]
    doc['genre'] = data[3]
    doc['finished'] = data[4]
    print(doc)
    print()