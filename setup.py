from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics
import os
db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db.init_app(app)

    
#db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    age = db.Column(db.Integer)
    cpp = db.Column(db.Integer)
    c = db.Column(db.Integer)
    py = db.Column(db.Integer)
    php = db.Column(db.Integer)
    lv = db.Column(db.Integer)
    ms = db.Column(db.Integer)
    sql = db.Column(db.Integer)
    html = db.Column(db.Integer)
    jv = db.Column(db.Integer)
    ja = db.Column(db.Integer)
    team = db.Column(db.Integer)
    comm = db.Column(db.Integer)
    time = db.Column(db.Integer)
    risk = db.Column(db.Integer)
    dec = db.Column(db.Integer)
    lead = db.Column(db.Integer)
    cult = db.Column(db.Integer)
    pres = db.Column(db.Integer)
    eng = db.Column(db.Integer)
    ger = db.Column(db.Integer)
    fr = db.Column(db.Integer)
    esp = db.Column(db.Integer)
    rus = db.Column(db.Integer)
    ita = db.Column(db.Integer)
    chn = db.Column(db.Integer)
    jap = db.Column(db.Integer)
    arb = db.Column(db.Integer)

    def __init__(self, age, cpp, c, py, php, lv, ms, sql, html, jv, ja, team, comm, time, risk, dec, lead,
                 cult, pres, eng, ger, fr, esp, rus, ita, chn, jap, arb):
        self.age = age
        self.cpp = cpp
        self.c = c
        self.py = py
        self.php = php
        self.lv = lv
        self.ms = ms
        self.sql = sql
        self.html = html
        self.jv = jv
        self.ja = ja
        self.team = team
        self.comm = comm
        self.time = time
        self.risk = risk
        self.dec = dec
        self.lead = lead
        self.cult = cult
        self.pres = pres
        self.eng = eng
        self.ger = ger
        self.fr = fr
        self.esp = esp
        self.rus = rus
        self.ita = ita
        self.chn = chn
        self.jap = jap
        self.arb = arb

db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/form")
def show_form():
    return render_template('form.html')

@app.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', formdata=fd)


