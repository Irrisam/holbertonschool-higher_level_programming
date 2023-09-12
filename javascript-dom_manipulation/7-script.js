const list_movies = document.getElementById("list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then ((response) => {
        return response.json();
    })
    .then ((data) => {
        const movies = data.results;
        list_movies.textContent = data.title

        movies.forEach((movie) => {
            const item_list =  document.createElement("li");
            item_list.textContent = movie.title;
            list_movies.appendChild(item_list);
        });
    })
