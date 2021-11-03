/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunct() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
//have to have multiple calls in order to work for multiple dropdowns
  function myFuncti() {
    document.getElementById("Friends").classList.toggle("show");
  }
  
  // Close the dropdown if the user clicks outside of it
  //currently only works for one of the drop downs

  
  window.onclick = function(e) {
    if (!e.target.matches('.dropbtn')) {
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
      }
    }
  }