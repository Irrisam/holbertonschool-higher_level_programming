main_list = $("UL.my_list");
$ (document).ready(function (){
    var newListItem = $("<li>New Item</li>");
    var add_item = $("DIV#add_item");
    add_item.click(function (){
        main_list.append(newListItem);
    });
});
