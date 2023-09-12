add_item_button = document.getElementById("add_item");
list_tag = document.querySelector(".my_list");

add_item_button.addEventListener("click", function() {
    var new_item = document.createElement("li");
    var text = document.createTextNode("Item");
    new_item.appendChild(text)
    list_tag.appendChild(new_item);
})

