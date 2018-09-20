$(document).ready(function(){ 
  
  $('img.next').on('click', function(){
    var currentImg = $('img.active');
    console.log(currentImg);
    var nextImg = currentImg.next();

    if(nextImg.length){
      currentImg.removeClass('active').css('z-index', -10);
      nextImg.addClass('active').css('z-index', 10);
    
    }
  });

  $('img.prev').on('click', function(){
    var currentImg = $('img.active');
    var prevImg = currentImg.prev();

    if(prevImg.length){
      currentImg.removeClass('active').css('z-index', -10);
      prevImg.addClass('active').css('z-index', 10);
    }
  });

});