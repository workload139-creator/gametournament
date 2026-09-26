const socket=new WebSocket(
"ws://"+window.location.host+"/ws/leaderboard/"
);

socket.onmessage=(e)=>{

const data=JSON.parse(e.data);

console.log(data);

};
