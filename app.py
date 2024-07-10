from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Food Input API"

@app.route('/menus', methods=['GET'])
def get_menus():
    # 여기에 크롤링 로직을 구현합니다
    menus = {
        "금양체질": ["조개", "게", "문어"],
        "금음체질": ["소고기", "양고기"],
        "목양체질": ["닭고기", "오리고기"],
        "목음체질": ["돼지고기", "생선"],
        "토양체질": ["채소", "과일"],
        "토음체질": ["곡물", "견과류"],
        "수양체질": ["해조류", "버섯"],
        "수음체질": ["두부", "콩류"]
    }
    
    constitution = request.args.get('constitution', default='all', type=str)
    
    if constitution != 'all' and constitution in menus:
        return jsonify({constitution: menus[constitution]})
    else:
        return jsonify(menus)

if __name__ == '__main__':
    app.run(debug=True)
