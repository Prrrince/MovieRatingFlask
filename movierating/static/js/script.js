
function searchOpen(){
  searchContainer = document.getElementById('searchContainer');
  searchContainer.classList.remove('hidden');
}

function searchClose(){
  searchContainer = document.getElementById('searchContainer');
  searchContainer.classList.add('hidden');
}

let inputFocus = function(e){
  let el = e.target || e;
  if(el.value){
    el.nextElementSibling.style.top = '-1rem';
  }
  else{
    el.nextElementSibling.style.top = '';
  }
}




let els = document.getElementsByClassName('form-control');

for (var i = 0; i < els.length; i++) {
  inputFocus(els[i]);
  els[i].addEventListener("blur", inputFocus);
}
