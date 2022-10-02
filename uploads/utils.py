import json

import loger as loger
from flask import render_template, logging


def load_posts(path='posts.json'):
    posts = []
    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)

    return posts

def search_posts(key_word):
    posts_found = []
    posts_json = load_posts()
    for post in posts_json:
        if key_word.lower() in post['content'].lower():
            posts_found.append(post)
    loger.info(f"User search {posts_found}")
    return posts_found

def save_picture(picture):
    filename = picture.filename
    filetype = filename.split('.')[-1]
    if filetype not in ['jpg', 'jpeg', 'svg', 'png']:
        loger.info(f"{filename} is not a picture")
        return "not images"

    try:
        picture.save(f'uploads/images/{filename}')
    except Exception:
        loger.error(f"Error with uploading file {filename}")
        return "Error with uploading file"

    return f'/uploads/images/{filename}'

def add_post(post):
    posts = load_posts()
    posts.append(post)
    save_posts_to_json(posts)


def save_posts_to_json(posts, path='posts.json'):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)



