function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function scrollPage(scroll = 5) {
    var currentScroll = 0;
    while (currentScroll < scroll)
    {
        console.log("Scroll loop: " + currentScroll);
        window.scrollTo(0, document.body.scrollHeight);
        currentScroll++;

        await sleep(2000);
    }
}