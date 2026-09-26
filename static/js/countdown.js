const target=new Date("2026-12-31T20:00:00");

setInterval(()=>{

const now=new Date();

const diff=target-now;

if(diff<=0)return;

const h=Math.floor(diff/3600000);

const m=Math.floor(diff%3600000/60000);

const s=Math.floor(diff%60000/1000);

const el=document.getElementById("countdown");

if(el){

el.innerHTML=`${h}h ${m}m ${s}s`;

}

},1000);
