$(document).ready(function () {
  $("#video-streams").hide();

  $(".egg").click(function () {
    $("#video-streams").slideToggle();

    $(".Click-here").click(function () {
      $("this").hide();

   
    });
  });
});

function hideButton(x) {
  x.style.display = 'none'
}


let coin = document.querySelector(".coin");
let flipBtn = document.querySelector("#p-button");
let resetBtn = document.querySelector("#n-button");
let point = 0;

let NEXT_TIME = 0;
flipBtn.addEventListener("click", () => {
  point = localStorage.getItem("head-key")
  let i = Math.floor(Math.random() * 2);
  coin.style.animation = "none";
  let ourStorage = window.localStorage;
  if (i) {
    setTimeout(function () {
      coin.style.animation = "spin-point 3s forwards";
    }, 300);
    point++;
    localStorage.setItem("head-key", point);
  }
  else {
    setTimeout(function () {
      coin.style.animation = "spin-NEXT_TIME 3s forwards";
    }, 300);
    NEXT_TIME++;
  }
  setTimeout(updateStats, 3000);
  disableButton();

});
// ........................popup'''''''''''''''''''
$(".Click-here").on('click', function () {
  $(".custom-model-main").addClass('model-open');
});
$(".close-btn, .bg-overlay").click(function () {
  $(".custom-model-main").removeClass('model-open');
});

function openForm() {
  document.getElementById("hid").style.display = "show";
}
function closeForm() {
  document.getElementById("hid").style.display = "none";
}



function openForm() {
  document.getElementById("video-streams").style.display = "show";
}
function closeForm() {
  document.getElementById("popupForm").style.display = "none";
}


function updateStats(){
  document.querySelector("#point-count").textContent = `point:  ${localStorage.getItem("head-key")}`;
    if (point == 50) {
      document.getElementById("div1").style.display = "block";
     
    }
  
}
function deleteItems() {
  localStorage.clear();
}
