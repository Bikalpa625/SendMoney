document.getElementById("burger-icon").addEventListener("click", function () {
    var mobileMenu = document.getElementById("mobile-menu");
    mobileMenu.classList.toggle("hidden");
});
document.getElementById("profile-picture").addEventListener("click", function () {
    var dropdownMenu = document.getElementById("dropdown-menu");
    dropdownMenu.classList.toggle("hidden");
});

// Close the dropdown if the user clicks outside of it
window.addEventListener("click", function(e) {
    var profilePicture = document.getElementById("profile-picture");
    var dropdownMenu = document.getElementById("dropdown-menu");

    if (!profilePicture.contains(e.target) && !dropdownMenu.contains(e.target)) {
        dropdownMenu.classList.add("hidden");
    }
});