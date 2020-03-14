function check_form(){
    var f = document.forms["form"].elements;
    var cansubmit = true;
    for (var i = 0; i < f.length-1; i++) {
        if (f[i].value.length == 0){
             cansubmit = false;
        }
    }
    if (cansubmit) {
        document.getElementById('submit_button').disabled = false;
    }
    else {
        document.getElementById('submit_button').disabled = 'disabled';
    }
}

function loader(){
    document.getElementById('loader').style.display='block';
    document.getElementById('answer-box').style.display='none';
}
