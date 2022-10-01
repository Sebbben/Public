
chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    var qr = new VanillaQR({url: url,});
    document.getElementById("out").appendChild(qr.domElement);
});

document.getElementById("btn").addEventListener("click", () => {
    let url = document.getElementById("inp").value;
    var qr = new VanillaQR({url: url,});
    document.getElementById("out").appendChild(qr.domElement);
})