from flask import Flask, render_template, url_for, request, jsonify
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route("/process/orderBy")
def get_order_by():
    order_by = request.args.get('orderBy')
    if user_input == None:
        order_by = "DESC"
        most_rated_shows = queries.get_most_rated('rating', order_by)
    if user_input != None:
        order_by = request.args.get('orderBy')
        most_rated_shows = queries.get_most_rated('rating', order_by)
    #return jsonify(most_rated_shows)
    return test


@app.route('/shows/most-rated')
def most_rated():
    start = 0
    end = 15
    current_page = int(start)
    next_page = current_page+1
    most_rated_shows = queries.get_most_rated('rating', 'DESC')
    show_count = queries.get_shows_count()
    page_count = math.floor(show_count[0]['count']/16)
    return render_template('most_rated_shows.html', most_rated_shows = most_rated_shows, page_count = page_count, start = start, end = end, current_page=current_page, next_page=next_page)


@app.route('/shows/most-rated/<pgnum>')
def test(pgnum):
    start = 16*int(pgnum)-1
    end = start+15
    current_page = int(pgnum)
    next_page = current_page+1
    prev_page = current_page-1
    most_rated_shows = queries.get_most_rated('rating', 'DESC')
    show_count = queries.get_shows_count()
    page_count = math.floor(show_count[0]['count']/16)
    return render_template('most_rated_shows.html', most_rated_shows = most_rated_shows, page_count = page_count, start = start, end = end, current_page=current_page, next_page=next_page, prev_page=prev_page)



def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
