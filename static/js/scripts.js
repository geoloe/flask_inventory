function activate(value){
    document.getElementById(value).className += " is-active";
}

function deactivate(value){
    document.getElementById(value).className =
    document.getElementById(value).className.replace
    ( /(?:^|\s)modal is-active(?!\S)/g , 'modal' )
}

function hasClass(element, className) {
  return (' ' + element.className + ' ').indexOf(' ' + className+ ' ') > -1;
}

function next(){
  var elements = document.querySelectorAll(".step-item:not(.is-success)");
  var contents = document.querySelectorAll(".step-content.has-text-centered:not(.is-active)");
  console.log("steps length: " + elements.length);
  console.log("content length: " + contents.length);
  for(var t = 0, m = elements.length; t < m; m++) {
      elements[t].className += " is-success is-active";
      contents[t].className += " has-text-centered is-active";
      break;
  }
}
function previous(){
  var elements = document.querySelectorAll(".step-item.is-success");
  var contents = document.querySelectorAll(".step-content.is-active");
  for(var t = elements.length - 1, m = 0; t > m; t--) {
      elements[t].className = "step-item";
      contents[t].className = "step-content has-text-centered";
      break;
  }
}
//global arrays containing item-ids and names from Item Table
const item_ids = [];
const item_names = [];

function selectrow(row){
  //Remove is-selected class from clicked row element
  if (row.classList.contains('is-selected')){
    //Get row item-id value from clicked row element to be unselected
    var id = row.querySelectorAll("td")[0].innerHTML;
    console.log("Unselected Item id: " + id);
    //If unselected item is in Array, then remove it from array
    if (item_ids.includes(id)) {
      item_ids.splice(item_ids.indexOf(id), 1);
    }

    var name = row.querySelectorAll("td")[1].innerHTML;
    console.log("Unselected Item name: " + name);
    if (item_names.includes(name)) {
      item_names.splice(item_names.indexOf(name), 1);
    }

    console.log("Current ids: " + item_ids);
    console.log("Current ids: " + item_names);

    row.className = row.className.replace(" odd is-selected", " odd");
    row.className = row.className.replace(" even is-selected", " even");
  }
  //Add is-selected class from clicked row element
  else{
    row.className += " is-selected";
    //Get row item-id value from clicked row element to be selected
    var id = row.querySelectorAll("td")[0].innerHTML;
    console.log("Selected Item id: " + id);
    //If selected item is not in Array, then add it to array
    if (!item_ids.includes(id)) {
      item_ids.push(id);
    }

    var name = row.querySelectorAll("td")[1].innerHTML;
    console.log("Unselected Item name: " + name);
    if (!item_names.includes(name)) {
      item_names.push(name);
    }

    console.log("Current ids: " + item_ids);
    console.log("Current ids: " + item_names);
  }
}

function add_items(){
    // Get the element where the inputs will be added to
    var container = document.getElementById("delete-inputs");
    // Remove every children it had before
    while (container.hasChildNodes()) {
      container.removeChild(container.lastChild);
    }
    var input = document.createElement("div");
    input.className = "content";
    var list = document.createElement("ul");
    container.appendChild(input);
    input.appendChild(list)
    for (i=0;i<item_ids.length;i++){
      // Create an <li> element, set its type and name attributes
      var text = document.createElement("li");

      var hidden = document.createElement("input");
      hidden.type = "hidden"
      hidden.name = item_names[i]
      hidden.value = item_ids[i];

      text.innerHTML = "Item: '" + item_names[i] + "'";

      container.appendChild(input);
      input.appendChild(list)
      list.appendChild(text)
      list.appendChild(hidden)
    }
}

function rows(){
  var rows = document.querySelectorAll("tr");
  for (i = 0; i < rows.length; i++) {
    rows[i].className = rows[i].className.replace("is-selected", "");
  }
}
/*
function switcher(){
  var result = document.getElementById("useroption").checked ? 'yes' : 'no'
  if (result == "yes"){
    document.getElementById('email_input').style.visibility = "visible";
    document.getElementById('username_input').style.visibility = "hidden";
  }
  else {
    document.getElementById('email_input').style.visibility = "hidden";
    document.getElementById('username_input').style.visibility = "visible";
  }

}
*/

function apiTab(evt, apiTab) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with name="my-tab" and remove the class "is-active"
    tablinks = document.getElementsByName("my-tab");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace("is-active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(apiTab).style.display = "block";
    document.getElementById(apiTab).style.visibility = "visible";
    document.getElementById(evt).className += "is-active"
  }

function quickview(value) {
  var quickview = document.getElementById(value);
  if (quickview.className == "quickview is-active") {
    console.log(quickview.className)
    quickview.className = "quickview"
  }
  else{
    quickview.className += " is-active";
  }
}

function accordion(value){
  var accordion = document.getElementById(value);
  if (accordion.className == "accordion is-active") {
    console.log(accordion.className)
    accordion.className = "accordion"
  }
  else{
    accordion.className += " is-active";
  }
}

function pageloader(value){
  var loader = document.getElementById(value);
  loader.className += " is-active";
}

$('#items-table').DataTable( {
  dom: 'Bfrtip',
  buttons: [
      'colvis',
      'excel',
      'print',
      'copy'
  ]
} );

$('#categories-table').DataTable( {
  dom: 'Bfrtip',
  buttons: [
      'colvis',
      'excel',
      'print',
      'copy'
  ]
} );

$('#subcategories-table').DataTable( {
  dom: 'Bfrtip',
  buttons: [
      'colvis',
      'excel',
      'print',
      'copy'
  ]
} );

$(document).ready(function() {

  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(function() {

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");
      $("#burger").toggleClass("is-active");

  });
});