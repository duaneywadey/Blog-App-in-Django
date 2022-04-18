   $(document).ready(function(){
        $("p").click(function(){
            $(this).hide();
        });

        $("button").click(function(){
            $("#postObj").fadeIn("post");
        });
    });

