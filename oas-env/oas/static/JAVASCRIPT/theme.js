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
     
        


























         document.addEventListener('DOMContentLoaded', function() {
          var showFormBtn = document.getElementById('show-review-form-btn');
          var reviewFormContainer = document.getElementById('review-form-container');
      
          showFormBtn.addEventListener('click', function() {
              // Toggle visibility of the review form
              if (reviewFormContainer.style.display === 'none' || reviewFormContainer.style.display === '') {
                  reviewFormContainer.style.display = 'block';
                  showFormBtn.textContent = 'Cancel';
              } else {
                  reviewFormContainer.style.display = 'none';
                  showFormBtn.textContent = 'Add Review';
              }
          });
      });