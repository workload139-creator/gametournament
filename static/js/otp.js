import { getAuth, RecaptchaVerifier, signInWithPhoneNumber } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";

const auth = getAuth(window.app);

window.recaptcha = new RecaptchaVerifier(auth, "recaptcha-container", {});

document.getElementById("sendOtp")?.addEventListener("click", () => {

const phone = document.getElementById("phone").value;

signInWithPhoneNumber(auth, phone, window.recaptcha)

.then(res => {

window.confirmationResult = res;

window.location = "/accounts/verify/";

});

});

document.getElementById("verifyBtn")?.addEventListener("click", () => {

const code = document.getElementById("otp").value;

window.confirmationResult.confirm(code)

.then(() => {

window.location="/accounts/dashboard/";

});

});
