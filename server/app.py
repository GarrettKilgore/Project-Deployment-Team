from flask import Flask
from flask import request
#from dummydb import DummyDB
from db import DB

app = Flask(__name__)

@app.route("/movies/<int:id>", methods=["OPTIONS"])
def do_preflight(id):
	return '', 204, {"Access-Control-Allow-Origin": "*",
				     "Access-Control-Allow-Methods": "PUT, DELETE",
					 "Access-Control-Allow-Headers": "Content-Type"}

@app.route("/movies", methods=["GET"])
def get_movies():
	db = DB('trails.db')
	movies = db.readAllRecords()
	return movies, {"Access-Control-Allow-Origin": "*"}

@app.route("/movies/<int:id>", methods=["PUT"])
def edit_movie(id):
    db = DB('trails.db')
    print(request.form)
    d = {
    "name": request.form.get('name', ''),
    "movie": request.form.get('movie', ''),
    "genre": request.form.get('genre', ''),
    "rating": request.form.get('rating', ''),
    "review": request.form.get('review', '')
}
    db.editRecord(id, d)
    return "Edited", 200, {"Access-Control-Allow-Origin": "*"}

@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    print("I am deleting the movie: ", id)

    db = DB('trails.db')
    review = db.getReview(id)
    if review:
        db.deleterecord(id)
        return f"Deleted id {id}", 200, {"Access-Control-Allow-Origin": "*"}
    else:
        return f"Cannot delete movie with id {id}", 404, {"Access-Control-Allow-Origin": "*"}
	
@app.route("/movies", methods=["POST"])
def get_movie():
    db = DB('trails.db')
    d = {
        "name": request.form.get('name', ''),
        "movie": request.form.get('movie', ''),
        "genre": request.form.get('genre', ''),
        "rating": request.form.get('rating', ''),
        "review": request.form.get('review', '')
    }
    db.saveRecord(d)
    return "Created", 201, {"Access-Control-Allow-Origin": "*"}

@app.route("/movies/<int:id>", methods=["GET"])
def get_movie_by_id(id):
    db = DB('trails.db')
    review = db.getReview(id)
    if review:
        return review, 200, {"Access-Control-Allow-Origin": "*"}
    else:
        return {"error": f"No review found with id {id}"}, 404, {"Access-Control-Allow-Origin": "*"}


@app.route("/<name>")
def hello():
	return "YOU ARE HOME"

def main():
	app.run(host='0.0.0.0', port=5000)

main()
