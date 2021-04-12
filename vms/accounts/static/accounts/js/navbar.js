$(function () {

    $(window).scroll(function () {
        var scrolling = $(this).scrollTop();


        if (scrolling > 90) {
            $('.navbar').addClass('navbg');
        } else {
            $('.navbar').removeClass('navbg')
        }
    });

});
