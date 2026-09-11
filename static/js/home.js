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