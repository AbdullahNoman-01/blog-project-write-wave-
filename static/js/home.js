function toggleMenu(postId) {
    const currentMenu = document.getElementById(`menu-${postId}`);
    document.querySelectorAll(".post-menu").forEach(menu => {
        if (menu !== currentMenu) {
            menu.classList.remove("show");
        }
    });
    currentMenu.classList.toggle("show");
}

document.addEventListener("click", function (event) {
    if (!event.target.closest(".post-menu-wrapper")) {
        document.querySelectorAll(".post-menu").forEach(menu => {
            menu.classList.remove("show");
        });
    }
});



function toggleComments(postId) {
    const comments = document.getElementById(
        "comments-" + postId
    );

    if (!comments) {
        console.log("Comments section not found:", postId);
        return;
    }

    if (comments.style.display === "none") {
        comments.style.display = "block";
    } else {
        comments.style.display = "none";
    }
}




const seeMoreTopics = document.getElementById("seeMoreTopics");
const extraTopics = document.querySelectorAll(".extra-topic");
if (seeMoreTopics) {
    seeMoreTopics.addEventListener("click", function () {
        const isHidden = extraTopics[0].style.display === "" ||
                            extraTopics[0].style.display === "none";

        extraTopics.forEach(topic => {
            topic.style.display = isHidden ? "flex" : "none";
        });
        this.textContent = isHidden
            ? "Show less"
            : "See more topics";
    });
}






function closeLoginNotice() {
    const notice = document.getElementById("loginNotice");
    if (notice) {
        notice.style.display = "none";
    }
}


function toggleReplies(commentId) {
    const replies = document.getElementById(
        "replies-" + commentId
    );
    const icon = document.getElementById(
        "reply-icon-" + commentId
    );
    if (!replies || !icon) {
        return;
    }
    if (replies.style.display === "none") {
        replies.style.display = "block";
        icon.textContent = "↑";
    } else {

        replies.style.display = "none";
        icon.textContent = "↓";

    }
}