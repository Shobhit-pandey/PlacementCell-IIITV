$(document).ready(function() {
    
    /* Every time the window is scrolled ... */
  
 /*   var divs = $('.banner');
$(window).scroll(function(){
   if($(window).scrollTop()<=100){
         divs.fadeIn(1000);
   } else {
         divs.fadeOut(1000);
   }
});
 */


 //Parallax 
function simpleParallax() {
    //This variable is storing the distance scrolled
    var scrolled = $(window).scrollTop() + 1;

    //Every element with the class "scroll" will have parallax background 
    //Change the "0.3" for adjusting scroll speed.
    $('.scroll').css('background-position', '0' + -(scrolled * 0.3) + 'px');
}
//Everytime we scroll, it will fire the function
$(window).scroll(function (e) {
    simpleParallax();
});
   
});