from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模擬文章資料（用 list 儲存）
posts = [
    {"id": 1, "title": "第一篇文章", "author": "小明", "content": "這是我的第一篇部落格內容！"},
    {"id": 2, "title": "Flask 好好玩", "author": "小華", "content": "今天學會了 Flask 的模板系統。"}
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        return "找不到這篇文章", 404
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        new_id = max([p['id'] for p in posts]) + 1 if posts else 1
        posts.append({"id": new_id, "title": title, "author": author, "content": content})
        return redirect(url_for('index'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
