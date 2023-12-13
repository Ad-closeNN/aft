/*==== Sticky Navigation ====*/

$(window).on("scroll", function () {
    var o = $(window).scrollTop(),
        t = $("nav");
    o > 1 ? t.addClass("sticky-top") : t.removeClass("sticky-top")
}), $('.nav-link').on('click', function () {
    $('.navbar-collapse').collapse('hide')
});

/*==== Current section highlight in the navigation bar ====*/
$(window).on("scroll", function () {
    var currentPos = $(window).scrollTop();

    $('.navbar li a').each(function () {
        var sectionLink = $(this);
        // capture the height of the navbar
        var navHeight = $('#navbarNav').outerHeight() + 1;
        var section = $(sectionLink.attr('href'));

        // subtract the navbar height from the top of the section
        if (section.position().top - navHeight <= currentPos && sectionLink.offset().top + section.height() > currentPos) {
            $('.navbar li').removeClass('current');
            sectionLink.parent().addClass('current');
        } else {
            sectionLink.parent().removeClass('current');
        }
    });
});

/*======= go to top ========*/

//-------------------------------------------------------------------------
//scroll top js
//-----------------------------------------
$(window).scroll(function () {
    if ($(this).scrollTop() >= 50) { // If page is scrolled more than 50px
        $('.gotop').fadeIn(200); // Fade in the arrow
    } else {
        $('.gotop').fadeOut(200); // Else fade out the arrow
    }
});
$('.gotop').click(function () { // When arrow is clicked
    $('body,html').animate({
        scrollTop: 0 // Scroll to top of body
    }, 1000);
});

//-----------------------------------------------------------------
// Smooth Scrolling
//------------------------------------------------------
$('.smoothscroll').on('click', function (e) {

    e.preventDefault();

    var target = this.hash,
        $target = $(target);

    $('html, body').stop().animate({
        'scrollTop': $target.offset().top
    }, 800, 'swing', function () {
        window.location.hash = target;
    });

});

