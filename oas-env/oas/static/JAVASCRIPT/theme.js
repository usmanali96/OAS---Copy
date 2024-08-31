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



  //var target_mili_sec = new Date("Oct 10, 2022 14:30:0").getTime();
       //   function timer() {
       //       var now_mili_sec = new Date().getTime();
       //       var remaining_sec = Math.floor( (target_mili_sec - now_mili_sec) / 1000 );

        //      var day = Math.floor(remaining_sec / (3600 * 24));
         //     var hour = Math.floor((remaining_sec % (3600 * 24)) / 3600);
         //     var min = Math.floor((remaining_sec % 3600) / 60);
          //    var sec = Math.floor(remaining_sec % 60);

           //   document.querySelector("#day").innerHTML = day;
           //   document.querySelector("#hour").innerHTML = hour;
           //   document.querySelector("#min").innerHTML = min;
           //   document.querySelector("#sec").innerHTML = sec;
      //   }

       //   setInterval(timer, 1000); //1000 it means 1 sec
          


          function cdtime(targetDate){
            var thisobj=this
            this.syncinfo = {afterSec:300, currentSec:0} // resync current time with user's computer time after every x seconds (afterSec prop)
            this.targetDate = new Date(targetDate)
            this.currentDate = ''
            this.oncountdown = function(ms){}
            this.diff
          }
          
          
          cdtime.prototype.getDifference=function(){
            this.diff = this.targetDate - this.currentDate
          }
          
          cdtime.prototype.startCount = function(){
            var thisobj = this
            var syncinfo = this.syncinfo
            var updatetimer = setInterval(function(){ // update countdown every second
              if (syncinfo.currentSec >= syncinfo.afterSec){ // sync currentDate with time on user computer?
                thisobj.currentDate = new Date()
                syncinfo.currentSec = 0
              }
              else{
                thisobj.currentDate.setSeconds( thisobj.currentDate.getSeconds() + 1 )
              }
              thisobj.getDifference()
              thisobj.oncountdown(thisobj.diff)
              syncinfo.currentSec++
              if (thisobj.diff <= 0){
                clearInterval(updatetimer)
              }
            }, 1000) //update every second
          }
          
          cdtime.prototype.start = function(){
            this.currentDate = new Date()
            this.getDifference()
            this.oncountdown(this.diff)
            if (this.diff > 0){
              this.startCount()
            }
          }
          
      //    cdtime.formatDuration = function(ms, baseunit){
     //       var timediff = ms/1000 // time remaining in sec
     //       var oneMinute=60 //minute unit in seconds
     //       var oneHour=60*60 //hour unit in seconds
     //       var oneDay=60*60*24 //day unit in seconds
     //       var dayfield=Math.floor(timediff/oneDay)
      //      var hourfield=Math.floor((timediff-dayfield*oneDay)/oneHour)
      //      var minutefield=Math.floor((timediff-dayfield*oneDay-hourfield*oneHour)/oneMinute)
        //    var secondfield=Math.floor((timediff-dayfield*oneDay-hourfield*oneHour-minutefield*oneMinute))
        //    if (baseunit=="hours"){ //if base unit is hours, set "hourfield" to be topmost level
         //     hourfield=dayfield*24+hourfield
          //    dayfield="n/a"
          //  }
          //  else if (baseunit=="minutes"){ //if base unit is minutes, set "minutefield" to be topmost level
          //    minutefield=dayfield*24*60+hourfield*60+minutefield
            //  dayfield=hourfield="n/a"
        //    }
     //       else if (baseunit=="seconds"){ //if base unit is seconds, set "secondfield" to be topmost level
    //          var secondfield=timediff
        //      dayfield=hourfield=minutefield="n/a"
      //      }
   //        return{
         //     days: dayfield,
     //         hours: hourfield,
     //         minutes: minutefield,
     //         seconds: secondfield
     //       }
     //     }
          






         //   document.addEventListener('DOMContentLoaded', function() {
          //  const timers = document.querySelectorAll('.timer-overlay');
        
            //timers.forEach(timer => {
                // Get the countdown date and parse it
              //  const countdownDateStr = timer.getAttribute('data-countdown');
                //const countdownDate = new Date(countdownDateStr).getTime();
        
                //if (isNaN(countdownDate)) {
                 //   console.error("Invalid countdown date:", countdownDateStr);
                 //   return; // Exit if the date is invalid
               // }
        
       //         const interval = setInterval(function() {
         //           const now = new Date().getTime();
           //         const distance = countdownDate - now;
        
             //       if (distance < 0) {
               //         clearInterval(interval);
                 //       timer.querySelector('.days').textContent = '00';
                   //     timer.querySelector('.hours').textContent = '00';
                     //   timer.querySelector('.minutes').textContent = '00';
                       // timer.querySelector('.seconds').textContent = '00';
                        //return;
                    //}
        
          //          const days = Math.floor(distance / (1000 * 60 * 60 * 24));
          //          const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          //          const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
           //
            //        timer.querySelector('.days').textContent = days < 10 ? '0' + days : days;
           //         timer.querySelector('.hours').textContent = hours < 10 ? '0' + hours : hours;
             //       timer.querySelector('.minutes').textContent = minutes < 10 ? '0' + minutes : minutes;
             //       timer.querySelector('.seconds').textContent = seconds < 10 ? '0' + seconds : seconds;
             //   }, 1000);
         //   });
     
        




















         $(document).ready(function() {
          var slider = $("#slider");
          var thumb = $("#thumb");
          var slidesPerPage = 4; //globaly define number of elements per page
          var syncedSecondary = true;
          slider.owlCarousel({
              items: 1,
              slideSpeed: 2000,
              nav: false,
              autoplay: false, 
              dots: false,
              loop: true,
              responsiveRefreshRate: 200
          }).on('changed.owl.carousel', syncPosition);
          thumb
              .on('initialized.owl.carousel', function() {
                  thumb.find(".owl-item").eq(0).addClass("current");
              })
              .owlCarousel({
                  items: slidesPerPage,
                  dots: false,
                  nav: true,
                  item: 4,
                  smartSpeed: 200,
                  slideSpeed: 500,
                  slideBy: slidesPerPage, 
                navText: ['<svg width="18px" height="18px" viewBox="0 0 11 20"><path style="fill:none;stroke-width: 1px;stroke: #000;" d="M9.554,1.001l-8.607,8.607l8.607,8.606"/></svg>', '<svg width="25px" height="25px" viewBox="0 0 11 20" version="1.1"><path style="fill:none;stroke-width: 1px;stroke: #000;" d="M1.054,18.214l8.606,-8.606l-8.606,-8.607"/></svg>'],
                  responsiveRefreshRate: 100
              }).on('changed.owl.carousel', syncPosition2);
          function syncPosition(el) {
              var count = el.item.count - 1;
              var current = Math.round(el.item.index - (el.item.count / 2) - .5);
              if (current < 0) {
                  current = count;
              }
              if (current > count) {
                  current = 0;
              }
              thumb
                  .find(".owl-item")
                  .removeClass("current")
                  .eq(current)
                  .addClass("current");
              var onscreen = thumb.find('.owl-item.active').length - 1;
              var start = thumb.find('.owl-item.active').first().index();
              var end = thumb.find('.owl-item.active').last().index();
              if (current > end) {
                  thumb.data('owl.carousel').to(current, 100, true);
              }
              if (current < start) {
                  thumb.data('owl.carousel').to(current - onscreen, 100, true);
              }
          }
          function syncPosition2(el) {
              if (syncedSecondary) {
                  var number = el.item.index;
                  slider.data('owl.carousel').to(number, 100, true);
              }
          }
          thumb.on("click", ".owl-item", function(e) {
              e.preventDefault();
              var number = $(this).index();
              slider.data('owl.carousel').to(number, 300, true);
          });
  
  
              $(".qtyminus").on("click",function(){
                  var now = $(".qty").val();
                  if ($.isNumeric(now)){
                      if (parseInt(now) -1> 0)
                      { now--;}
                      $(".qty").val(now);
                  }
              })            
              $(".qtyplus").on("click",function(){
                  var now = $(".qty").val();
                  if ($.isNumeric(now)){
                      $(".qty").val(parseInt(now)+1);
                  }
              });
      });