@app.route("/result")
def show_result():
    fd_list = db.session.query(Formdata).all()

    # Some simple statistics for sample questions
    age = []
    cpp1 = []
    cpp2 = []
    cpp3 = []
    cpp4 = []
    cpp5 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    py1 = []
    py2 = []
    py3 = []
    py4 = []
    py5 = []
    php1 = []
    php2 = []
    php3 = []
    php4 = []
    php5 = []
    lv1 = []
    lv2 = []
    lv3 = []
    lv4 = []
    lv5 = []
    ms1 = []
    ms2 = []
    ms3 = []
    ms4 = []
    ms5 = []
    sql1 = []
    sql2 = []
    sql3 = []
    sql4 = []
    sql5 = []
    html1 = []
    html2 = []
    html3 = []
    html4 = []
    html5 = []
    jv1 = []
    jv2 = []
    jv3 = []
    jv4 = []
    jv5 = []
    ja1 = []
    ja2 = []
    ja3 = []
    ja4 = []
    ja5 = []
    team1 = []
    team2 = []
    team3 = []
    team4 = []
    team5 = []
    comm1 = []
    comm2 = []
    comm3 = []
    comm4 = []
    comm5 = []
    time1 = []
    time2 = []
    time3 = []
    time4 = []
    time5 = []
    risk1 = []
    risk2 = []
    risk3 = []
    risk4 = []
    risk5 = []
    dec1 = []
    dec2 = []
    dec3 = []
    dec4 = []
    dec5 = []
    lead1 = []
    lead2 = []
    lead3 = []
    lead4 = []
    lead5 = []
    cult1 = []
    cult2 = []
    cult3 = []
    cult4 = []
    cult5 = []
    pres1 = []
    pres2 = []
    pres3 = []
    pres4 = []
    pres5 = []
    eng1 = []
    eng2 = []
    eng3 = []
    eng4 = []
    eng5 = []
    ger1 = []
    ger2 = []
    ger3 = []
    ger4 = []
    ger5 = []
    fr1 = []
    fr2 = []
    fr3 = []
    fr4 = []
    fr5 = []
    esp1 = []
    esp2 = []
    esp3 = []
    esp4 = []
    esp5 = []
    rus1 = []
    rus2 = []
    rus3 = []
    rus4 = []
    rus5 = []
    ita1 = []
    ita2 = []
    ita3 = []
    ita4 = []
    ita5 = []
    chn1 = []
    chn2 = []
    chn3 = []
    chn4 = []
    chn5 = []
    jap1 = []
    jap2 = []
    jap3 = []
    jap4 = []
    jap5 = []
    arb1 = []
    arb2 = []
    arb3 = []
    arb4 = []
    arb5 = []

    for el in fd_list:
        age.append(el.age)
        if el.age == 1:
            cpp1.append(el.cpp)
            c1.append(el.c)
            py1.append(el.py)
            php1.append(el.php)
            lv1.append(el.lv)
            ms1.append(el.ms)
            sql1.append(el.sql)
            html1.append(el.html)
            jv1.append(el.jv)
            ja1.append(el.ja)
            team1.append(el.team)
            comm1.append(el.comm)
            time1.append(el.time)
            risk1.append(el.risk)
            dec1.append(el.dec)
            lead1.append(el.lead)
            cult1.append(el.cult)
            pres1.append(el.pres)
            eng1.append(el.eng)
            ger1.append(el.ger)
            fr1.append(el.fr)
            esp1.append(el.esp)
            rus1.append(el.rus)
            ita1.append(el.ita)
            chn1.append(el.chn)
            jap1.append(el.jap)
            arb1.append(el.arb)
        elif el.age == 2:
            cpp2.append(el.cpp)
            c2.append(el.c)
            py2.append(el.py)
            php2.append(el.php)
            lv2.append(el.lv)
            ms2.append(el.ms)
            sql2.append(el.sql)
            html2.append(el.html)
            jv2.append(el.jv)
            ja2.append(el.ja)
            team2.append(el.team)
            comm2.append(el.comm)
            time2.append(el.time)
            risk2.append(el.risk)
            dec2.append(el.dec)
            lead2.append(el.lead)
            cult2.append(el.cult)
            pres2.append(el.pres)
            eng2.append(el.eng)
            ger2.append(el.ger)
            fr2.append(el.fr)
            esp2.append(el.esp)
            rus2.append(el.rus)
            ita2.append(el.ita)
            chn2.append(el.chn)
            jap2.append(el.jap)
            arb2.append(el.arb)
        elif el.age == 3:
            cpp3.append(el.cpp)
            c3.append(el.c)
            py3.append(el.py)
            php3.append(el.php)
            lv3.append(el.lv)
            ms3.append(el.ms)
            sql3.append(el.sql)
            html3.append(el.html)
            jv3.append(el.jv)
            ja3.append(el.ja)
            team3.append(el.team)
            comm3.append(el.comm)
            time3.append(el.time)
            risk3.append(el.risk)
            dec3.append(el.dec)
            lead3.append(el.lead)
            cult3.append(el.cult)
            pres3.append(el.pres)
            eng3.append(el.eng)
            ger3.append(el.ger)
            fr3.append(el.fr)
            esp3.append(el.esp)
            rus3.append(el.rus)
            ita3.append(el.ita)
            chn3.append(el.chn)
            jap3.append(el.jap)
            arb3.append(el.arb)
        elif el.age == 4:
            cpp4.append(el.cpp)
            c4.append(el.c)
            py4.append(el.py)
            php4.append(el.php)
            lv4.append(el.lv)
            ms4.append(el.ms)
            sql4.append(el.sql)
            html4.append(el.html)
            jv4.append(el.jv)
            ja4.append(el.ja)
            team4.append(el.team)
            comm4.append(el.comm)
            time4.append(el.time)
            risk4.append(el.risk)
            dec4.append(el.dec)
            lead4.append(el.lead)
            cult4.append(el.cult)
            pres4.append(el.pres)
            eng4.append(el.eng)
            ger4.append(el.ger)
            fr4.append(el.fr)
            esp4.append(el.esp)
            rus4.append(el.rus)
            ita4.append(el.ita)
            chn4.append(el.chn)
            jap4.append(el.jap)
            arb4.append(el.arb)
        else:
            cpp5.append(el.cpp)
            c5.append(el.c)
            py5.append(el.py)
            php5.append(el.php)
            lv5.append(el.lv)
            ms5.append(el.ms)
            sql5.append(el.sql)
            html5.append(el.html)
            jv5.append(el.jv)
            ja5.append(el.ja)
            team5.append(el.team)
            comm5.append(el.comm)
            time5.append(el.time)
            risk5.append(el.risk)
            dec5.append(el.dec)
            lead5.append(el.lead)
            cult5.append(el.cult)
            pres5.append(el.pres)
            eng5.append(el.eng)
            ger5.append(el.ger)
            fr5.append(el.fr)
            esp5.append(el.esp)
            rus5.append(el.rus)
            ita5.append(el.ita)
            chn5.append(el.chn)
            jap5.append(el.jap)
            arb5.append(el.arb)

    if cpp1:
        mean_cpp1 = statistics.mean(cpp1)
    else:
        mean_cpp1 = 0

    if cpp2:
        mean_cpp2 = statistics.mean(cpp2)
    else:
        mean_cpp2 = 0

    if cpp3:
        mean_cpp3 = statistics.mean(cpp3)
    else:
        mean_cpp3 = 0

    if cpp4:
        mean_cpp4 = statistics.mean(cpp4)
    else:
        mean_cpp4 = 0

    if cpp5:
        mean_cpp5 = statistics.mean(cpp5)
    else:
        mean_cpp5 = 0

    if c1:
        mean_c1 = statistics.mean(c1)
    else:
        mean_c1 = 0

    if c2:
        mean_c2 = statistics.mean(c2)
    else:
        mean_c2 = 0

    if c3:
        mean_c3 = statistics.mean(c3)
    else:
        mean_c3 = 0

    if c4:
        mean_c4 = statistics.mean(c4)
    else:
        mean_c4 = 0

    if c5:
        mean_c5 = statistics.mean(c5)
    else:
        mean_c5 = 0

    if py1:
        mean_py1 = statistics.mean(py1)
    else:
        mean_py1 = 0

    if py2:
        mean_py2 = statistics.mean(py2)
    else:
        mean_py2 = 0

    if py3:
        mean_py3 = statistics.mean(py3)
    else:
        mean_py3 = 0

    if py4:
        mean_py4 = statistics.mean(py4)
    else:
        mean_py4 = 0

    if py5:
        mean_py5 = statistics.mean(py5)
    else:
        mean_py5 = 0

    if php1:
        mean_php1 = statistics.mean(php1)
    else:
        mean_php1 = 0

    if php2:
        mean_php2 = statistics.mean(php2)
    else:
        mean_php2 = 0

    if php3:
        mean_php3 = statistics.mean(php3)
    else:
        mean_php3 = 0

    if php4:
        mean_php4 = statistics.mean(php4)
    else:
        mean_php4 = 0

    if php5:
        mean_php5 = statistics.mean(php5)
    else:
        mean_php5 = 0

    if lv1:
        mean_lv1 = statistics.mean(lv1)
    else:
        mean_lv1 = 0

    if lv2:
        mean_lv2 = statistics.mean(lv2)
    else:
        mean_lv2 = 0

    if lv3:
        mean_lv3 = statistics.mean(lv3)
    else:
        mean_lv3 = 0

    if lv4:
        mean_lv4 = statistics.mean(lv4)
    else:
        mean_lv4 = 0

    if lv5:
        mean_lv5 = statistics.mean(lv5)
    else:
        mean_lv5 = 0

    if ms1:
        mean_ms1 = statistics.mean(ms1)
    else:
        mean_ms1 = 0

    if ms2:
        mean_ms2 = statistics.mean(ms2)
    else:
        mean_ms2 = 0

    if ms3:
        mean_ms3 = statistics.mean(ms3)
    else:
        mean_ms3 = 0

    if ms4:
        mean_ms4 = statistics.mean(ms4)
    else:
        mean_ms4 = 0

    if ms5:
        mean_ms5 = statistics.mean(ms5)
    else:
        mean_ms5 = 0

    if sql1:
        mean_sql1 = statistics.mean(sql1)
    else:
        mean_sql1 = 0

    if sql2:
        mean_sql2 = statistics.mean(sql2)
    else:
        mean_sql2 = 0

    if sql3:
        mean_sql3 = statistics.mean(sql3)
    else:
        mean_sql3 = 0

    if sql4:
        mean_sql4 = statistics.mean(sql4)
    else:
        mean_sql4 = 0

    if sql5:
        mean_sql5 = statistics.mean(sql5)
    else:
        mean_sql5 = 0

    if html1:
        mean_html1 = statistics.mean(html1)
    else:
        mean_html1 = 0

    if html2:
        mean_html2 = statistics.mean(html2)
    else:
        mean_html2 = 0

    if html3:
        mean_html3 = statistics.mean(html3)
    else:
        mean_html3 = 0

    if html4:
        mean_html4 = statistics.mean(html4)
    else:
        mean_html4 = 0

    if html5:
        mean_html5 = statistics.mean(html5)
    else:
        mean_html5 = 0

    if jv1:
        mean_jv1 = statistics.mean(jv1)
    else:
        mean_jv1 = 0

    if jv2:
        mean_jv2 = statistics.mean(jv2)
    else:
        mean_jv2 = 0

    if jv3:
        mean_jv3 = statistics.mean(jv3)
    else:
        mean_jv3 = 0

    if jv4:
        mean_jv4 = statistics.mean(jv4)
    else:
        mean_jv4 = 0

    if jv5:
        mean_jv5 = statistics.mean(jv5)
    else:
        mean_jv5 = 0

    if ja1:
        mean_ja1 = statistics.mean(ja1)
    else:
        mean_ja1 = 0

    if ja2:
        mean_ja2 = statistics.mean(ja2)
    else:
        mean_ja2 = 0

    if ja3:
        mean_ja3 = statistics.mean(ja3)
    else:
        mean_ja3 = 0

    if ja4:
        mean_ja4 = statistics.mean(ja4)
    else:
        mean_ja4 = 0

    if ja5:
        mean_ja5 = statistics.mean(ja5)
    else:
        mean_ja5 = 0

    if team1:
        mean_team1 = statistics.mean(team1)
    else:
        mean_team1 = 0

    if team2:
        mean_team2 = statistics.mean(team2)
    else:
        mean_team2 = 0

    if team3:
        mean_team3 = statistics.mean(team3)
    else:
        mean_team3 = 0

    if team4:
        mean_team4 = statistics.mean(team4)
    else:
        mean_team4 = 0

    if team5:
        mean_team5 = statistics.mean(team5)
    else:
        mean_team5 = 0

    if comm1:
        mean_comm1 = statistics.mean(comm1)
    else:
        mean_comm1 = 0

    if comm2:
        mean_comm2 = statistics.mean(comm2)
    else:
        mean_comm2 = 0

    if comm3:
        mean_comm3 = statistics.mean(comm3)
    else:
        mean_comm3 = 0

    if comm4:
        mean_comm4 = statistics.mean(comm4)
    else:
        mean_comm4 = 0

    if comm5:
        mean_comm5 = statistics.mean(comm5)
    else:
        mean_comm5 = 0

    if time1:
        mean_time1 = statistics.mean(time1)
    else:
        mean_time1 = 0

    if time2:
        mean_time2 = statistics.mean(time2)
    else:
        mean_time2 = 0

    if time3:
        mean_time3 = statistics.mean(time3)
    else:
        mean_time3 = 0

    if time4:
        mean_time4 = statistics.mean(time4)
    else:
        mean_time4 = 0

    if time5:
        mean_time5 = statistics.mean(time5)
    else:
        mean_time5 = 0

    if risk1:
        mean_risk1 = statistics.mean(risk1)
    else:
        mean_risk1 = 0

    if risk2:
        mean_risk2 = statistics.mean(risk2)
    else:
        mean_risk2 = 0

    if risk3:
        mean_risk3 = statistics.mean(risk3)
    else:
        mean_risk3 = 0

    if risk4:
        mean_risk4 = statistics.mean(risk4)
    else:
        mean_risk4 = 0

    if risk5:
        mean_risk5 = statistics.mean(risk5)
    else:
        mean_risk5 = 0

    if dec1:
        mean_dec1 = statistics.mean(dec1)
    else:
        mean_dec1 = 0

    if dec2:
        mean_dec2 = statistics.mean(dec2)
    else:
        mean_dec2 = 0

    if dec3:
        mean_dec3 = statistics.mean(dec3)
    else:
        mean_dec3 = 0

    if dec4:
        mean_dec4 = statistics.mean(dec4)
    else:
        mean_dec4 = 0

    if dec5:
        mean_dec5 = statistics.mean(dec5)
    else:
        mean_dec5 = 0

    if lead1:
        mean_lead1 = statistics.mean(lead1)
    else:
        mean_lead1 = 0

    if lead2:
        mean_lead2 = statistics.mean(lead2)
    else:
        mean_lead2 = 0

    if lead3:
        mean_lead3 = statistics.mean(lead3)
    else:
        mean_lead3 = 0

    if lead4:
        mean_lead4 = statistics.mean(lead4)
    else:
        mean_lead4 = 0

    if lead5:
        mean_lead5 = statistics.mean(lead5)
    else:
        mean_lead5 = 0

    if cult1:
        mean_cult1 = statistics.mean(cult1)
    else:
        mean_cult1 = 0

    if cult2:
        mean_cult2 = statistics.mean(cult2)
    else:
        mean_cult2 = 0

    if cult3:
        mean_cult3 = statistics.mean(cult3)
    else:
        mean_cult3 = 0

    if cult4:
        mean_cult4 = statistics.mean(cult4)
    else:
        mean_cult4 = 0

    if cult5:
        mean_cult5 = statistics.mean(cult5)
    else:
        mean_cult5 = 0

    if pres1:
        mean_pres1 = statistics.mean(pres1)
    else:
        mean_pres1 = 0

    if pres2:
        mean_pres2 = statistics.mean(pres2)
    else:
        mean_pres2 = 0

    if pres3:
        mean_pres3 = statistics.mean(pres3)
    else:
        mean_pres3 = 0

    if pres4:
        mean_pres4 = statistics.mean(pres4)
    else:
        mean_pres4 = 0

    if pres5:
        mean_pres5 = statistics.mean(pres5)
    else:
        mean_pres5 = 0

    if eng1:
        mean_eng1 = statistics.mean(eng1)
    else:
        mean_eng1 = 0

    if eng2:
        mean_eng2 = statistics.mean(eng2)
    else:
        mean_eng2 = 0

    if eng3:
        mean_eng3 = statistics.mean(eng3)
    else:
        mean_eng3 = 0

    if eng4:
        mean_eng4 = statistics.mean(eng4)
    else:
        mean_eng4 = 0

    if eng5:
        mean_eng5 = statistics.mean(eng5)
    else:
        mean_eng5 = 0

    if ger1:
        mean_ger1 = statistics.mean(ger1)
    else:
        mean_ger1 = 0

    if ger2:
        mean_ger2 = statistics.mean(ger2)
    else:
        mean_ger2 = 0

    if ger3:
        mean_ger3 = statistics.mean(ger3)
    else:
        mean_ger3 = 0

    if ger4:
        mean_ger4 = statistics.mean(ger4)
    else:
        mean_ger4 = 0

    if ger5:
        mean_ger5 = statistics.mean(ger5)
    else:
        mean_ger5 = 0

    if fr1:
        mean_fr1 = statistics.mean(fr1)
    else:
        mean_fr1 = 0

    if fr2:
        mean_fr2 = statistics.mean(fr2)
    else:
        mean_fr2 = 0

    if fr3:
        mean_fr3 = statistics.mean(fr3)
    else:
        mean_fr3 = 0

    if fr4:
        mean_fr4 = statistics.mean(fr4)
    else:
        mean_fr4 = 0

    if fr5:
        mean_fr5 = statistics.mean(fr5)
    else:
        mean_fr5 = 0

    if esp1:
        mean_esp1 = statistics.mean(esp1)
    else:
        mean_esp1 = 0

    if esp2:
        mean_esp2 = statistics.mean(esp2)
    else:
        mean_esp2 = 0

    if esp3:
        mean_esp3 = statistics.mean(esp3)
    else:
        mean_esp3 = 0

    if esp4:
        mean_esp4 = statistics.mean(esp4)
    else:
        mean_esp4 = 0

    if esp5:
        mean_esp5 = statistics.mean(esp5)
    else:
        mean_esp5 = 0

    if rus1:
        mean_rus1 = statistics.mean(rus1)
    else:
        mean_rus1 = 0

    if rus2:
        mean_rus2 = statistics.mean(rus2)
    else:
        mean_rus2 = 0

    if rus3:
        mean_rus3 = statistics.mean(rus3)
    else:
        mean_rus3 = 0

    if rus4:
        mean_rus4 = statistics.mean(rus4)
    else:
        mean_rus4 = 0

    if rus5:
        mean_rus5 = statistics.mean(rus5)
    else:
        mean_rus5 = 0

    if ita1:
        mean_ita1 = statistics.mean(ita1)
    else:
        mean_ita1 = 0

    if ita2:
        mean_ita2 = statistics.mean(ita2)
    else:
        mean_ita2 = 0

    if ita3:
        mean_ita3 = statistics.mean(ita3)
    else:
        mean_ita3 = 0

    if ita4:
        mean_ita4 = statistics.mean(ita4)
    else:
        mean_ita4 = 0

    if ita5:
        mean_ita5 = statistics.mean(ita5)
    else:
        mean_ita5 = 0

    if chn1:
        mean_chn1 = statistics.mean(chn1)
    else:
        mean_chn1 = 0

    if chn2:
        mean_chn2 = statistics.mean(chn2)
    else:
        mean_chn2 = 0

    if chn3:
        mean_chn3 = statistics.mean(chn3)
    else:
        mean_chn3 = 0

    if chn4:
        mean_chn4 = statistics.mean(chn4)
    else:
        mean_chn4 = 0

    if chn5:
        mean_chn5 = statistics.mean(chn5)
    else:
        mean_chn5 = 0

    if jap1:
        mean_jap1 = statistics.mean(jap1)
    else:
        mean_jap1 = 0

    if jap2:
        mean_jap2 = statistics.mean(jap2)
    else:
        mean_jap2 = 0

    if jap3:
        mean_jap3 = statistics.mean(jap3)
    else:
        mean_jap3 = 0

    if jap4:
        mean_jap4 = statistics.mean(jap4)
    else:
        mean_jap4 = 0

    if jap5:
        mean_jap5 = statistics.mean(jap5)
    else:
        mean_jap5 = 0

    if arb1:
        mean_arb1 = statistics.mean(arb1)
    else:
        mean_arb1 = 0

    if arb2:
        mean_arb2 = statistics.mean(arb2)
    else:
        mean_arb2 = 0

    if arb3:
        mean_arb3 = statistics.mean(arb3)
    else:
        mean_arb3 = 0

    if arb4:
        mean_arb4 = statistics.mean(arb4)
    else:
        mean_arb4 = 0

    if arb5:
        mean_arb5 = statistics.mean(arb5)
    else:
        mean_arb5 = 0

