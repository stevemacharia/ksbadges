$('.search-button').click(function(){
    $(this).parent().toggleClass('open');
  });


  // When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
  if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
    document.getElementById("navbar").style.backgroundColor = "white";
    document.getElementById("NavbarBrand").style.backgroundImage = "url('/static/alexadashcams/images/alexa-dashcam-logo.png')";

    document.getElementById("navbar").style.position = "fixed";
    document.getElementById("NavIcon1").style.color = "black";
    document.getElementById("NavIcon2").style.color = "black";
    // document.getElementById("NavIcon3").style.color = "black";
 
    document.getElementById("ToggleButton").style.color = "black";

    var x = document.getElementsByClassName("nav-link");
    var i;
    for (i = 0; i < x.length; i++) {
      x[i].style.color = "#1d1d1d","!important";
    }
    
  } else {
    document.getElementById("navbar").style.backgroundColor = "transparent";
    document.getElementById("NavbarBrand").style.backgroundImage = "url('/static/alexadashcams/images/alexa-dashcam-logo-B.png')";
    document.getElementById("NavIcon1").style.color = "white";
    document.getElementById("NavIcon2").style.color = "white";
    // document.getElementById("NavIcon3").style.color = "white";
   
    document.getElementById("ToggleButton").style.color = "white";

    document.getElementById("ToggleButton").style.color = "black";

    var x = document.getElementsByClassName("nav-link");
    var i;
    for (i = 0; i < x.length; i++) {
      x[i].style.color = "white","!important";
    }

  }
}

window.setTimeout(function() {
  $(".alert").fadeTo(100, 0).slideUp(150, function(){
      $(this).remove(); 
  });
}, 1000);


var URLS = {
  addItem:        '{% url "cart-add" %}',
  removeItem:     '{% url "cart-remove" %}',
  changeQuantity: '{% url "cart-change-quantity" %}',
  emptyCart:      '{% url "cart-empty" %}',
}