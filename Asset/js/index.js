function toggleMenu(){
    if (innerWidth < 768 ){
        var menuToggle = document.querySelector('.toggle');
        menuToggle.classList.toggle('open');
        var navigatation = document.querySelector('.navigatationBar');
        navigatation.classList.toggle('open');
    }
}