
function addNote(){
    let addNoteForm = document.getElementById("addNoteForm");

    if (addNoteForm.style.display == "none"){
        addNoteForm.style.display = "block" ;
    }else{
        addNoteForm.style.display = "none" ;
    }

}

function searchBar(){
    let search_bar = document.getElementById("search_bar");

    if (search_bar.style.display == "none"){
        search_bar.style.display = "block" ;
    }else{
        search_bar.style.display = "none" ;
    }
}
