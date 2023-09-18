headr = $("header");
$ (document).ready(function (){
    var red_header = $("DIV#red_header");
    red_header.click(function (){
        red_header.css("color", "#FF0000");
    });
});