headr = $("header");
$ (document).ready(function (){
    toggle_header = $("DIV#toggle_header");
    toggle_header.click(function (){
        if (headr.hasClass("red")){
            headr.removeClass("red");
            headr.addClass("green")
        }
        else if (headr.hasClass("green")){
            headr.removeClass("green");
            headr.addClass("red");
        }
        else
        headr.addClass("red");
    });
});
