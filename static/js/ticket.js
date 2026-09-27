const canvas=document.getElementById("ticketQR");

const ctx=canvas.getContext("2d");

canvas.width=220;
canvas.height=220;

ctx.fillStyle="#111";
ctx.fillRect(0,0,220,220);

ctx.fillStyle="#ff7b00";
ctx.fillRect(20,20,180,180);

function downloadTicket(){

const a=document.createElement("a");

a.download="ticket.png";

a.href=canvas.toDataURL();

a.click();

}