# Prepare data for google charts
    data1 = ['C/C++ 18-20', mean_cpp1, 'blue']
    data2 = ['C/C++ 21-25', mean_cpp2, 'green']
    data3 = ['C/C++ 26-30', mean_cpp3, 'red']
    data4 = ['C/C++ 31-40', mean_cpp4, 'yellow']
    data5 = ['C/C++ 40+', mean_cpp5, 'purple']
    data6 = ['C# 18-20', mean_c1, 'blue']
    data7 = ['C# 21-25', mean_c2, 'green']
    data8 = ['C# 26-30', mean_c3, 'red']
    data9 = ['C# 31-40', mean_c4, 'yellow']
    data10 = ['C# 40+', mean_c5, 'purple']
    data11 = ['Python 18-20', mean_py1, 'blue']
    data12 = ['Python 21-25', mean_py2, 'green']
    data13 = ['Python 26-30', mean_py3, 'red']
    data14 = ['Python 31-40', mean_py4, 'yellow']
    data15 = ['Python 40+', mean_py5, 'purple']
    data16 = ['PHP 18-20', mean_php1, 'blue']
    data17 = ['PHP 21-25', mean_php2, 'green']
    data18 = ['PHP 26-30', mean_php3, 'red']
    data19 = ['PHP 31-40', mean_php4, 'yellow']
    data20 = ['PHP 40+', mean_php5, 'purple']
    data21 = ['Labview 18-20', mean_lv1, 'blue']
    data22 = ['Labview 21-25', mean_lv2, 'green']
    data23 = ['Labview 26-30', mean_lv3, 'red']
    data24 = ['Labview 31-40', mean_lv4, 'yellow']
    data25 = ['Labview 40+', mean_lv5, 'purple']
    data31 = ['Matlab/Simulink/Octave 18-20', mean_ms1, 'blue']
    data32 = ['Matlab/Simulink/Octave 21-25', mean_ms2, 'green']
    data33 = ['Matlab/Simulink/Octave 26-30', mean_ms3, 'red']
    data34 = ['Matlab/Simulink/Octave 31-40', mean_ms4, 'yellow']
    data35 = ['Matlab/Simulink/Octave 40+', mean_ms5, 'purple']
    data36 = ['SQL 18-20', mean_sql1, 'blue']
    data37 = ['SQL 21-25', mean_sql2, 'green']
    data38 = ['SQL 26-30', mean_sql3, 'red']
    data39 = ['SQL 31-40', mean_sql4, 'yellow']
    data40 = ['SQL 40+', mean_sql5, 'purple']
    data41 = ['HTML 18-20', mean_html1, 'blue']
    data42 = ['HTML 21-25', mean_html2, 'green']
    data43 = ['HTML 26-30', mean_html3, 'red']
    data44 = ['HTML 31-40', mean_html4, 'yellow']
    data45 = ['HTML 40+', mean_html5, 'purple']
    data46 = ['Java Script 18-20', mean_jv1, 'blue']
    data47 = ['Java Script 21-25', mean_jv2, 'green']
    data48 = ['Java Script 26-30', mean_jv3, 'red']
    data49 = ['Java Script 31-40', mean_jv4, 'yellow']
    data50 = ['Java Script 40+', mean_jv5, 'purple']
    data56 = ['Java 18-20', mean_ja1, 'blue']
    data57 = ['Java 21-25', mean_ja2, 'green']
    data58 = ['Java 26-30', mean_ja3, 'red']
    data59 = ['Java 31-40', mean_ja4, 'yellow']
    data60 = ['Java 40+', mean_ja5, 'purple']
    data61 = ['Teamwork 18-20', mean_team1, 'blue']
    data62 = ['Teamwork 21-25', mean_team2, 'green']
    data63 = ['Teamwork 26-30', mean_team3, 'red']
    data64 = ['Teamwork 31-40', mean_team4, 'yellow']
    data65 = ['Teamwork 40+', mean_team5, 'purple']
    data66 = ['Communication skills 18-20', mean_comm1, 'blue']
    data67 = ['Communication skills 21-25', mean_comm2, 'green']
    data68 = ['Communication skills 26-30', mean_comm3, 'red']
    data69 = ['Communication skills 31-40', mean_comm4, 'yellow']
    data70 = ['Communication skills 40+', mean_comm5, 'purple']
    data71 = ['Time management 18-20', mean_time1, 'blue']
    data72 = ['Time management 21-25', mean_time2, 'green']
    data73 = ['Time management 26-30', mean_time3, 'red']
    data74 = ['Time management 31-40', mean_time4, 'yellow']
    data75 = ['Time management 40+', mean_time5, 'purple']
    data77 = ['Risk taking 18-20', mean_risk1, 'blue']
    data78 = ['Risk taking 21-25', mean_risk2, 'green']
    data79 = ['Risk taking 26-30', mean_risk3, 'red']
    data80 = ['Risk taking 31-40', mean_risk4, 'yellow']
    data81 = ['Risk taking 40+', mean_risk5, 'purple']
    data82 = ['Fast decision making 18-20', mean_dec1, 'blue']
    data83 = ['Fast decision making 21-25', mean_dec2, 'green']
    data84 = ['Fast decision making 26-30', mean_dec3, 'red']
    data85 = ['Fast decision making 31-40', mean_dec4, 'yellow']
    data86 = ['Fast decision making 40+', mean_dec5, 'purple']
    data87 = ['Leadership 18-20', mean_lead1, 'blue']
    data88 = ['Leadership 21-25', mean_lead2, 'green']
    data89 = ['Leadership 26-30', mean_lead3, 'red']
    data90 = ['Leadership 31-40', mean_lead4, 'yellow']
    data91 = ['Leadership 40+', mean_lead5, 'purple']
    data92 = ['Cultural intelligence 18-20', mean_cult1, 'blue']
    data93 = ['Cultural intelligence 21-25', mean_cult2, 'green']
    data94 = ['Cultural intelligence 26-30', mean_cult3, 'red']
    data95 = ['Cultural intelligence 31-40', mean_cult4, 'yellow']
    data96 = ['Cultural intelligence 40+', mean_cult5, 'purple']
    data97 = ['Presenting 18-20', mean_pres1, 'blue']
    data98 = ['Presenting 21-25', mean_pres2, 'green']
    data99 = ['Presenting 26-30', mean_pres3, 'red']
    data100 = ['Presenting 31-40', mean_pres4, 'yellow']
    data101 = ['Presenting 40+', mean_pres5, 'purple']
    data102 = ['English 18-20', mean_eng1, 'blue']
    data103 = ['English 21-25', mean_eng2, 'green']
    data104 = ['English 26-30', mean_eng3, 'red']
    data105 = ['English 31-40', mean_eng4, 'yellow']
    data106 = ['English 40+', mean_eng5, 'purple']
    data107 = ['German 18-20', mean_ger1, 'blue']
    data108 = ['German 21-25', mean_ger2, 'green']
    data109 = ['German 26-30', mean_ger3, 'red']
    data110 = ['German 31-40', mean_ger4, 'yellow']
    data111 = ['German 40+', mean_ger5, 'purple']
    data112 = ['French 18-20', mean_fr1, 'blue']
    data113 = ['French 21-25', mean_fr2, 'green']
    data114 = ['French 26-30', mean_fr3, 'red']
    data115 = ['French 31-40', mean_fr4, 'yellow']
    data116 = ['French 40+', mean_fr5, 'purple']
    data117 = ['Spanish 18-20', mean_esp1, 'blue']
    data118 = ['Spanish 21-25', mean_esp2, 'green']
    data119 = ['Spanish 26-30', mean_esp3, 'red']
    data120 = ['Spanish 31-40', mean_esp4, 'yellow']
    data121 = ['Spanish 40+', mean_esp5, 'purple']
    data122 = ['Russian 18-20', mean_rus1, 'blue']
    data123 = ['Russian 21-25', mean_rus2, 'green']
    data124 = ['Russian 26-30', mean_rus3, 'red']
    data125 = ['Russian 31-40', mean_rus4, 'yellow']
    data126 = ['Russian 40+', mean_rus5, 'purple']
    data127 = ['Italian 18-20', mean_ita1, 'blue']
    data128 = ['Italian 21-25', mean_ita2, 'green']
    data129 = ['Italian 26-30', mean_ita3, 'red']
    data130 = ['Italian 31-40', mean_ita4, 'yellow']
    data131 = ['Italian 40+', mean_ita5, 'purple']
    data132 = ['Chinese 18-20', mean_chn1, 'blue']
    data133 = ['Chinese 21-25', mean_chn2, 'green']
    data134 = ['Chinese 26-30', mean_chn3, 'red']
    data135 = ['Chinese 31-40', mean_chn4, 'yellow']
    data136 = ['Chinese 40+', mean_chn5, 'purple']
    data137 = ['Japanese 18-20', mean_jap1, 'blue']
    data138 = ['Japanese 21-25', mean_jap2, 'green']
    data139 = ['Japanese 26-30', mean_jap3, 'red']
    data140 = ['Japanese 31-40', mean_jap4, 'yellow']
    data141 = ['Japanese 40+', mean_jap5, 'purple']
    data142 = ['Arabian 18-20', mean_arb1, 'blue']
    data143 = ['Arabian 21-25', mean_arb2, 'green']
    data144 = ['Arabian 26-30', mean_arb3, 'red']
    data145 = ['Arabian 31-40', mean_arb4, 'yellow']
    data146 = ['Arabian 31-40', mean_arb5, 'purple']

    return render_template('result.html', data1=data1, data2=data2, data3=data3, data4=data4, data5=data5, data6=data6,
                           data7=data7, data8=data8, data9=data9, data10=data10, data11=data11, data12=data12,
                           data13=data13, data14=data14, data15=data15, data16=data16, data17=data17, data18=data18,
                           data19=data19, data20=data20, data21=data21, data22=data22, data23=data23, data24=data24,
                           data25=data25,
                           data31=data31, data32=data32, data33=data33, data34=data34, data35=data35, data36=data36,
                           data37=data37, data38=data38, data39=data39, data40=data40, data41=data41, data42=data42,
                           data43=data43, data44=data44, data45=data45, data46=data46, data47=data47, data48=data48,
                           data49=data49, data50=data50, data56=data56, data57=data57, data58=data58, data59=data59,
                           data60=data60,
                           data61=data61, data62=data62, data63=data63, data64=data64, data65=data65, data66=data66,
                           data67=data67, data68=data68, data69=data69, data70=data70, data71=data71, data72=data72,
                           data73=data73, data74=data74, data75=data75, data77=data77, data78=data78,
                           data79=data79, data80=data80, data81=data81, data82=data82, data83=data83, data84=data84,
                           data85=data85, data86=data86, data87=data87, data88=data88, data89=data89, data90=data90,
                           data91=data91, data92=data92, data93=data93, data94=data94, data95=data95, data96=data96,
                           data97=data97, data98=data98, data99=data99, data100=data100, data101=data101,
                           data102=data102, data103=data103, data104=data104, data105=data105, data106=data106,
                           data107=data107, data108=data108, data109=data109, data110=data110, data111=data111,
                           data112=data112, data113=data113, data114=data114, data115=data115, data116=data116,
                           data117=data117, data118=data118, data119=data119, data120=data120, data121=data121,
                           data122=data122, data123=data123, data124=data124, data125=data125, data126=data126,
                           data127=data127, data128=data128, data129=data129, data130=data130, data131=data131,
                           data132=data132, data133=data133, data134=data134, data135=data135, data136=data136,
                           data137=data137, data138=data138, data139=data139, data140=data140, data141=data141,
                           data142=data142, data143=data143, data144=data144, data145=data145, data146=data146)


@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    age = request.form['age']
    cpp = request.form['cpp']
    c = request.form['c']
    py = request.form['py']
    php = request.form['php']
    lv = request.form['lv']
    ms = request.form['ms']
    sql = request.form['sql']
    html = request.form['html']
    jv = request.form['jv']
    ja = request.form['ja']
    team = request.form['team']
    comm = request.form['comm']
    time = request.form['time']
    risk = request.form['risk']
    dec = request.form['dec']
    lead = request.form['lead']
    cult = request.form['cult']
    pres = request.form['pres']
    eng = request.form['eng']
    ger = request.form['ger']
    fr = request.form['fr']
    esp = request.form['esp']
    rus = request.form['rus']
    ita = request.form['ita']
    chn = request.form['chn']
    jap = request.form['jap']
    arb = request.form['arb']

    # Save the data
    fd = Formdata(age, cpp, c, py, php, lv, ms, sql, html, jv, ja, team, comm, time, risk, dec, lead, cult,
                  pres, eng, ger, fr, esp, rus, ita, chn, jap, arb)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()
