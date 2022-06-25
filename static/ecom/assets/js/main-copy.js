$(document).ready(function () {
  /*-------Navbar Shrink---------*/
  $(window).on("scroll", function () {
    if ($(this).scrollTop() > 90) {
      $(".navbar").addClass("navbar-shrink");
    } else {
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

  /* -------------------Domain Search-------------------*/

  // !(function () {
  //   var e = document.querySelector("#ir_form"),
  //     n = document.querySelector("#ir_domain"),
  //     t = document.querySelector("#ir_link");
  //   e.addEventListener("submit", function (o) {
  //     o.preventDefault(),
  //       (t.value =
  //         "https://www.namecheap.com/domains/registration/results.aspx?domain=" +
  //         n.value);
  //     if (e.domain.value === "") {
  //       window.location.href = document.querySelector("#ir_url").href;
  //     } else {
  //       e.submit();
  //     }
  //   });
  // })();
});
