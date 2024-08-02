$('.owl-carousel-1').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    navText: [
      "<i class='fa fa-caret-left'></i>",
      "<i class='fa fa-caret-right'></i>"
    ],
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
      0: {
        items: 1
      },
      600: {
        items: 3
      },
      1000: {
        items: 5
      }
    }
  })



  var target_mili_sec = new Date("Oct 10, 2022 14:30:0").getTime();
          function timer() {
              var now_mili_sec = new Date().getTime();
              var remaining_sec = Math.floor( (target_mili_sec - now_mili_sec) / 1000 );

              var day = Math.floor(remaining_sec / (3600 * 24));
              var hour = Math.floor((remaining_sec % (3600 * 24)) / 3600);
              var min = Math.floor((remaining_sec % 3600) / 60);
              var sec = Math.floor(remaining_sec % 60);

              document.querySelector("#day").innerHTML = day;
              document.querySelector("#hour").innerHTML = hour;
              document.querySelector("#min").innerHTML = min;
              document.querySelector("#sec").innerHTML = sec;
          }

          setInterval(timer, 1000); //1000 it means 1 sec
          







  
