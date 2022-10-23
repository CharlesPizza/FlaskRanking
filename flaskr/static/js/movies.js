const toQueue = []
let ulEl = document.getElementById("ul-el")
function add_to(movie){
  console.log('movies.js called')
  toQueue.push(movie)
  console.log(toQueue)
  renderQueue()
};
function renderQueue(){
    let listItems = "";
    for (var i=0; i<toQueue.length; i++) {
        listItems += `
        <li>
            ${toQueue[i]}
        </li>`
    };
    ulEl.innerHTML = listItems
};