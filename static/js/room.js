function copyRoom(){

const room=document.getElementById("roomid").value;

const pass=document.getElementById("roompass").value;

navigator.clipboard.writeText(

`Room ID: ${room}\nPassword: ${pass}`

);

alert("Room Copied!");

}

function sendWhatsApp(){

const room=document.getElementById("roomid").value;

const pass=document.getElementById("roompass").value;

const text=`🔥 FF Tournament\nRoom ID: ${room}\nPassword: ${pass}`;

window.open(

`https://wa.me/?text=${encodeURIComponent(text)}`

);

}
