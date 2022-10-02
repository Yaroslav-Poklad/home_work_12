from json import JSONDecodeError

from flask import Blueprint, render_template, request

from uploads.utils import search_posts

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', url_prefix='/')

@main_blueprint.route('/')
def main_index():
    return render_template('index.html')

@main_blueprint.route('/search/')
def search_page():
    key_word = request.args.get('s')
    try:
        posts = search_posts(key_word)
    except FileNotFoundError:
        return "File Not Found"
    except JSONDecodeError:
        return "Can`t convert to JSON"
    else:
        return render_template('post_list.html', posts=posts, key_word=key_word)






