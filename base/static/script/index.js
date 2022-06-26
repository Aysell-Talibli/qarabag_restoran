const header = document.querySelector('.header__back')
const headerBig = document.querySelector('.header')
const headmenu = document.querySelectorAll('.head_menu li a')



$(window).scroll(function () {
    if ($(window).scrollTop() > 1) {
        header.style.backgroundColor = '#fff'
        header.style.opacity = '1'
        headerBig.style.boxShadow = '0 0 20px 1px #000'
        headmenu.forEach((item) => {
            item.style.color = '#000'
        })
    }
    else {
        header.style.backgroundColor = 'rgb(145, 145, 145)'
        header.style.opacity = '0.3'
        headerBig.style.boxShadow = ''
        headmenu.forEach((item) => {
            item.style.color = '#fff'
        })
    }

})




document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e){
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior : "smooth"
        });
    });
});



