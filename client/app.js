console.log("connected");

const movies_div = document.querySelector("#movie_reviews");
let editID = null;

function load(){
	//blank out the movie_reviews div
	movies_div.innerHTML = ""

fetch("http://localhost:5000/movies")
.then(function(response) {
	response.json()
	.then(function(data) {
		console.log(data);
		data.forEach(movie => load_movies(movie))
		});
	});
}

function load_movies(movie) {
    let div = document.createElement("div");
    div.classList.add("review-box");

    let h3 = document.createElement("h3");
    let p1 = document.createElement("p");
    let p2 = document.createElement("p");
    let p3 = document.createElement("p");
	let p4 = document.createElement("p");

    let editButton = document.createElement("button");
    editButton.innerText = "Edit";
    editButton.onclick = function() {
        do_edit(movie);
    };

    let delButton = document.createElement("button");
    delButton.innerText = "Delete";
    delButton.onclick = function() {
        do_delete(movie.id);
    };

    h3.innerText = movie.name;
    p1.innerHTML = "<strong>Movie:</strong> " + movie.movie;
	p2.innerHTML = "<strong>Genre:</strong> " + movie.genre;
    p3.innerHTML = "<strong>Rating:</strong> " + movie.rating;
    p4.innerHTML = "<strong>Review:</strong> " + movie.review;

	let buttonContainer = document.createElement("div");
	buttonContainer.classList.add("button-container");
	buttonContainer.appendChild(editButton);
	buttonContainer.appendChild(delButton);
	div.append(h3, p1, p2, p3, p4, buttonContainer);
	
    movies_div.append(div);
}


function reset_form() {
	document.querySelector("#reviewer_name").value = ""
	document.querySelector("#movie_input_name").value = ""
	document.querySelector("#movie_input_genre").value = "";
	document.querySelector("#movie_input_rating").value = ""
	document.querySelector("#movie_input_review").value = ""
	document.querySelector("#movie_submit_button").innerHTML = "SUBMIT"
}

function do_edit(movie) {
    console.log("You are going to edit movie: ", movie.id);
    document.querySelector("#reviewer_name").value = movie.name;
	document.querySelector("#movie_input_genre").value = movie.genre;
    document.querySelector("#movie_input_name").value = movie.movie;
    document.querySelector("#movie_input_rating").value = movie.rating;
    document.querySelector("#movie_input_review").value = movie.review;

    document.querySelector("#movie_submit_button").innerHTML = "SAVE";
    editID = movie.id;
}

function do_delete(id) {
	console.log("You are going to delete trail: ", id)
	let foo = confirm("Are you sure?")
	console.log(foo)
	fetch("http://localhost:5000/movies/"+id, {
		method: "DELETE",
		headers: {
			"Content-Type": "application/x-www-form-urlencoded"
		}
	})
		.then(function(response) {
    		console.log("Deleted");
    		load();
		})
}

function addnewReview(){
	//get the form data
	let name = document.querySelector("#reviewer_name").value
	let movie = document.querySelector("#movie_input_name").value
	let genre = document.querySelector("#movie_input_genre").value;
	let rating = document.querySelector("#movie_input_rating").value
	let review = document.querySelector("#movie_input_review").value

	
	console.log("The name is ", name)
	console.log("The name is ", movie)
	console.log("The name is ", genre)
	console.log("The name is ", rating)
	console.log("The name is ", review)


	//get it ready to send to api
	let data = "name=" + encodeURIComponent(name)
         + "&movie=" + encodeURIComponent(movie)
         + "&genre=" + encodeURIComponent(genre)
         + "&rating=" + encodeURIComponent(rating)
         + "&review=" + encodeURIComponent(review);
	console.log(data)

	let submit_method = "POST";
    const button_text = document.querySelector("#movie_submit_button").innerHTML;
    let url = "http://localhost:5000/movies";

    if (button_text === "SAVE") {
        submit_method = "PUT";
        url = "http://localhost:5000/movies/" + editID;
    }

	//send to api
	fetch(url, {
        method: submit_method,
        body: data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    })
    .then(function(response) {
        console.log("Saved:", response);
        reset_form();
        load();
    });
}
	//display results

let button = document.querySelector("#movie_submit_button")
button.onclick = addnewReview
load()