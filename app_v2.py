#!/usr/bin/env python3
"""Highly interactive AI Agent style portfolio website."""
from flask import Flask, render_template, send_from_directory, jsonify, abort
from pathlib import Path
import os
import time

app = Flask(__name__, template_folder='templates')

# Site configuration - aligned with original Canva site
SITE_CONFIG = {
    'title': 'linzihyang studio',
    'author': '林子揚 Lin Zih-Yang',
    'tagline': '用影像說話，為品牌發聲',
    'subtitle': '我是林子揚 管理雜誌-百大講師\n一位結合攝影藝術與行銷策略的創作者\n從鏡頭到市場\n我協助品牌與個人打造獨特視覺與策略定位',
    'email': 'zerokevinlin@gmail.com',
    'phone': '(+886) 0910227975',
    'wechat': 'zerokevinlin',
    'social': {
        'facebook': 'https://www.facebook.com/linzihyangstudio',
        'instagram': 'https://www.instagram.com/lin_zihyang/',
        'youtube': 'https://www.youtube.com/@Mr-Lin-studio',
        'line': 'https://lin.ee/NCmDKig'
    },
    'about_full': '我是林子揚，我是一名自由攝影師與行銷顧問，畢業於醫事放射系，專注於影像創作、品牌行銷與數位經營策略。致力於企業行銷培訓與品牌視覺塑造。\n\n在攝影領域，曾與多家婚紗工作室合作，專精於婚紗、人像、品牌形象與商業攝影，透過影像為品牌與個人打造獨特風格，提升市場競爭力。\n\n此外，我也深耕數位行銷與品牌經營輔導，曾為多家企業提供行銷策略指導，涵蓋了社群行銷、內容行銷、品牌定位與電商經營，幫助品牌強化市場影響力。\n\n我相信「影像與行銷的結合」是品牌成功的關鍵。',
    'philosophy': '時間會飛逝\n記憶會消失\n影像是記憶的催化劑\n就像是檯時光機\n穿梭在不同的時空裡\n回到每個旅程中\n\n一旦少了影像\n在美好的回憶也會隨著時間而流逝',
    'credentials': [
        '鈜薪(股)公司_業務經理',
        '網媒特約記者',
        '小島3.5度親子餐廳_特約攝影師',
        '醫事放射師',
        'QUESTA品牌創辦人',
        '美麗華實業社輔導顧問',
        'RESAMAKEUP_攝影師',
        '藝思特行銷有限公司_攝影師',
        '33嫁紗美學空間_攝影師',
        'I.Dear婚紗工作室_攝影師',
        '關策公關公司_攝影師',
        '寶德攝影_海外攝影師',
        '藝崧婚紗工作室_攝影師',
        '絆嵐攝_攝影師'
    ],
    'clients': [
        '網路行銷人才培訓',
        '沐光能量手作',
        'baboo_toys',
        '森饗鍋物 Senn shabu',
        '巨宇翔(股)公司',
        '薡茶加盟連鎖集團',
        '大全鋼閥實業(股)公司',
        '鏈發射出機械(股)公司',
        '金商(股)公司',
        '桃映梨山果',
        '三業(股)公司',
        '凌網知識(股)公司',
        '路益(股)公司',
        '遊城實業(股)公司',
        '優迪國際(股)公司',
        '資通電腦(股)'
    ],
    'awards': [
        '新娘物語-2018 年度「婚禮人100+ 年鑑」',
        '新娘物語-2019 年度「婚禮人100+ 年鑑」'
    ],
    'services': [
        {
            'title': '婚紗與品牌攝影',
            'desc': '從婚紗人像、品牌形象到商業拍攝，致力於將視覺藝術與數位行銷整合，為品牌與個人創造更具影響力的市場價值。',
            'icon': '📸'
        },
        {
            'title': '數位行銷與企業顧問',
            'desc': '運用網頁強化IP識別度，視覺強度決定你的行銷力度。從品牌定位到社群營運，全方位數位行銷策略規劃。',
            'icon': '📱'
        },
        {
            'title': 'AI 影像應用',
            'desc': '運用AI工具提升影像呈現度，結合AI和素材讓影像加分，從文字生圖片到圖片轉換成影像，全面提升創作效率。',
            'icon': '🤖'
        }
    ],
    'courses': [
        {
            'title': '行銷學的靈魂 -攝影篇',
            'hours': 6,
            'level': 'mini',
            'desc': '靜態照片拍攝實務操作\n人物、建築、擺拍技巧演練',
            'note': '迷你班一人即可開課\n上課須自備電腦\n上課時間與地點依招生人數而定\n上課時數：6小時\n上課時間：09:00-12:00，13:00-16:00\n上課費用：依人數制定[含稅.教材.午餐]\n報名方式：zerokevinlin@gmail.com'
        },
        {
            'title': '微行銷趨勢',
            'hours': 6,
            'level': 'mini',
            'desc': '微行銷趨勢-教你用手機拍攝影片、微廣告\n用照片說故事行銷技巧',
            'note': '迷你班一人即可開課\n上課須自備電腦\n上課時間與地點依招生人數而定\n上課時數：6小時\n上課時間：09:00-12:00，13:00-16:00\n上課費用：依人數制定[含稅.教材.午餐]\n報名方式：zerokevinlin@gmail.com'
        },
        {
            'title': 'AI影像提升社群魅力',
            'hours': 12,
            'level': 'mini',
            'desc': 'AI行銷-從分析、集客到回流\n有效AI文案\n挖掘自我的價值\nAI透視差異',
            'note': '迷你班一人即可開課\n上課須自備電腦\n上課時間與地點依招生人數而定\n上課時數：12小時\n上課時間：09:00-12:00，13:00-16:00\n上課費用：依人數制定[含稅.教材.午餐]\n報名方式：zerokevinlin@gmail.com'
        },
        {
            'title': '文宣視覺技巧',
            'hours': 12,
            'level': 'mini',
            'desc': '文宣視覺技巧，提升TA感受度。\nAI影像產出\n高效文宣工具',
            'note': '迷你班一人即可開課\n上課須自備電腦\n上課時間與地點依招生人數而定\n上課時數：12小時，共兩天\n上課時間：09:00-12:00，13:00-16:00\n上課費用：依人數制定[含稅.教材.午餐]\n報名方式：zerokevinlin@gmail.com'
        },
        {
            'title': 'AI行銷-從分析、集客到回流',
            'hours': 24,
            'level': 'advanced',
            'desc': 'AI市場分析\n社群集客引流\nAI提升回流率',
            'note': '我們會在從分析到挖掘產品價值，再進行定位，最後是利用影像的呈現，讓商品除了襯托出本身的價值之外進而可以提高受眾，除了精準打擊同時也可以得到市場認可，最後是引領消費者走出不同的產品高度。\n\n客訂化實作教學，依照學員需求手把手讓小白到獨立完成項目，這堂課程主打的就是新手或者公司在職培訓的需求，讓學員在短時間就可以上手，降低公司培訓成本，同時也提供多元職業技能。\n\n此方案將確保有成品輸出及在職場上的應用，獨立完成的進度須依照訓練時數及熟練度而視，最後將還有一年內的免費咨詢乙次。'
        },
        {
            'title': 'AI工具的應用與整合',
            'hours': 24,
            'level': 'advanced',
            'desc': 'AI工具的應用與整合\n影片的类型及趋势\n摄影通用法则和技巧\n运用AI工具',
            'note': '包班制\n上課時數：客製化內容及時數\n上課費用：依人數制定[含稅.教材]\n報名方式：zerokevinlin@gmail.com'
        },
        {
            'title': '企業全案培訓班',
            'hours': 30,
            'level': 'enterprise',
            'desc': '1.紅海v.s 藍海\n2.邏輯規劃與堆疊\n3.利用AI找出TA\n4.AI工具運用與分析\n5.實作演練',
            'note': '1.社群趨勢與走向\n2.社群媒體與網站差異\n3.提升集客力\n4.實作演練'
        }
    ],
    'portfolio_categories': [
        {'name': 'all', 'label': '全部'},
        {'name': 'wedding', 'label': '婚紗'},
        {'name': 'portrait', 'label': '人像'},
        {'name': 'brand', 'label': '品牌'},
        {'name': 'architecture', 'label': '建築'}
    ]
}

