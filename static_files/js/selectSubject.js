/* This creates window for subject selection when 
   Creating a post
*/

function selectSubect() {
    document.getElementById("subjectList").classList.toggle("show");
    let subjectName = document.getElementById("subjectList").value;
    console.log(subjectName);
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      for (let i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }