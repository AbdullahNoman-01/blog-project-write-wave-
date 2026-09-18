function toggleReplies(commentId) {
    const replies = document.getElementById(
        "replies-" + commentId
    );
    const icon = document.getElementById(
        "toggle-icon-" + commentId
    );
    if (replies.style.display === "none") {
        replies.style.display = "block";
        icon.textContent = "−";
    } else {
        replies.style.display = "none";
        icon.textContent = "+";
    }
}
function showReplyForm(commentId) {
    const form = document.getElementById(
        "reply-form-" + commentId
    );
    if (form.style.display === "none") {

        form.style.display = "block";
    } else {
        form.style.display = "none";
    }
}