# Portfolio items with real images
PORTFOLIO_ITEMS = [
    {'title': '永恆誓言', 'category': 'wedding', 'desc': '婚紗攝影', 'img': 'assets/images/portfolio/001.jpg'},
    {'title': '靈魂肖像', 'category': 'portrait', 'desc': '人像攝影', 'img': 'assets/images/portfolio/002.jpg'},
    {'title': '品牌視覺', 'category': 'brand', 'desc': '商業攝影', 'img': 'assets/images/portfolio/003.jpg'},
    {'title': '光影建築', 'category': 'architecture', 'desc': '建築攝影', 'img': 'assets/images/portfolio/004.jpg'},
    {'title': '產品美學', 'category': 'brand', 'desc': '商品攝影', 'img': 'assets/images/portfolio/005.jpg'},
    {'title': '情緒寫真', 'category': 'portrait', 'desc': '人像攝影', 'img': 'assets/images/portfolio/006.jpg'},
    {'title': '永恆誓言2', 'category': 'wedding', 'desc': '婚紗攝影', 'img': 'assets/images/portfolio/007.jpg'},
    {'title': '靈魂肖像2', 'category': 'portrait', 'desc': '人像攝影', 'img': 'assets/images/portfolio/008.jpg'},
    {'title': '品牌視覺2', 'category': 'brand', 'desc': '商業攝影', 'img': 'assets/images/portfolio/009.jpg'},
    {'title': '光影建築2', 'category': 'architecture', 'desc': '建築攝影', 'img': 'assets/images/portfolio/010.jpg'},
    {'title': '產品美學2', 'category': 'brand', 'desc': '商品攝影', 'img': 'assets/images/portfolio/011.jpg'},
    {'title': '情緒寫真2', 'category': 'portrait', 'desc': '人像攝影', 'img': 'assets/images/portfolio/012.jpg'}
]

@app.route('/')
def home():
    return render_template('home.html', config=SITE_CONFIG, portfolio=PORTFOLIO_ITEMS)

@app.route('/about')
def about():
    return render_template('about.html', config=SITE_CONFIG)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', config=SITE_CONFIG, portfolio=PORTFOLIO_ITEMS)

@app.route('/courses')
def courses():
    return render_template('courses.html', config=SITE_CONFIG, courses=SITE_CONFIG['courses'])

@app.route('/contact')
def contact():
    return render_template('contact.html', config=SITE_CONFIG)
@app.route('/api/config')
def api_config():
    return jsonify(SITE_CONFIG)

@app.route('/api/portfolio')
def api_portfolio():
    return jsonify(PORTFOLIO_ITEMS)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
