document.getElementById("payBtn")?.addEventListener("click",()=>{

const options={

key:"rzp_test_xxxxx",

amount:5000,

currency:"INR",

name:"FF Tournament Pro",

description:"Tournament Entry",

handler:function(res){

alert("Payment Successful: "+res.razorpay_payment_id);

}

};

new Razorpay(options).open();

});
