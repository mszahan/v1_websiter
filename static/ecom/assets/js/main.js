

$(document).ready(function() {
  /*-------Navbar Shrink---------*/
  $(window).on("scroll", function(){
    if($(this).scrollTop() > 90){
      $(".navbar").addClass("navbar-shrink");
    } 
    else{
      $(".navbar").removeClass("navbar-shrink");
    }
  });
  /*---------------------Feature-carousel----------------------*/

  $(".features-carousel").owlCarousel({
    loop: true,
    margin: 0,
    autoplay: true,
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 2,
        nav: false,
      },
      1000: {
        items: 3,

      },
    },
  });
  /*---------------------screenshot-carousel----------------------*/

  $(".screenshot-carousel").owlCarousel({
    loop: true,
    margin: 0,
    autoplay: true,
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 2,
        nav: false,
      },
      1000: {
        items: 4,

      },
    },
  });
  /*---------------------Testimonial-Carousel----------------------*/

  $(".testimonials-carousel").owlCarousel({
    loop: true,
    margin: 0,
    // autoplay: true,
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 2,
        nav: false,
      },
      1000: {
        items: 3,

      },
    },
  });


});
