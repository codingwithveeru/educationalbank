const chatBtn=document.getElementById("chat-btn");

const chat=document.getElementById("aiChat");

const closeBtn=document.getElementById("closeChat");

chatBtn.onclick=()=>{

chat.style.display="flex";

}

closeBtn.onclick=()=>{

chat.style.display="none";

}

const send=document.getElementById("sendBtn");

const input=document.getElementById("userMessage");

const body=document.getElementById("chatBody");

send.onclick=()=>{

if(input.value=="") return;

body.innerHTML+=`<div class="user-message">${input.value}</div>`;

input.value="";

body.scrollTop=body.scrollHeight;

}