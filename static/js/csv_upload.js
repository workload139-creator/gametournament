function uploadCSV(){

const file=document.getElementById("csvFile").files[0];

if(!file){

alert("Select CSV");

return;

}

alert("CSV Ready");

}
