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
const item_descriptions = [];
const item_urls = [];
const item_brand = [];
const item_color = [];
const item_number = [];
const item_count = [];
const item_cat = [];
const item_sub = [];
const selected_items = [];

function selectrow(row){
  //Remove is-selected class from clicked row element
  if (row.classList.contains('is-selected')){
    //Get row item-id value from clicked row element to be unselected
    var id = row.querySelectorAll("td")[0].innerHTML;
    //If unselected item is in Array, then remove it from array
    if (item_ids.includes(id)) {
      item_ids.splice(item_ids.indexOf(id), 1);
    }
    
    var name = row.querySelectorAll("td")[1].innerHTML;
    //If unselected item is in Array, then remove it from array
    if (item_names.includes(name)) {
      item_names.splice(item_names.indexOf(name), 1);
    }

    var desc = row.querySelectorAll("td")[2].innerHTML;
    if (item_descriptions.includes(desc)) {
      item_descriptions.splice(item_descriptions.indexOf(desc), 1);
    }

    var url = row.querySelectorAll("td")[3].innerHTML;
    if (item_urls.includes(url)) {
      item_urls.splice(item_urls.indexOf(url), 1);
    }

    var brand = row.querySelectorAll("td")[4].innerHTML;
    if (item_brand.includes(brand)) {
      item_brand.splice(item_brand.indexOf(brand), 1);
    }

    var color = row.querySelectorAll("td")[5].innerHTML;
    if (item_color.includes(color)) {
      item_color.splice(item_color.indexOf(color), 1);
    }

    var number = row.querySelectorAll("td")[6].innerHTML;
    if (item_number.includes(number)) {
      item_number.splice(item_number.indexOf(number), 1);
    }

    var count = row.querySelectorAll("td")[7].innerHTML;
    if (item_count.includes(count)) {
      item_count.splice(item_count.indexOf(count), 1);
    }

    var cat = row.querySelectorAll("td")[8].innerHTML;
    if (item_cat.includes(cat)) {
      item_cat.splice(item_cat.indexOf(cat), 1);
    }

    var sub = row.querySelectorAll("td")[9].innerHTML;
    if (item_sub.includes(sub)) {
      item_sub.splice(item_sub.indexOf(count), 1);
    }

    console.log("Current ids: " + item_ids);
    console.log("Current names: " + item_names);
    console.log("Current urls: " + item_urls);
    console.log("Current desc: " + item_descriptions);
    console.log("Current brand: " + item_brand);
    console.log("Current count: " + item_count);
    console.log("Current color: " + item_color);
    console.log("Current cats: " + item_cat);
    console.log("Current item number: " + item_number);
    console.log("Current subs: " + item_sub);

    row.className = row.className.replace(" odd is-selected", " odd");
    row.className = row.className.replace(" even is-selected", " even");
  }
  //Add is-selected class from clicked row element
  else{
    row.className += " is-selected";
    //Get row item-id value from clicked row element to be selected
    //If selected item is not in Array, then add it to array
    var id = row.querySelectorAll("td")[0].innerHTML;
    item_ids.push(id);

    var name = row.querySelectorAll("td")[1].innerHTML;
    item_names.push(name);

    var desc = row.querySelectorAll("td")[2].innerHTML;
    item_descriptions.push(desc);

    var url = row.querySelectorAll("td")[3].innerHTML;
    item_urls.push(url);

    var brand = row.querySelectorAll("td")[4].innerHTML;
    item_brand.push(brand);

    var color = row.querySelectorAll("td")[5].innerHTML;
    item_color.push(color);

    var number = row.querySelectorAll("td")[6].innerHTML;
    item_number.push(number);

    var count = row.querySelectorAll("td")[7].innerHTML;
    item_count.push(count);

    var cat = row.querySelectorAll("td")[8].innerHTML;
    item_cat.push(cat);

    var sub = row.querySelectorAll("td")[9].innerHTML;
    item_sub.push(sub);

    console.log("Current ids: " + item_ids);
    console.log("Current names: " + item_names);
    console.log("Current urls: " + item_urls);
    console.log("Current desc: " + item_descriptions);
    console.log("Current brand: " + item_brand);
    console.log("Current count: " + item_count);
    console.log("Current color: " + item_color);
    console.log("Current cats: " + item_cat);
    console.log("Current item number: " + item_number);
    console.log("Current subs: " + item_sub);
  }
}

function add_items_to_delete(){
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
      hidden.type = "hidden";
      hidden.name = item_names[i];
      hidden.value = item_ids[i];

      text.innerHTML = "Item: '" + item_names[i] + "'";

      container.appendChild(input);
      input.appendChild(list);
      list.appendChild(text);
      list.appendChild(hidden);
    }
}

function edit_items_info(){

  if (item_ids.length == 0){
    alert("Please select an item");
    var container = document.getElementById("edit-tabs");
    var msg = document.createElement("div");
    msg.className = "notification is-info";
    msg.innerHTML = "No items selected";
    container.appendChild(msg);
  }
  else{

  // Get the element where the inputs will be added to
  var container = document.getElementById("edit-tabs");

  var list = document.createElement("ul");
  container.appendChild(list);
  for (i=0;i<item_ids.length;i++){
    // Create an <li> element, set its type and name attributes
    var text = document.createElement("li");
    text.id = "item-tab_"+item_ids[i];
    if(i==0){
      text.className = "is-active";
    }
    else{
      text.className = "";
    }
    text.setAttribute("name","items-tab")
    var innertext = document.createElement("a");
    innertext.innerHTML = item_names[i];
    if(i==0){
      text.setAttribute("onclick","itemTab('item-tab_"+""+item_ids[i]+"'"+","+"'item_"+""+item_ids[i]+"')");    
    }
    else{
      text.setAttribute("onclick","itemTab('item-tab_"+""+item_ids[i]+"'"+","+"'item_"+""+item_ids[i]+"')");
    }
    text.appendChild(innertext);

    list.appendChild(text);

    //Create Edit tab content
  }
  }
}

function del_item_tabs_on_close(){
  const myNode = document.getElementById("edit-tabs");
  while (myNode.lastElementChild) {
    myNode.removeChild(myNode.lastElementChild);
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

function itemTab(evt, itemTab) {
  // Declare all variables
  var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("item-tab-content");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  
  // Get all elements with name="my-tab" and remove the class "is-active"
  tablinks = document.getElementsByName("items-tab");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace("is-active", "");
  }
  
  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(itemTab).style.display = "block";
  document.getElementById(itemTab).style.visibility = "visible";
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

function insertAfter(referenceNode, newNode) {
  referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}