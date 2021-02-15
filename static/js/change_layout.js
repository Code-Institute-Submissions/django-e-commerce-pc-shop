


//  To loop over all items and select all with same class 
//  https://stackoverflow.com/questions/42416214/how-do-i-change-multiple-elements-with-same-class-name-using-javascript

// To setDisplay on all elements with same className
function setDisplay(className, displayValue) {
  var items = document.getElementsByClassName(className);
  for (var i=0; i < items.length; i++) {
    items[i].style.display = displayValue;
  }
}

//  To hide all elements with listLayout classes
function gridLayout() {
  setDisplay("gridLayout", "block");
  setDisplay("listLayout", "none");
}

//  To hide all elements with listLayout classes
function listLayout() {
  setDisplay("gridLayout", "none");
  setDisplay("listLayout", "block");
}


//  Layout icons idea
//  https://codepen.io/BraadMartin/pen/NPPzJX

//  To add and remove active on layout click
$("#list-view").click(function(){
    $(".active").removeClass("active");
    $(this).addClass("active")
});

$("#grid-view").click(function(){
    $(".active").removeClass("active");
    $(this).addClass("active")
});