fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then ((response) => {
        return response.json();
    })
    .then ((data) => {
        hello = data.hello;
        hello_button = document.getElementById("hello");
        hello_button.textContent = hello;
    })