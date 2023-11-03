//NavBar
function hideIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    var myforum = document.getElementById("myforum");
    var createpost = document.getElementById("createpost");
    var search = document.getElementById("searching");
    iconBar.setAttribute("style", "display:none;");
    myforum.classList.add("hide");
    search.classList.add("hide");
    createpost.classList.add("hide");
    navigation.classList.remove("hide");
}

function showIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    var myforum = document.getElementById("myforum");
    var createpost = document.getElementById("createpost")
    var search = document.getElementById("searching")
    iconBar.setAttribute("style", "display:block;");
    myforum.classList.remove("hide");
    search.classList.remove("hide");
    createpost.classList.remove("hide");
    navigation.classList.add("hide");
}

//Comment
function showComment(){
    var commentArea = document.getElementById("comment-area");
    commentArea.classList.remove("hide");
}

document.getElementById("hide-button").addEventListener("click", function(event) {
    event.preventDefault();
    var commentArea = document.getElementById("comment-area");
    commentArea.classList.add("hide");
});
//Reply
function showReplies(id){
    var replyArea = document.getElementById(id);
    replyArea.classList.remove("hide");
}

function hideReplies(event, id){
    event.preventDefault();
    var replyArea = document.getElementById(id);
    replyArea.classList.add("hide");
}

/*$(document).ready(function() {
    $(".edit-comment").click(function(e) {
        e.preventDefault();
        $("#edit-comment-modal").show();
    });
});

$(document).ready(function() {
    $(".edit-comment").click(function(e) {
        e.preventDefault();
        $("#edit-comment-modal").show();
    });

    $("#edit-comment-modal").on("submit", "form", function(e) {
        e.preventDefault();
        $("#edit-comment-modal").hide();
    });
});*/

$(window).load(function(){
    if ($('#refreshed').val() == "false") {
      $('#refreshed').val("true"); 
    }
    else {
      $('#refreshed').val("false");
      location.reload();
    }
  });


