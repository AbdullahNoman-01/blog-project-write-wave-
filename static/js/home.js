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
    const commentsSection = document.getElementById(
        `comments-${postId}`
    );
    if (commentsSection.style.display === "none") {
        commentsSection.style.display = "block";
    } else {
        commentsSection.style.display = "none";
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

