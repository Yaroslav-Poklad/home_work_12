import json

from flask import render_template


def load_posts(path='posts.json'):
    posts = []
    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)

    return posts

def search_posts(substr):
    posts_found = []
    posts_json = load_posts()
    for post in posts_json:
        if substr in post['content']:
            posts_found.append(post)

    return posts_found

def save_picture(picture):
    filename = picture.filename
    filetype = filename.split('.')[-1]
    if filetype not in ['jpg', 'jpeg', 'svg', 'png']:
        return

    picture.save(f'./uploads/images/{filename}')

    return render_template('post_uploaded.html')

def add_post(post):
    posts = load_posts()
    posts.append(post)
    save_posts_to_json(posts)


def save_posts_to_json(posts, path='posts.json'):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(posts, file)

