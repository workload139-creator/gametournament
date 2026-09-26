const target=new Date("2026-12-31 20:00:00");

setInterval(()=>{

const now=new Date();

const diff=target-now;

const hours=Math.floor(diff/3600000);

const mins=Math.floor(diff%3600000/60000);

const sec=Math.floor(diff%60000/1000);

const el=document.getElementById("countdown");

if(el){

el.innerHTML=`${hours}h ${mins}m ${sec}s`;

}

},1000);
