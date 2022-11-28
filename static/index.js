function rechercherAvecXHR(){

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4) {
            document.getElementById("table").innerHTML = xhr.responseText;
        }
    }
    query = document.getElementById("recherche").value
    xhr.open("GET", "/query?q=" + query, true)
    xhr.send()
}
