function showToast(message) {
  const toaster = document.getElementById("toaster");
  toaster.textContent = message;
  toaster.style.display = "block";
  setTimeout(function () {
    toaster.style.display = "none";
  }, 5000);
  toaster.addEventListener("click", function () {
    window.location.href = `https://sepolia.etherscan.io/tx/${message.substring(
      message.indexOf("0x")
    )}`;
  });
}

function showLoader() {
  document.getElementById("loader").style.display = "block";
}
