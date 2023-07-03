//NavBar
function hideIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display:none;");
    navigation.classList.remove("hide");
}

function showIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display:block;");
    navigation.classList.add("hide");
}

//Comment
function showComment(){
    var commentArea = document.getElementById("comment-area");
    commentArea.classList.remove("hide");
}

function hideComment(){
    var commentArea = document.getElementById("comment-area");
    commentArea.classList.add("hide");
}
//Reply
function showReplies(id){
    var replyArea = document.getElementById(id);
    replyArea.classList.remove("hide");
}

function hideReplies(id){
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
