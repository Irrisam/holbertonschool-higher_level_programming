headr = $("header");
$ (document).ready(function (){
    var red_header = $("DIV#red_header");
    red_header.click(function (){
        headr.addClass("red");
    });
});
