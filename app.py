#!/usr/bin/env python3
"""Multi-page portfolio website for linzihyang studio."""
from flask import Flask, render_template, send_from_directory, abort, request
from pathlib import Path
import os

app = Flask(__name__)

# Site configuration
SITE_CONFIG = {
    'title': 'linzihyang studio',
    'author': '林子揚 Lin Zih-Yang',
    'tagline': '用影像說話，為品牌發聲',
    'email': 'zerokevinlin@gmail.com',
    'phone': '+886 910-227-975',
    'social': {
        'facebook': 'https://www.facebook.com/linzihyangstudio',
        'instagram': 'https://www.instagram.com/lin_zihyang/',
        'youtube': 'https://www.youtube.com/@Mr-Lin-studio',
        'line': 'https://lin.ee/NCmDKig'
    }
}

# Portfolio data
PORTFOLIO_ITEMS = [
    {'title': '永恆誓言', 'category': 'wedding', 'desc': '婚紗攝影', 'img': 'portfolio_001.jpg'},
    {'title': '靈魂肖像', 'category': 'portrait', 'desc': '人像攝影', 'img': 'portfolio_002.jpg'},
    {'title': '品牌視覺', 'category': 'brand', 'desc': '商業攝影', 'img': 'portfolio_003.jpg'},
    {'title': '光影建築', 'category': 'architecture', 'desc': '建築攝影', 'img': 'portfolio_004.jpg'},
    {'title': '產品美學', 'category': 'brand', 'desc': '商品攝影', 'img': 'portfolio_005.jpg'},
    {'title': '情緒寫真', 'category': 'portrait', 'desc': '人像攝影', 'img': 'portfolio_006.jpg'}
]

# Courses data
COURSES = [
    {'title': 'AI 影像行銷入門班', 'hours': 6, 'level': 'mini', 'desc': 'AI 在行銷端的角色、影像拍攝要點、構圖說故事'},
    {'title': '影像行銷實戰班', 'hours': 12, 'level': 'mini', 'desc': '學會影片和照片的通用技巧，影像類型及趨勢'},
    {'title': 'AI 影像深度應用班', 'hours': 24, 'level': 'advanced', 'desc': 'AI 影像技術基礎原理、工具比較與選擇'},
    {'title': '企業全案培訓班', 'hours': 30, 'level': 'enterprise', 'desc': '紅海 vs 藍海市場分析、邏輯規劃與堆疊'}
]

@app.route('/')
def home():
    return render_template('home.html', config=SITE_CONFIG, portfolio=PORTFOLIO_ITEMS)

@app.route('/about')
def about():
    return render_template('about.html', config=SITE_CONFIG)

@app.route('/portfolio')
def portfolio():
    categories = ['all'] + list(set(item['category'] for item in PORTFOLIO_ITEMS))
    return render_template('portfolio.html', config=SITE_CONFIG, portfolio=PORTFOLIO_ITEMS, categories=categories)

@app.route('/courses')
def courses():
    return render_template('courses.html', config=SITE_CONFIG, courses=COURSES)

@app.route('/contact')
def contact():
    return render_template('contact.html', config=SITE_CONFIG)

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
