from base import Players, engine, Session
from sqlalchemy  import desc



def tables(playername, playrecord = 0):
    sessia = Session(bind = engine)

    table = Players(name = playername, record = playrecord)
    sessia.add(table)

    sessia.commit()
    sessia.close()


def ifs(name):
    session = Session(bind = engine)
    queryy = session.query(Players)
    q = queryy.all()
    for qq in q:
        if qq.name == name:
            return True 
    return False


def update(playername, playerscore):
    session = Session(bind = engine)
    queryy = session.query(Players)
    q = queryy.filter(Players.name == playername)
    firstt = q.first()
    firstt.record = playerscore
    session.commit()
    session.close()


def player(name):
    session = Session(bind = engine)
    queryy = session.query(Players)
    q = queryy.filter(Players.name == name)
    firstt = q.first()
    return firstt.record


def top(intt = 5):
    session = Session(bind = engine)
    queryy = session.query(Players)
    q = queryy.order_by(desc(Players.record))
    all = q.all()
    d = all[:intt]
    return d

