window.addEventListener('scroll',
    function(){
        document.getElementById('head').classList.toggle('stick',window.scrollY>200);
    })