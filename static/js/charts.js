function loadChart(normal,moderate,severe){

var ctx = document.getElementById("resultChart");

new Chart(ctx,{

type:"pie",

data:{

labels:["Normal","Moderate","Severe"],

datasets:[{

label:"Detection Results",



backgroundColor:[
"#2ecc71",
"#f39c12",
"#e74c3c"
]

}]

}

});

}