if("serviceWorker" in navigator){
navigator.serviceWorker.register("/pwa/service-worker.js");
}
let deferredPrompt;

window.addEventListener("beforeinstallprompt",(e)=>{

e.preventDefault();

deferredPrompt=e;

});
