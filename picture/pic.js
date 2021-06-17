function change_size(x) {
    document.getElementById("my_pic").width = x;

}

function blr() {

    if (document.getElementById("blur").checked) {

        document.getElementById("my_pic").style.filter += "blur(5px)";

    } else {

        let s = document.getElementById("my_pic").style.filter;
        s = s.replace("blur(5px)", "")
       document.getElementById("my_pic").style.filter =s;

    }
}

function gray() {

    if (document.getElementById("gray").checked) {
        document.getElementById("my_pic").style.filter += "grayscale()";

    } else {
        let s = document.getElementById("my_pic").style.filter;
        s = s.replace("grayscale()", '');
        document.getElementById("my_pic").style.filter = s;

    }
}

function cntrs()
{
    if (document.getElementById("ctr").checked) {
        document.getElementById("my_pic").style.filter += "invert(100%)";

    } else {
        let s = document.getElementById("my_pic").style.filter;
        s = s.replace("invert(100%)", '');
        document.getElementById("my_pic").style.filter = s;

    }
}

