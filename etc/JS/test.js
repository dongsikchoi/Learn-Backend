function randomClick() {
  var liElements = document.querySelectorAll('div.list_area.listOn > ul > li');
  
  var nonZeroLiElements = Array.from(liElements).filter(function(li) {
    return li.querySelector('strong').textContent.trim() !== "0";
  });
  
  if (nonZeroLiElements.length === 0) {
    var reloadButton = document.getElementById('btnReloadSchedule');
    reloadButton.click();
  } else {
    var randomIndex = Math.floor(Math.random() * nonZeroLiElements.length);
    nonZeroLiElements[randomIndex].click();
  }
}

function runRandomClick() {
  var randomInterval = Math.floor(Math.random() * 2000) + 2000; // 2000ms에서 4000ms
  setTimeout(function() {
    randomClick(); 
    runRandomClick(); 
  }, randomInterval);
}

runRandomClick(); 