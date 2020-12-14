window.onload = function(){
    // preloader
    document.querySelector(".loader").style.display = "none";

    // new upload page buttons
    // artist
    document.getElementById("artist-upload-btn").addEventListener('click', function() {
        document.getElementById("crewPiece").classList.add("hidden");
        document.getElementById("artistPiece").classList.remove("hidden");
    });
    // crew
    document.getElementById("crew-upload-btn").addEventListener('click', function() {
        document.getElementById("artistPiece").classList.add("hidden");
        document.getElementById("crewPiece").classList.remove("hidden");
    });
};