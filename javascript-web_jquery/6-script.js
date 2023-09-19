headr = $("header");
$ (document).ready(function (){
    var update_header = $("DIV#update_header");
    update_header.click(function (){
        headr.text("New Header!!!");
    });
});
