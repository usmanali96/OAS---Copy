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
          
          cdtime.formatDuration = function(ms, baseunit){
            /*
            Usage: cdtime.formatDuration(ms, baseunit)
              1) ms param: Time left in milliseconds
              2) baseunit: The topmost unit to calculate the remaining time using: "days", "hours", "minutes", or "seconds"
                  If baseunit is "hours" for example, function will calculate the number of hours plus minutes plus seconds left for the specified ms duration
                  If baseunit is "minutes" for example, function will calculate the number of minutes plus seconds left for the specified ms duration
          
            Returns: object containing the time left in the specified baseunit plus sub units. Other units will return "n/a"
              {
                days: int,
                hours: int,
                minutes: int,
                seconds: int
              }
            */
            var timediff = ms/1000 // time remaining in sec
            var oneMinute=60 //minute unit in seconds
            var oneHour=60*60 //hour unit in seconds
            var oneDay=60*60*24 //day unit in seconds
            var dayfield=Math.floor(timediff/oneDay)
            var hourfield=Math.floor((timediff-dayfield*oneDay)/oneHour)
            var minutefield=Math.floor((timediff-dayfield*oneDay-hourfield*oneHour)/oneMinute)
            var secondfield=Math.floor((timediff-dayfield*oneDay-hourfield*oneHour-minutefield*oneMinute))
            if (baseunit=="hours"){ //if base unit is hours, set "hourfield" to be topmost level
              hourfield=dayfield*24+hourfield
              dayfield="n/a"
            }
            else if (baseunit=="minutes"){ //if base unit is minutes, set "minutefield" to be topmost level
              minutefield=dayfield*24*60+hourfield*60+minutefield
              dayfield=hourfield="n/a"
            }
            else if (baseunit=="seconds"){ //if base unit is seconds, set "secondfield" to be topmost level
              var secondfield=timediff
              dayfield=hourfield=minutefield="n/a"
            }
            return{
              days: dayfield,
              hours: hourfield,
              minutes: minutefield,
              seconds: secondfield
            }
          }
          















// Set the date we're counting down to
var countDownDate = new Date("Aug 30, 2024 15:00:00").getTime();

// Update the count down every 1 second
var countdownfunction1 = setInterval(function() {
  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the countdown date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes, and seconds
  var days1 = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours1 = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes1 = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds1 = Math.floor((distance % (1000 * 60)) / 1000);

  // Output the result in an element with id="days1", etc.
  document.getElementById("days1").innerHTML = days1;
  document.getElementById("hours1").innerHTML = hours1;
  document.getElementById("minutes1").innerHTML = minutes1;
  document.getElementById("seconds1").innerHTML = seconds1;

  // If the countdown is over, display "EXPIRED"
  if (distance < 0) {
    clearInterval(countdownfunction1);
    document.querySelector(".count").innerHTML = "EXPIRED";
  }
}, 1000);


